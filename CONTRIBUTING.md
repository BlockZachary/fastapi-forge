# Contributing to FastAPI-Forge

Thank you for your interest in contributing to FastAPI-Forge! 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Style Guide](#style-guide)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/fastapi-forge.git
   cd fastapi-forge
   ```

## Development Setup

### Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/) (recommended)

### Install Dependencies

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv sync --group dev

# Activate the virtual environment
source .venv/bin/activate

# Verify installation
forge version
```

### Project Structure

```
fastapi-forge/
├── fastapi_forge/           # Main package
│   ├── __init__.py
│   ├── cli.py               # CLI entry point
│   ├── commands/            # Command implementations
│   ├── generator.py         # Template engine
│   ├── models.py            # Data models
│   ├── prompts.py           # Interactive prompts
│   └── templates/           # Jinja2 templates
├── tests/                   # Test suite
├── pyproject.toml           # Project configuration
├── DESIGN.md                # Design document
├── TODO.md                  # Development tasks
└── CHANGELOG.md             # Changelog
```

## Making Changes

### Branch Naming

Use descriptive branch names:

- `feature/add-mongodb-support`
- `fix/template-rendering-bug`
- `docs/update-readme`
- `refactor/simplify-generator`

### Creating a Branch

```bash
git checkout -b feature/your-feature-name
```

### Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

**Types:**

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**

```bash
feat(generator): add MySQL support
fix(cli): handle keyboard interrupt gracefully
docs(readme): add installation instructions
test(models): add ProjectConfig validation tests
```

## Testing

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_generator.py

# Run with coverage report
uv run pytest --cov=fastapi_forge --cov-report=html
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files as `test_*.py`
- Use descriptive test function names: `test_should_generate_project_with_postgres`

**Example Test:**

```python
import pytest
from fastapi_forge.models import ProjectConfig, DatabaseType

def test_project_config_generates_slug():
    config = ProjectConfig(project_name="My Awesome API")
    assert config.project_slug == "my_awesome_api"
```

## Submitting Changes

### Before Submitting

1. **Run tests** and ensure all pass:

   ```bash
   uv run pytest
   ```

2. **Run linting**:

   ```bash
   uv run ruff check .
   uv run ruff format .
   ```

3. **Update documentation** if needed

4. **Update CHANGELOG.md** with your changes

### Pull Request Process

1. **Push your branch** to your fork:

   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open a Pull Request** on GitHub

3. **Fill out the PR template** with:
   - Description of changes
   - Related issue (if any)
   - Screenshots (for UI changes)

4. **Wait for review** - maintainers will review and provide feedback

5. **Address feedback** and update your PR as needed

## Style Guide

### Python Code Style

- Follow [PEP 8](https://pep8.org/)
- Use [Ruff](https://docs.astral.sh/ruff/) for linting and formatting
- Maximum line length: 120 characters
- Use type hints for function signatures

**Example:**

```python
from pathlib import Path

def generate_project(
    config: ProjectConfig,
    output_dir: Path | None = None,
) -> list[Path]:
    """
    Generate a FastAPI project from templates.

    Args:
        config: Project configuration
        output_dir: Output directory (default: current directory)

    Returns:
        List of paths to generated files
    """
    ...
```

### Template Style

- Use `.jinja` extension for template files
- Use meaningful variable names
- Add conditional blocks for optional features

**Example:**

```jinja
{% if use_database %}
from app.core.database import get_db
{% endif %}
```

## 🙏 Thank You!

Your contributions help make FastAPI-Forge better for everyone. We appreciate your time and effort!

If you have any questions, feel free to open an issue or reach out to the maintainers.
