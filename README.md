# AWS Free Guard

[![CI](https://github.com/kafle1/aws-free-guard/workflows/CI/badge.svg)](https://github.com/kafle1/aws-free-guard/actions)
[![PyPI version](https://badge.fury.io/py/aws-free-guard.svg)](https://pypi.org/project/aws-free-guard/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A CLI tool that protects your AWS account from unexpected charges by enforcing free tier limits and providing account cleanup functionality.

## Features

- **40+ AWS Services** - Comprehensive analysis across EC2, S3, Lambda, RDS, VPC, and more
- **Multi-region support** - Analyze all regions simultaneously
- **Cost analysis** - Real-time cost monitoring and predictions
- **Safety first** - Dry-run mode and confirmation prompts
- **Smart cleanup** - Dependency-aware resource deletion

## Installation

```bash
pip install aws-free-guard
```

## Quick Start

1. **Configure AWS credentials:**
   ```bash
   export AWS_ACCESS_KEY_ID=your-access-key
   export AWS_SECRET_ACCESS_KEY=your-secret-key
   export AWS_DEFAULT_REGION=us-east-1
   ```

2. **Analyze your account:**
   ```bash
   aws-free-guard free --all-regions
   ```

3. **Clean unused resources:**
   ```bash
   aws-free-guard clean --dry-run --all-regions
   ```

## Commands

- `aws-free-guard free` - Analyze account and enforce free tier limits
- `aws-free-guard clean` - Remove unused resources safely
- `aws-free-guard cost` - Analyze costs and usage patterns
- `aws-free-guard status` - Show account health overview
- `aws-free-guard backup` - Backup resource configurations

## Options

- `--dry-run` - Preview changes without applying them
- `--all-regions` - Analyze/clean all regions
- `--services` - Specify services to analyze
- `--profile` - Use specific AWS profile
- `--region` - Use specific AWS region

## Requirements

- Python 3.9+
- AWS CLI configured with appropriate permissions

## License

MIT License - see [LICENSE](LICENSE) for details
