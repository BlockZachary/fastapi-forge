"""
Generator Tests

Tests for the Jinja2 template engine and project generation.
"""

import tempfile
from pathlib import Path

import pytest

from fastapi_forge.generator import ProjectGenerator
from fastapi_forge.models import DatabaseType, PackageManager, ProjectConfig


class TestProjectGenerator:
    """Tests for ProjectGenerator class."""

    @pytest.fixture
    def basic_config(self) -> ProjectConfig:
        """Create a basic project configuration for testing."""
        return ProjectConfig(
            project_name="Test Project",
            project_description="A test project",
            author_name="Test Author",
            author_email="test@example.com",
            package_manager=PackageManager.UV,
            database=DatabaseType.POSTGRES,
            use_auth=True,
            use_redis=True,
            use_docker=True,
            use_docker_compose=True,
        )

    @pytest.fixture
    def minimal_config(self) -> ProjectConfig:
        """Create a minimal project configuration for testing."""
        return ProjectConfig(
            project_name="Minimal Project",
            package_manager=PackageManager.PIP,
            database=DatabaseType.NONE,
            use_auth=False,
            use_redis=False,
            use_docker=False,
            use_docker_compose=False,
        )

    def test_generator_initialization(self, basic_config: ProjectConfig) -> None:
        """Test generator can be initialized with config."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "test_project"
            generator = ProjectGenerator(basic_config, output_dir)

            assert generator.config == basic_config
            assert generator.output_dir == output_dir
            assert generator.env is not None

    def test_template_context(self, basic_config: ProjectConfig) -> None:
        """Test template context contains expected variables."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "test_project"
            generator = ProjectGenerator(basic_config, output_dir)
            context = generator._get_template_context()

            # Check basic config values
            assert context["project_name"] == "Test Project"
            assert context["project_slug"] == "test_project"
            assert context["description"] == "A test project"
            assert context["author_name"] == "Test Author"
            assert context["author_email"] == "test@example.com"

            # Check feature flags
            assert context["use_auth"] is True
            assert context["use_redis"] is True
            assert context["use_docker"] is True

            # Check convenience flags
            assert context["use_uv"] is True
            assert context["use_poetry"] is False
            assert context["database_type"] == "postgres"

    def test_generate_creates_output_directory(
        self, basic_config: ProjectConfig
    ) -> None:
        """Test that generate() creates the output directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "new_project"
            generator = ProjectGenerator(basic_config, output_dir)

            assert not output_dir.exists()
            generator.generate()
            assert output_dir.exists()
            assert output_dir.is_dir()

    def test_generate_creates_files(self, basic_config: ProjectConfig) -> None:
        """Test that generate() creates expected files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "test_project"
            generator = ProjectGenerator(basic_config, output_dir)
            generated_files = generator.generate()

            # Should generate multiple files
            assert len(generated_files) > 0

            # Check for essential files
            expected_files = [
                "pyproject.toml",
                "README.md",
                ".gitignore",
                "app/__init__.py",
                "app/main.py",
            ]
            for file in expected_files:
                assert (output_dir / file).exists(), f"Missing file: {file}"

    def test_generate_without_database(self, minimal_config: ProjectConfig) -> None:
        """Test generation without database doesn't create alembic files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "minimal_project"
            generator = ProjectGenerator(minimal_config, output_dir)
            generator.generate()

            # Should not have alembic files when database is none
            assert not (output_dir / "alembic.ini").exists()
            assert not (output_dir / "alembic").exists()

    def test_generate_without_docker(self, minimal_config: ProjectConfig) -> None:
        """Test generation without docker doesn't create docker files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "minimal_project"
            generator = ProjectGenerator(minimal_config, output_dir)
            generator.generate()

            # Should not have docker files
            assert not (output_dir / "Dockerfile").exists()
            assert not (output_dir / "docker-compose.yml").exists()

    def test_generate_with_all_features(self, basic_config: ProjectConfig) -> None:
        """Test generation with all features enabled."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "full_project"
            generator = ProjectGenerator(basic_config, output_dir)
            generator.generate()

            # Should have all feature files
            assert (output_dir / "Dockerfile").exists()
            assert (output_dir / "docker-compose.yml").exists()
            assert (output_dir / "alembic.ini").exists()
            assert (output_dir / "alembic" / "env.py").exists()
            assert (output_dir / "app" / "core" / "auth.py").exists()
            assert (output_dir / "app" / "core" / "redis.py").exists()

    def test_pyproject_content_uv(self, basic_config: ProjectConfig) -> None:
        """Test pyproject.toml content for uv package manager."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "test_project"
            generator = ProjectGenerator(basic_config, output_dir)
            generator.generate()

            pyproject = (output_dir / "pyproject.toml").read_text()
            assert "test_project" in pyproject
            assert "fastapi" in pyproject.lower()

    def test_readme_content(self, basic_config: ProjectConfig) -> None:
        """Test README.md contains project information."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "test_project"
            generator = ProjectGenerator(basic_config, output_dir)
            generator.generate()

            readme = (output_dir / "README.md").read_text()
            assert "Test Project" in readme
            assert "A test project" in readme

    def test_different_package_managers(self) -> None:
        """Test generation with different package managers."""
        for pm in PackageManager:
            config = ProjectConfig(
                project_name=f"{pm.value} Project",
                package_manager=pm,
                database=DatabaseType.SQLITE,
            )

            with tempfile.TemporaryDirectory() as tmpdir:
                output_dir = Path(tmpdir) / f"{pm.value}_project"
                generator = ProjectGenerator(config, output_dir)
                generator.generate()

                assert (output_dir / "pyproject.toml").exists()

    def test_different_databases(self) -> None:
        """Test generation with different database types."""
        for db in DatabaseType:
            config = ProjectConfig(
                project_name=f"{db.value} Project",
                package_manager=PackageManager.UV,
                database=db,
            )

            with tempfile.TemporaryDirectory() as tmpdir:
                output_dir = Path(tmpdir) / f"{db.value}_project"
                generator = ProjectGenerator(config, output_dir)
                generator.generate()

                # pyproject.toml should always exist
                assert (output_dir / "pyproject.toml").exists()

                # alembic should only exist if database is not none
                if db != DatabaseType.NONE:
                    assert (output_dir / "alembic.ini").exists()
                else:
                    assert not (output_dir / "alembic.ini").exists()
