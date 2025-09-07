# AWS Free Guard - Comprehensive AWS Account Protection

[![CI](https://github.com/kafle1/aws-free-guard/workflows/CI/badge.svg)](https://github.com/kafle1/aws-free-guard/actions)
[![PyPI version](https://badge.fury.io/py/aws-free-guard.svg)](https://pypi.org/project/aws-free-guard/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/kafle1/aws-free-guard/branch/main/graph/badge.svg)](https://codecov.io/gh/kafle1/aws-free-guard)

A powerful CLI tool that protects your AWS account from unexpected charges by enforcing free tier limits and providing comprehensive account reset functionality.

## 🚀 Features

### Comprehensive Service Coverage
- **40+ AWS Services** analyzed and monitored
- **Multi-region support** - analyze all regions simultaneously
- **Real-time cost analysis** using AWS Cost Explorer
- **Machine learning predictions** for future costs
- **Advanced risk assessment** with confidence scores

### Smart Analysis & Recommendations
- **Usage pattern analysis** with growth rate predictions
- **Cost optimization suggestions** based on AWS best practices
- **Resource dependency mapping** to prevent accidental deletions
- **Backup coverage analysis** across all services
- **Security posture assessment**

### Safety First Design
- **Dry-run mode** for all operations
- **Confirmation prompts** for destructive actions
- **IAM protection** - never deletes critical IAM resources
- **Dependency-aware cleanup** - safe deletion order
- **Rollback capabilities** for failed operations

### Enterprise-Grade Features
- **JSON/CSV export** for compliance reporting
- **Scheduled monitoring** with alerts
- **Multi-account support** via AWS profiles
- **Audit logging** of all operations
- **Integration APIs** for CI/CD pipelines

## 📋 Prerequisites

- Python 3.11+
- AWS CLI configured with appropriate permissions
- Required Python packages (installed automatically)

## 🛠️ Installation

### From PyPI (Recommended)

```bash
pip install aws-free-guard
```

### From Source

```bash
# Clone the repository
git clone https://github.com/kafle1/aws-free-guard.git
cd aws-free-guard

# Install in development mode
pip install -e .
```

### Requirements

- Python 3.9+
- AWS CLI configured with appropriate permissions (see [AWS Permissions](#aws-permissions-required))

## ⚡ Quick Start

### 1. Configure AWS Credentials

```bash
# Option 1: Environment variables
export AWS_ACCESS_KEY_ID=your-access-key
export AWS_SECRET_ACCESS_KEY=your-secret-key
export AWS_DEFAULT_REGION=us-east-1

# Option 2: AWS CLI profile
aws configure --profile aws-free-guard
```

### 2. Run Comprehensive Analysis

```bash
# Analyze all services in all regions
./run-aws-free-guard.sh free --all-regions

# Analyze specific services
./run-aws-free-guard.sh free --services ec2 s3 lambda rds

# Get detailed analysis with recommendations
./run-aws-free-guard.sh free --detailed --output table
```

### 3. View Cost Analysis

```bash
# Analyze costs for the last 30 days
./run-aws-free-guard.sh cost --days 30

# Export cost data to JSON
./run-aws-free-guard.sh cost --output json > costs.json
```

### 4. Clean Account (Safe Mode)

```bash
# Dry-run cleanup to see what would be deleted
./run-aws-free-guard.sh clean --dry-run --all-regions

# Actually clean the account (with confirmation)
./run-aws-free-guard.sh clean --all-regions
```

## 📊 Command Reference

### `free` - Analyze Account & Enforce Free Tier

```bash
aws-free-guard free [OPTIONS]

Options:
  --services TEXT           Specific services to analyze
  --all-regions            Analyze all regions
  --output [table|json|summary]  Output format
  --detailed               Show detailed analysis
  --profile TEXT           AWS profile to use
  --region TEXT            AWS region to use
```

### `clean` - Clean Account Resources

```bash
aws-free-guard clean [OPTIONS]

Options:
  --services TEXT           Specific services to clean
  --all-regions            Clean all regions
  --dry-run                Preview changes without applying
  --force                  Skip confirmation prompts
  --profile TEXT           AWS profile to use
  --region TEXT            AWS region to use
```

### `cost` - Analyze Costs & Usage

```bash
aws-free-guard cost [OPTIONS]

Options:
  --days INTEGER           Days to analyze (default: 30)
  --output [table|json]    Output format
  --profile TEXT           AWS profile to use
  --region TEXT            AWS region to use
```

### `status` - Account Health Check

```bash
aws-free-guard status [OPTIONS]

Options:
  --profile TEXT           AWS profile to use
  --region TEXT            AWS region to use
```

### `backup` - Backup Resources

```bash
aws-free-guard backup [OPTIONS] BACKUP_DIR

Options:
  --services TEXT           Specific services to backup
  --profile TEXT            AWS profile to use
  --region TEXT            AWS region to use
```

## 🔍 Supported AWS Services

### Core Services
- **EC2** - Instances, volumes, snapshots, AMIs, key pairs
- **S3** - Buckets, objects, storage classes, lifecycle rules
- **Lambda** - Functions, layers, event sources
- **RDS** - Instances, snapshots, parameter groups, option groups
- **VPC** - Networks, subnets, security groups, NAT gateways, endpoints

### Advanced Services
- **IAM** - Users, roles, policies, groups (conservative cleanup)
- **CloudFormation** - Stacks and nested stacks
- **DynamoDB** - Tables, global tables, backups
- **Kinesis** - Streams, firehose, analytics
- **SNS/SQS** - Topics, queues, subscriptions
- **API Gateway** - REST APIs, WebSocket APIs, usage plans
- **CloudFront** - Distributions, origins, behaviors
- **Route53** - Hosted zones, records
- **ELB/ALB** - Load balancers, target groups
- **ECS/EKS** - Clusters, services, pods
- **EMR** - Clusters, instance groups
- **Glue** - Databases, tables, crawlers, jobs
- **Redshift** - Clusters, snapshots, parameter groups
- **ElastiCache** - Clusters, replication groups
- **Batch** - Job queues, compute environments
- **Step Functions** - State machines, executions
- **EventBridge** - Rules, event buses
- **Systems Manager** - Parameters, documents
- **Secrets Manager** - Secrets
- **KMS** - Keys, grants
- **WAF/Shield** - Web ACLs, rules, protections
- **GuardDuty** - Detectors, findings
- **Inspector** - Assessment targets, templates
- **Config** - Rules, conformance packs
- **Organizations** - Accounts, policies
- **Support** - Cases, trusted advisor
- **Trusted Advisor** - Recommendations

## 🎯 Free Tier Limits Enforced

### EC2
- 750 hours/month for t2.micro instances
- 30GB EBS storage
- Basic monitoring (CloudWatch)

### S3
- 5GB standard storage
- 20,000 GET requests
- 2,000 PUT requests

### Lambda
- 1M requests/month
- 400,000 GB-seconds compute time
- 5GB storage for layers

### RDS
- 750 hours/month for db.t2.micro
- 20GB storage
- Basic monitoring

### And many more...

## ⚠️ Safety Features

### Conservative IAM Handling
- Never deletes IAM users, roles, or policies automatically
- Only suggests cleanup for obvious test resources
- Requires explicit confirmation for any IAM changes

### Dependency-Aware Cleanup
- Analyzes resource dependencies before deletion
- Prevents deletion of resources that others depend on
- Safe deletion order to avoid orphaned resources

### Backup Integration
- Analyzes existing backup coverage
- Suggests backup strategies before cleanup
- Integrates with AWS Backup service

### Rollback Capabilities
- Tracks all changes for potential rollback
- CloudFormation stack-based deployments where possible
- Manual rollback scripts for complex scenarios

## 📈 Advanced Features

### Cost Prediction Engine
- Machine learning-based cost forecasting
- Usage pattern analysis with trend detection
- Seasonal cost variation modeling
- Budget vs. actual cost comparisons

### Risk Assessment
- Multi-factor risk scoring
- Confidence intervals for predictions
- Historical risk pattern analysis
- Compliance posture assessment

### Automated Optimization
- Right-sizing recommendations
- Storage class optimization
- Reserved instance suggestions
- Unused resource identification

### Monitoring & Alerting
- Real-time cost monitoring
- Budget threshold alerts
- Usage anomaly detection
- Scheduled compliance checks

## 🔧 Configuration

### Environment Variables

```bash
# AWS Credentials
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_DEFAULT_REGION=us-east-1

# Tool Configuration
AWS_FREE_GUARD_LOG_LEVEL=INFO
AWS_FREE_GUARD_DRY_RUN=true
AWS_FREE_GUARD_BACKUP_DIR=./backups
```

### AWS Permissions Required

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:*",
        "s3:*",
        "lambda:*",
        "rds:*",
        "vpc:*",
        "iam:List*",
        "iam:Get*",
        "cloudformation:*",
        "dynamodb:*",
        "kinesis:*",
        "sns:*",
        "sqs:*",
        "apigateway:*",
        "cloudfront:*",
        "route53:*",
        "elasticloadbalancing:*",
        "ecs:*",
        "eks:*",
        "emr:*",
        "glue:*",
        "redshift:*",
        "elasticache:*",
        "batch:*",
        "states:*",
        "events:*",
        "ssm:*",
        "secretsmanager:*",
        "kms:*",
        "waf:*",
        "shield:*",
        "guardduty:*",
        "inspector:*",
        "config:*",
        "organizations:*",
        "support:*",
        "ce:*"
      ],
      "Resource": "*"
    }
  ]
}
```

## 📊 Output Examples

### Comprehensive Analysis
```
🔍 Starting comprehensive AWS analysis...
✅ Account: 123456789012
📍 Region: us-east-1
🔧 Profile: default

AWS Resources in us-east-1
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━┓
┃ Service       ┃ Resources  ┃ Status  ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━┩
│ EC2           │ 0          │ ✅ OK   │
│ S3            │ 2          │ ⚠️ Check│
│ Lambda        │ 0          │ ✅ OK   │
│ RDS           │ 0          │ ✅ OK   │
│ VPC           │ 1          │ ⚠️ Check│
└───────────────┴────────────┴─────────┘

💡 Recommendations:
  • Delete 2 empty S3 buckets
  • Review NAT Gateway charges in VPC

💰 Current Monthly Cost: $0.00
🔮 Predicted Next Month: $0.00
✅ LOW RISK - Account appears safe
```

### Cost Analysis
```
💰 Total Monthly Cost: $12.34
Cost Breakdown by Service
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Service               ┃ Cost   ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ EC2 - Running Hours   │ $8.50  │
│ S3 - Storage          │ $2.80  │
│ CloudWatch - Metrics  │ $1.04  │
└───────────────────────┴────────┘
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add comprehensive tests
4. Ensure all lint checks pass
5. Submit a pull request

## 📝 License

MIT License - see LICENSE file for details

## 🆘 Support

- **Issues**: GitHub Issues
- **Documentation**: Wiki
- **Community**: GitHub Discussions

## 🔄 Changelog

### v2.0.0 - Comprehensive Overhaul
- Added 40+ AWS service support
- Multi-region analysis
- Cost prediction engine
- Advanced risk assessment
- Machine learning features
- Enterprise-grade safety features

### v1.0.0 - Initial Release
- Basic EC2, S3, Lambda, RDS support
- Single-region analysis
- Simple cost estimation
- Basic safety features

---

**⚠️ Disclaimer**: This tool is provided as-is. Always test with `--dry-run` first and backup critical resources before running cleanup operations.
