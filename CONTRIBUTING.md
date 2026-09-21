# Contributing to SwipeFlow Python SDK

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the SwipeFlow Python SDK.

## Code of Conduct

Be respectful and inclusive. We welcome contributors of all backgrounds and experience levels.

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Git
- pip

### Development Setup

1. Clone the repository:
```bash
git clone https://github.com/swipeflow/swipeflow-api-py.git
cd swipeflow-api-py
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -e ".[dev]"
```

## Development Workflow

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_client.py
```

### Where code lives

- `swipeflow_api/generated/` is produced by `scripts/generate.py` from the OpenAPI spec. Never edit it by hand.
- `swipeflow_api/client.py` is the only hand-written SDK code (authentication, defaults, error raising). Endpoint- or model-specific code does not belong there.

### Making Changes

1. Create a feature branch:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes following the coding guidelines below.

3. Write tests for new functionality.

4. Ensure all tests pass.

5. Commit with clear, descriptive messages:
```bash
git commit -m "feat: add new feature description"
```

6. Push to your fork:
```bash
git push origin feature/your-feature-name
```

7. Open a Pull Request with a clear description.

## Coding Guidelines

### Python Style

- Follow PEP 8
- Use type hints for all function signatures
- Write docstrings for public functions and classes
- Keep lines under 120 characters

### Comments

Only add comments when explaining "why", not "what". Good code is self-documenting.

### Tests

- Write tests for new functionality
- Use descriptive test names: `test_create_item_with_valid_data`
- Use fixtures for common setup

Wrapper tests use `httpx.MockTransport` (see `tests/test_client.py`); tests that hit the real API must skip themselves unless `SWIPEFLOW_API_KEY` is set.

## Regenerating from OpenAPI

When the API changes, download the live spec and regenerate:

```bash
python scripts/generate.py
```

Commit the resulting changes to `swipeflow_api/generated/`. Method names come from each operation's `operationId` in the spec.

## Documentation

- Update README.md if you change user-facing behavior
- Add docstrings to public APIs
- Include examples for new features
- Update this CONTRIBUTING.md if you change contribution guidelines

## Pull Request Process

1. **Title**: Use conventional commit format
   - `feat: add new feature`
   - `fix: resolve issue`
   - `docs: update documentation`
   - `refactor: improve code`

2. **Description**: Explain what and why
   - What does this PR do?
   - Why is this change needed?
   - Are there any breaking changes?

3. **Testing**: Ensure
   - All tests pass
   - New tests added for new features

4. **Code Quality**: Ensure
   - `swipeflow_api/generated/` matches `python scripts/generate.py` output

5. **Review**: Address reviewer feedback promptly

## Reporting Issues

- Use GitHub Issues for bug reports and feature requests
- Include:
  - Python version
  - SDK version
  - Minimal reproducible example
  - Expected vs actual behavior
  - Error messages/tracebacks

## Commit Message Guidelines

Follow conventional commits format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `refactor`: Code refactoring
- `test`: Test additions/changes
- `chore`: Maintenance tasks

**Example**:
```
feat(client): support bearer tokens

Allow SwipeFlowClient to authenticate with a JWT via token=...

Fixes #123
```

## Release Process

(For maintainers)

1. Update version in:
   - `pyproject.toml`

2. Update CHANGELOG

3. Tag release:
```bash
git tag -a vX.Y.Z -m "Release vX.Y.Z"
git push origin vX.Y.Z
```

4. Build and publish from a clean `dist/` so no stale artifacts are uploaded:
```bash
rm -rf dist build
python -m build
python -m twine upload dist/*
```

## Questions?

- 📖 Check the [README](README.md)
- 📧 Email [support@swipeflow.io](mailto:support@swipeflow.io)

---

Thank you for contributing! 🎉
