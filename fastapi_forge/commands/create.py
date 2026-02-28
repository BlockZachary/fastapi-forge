"""
Create Command - Project Creation Logic

This module handles the 'forge create' command implementation.
"""

from rich.console import Console
from rich.panel import Panel

from fastapi_forge.models import (
    DatabaseType,
    PackageManager,
    ProjectConfig,
)
from fastapi_forge.prompts import (
    collect_project_config,
    confirm_config,
)

console = Console()


def create_project(
    project_name: str,
    package_manager: str | None = None,
    database: str | None = None,
    auth: bool | None = None,
    docker: bool | None = None,
    no_interactive: bool = False,
) -> None:
    """
    Create a new FastAPI project.

    Args:
        project_name: Name of the project to create
        package_manager: Package manager to use (uv, poetry, pip)
        database: Database to use (postgres, mysql, sqlite, none)
        auth: Whether to include JWT authentication
        docker: Whether to generate Docker configuration
        no_interactive: Skip interactive prompts
    """
    try:
        if no_interactive:
            # Non-interactive mode: use defaults or provided values
            config = ProjectConfig(
                project_name=project_name,
                package_manager=PackageManager(package_manager or "uv"),
                database=DatabaseType(database or "postgres"),
                use_auth=auth if auth is not None else True,
                use_docker=docker if docker is not None else True,
                use_docker_compose=docker if docker is not None else True,
            )
        else:
            # Interactive mode: collect configuration through prompts
            try:
                config = collect_project_config(project_name)

                # Ask for confirmation
                if not confirm_config(config):
                    console.print("\n[yellow]Project creation cancelled.[/yellow]")
                    return
            except KeyboardInterrupt:
                return

        # Display confirmation
        console.print(
            Panel(
                f"[bold green]✅ Configuration ready![/bold green]\n\n"
                f"Project: [cyan]{config.project_name}[/cyan]\n"
                f"Slug: [cyan]{config.project_slug}[/cyan]\n"
                f"Package Manager: [cyan]{config.package_manager.value}[/cyan]\n"
                f"Database: [cyan]{config.database.value}[/cyan]",
                title="Ready to Generate",
                border_style="green",
            )
        )

        # TODO: Implement project generation (Issue #12)
        console.print(
            "\n[yellow]⚠️  Project generation not yet implemented.[/yellow]\n"
            "This will be completed in Issue #12.\n"
        )

    except ValueError as e:
        console.print(f"\n[red]❌ Error: {e}[/red]")
        raise SystemExit(1)
