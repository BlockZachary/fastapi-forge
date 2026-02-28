"""
FastAPI-Forge: A highly modular FastAPI project scaffolding CLI tool.

This package provides a CLI tool for generating FastAPI projects with
best practices including Clean Architecture, Docker support, database
integration, and authentication.
"""

__version__ = "0.1.0"
__author__ = "Zachary"
__email__ = "zachary@example.com"

from fastapi_forge.cli import app

__all__ = ["app", "__version__"]
