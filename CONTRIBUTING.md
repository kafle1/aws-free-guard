# Contributing to AWS Free Guard

Thank you for your interest in contributing to AWS Free Guard! This document provides guidelines and information for contributors.

## 🚀 Quick Start

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/aws-free-guard.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
5. Install development dependencies: `pip install -e .[dev]`
6. Install pre-commit hooks: `pre-commit install`

## 📋 Development Workflow

### 1. Choose an Issue
- Check the [Issues](https://github.com/yourusername/aws-free-guard/issues) page
- Look for issues labeled `good first issue` or `help wanted`
- Comment on the issue to indicate you're working on it

### 2. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-number-description
```

### 3. Make Changes
- Write tests for new features
- Follow the existing code style
- Update documentation as needed
- Ensure all tests pass

### 4. Commit Changes
```bash
git add .
git commit -m "feat: add your feature description"
```

Use conventional commit format:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation
- `style:` for formatting
- `refactor:` for code refactoring
- `test:` for tests
- `chore:` for maintenance

### 5. Push and Create Pull Request
```bash
git push origin your-branch-name
```
Then create a Pull Request on GitHub.

## 🧪 Testing

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/unit/test_specific.py

# Run tests matching pattern
pytest -k "test_name"
```

### Writing Tests
- Place tests in the appropriate directory under `tests/`
- Use descriptive test names
- Follow the existing test patterns
- Mock AWS services for unit tests
- Use fixtures for common test setup

## 📝 Code Style

This project uses several tools to maintain code quality:

### Black (Code Formatting)
```bash
black src/ tests/
```

### isort (Import Sorting)
```bash
isort src/ tests/
```

### flake8 (Linting)
```bash
flake8 src/ tests/
```

### mypy (Type Checking)
```bash
mypy src/
```

### Pre-commit Hooks
All of these checks run automatically on commit. You can also run them manually:
```bash
pre-commit run --all-files
```

## 🏗️ Project Structure

```
aws-free-guard/
├── src/
│   ├── cli/           # Command-line interface
│   ├── lib/           # Core business logic
│   └── models/        # Data models
├── tests/             # Test suite
│   ├── unit/          # Unit tests
│   ├── integration/   # Integration tests
│   └── contract/      # Contract tests
├── docs/              # Documentation
├── scripts/           # Development scripts
└── specs/             # Specifications and requirements
```

## 🔒 Security

- Never commit AWS credentials or sensitive information
- Use environment variables for configuration
- Follow AWS security best practices
- Report security issues privately to maintainers

## 📚 Documentation

- Update README.md for user-facing changes
- Add docstrings to new functions and classes
- Update type hints for better IDE support
- Keep the changelog up to date

## 🤝 Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors. By participating, you agree to:

- Be respectful and inclusive
- Focus on constructive feedback
- Accept responsibility for mistakes
- Show empathy towards other contributors
- Help create a positive community

## 📞 Getting Help

- **Issues**: [GitHub Issues](https://github.com/yourusername/aws-free-guard/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/aws-free-guard/discussions)
- **Documentation**: [Wiki](https://github.com/yourusername/aws-free-guard/wiki)

## 🎯 Recognition

Contributors are recognized in:
- The changelog for each release
- GitHub's contributor insights
- Release notes

Thank you for contributing to AWS Free Guard! 🎉
