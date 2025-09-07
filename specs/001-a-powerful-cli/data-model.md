# Data Model: AWS Free Guard CLI Tool

## Entities

### AWS Account
- **Fields**:
  - account_id: string (AWS account ID)
  - region: string (default region)
  - credentials: dict (AWS credentials - not stored, used for auth)
- **Validation**: Valid AWS account ID format, credentials verified
- **Relationships**: Has many AWS Resources

### AWS Resource
- **Fields**:
  - resource_id: string (unique identifier)
  - service: string (e.g., 'ec2', 's3')
  - resource_type: string (e.g., 'instance', 'bucket')
  - region: string
  - current_usage: dict (current metrics)
  - free_tier_limit: dict (service-specific limits)
  - status: string ('free', 'charged', 'unknown')
- **Validation**: Service and type must be valid AWS services
- **Relationships**: Belongs to AWS Account

### Free Tier Limit
- **Fields**:
  - service: string
  - resource_type: string
  - limit_value: number
  - limit_unit: string (e.g., 'GB', 'hours', 'requests')
  - always_free: boolean (true if no charges ever)
- **Validation**: Positive limit values
- **Relationships**: Referenced by AWS Resource

### Operation Result
- **Fields**:
  - operation: string ('free', 'clean')
  - success: boolean
  - message: string
  - affected_resources: list of resource_ids
  - errors: list of error messages
- **Validation**: Operation must be valid command
- **Relationships**: N/A

## State Transitions

### AWS Resource Status
- unknown → free (after analysis)
- unknown → charged (if exceeds limits)
- free → charged (if usage increases)
- charged → free (after enforcement)

### Operation Flow
- idle → analyzing (start operation)
- analyzing → enforcing (for free command)
- analyzing → cleaning (for clean command)
- enforcing/cleaning → completed (success)
- enforcing/cleaning → failed (error)

## Validation Rules
- All AWS resources must be identifiable by service and type
- Free tier limits must be up-to-date with AWS documentation
- Operations must handle partial failures gracefully
- Credentials must be validated before any AWS API calls
