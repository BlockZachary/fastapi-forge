"""
ForgeAPI CLI - Command Line Interface

This module provides the main CLI application using Typer.
"""

import typer
from rich.console import Console
from rich.panel import Panel

from fastapi_forge import __version__

# Initialize Typer app
app = typer.Typer(
    name="forge",
    help="🚀 ForgeAPI - A highly modular FastAPI project scaffolding CLI tool",
    add_completion=False,
    rich_markup_mode="rich",
)

# Rich console for beautiful output
console = Console()


def version_callback(value: bool) -> None:
    """Display version information and exit."""
    if value:
        console.print(
            Panel(
                f"[bold cyan]ForgeAPI[/bold cyan] version [green]{__version__}[/green]\n\n"
                f"🚀 A highly modular FastAPI project scaffolding CLI tool\n"
                f"📚 Documentation: https://github.com/zachary/fastapi-forge",
                title="Version Info",
                border_style="cyan",
            )
        )
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version information and exit.",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """
    🚀 ForgeAPI - Create FastAPI projects with best practices.

    A highly modular FastAPI project scaffolding CLI tool for the AI application era.
    Generate projects with Clean Architecture, Docker, Authentication, and more.
    """
    pass


@app.command()
def create(
    project_name: str = typer.Argument(
        ...,
        help="Name of the project to create",
    ),
    package_manager: str = typer.Option(
        None,
        "--package-manager",
        "-pm",
        help="Package manager to use (uv, poetry, pip)",
    ),
    database: str = typer.Option(
        None,
        "--database",
        "-db",
        help="Database to use (postgres, mysql, sqlite, none)",
    ),
    auth: bool = typer.Option(
        None,
        "--auth/--no-auth",
        help="Include JWT authentication module",
    ),
    docker: bool = typer.Option(
        None,
        "--docker/--no-docker",
        help="Generate Docker configuration",
    ),
    no_interactive: bool = typer.Option(
        False,
        "--no-interactive",
        "-y",
        help="Skip interactive prompts and use defaults",
    ),
) -> None:
    """
    Create a new FastAPI project with the specified configuration.

    Examples:

        $ forge create my-api

        $ forge create my-api --package-manager uv --database postgres --auth --docker

        $ forge create my-api --no-interactive
    """
    from fastapi_forge.commands.create import create_project

    create_project(
        project_name=project_name,
        package_manager=package_manager,
        database=database,
        auth=auth,
        docker=docker,
        no_interactive=no_interactive,
    )


@app.command()
def version() -> None:
    """Show version information."""
    version_callback(True)


if __name__ == "__main__":
    app()
