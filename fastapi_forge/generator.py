"""
Project Generator Module

This module handles the generation of FastAPI projects from templates using Jinja2.
"""

import os
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from fastapi_forge.models import ProjectConfig

console = Console()

# Get the templates directory path
TEMPLATES_DIR = Path(__file__).parent / "templates"


class ProjectGenerator:
    """
    Project generator using Jinja2 templates.

    This class handles loading templates, rendering them with project configuration,
    and writing the generated files to the target directory.
    """

    def __init__(self, config: ProjectConfig, output_dir: Path | None = None):
        """
        Initialize the project generator.

        Args:
            config: Project configuration
            output_dir: Output directory for the generated project (default: current dir)
        """
        self.config = config
        self.output_dir = output_dir or Path.cwd()
        # output_dir is the project directory itself
        self.project_dir = self.output_dir

        # Initialize Jinja2 environment
        self.env = Environment(
            loader=FileSystemLoader(TEMPLATES_DIR),
            autoescape=select_autoescape(default=False),
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True,
        )

        # Add custom filters
        self.env.filters["snake_case"] = self._to_snake_case

    @staticmethod
    def _to_snake_case(value: str) -> str:
        """Convert a string to snake_case."""
        result = value.lower()
        result = result.replace("-", "_")
        result = result.replace(" ", "_")
        return "".join(c for c in result if c.isalnum() or c == "_")

    def _get_template_context(self) -> dict:
        """
        Get the template context from project configuration.

        Returns:
            Dictionary with all template variables
        """
        return {
            # Basic info
            "project_name": self.config.project_name,
            "project_slug": self.config.project_slug,
            "description": self.config.project_description,
            "project_description": self.config.project_description,
            "author_name": self.config.author_name,
            "author_email": self.config.author_email,
            "python_version": self.config.python_version,
            # Package manager
            "package_manager": self.config.package_manager.value,
            "use_uv": self.config.package_manager.value == "uv",
            "use_poetry": self.config.package_manager.value == "poetry",
            "use_pip": self.config.package_manager.value == "pip",
            # Database
            "database": self.config.database.value,
            "database_type": self.config.database.value,
            "use_postgres": self.config.database.value == "postgres",
            "use_mysql": self.config.database.value == "mysql",
            "use_sqlite": self.config.database.value == "sqlite",
            "use_database": self.config.database.value != "none",
            "use_alembic": self.config.use_alembic,
            # Features
            "use_auth": self.config.use_auth,
            "use_redis": self.config.use_redis,
            # Docker
            "use_docker": self.config.use_docker,
            "use_docker_compose": self.config.use_docker_compose,
            "docker_services": self.config.docker_services,
            # Testing & Quality
            "use_pytest": self.config.use_pytest,
            "use_ruff": self.config.use_ruff,
            # CI/CD & Editor
            "use_github_actions": self.config.use_github_actions,
            "use_vscode": self.config.use_vscode,
        }

    def _render_template(self, template_path: str, context: dict) -> str:
        """
        Render a template with the given context.

        Args:
            template_path: Path to the template file (relative to templates dir)
            context: Template context dictionary

        Returns:
            Rendered template content
        """
        template = self.env.get_template(template_path)
        return template.render(**context)

    def _should_include_template(self, template_path: str, context: dict) -> bool:
        """
        Check if a template should be included based on configuration.

        Args:
            template_path: Path to the template file
            context: Template context dictionary

        Returns:
            True if template should be included
        """
        # Check for conditional directories/files
        path_lower = template_path.lower()

        # Database related
        if "alembic" in path_lower and not context["use_alembic"]:
            return False
        if "database" in path_lower and not context["use_database"]:
            return False

        # Auth related
        if "auth" in path_lower and not context["use_auth"]:
            return False

        # Redis related
        if "redis" in path_lower and not context["use_redis"]:
            return False

        # Docker related
        if "docker" in path_lower:
            if "compose" in path_lower and not context["use_docker_compose"]:
                return False
            if not context["use_docker"]:
                return False

        # CI/CD related
        if ".github" in path_lower and not context["use_github_actions"]:
            return False

        # VS Code related
        if ".vscode" in path_lower and not context["use_vscode"]:
            return False

        # Pytest related
        if "pytest" in path_lower and not context["use_pytest"]:
            return False
        if "conftest" in path_lower and not context["use_pytest"]:
            return False

        # Ruff related
        if "ruff" in path_lower and not context["use_ruff"]:
            return False

        return True

    def _get_output_path(self, template_path: str) -> Path:
        """
        Get the output path for a template file.

        Args:
            template_path: Path to the template file

        Returns:
            Output path for the rendered file
        """
        # Remove .jinja extension
        output_path = template_path
        if output_path.endswith(".jinja"):
            output_path = output_path[:-6]

        # Handle special directory mappings
        # templates/base/app -> app
        if output_path.startswith("base/"):
            output_path = output_path[5:]

        return self.project_dir / output_path

    def _collect_templates(self) -> list[str]:
        """
        Collect all template files to be processed.

        Returns:
            List of template paths relative to templates directory
        """
        templates = []

        for root, _dirs, files in os.walk(TEMPLATES_DIR):
            for file in files:
                if file.endswith(".jinja"):
                    full_path = Path(root) / file
                    rel_path = full_path.relative_to(TEMPLATES_DIR)
                    templates.append(str(rel_path))

        return templates

    def generate(self) -> list[Path]:
        """
        Generate the project from templates.

        Returns:
            List of paths to generated files
        """
        # Check if project directory already exists
        if self.project_dir.exists():
            raise FileExistsError(
                f"Directory '{self.project_dir}' already exists. "
                "Please choose a different project name or remove the existing directory."
            )

        context = self._get_template_context()
        templates = self._collect_templates()
        generated_files: list[Path] = []

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task(
                "[cyan]Generating project...", total=len(templates)
            )

            # Create project directory
            self.project_dir.mkdir(parents=True, exist_ok=True)

            for template_path in templates:
                # Check if template should be included
                if not self._should_include_template(template_path, context):
                    progress.advance(task)
                    continue

                # Get output path
                output_path = self._get_output_path(template_path)

                # Create parent directories
                output_path.parent.mkdir(parents=True, exist_ok=True)

                # Render and write template
                try:
                    content = self._render_template(template_path, context)
                    output_path.write_text(content)
                    generated_files.append(output_path)
                except Exception as e:
                    console.print(f"[yellow]Warning: Failed to render {template_path}: {e}[/yellow]")

                progress.advance(task)

        return generated_files

    def cleanup(self) -> None:
        """Remove the generated project directory (for error recovery)."""
        if self.project_dir.exists():
            shutil.rmtree(self.project_dir)


def generate_project(config: ProjectConfig, output_dir: Path | None = None) -> list[Path]:
    """
    Generate a FastAPI project from templates.

    Args:
        config: Project configuration
        output_dir: Output directory (default: current directory)

    Returns:
        List of paths to generated files
    """
    generator = ProjectGenerator(config, output_dir)

    try:
        generated_files = generator.generate()
        console.print(f"\n[green]✅ Project generated at:[/green] {generator.project_dir}")
        return generated_files
    except FileExistsError as e:
        console.print(f"\n[red]❌ Error:[/red] {e}")
        raise
    except Exception as e:
        console.print(f"\n[red]❌ Error generating project:[/red] {e}")
        generator.cleanup()
        raise
