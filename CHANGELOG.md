# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-09-07

### Added
- **Initial release** of AWS Free Guard CLI tool
- **40+ AWS Services support** - Comprehensive analysis across EC2, S3, Lambda, RDS, VPC, and more
- **Multi-region support** - Analyze all AWS regions simultaneously
- **Cost analysis** - Real-time cost monitoring and predictions
- **Safety features**:
  - Dry-run mode for all operations
  - Confirmation prompts for destructive actions
  - Dependency-aware resource deletion
- **CLI Commands**:
  - `aws-free-guard free` - Analyze account and enforce free tier limits
  - `aws-free-guard clean` - Remove unused resources safely
  - `aws-free-guard cost` - Analyze costs and usage patterns
  - `aws-free-guard status` - Show account health overview
  - `aws-free-guard backup` - Backup resource configurations
- **Rich console output** with colors and progress bars
- **Comprehensive testing** with pytest and coverage reporting
- **Type checking** with mypy
- **Code quality** tools (black, isort, flake8)
- **CI/CD pipeline** with GitHub Actions supporting Python 3.9-3.12

### Changed
- Simplified README to clean and minimal version

### Technical Details
- **Python 3.9+** compatibility
- **Dependencies**: Click, boto3, Rich, pytest
- **License**: MIT
- **Build system**: setuptools with pyproject.toml

### Infrastructure
- GitHub Actions CI/CD pipeline
- Code coverage reporting with Codecov
- Automated testing across multiple Python versions
- Automated package building and publishing

---

## Types of changes
- `Added` for new features
- `Changed` for changes in existing functionality
- `Deprecated` for soon-to-be removed features
- `Removed` for now removed features
- `Fixed` for any bug fixes
- `Security` in case of vulnerabilities
