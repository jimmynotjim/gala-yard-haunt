.PHONY: help install install-dev install-pi venv test test-cov lint format check clean pre-commit update-deps

# Default target - show help
help:
	@echo "Pi-Thon Development Commands"
	@echo "============================"
	@echo ""
	@echo "Setup:"
	@echo "  make venv          Create virtual environment"
	@echo "  make install       Install core dependencies only"
	@echo "  make install-dev   Install with dev dependencies"
	@echo "  make install-pi    Install with Pi hardware dependencies"
	@echo ""
	@echo "Development:"
	@echo "  make format        Format code with Ruff"
	@echo "  make lint          Lint code with Ruff"
	@echo "  make typecheck     Run mypy type checking"
	@echo "  make test          Run tests with pytest"
	@echo "  make test-cov      Run tests with coverage report"
	@echo "  make check         Run all checks (lint + typecheck + test)"
	@echo ""
	@echo "Git Hooks:"
	@echo "  make pre-commit    Run pre-commit hooks on all files"
	@echo "  make install-hooks Install pre-commit hooks"
	@echo ""
	@echo "Maintenance:"
	@echo "  make update-deps   Update pre-commit hook versions"
	@echo "  make clean         Remove build artifacts and caches"
	@echo "  make clean-all     Remove everything including venv"

# Create virtual environment
venv:
	python3 -m venv venv
	@echo ""
	@echo "Virtual environment created!"
	@echo "Activate it with: source venv/bin/activate"

# Install core dependencies only
install:
	pip install -e .

# Install with development dependencies
install-dev:
	pip install -e ".[dev]"

# Install with Pi hardware dependencies (use on Raspberry Pi)
install-pi:
	pip install -e ".[dev,pi]"

# Format code with Ruff
format:
	ruff format .

# Lint code with Ruff
lint:
	ruff check .

# Fix linting issues automatically
lint-fix:
	ruff check . --fix

# Run type checking with mypy
typecheck:
	mypy src/

# Run tests
test:
	pytest $(ARGS)

# Run tests with coverage
test-cov:
	pytest --cov=src --cov-report=term-missing --cov-report=html
	@echo ""
	@echo "Coverage report generated in htmlcov/index.html"

# Run all checks
check: lint typecheck test
	@echo ""
	@echo "✓ All checks passed!"

# Install pre-commit hooks
install-hooks:
	pre-commit install
	@echo ""
	@echo "Pre-commit hooks installed!"

# Run pre-commit on all files
pre-commit:
	pre-commit run --all-files

# Update pre-commit hook versions
update-deps:
	pre-commit autoupdate
	@echo ""
	@echo "Pre-commit hooks updated! Don't forget to regenerate .secrets.baseline:"
	@echo "  detect-secrets scan > .secrets.baseline"

# Clean build artifacts and caches
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

# Clean everything including venv
clean-all: clean
	rm -rf venv/
	@echo ""
	@echo "Everything cleaned! Run 'make venv' to start fresh."
