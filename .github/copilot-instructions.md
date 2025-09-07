# GitHub Copilot Instructions for AWS Free Guard

## Project Overview
AWS Free Guard is a Python CLI tool that protects AWS accounts from unexpected charges by enforcing free tier limits and providing account reset functionality.

## Key Technologies
- **Python 3.11+**: Core language
- **Click**: CLI framework for command-line interface
- **boto3**: AWS SDK for Python
- **Rich**: Modern console UI with colors and progress bars
- **pytest**: Testing framework

## Architecture
- `src/cli/`: Command-line interface code
- `src/lib/`: Core business logic for AWS operations
- `src/models/`: Data models for AWS resources
- `tests/`: Unit and integration tests

## Development Guidelines
- Follow TDD: Write tests before implementation
- Use type hints for all functions
- Handle AWS errors gracefully with user-friendly messages
- Use Rich for beautiful console output
- Log structured information for debugging

## Common Patterns
- AWS service clients: `boto3.client('service')`
- CLI commands: `@click.command()` decorators
- Error handling: Try/except with specific AWS exceptions
- Progress bars: `rich.progress` for long operations
- Logging: `logging` module with JSON format

## AWS Services to Handle
- EC2: Instances, volumes, snapshots
- S3: Buckets, objects
- Lambda: Functions, layers
- RDS: Databases, snapshots
- VPC: Networks, subnets, security groups
- IAM: Users, roles, policies (with caution)

## Free Tier Limits
Research and implement limits for:
- EC2: 750 hours/month
- S3: 5GB storage, 20,000 GET requests
- Lambda: 1M requests, 400,000 GB-seconds
- RDS: 750 hours for db.t2.micro
- And many more...

## Safety First
- Always use dry-run mode for testing
- Confirm destructive operations
- Validate credentials before operations
- Handle partial failures gracefully
- Never delete IAM resources without explicit confirmation

## Testing Strategy
- Unit tests for individual functions
- Integration tests with mocked AWS services
- E2E tests with test AWS account
- Test both success and failure scenarios

## Code Style
- Black for formatting
- isort for import sorting
- flake8 for linting
- mypy for type checking
