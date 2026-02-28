"""
Models Tests - Test the Pydantic data models.
"""

import pytest

from fastapi_forge.models import (
    DatabaseType,
    PackageManager,
    ProjectConfig,
)


class TestPackageManager:
    """Tests for PackageManager enum."""

    def test_uv_value(self):
        """Test UV enum value."""
        assert PackageManager.UV.value == "uv"

    def test_poetry_value(self):
        """Test Poetry enum value."""
        assert PackageManager.POETRY.value == "poetry"

    def test_pip_value(self):
        """Test pip enum value."""
        assert PackageManager.PIP.value == "pip"


class TestDatabaseType:
    """Tests for DatabaseType enum."""

    def test_postgres_value(self):
        """Test PostgreSQL enum value."""
        assert DatabaseType.POSTGRES.value == "postgres"

    def test_mysql_value(self):
        """Test MySQL enum value."""
        assert DatabaseType.MYSQL.value == "mysql"

    def test_sqlite_value(self):
        """Test SQLite enum value."""
        assert DatabaseType.SQLITE.value == "sqlite"

    def test_none_value(self):
        """Test None enum value."""
        assert DatabaseType.NONE.value == "none"


class TestProjectConfig:
    """Tests for ProjectConfig model."""

    def test_minimal_config(self):
        """Test creating config with minimal required fields."""
        config = ProjectConfig(project_name="test-project")

        assert config.project_name == "test-project"
        assert config.project_slug == "test_project"
        assert config.package_manager == PackageManager.UV
        assert config.database == DatabaseType.POSTGRES

    def test_project_slug_generation(self):
        """Test automatic slug generation from project name."""
        config = ProjectConfig(project_name="My Awesome API")
        assert config.project_slug == "my_awesome_api"

        config2 = ProjectConfig(project_name="test-project-name")
        assert config2.project_slug == "test_project_name"

    def test_custom_slug(self):
        """Test providing a custom slug."""
        config = ProjectConfig(
            project_name="test-project",
            project_slug="custom_slug",
        )
        assert config.project_slug == "custom_slug"

    def test_alembic_disabled_with_no_database(self):
        """Test that Alembic is disabled when database is none."""
        config = ProjectConfig(
            project_name="test-project",
            database=DatabaseType.NONE,
            use_alembic=True,  # Should be overridden
        )
        assert config.use_alembic is False

    def test_docker_services_updated_for_postgres(self):
        """Test docker services include postgres when selected."""
        config = ProjectConfig(
            project_name="test-project",
            database=DatabaseType.POSTGRES,
            use_redis=True,
        )
        assert "postgres" in config.docker_services
        assert "redis" in config.docker_services

    def test_docker_services_updated_for_mysql(self):
        """Test docker services include mysql when selected."""
        config = ProjectConfig(
            project_name="test-project",
            database=DatabaseType.MYSQL,
            use_redis=False,
        )
        assert "mysql" in config.docker_services
        assert "redis" not in config.docker_services

    def test_full_config(self):
        """Test creating config with all fields."""
        config = ProjectConfig(
            project_name="my-api",
            project_description="My awesome API",
            author_name="John Doe",
            author_email="john@example.com",
            python_version="3.12",
            package_manager=PackageManager.POETRY,
            database=DatabaseType.MYSQL,
            use_alembic=True,
            use_auth=True,
            use_redis=True,
            use_docker=True,
            use_docker_compose=True,
            use_pytest=True,
            use_ruff=True,
            use_github_actions=True,
            use_vscode=True,
        )

        assert config.project_name == "my-api"
        assert config.project_description == "My awesome API"
        assert config.author_name == "John Doe"
        assert config.author_email == "john@example.com"
        assert config.python_version == "3.12"
        assert config.package_manager == PackageManager.POETRY
        assert config.database == DatabaseType.MYSQL

    def test_invalid_project_name(self):
        """Test validation of project name."""
        with pytest.raises(ValueError):
            ProjectConfig(project_name="")  # Empty name should fail

    def test_invalid_python_version(self):
        """Test validation of Python version."""
        with pytest.raises(ValueError):
            ProjectConfig(
                project_name="test",
                python_version="3.9",  # Not in allowed versions
            )
