# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Initial project structure with uv package management
- Design document (DESIGN.md)
- Development task tracking (TODO.md)
- CLI framework with Typer and Rich terminal output
- `forge version` and `forge create` commands
- Interactive prompts with Questionary for project configuration
- `ProjectConfig` Pydantic model with validation
- `PackageManager` enum (uv, poetry, pip)
- `DatabaseType` enum (postgres, mysql, sqlite, none)
- Non-interactive mode support (`-y` / `--no-interactive` flag)
- Unit tests for CLI and models (20 tests passing)

## [0.1.0] - TBD

### Added

- CLI framework with Typer
- Interactive project creation with Questionary
- Support for uv, Poetry, and pip package managers
- PostgreSQL, MySQL, and SQLite database templates
- SQLAlchemy 2.0 async models
- Alembic migration templates
- JWT authentication module
- Docker and docker-compose templates
- Pytest testing framework templates
- Ruff linter/formatter configuration
- GitHub Actions CI template
- VS Code configuration templates
