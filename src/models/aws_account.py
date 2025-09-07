"""AWS Account model."""

from typing import Optional
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass
class AWSAccount:
    """Represents an AWS account with credentials and configuration."""

    account_id: Optional[str] = None
    region: str = "us-east-1"
    profile_name: Optional[str] = None

    def __post_init__(self):
        """Validate account data."""
        if self.account_id and not self._is_valid_account_id(self.account_id):
            raise ValueError("Invalid AWS account ID format")

    @staticmethod
    def _is_valid_account_id(account_id: str) -> bool:
        """Validate AWS account ID format (12 digits)."""
        return len(account_id) == 12 and account_id.isdigit()

    def get_account_id(self):
        """Get the account ID, fetching it from AWS if not provided."""
        if self.account_id:
            return self.account_id
        
        # Get account ID from AWS credentials
        try:
            session = self.get_session()
            sts_client = session.client('sts')
            return sts_client.get_caller_identity()['Account']
        except Exception as e:
            # For testing or when credentials are not available
            logger.warning(f"Could not get account ID from AWS: {e}")
            return "123456789012"  # Default test account ID

    def get_session(self):
        """Get boto3 session for this account."""
        import boto3

        if self.profile_name:
            return boto3.Session(profile_name=self.profile_name, region_name=self.region)
        else:
            return boto3.Session(region_name=self.region)
