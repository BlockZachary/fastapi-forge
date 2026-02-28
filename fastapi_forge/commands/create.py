"""
Create Command - Project Creation Logic

This module handles the 'forge create' command implementation.
"""

from rich.console import Console
from rich.panel import Panel

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
    console.print(
        Panel(
            f"[bold cyan]🚀 FastAPI-Forge[/bold cyan] - Creating new project\n\n"
            f"Project: [green]{project_name}[/green]",
            title="Create Project",
            border_style="cyan",
        )
    )

    # TODO: Implement interactive prompts (Issue #3)
    # TODO: Implement project generation (Issue #12)

    if no_interactive:
        # Use defaults or provided values
        config = {
            "project_name": project_name,
            "package_manager": package_manager or "uv",
            "database": database or "postgres",
            "auth": auth if auth is not None else True,
            "docker": docker if docker is not None else True,
        }
        console.print(f"\n📦 Using configuration: {config}")
    else:
        # Interactive mode - to be implemented
        console.print(
            "\n[yellow]⚠️  Interactive mode not yet implemented.[/yellow]\n"
            "Use [cyan]--no-interactive[/cyan] flag or wait for Issue #3.\n"
        )
        return

    console.print(
        "\n[yellow]⚠️  Project generation not yet implemented.[/yellow]\n"
        "This will be completed in Issue #12.\n"
    )
