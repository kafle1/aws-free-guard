"""Free Tier Limit model."""

from typing import Dict, Any
from dataclasses import dataclass


@dataclass
class FreeTierLimit:
    """Represents free tier limits for AWS services."""

    service: str
    resource_type: str
    limit_value: float
    limit_unit: str
    always_free: bool = False
    additional_limits: Dict[str, Any] = None

    def __post_init__(self):
        """Validate limit data."""
        if not self.service:
            raise ValueError("Service is required")
        if not self.resource_type:
            raise ValueError("Resource type is required")
        if self.limit_value < 0:
            raise ValueError("Limit value must be non-negative")

        if self.additional_limits is None:
            self.additional_limits = {}

    def is_exceeded(self, usage: float) -> bool:
        """Check if usage exceeds the limit."""
        if self.always_free:
            return False
        return usage > self.limit_value

    @classmethod
    def get_common_limits(cls) -> Dict[str, 'FreeTierLimit']:
        """Get common AWS free tier limits."""
        return {
            "ec2_instances": cls(
                service="ec2",
                resource_type="instances",
                limit_value=750,  # hours per month
                limit_unit="hours",
                always_free=False
            ),
            "s3_storage": cls(
                service="s3",
                resource_type="storage",
                limit_value=5,  # GB
                limit_unit="GB",
                always_free=False
            ),
            "s3_requests": cls(
                service="s3",
                resource_type="requests",
                limit_value=20000,  # GET requests
                limit_unit="requests",
                always_free=False
            ),
            "lambda_requests": cls(
                service="lambda",
                resource_type="requests",
                limit_value=1000000,  # requests per month
                limit_unit="requests",
                always_free=False
            ),
            "rds_db_hours": cls(
                service="rds",
                resource_type="db_instances",
                limit_value=750,  # hours per month
                limit_unit="hours",
                always_free=False
            )
        }
