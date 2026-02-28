# FastAPI-Forge 🚀

[![PyPI version](https://badge.fury.io/py/fastapi-forge.svg)](https://badge.fury.io/py/fastapi-forge)
[![Python](https://img.shields.io/pypi/pyversions/fastapi-forge.svg)](https://pypi.org/project/fastapi-forge/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A highly modular FastAPI project scaffolding CLI tool for the AI application era.

## ✨ Features

- 🏗️ **Clean Architecture** - Auto-generate API/Service/DAO layered structure
- 📦 **Package Manager Choice** - Support uv (default), Poetry, or pip
- 🗄️ **Database Integration** - SQLAlchemy (Async) + Alembic migrations
- 🐳 **Docker Ready** - Optimized Dockerfile and docker-compose.yml
- 🔐 **JWT Authentication** - Out-of-the-box auth module
- ⚙️ **Multi-Environment Config** - dev/staging/prod configurations
- 🧪 **Testing Setup** - Pytest + pytest-asyncio pre-configured
- 🤖 **AI-Powered** (Coming Soon) - Generate models from natural language

## 📦 Installation

```bash
# Using pipx (recommended)
pipx install fastapi-forge

# Using uv
uv tool install fastapi-forge

# Using pip
pip install fastapi-forge
```

## 🚀 Quick Start

### Interactive Mode

```bash
forge create my-awesome-api
```

Follow the interactive prompts to configure your project:

```
🚀 FastAPI-Forge - Create New Project

? Project name: my-awesome-api
? Description: A awesome FastAPI project
? Author name: Your Name
? Author email: your@email.com
? Python version: 3.11

📦 Package Manager
? Select package manager: uv (recommended)

🗄️ Database
? Select database: PostgreSQL
? Enable Alembic migrations? Yes

🔐 Authentication
? Include JWT auth module? Yes

🐳 Docker
? Generate Docker configuration? Yes
? Generate docker-compose.yml? Yes

✅ Project my-awesome-api created successfully!
```

### Non-Interactive Mode

```bash
forge create my-api \
  --package-manager uv \
  --database postgres \
  --auth jwt \
  --docker \
  --no-interactive
```

## 📁 Generated Project Structure

```
my-awesome-api/
├── app/
│   ├── api/           # API routes
│   ├── config/        # Configuration
│   ├── core/          # Core utilities
│   ├── daos/          # Data Access Objects
│   ├── exceptions/    # Exception handlers
│   ├── models/        # SQLAlchemy models
│   ├── schemas/       # Pydantic schemas
│   ├── services/      # Business logic
│   └── utils/         # Utilities
├── alembic/           # Database migrations
├── tests/             # Test suite
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

## 🛠️ Commands

| Command | Description |
|---------|-------------|
| `forge create <name>` | Create a new FastAPI project |
| `forge version` | Show version information |
| `forge --help` | Show help message |

## 🤖 AI Features (Coming Soon)

```bash
# Generate SQLAlchemy model from description
forge add model "User with name, email, and subscription relationship"

# Generate CRUD API for a model
forge add api User --crud
```

## 📚 Documentation

- [Design Document](DESIGN.md)
- [Development Tasks](TODO.md)
- [Changelog](CHANGELOG.md)

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The awesome web framework
- [Typer](https://typer.tiangolo.com/) - CLI framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - Database toolkit
- [PROJECT_website](../PROJECT_website/backend) - Architecture reference
