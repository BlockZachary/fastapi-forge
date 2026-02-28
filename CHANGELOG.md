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
- Jinja2 template engine for project generation (`generator.py`)
- Complete base project templates:
  - FastAPI application structure (api, core, services, daos, models, schemas)
  - SQLAlchemy 2.0 async database configuration
  - Alembic migration setup
  - JWT authentication module
  - Redis integration
  - Docker and docker-compose configuration
  - Pytest testing framework with conftest.py
  - Ruff linter configuration
  - GitHub Actions CI workflow
  - VS Code configuration (settings, launch, extensions)
- Unit tests for CLI, models, and generator (31 tests passing)

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
