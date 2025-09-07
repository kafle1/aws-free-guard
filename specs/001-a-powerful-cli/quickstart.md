# Quickstart: AWS Free Guard CLI Tool

## Installation

1. **Prerequisites**:
   - Python 3.11+
   - AWS CLI configured with credentials
   - pip

2. **Install the tool**:
   ```bash
   pip install aws-free-guard
   ```

3. **Verify installation**:
   ```bash
   aws-free-guard --version
   ```

## Configuration

1. **AWS Credentials**:
   The tool uses standard AWS credential chain. Configure via:
   ```bash
   aws configure
   ```

2. **Permissions**:
   Ensure your AWS user has the following permissions:
   - Read access to all services
   - Write access to services you want to modify
   - IAM permissions for credential validation

## Basic Usage

### Make Account Free
```bash
aws-free-guard free
```
This command analyzes your AWS account and enforces free tier limits on all resources.

### Clean Account
```bash
aws-free-guard clean
```
This command deletes all resources and resets your account to like-new state.

**Warning**: This operation is destructive. Use `--dry-run` first.

## Advanced Usage

### Dry Run
```bash
aws-free-guard free --dry-run
aws-free-guard clean --dry-run
```

### Specific Services
```bash
aws-free-guard free --services ec2 s3
aws-free-guard clean --services ec2 s3
```

### Specific Region
```bash
aws-free-guard free --region us-east-1
```

### Skip Confirmation
```bash
aws-free-guard clean --confirm
```

## Examples

### Scenario 1: New Account Setup
```bash
# Configure AWS
aws configure

# Make sure account is free
aws-free-guard free

# Start experimenting safely
```

### Scenario 2: Clean Up After Testing
```bash
# Preview what will be deleted
aws-free-guard clean --dry-run

# Confirm and clean
aws-free-guard clean
```

## Troubleshooting

- **Permission Denied**: Check AWS credentials and IAM permissions
- **Region Issues**: Specify region with `--region`
- **Timeout**: Some operations may take time for large accounts
- **Errors**: Check logs with `--verbose` flag

## Next Steps

- Read the full documentation
- Join the community
- Report issues on GitHub
