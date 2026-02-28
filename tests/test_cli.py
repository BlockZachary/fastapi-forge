"""
CLI Tests - Test the command line interface.
"""

from typer.testing import CliRunner

from fastapi_forge.cli import app

runner = CliRunner()


def test_version_command():
    """Test the version command displays version info."""
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "ForgeAPI" in result.stdout
    assert "0.1.0" in result.stdout


def test_version_flag():
    """Test the --version flag displays version info."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "ForgeAPI" in result.stdout


def test_help_command():
    """Test the help command displays help info."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "ForgeAPI" in result.stdout
    assert "create" in result.stdout


def test_create_help():
    """Test the create command help."""
    result = runner.invoke(app, ["create", "--help"])
    assert result.exit_code == 0
    assert "project-name" in result.stdout.lower() or "PROJECT_NAME" in result.stdout
