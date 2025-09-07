"""AWS Resource model."""

from typing import Dict, Any
from dataclasses import dataclass
from enum import Enum


class ResourceStatus(Enum):
    """Status of AWS resource regarding free tier."""
    FREE = "free"
    CHARGED = "charged"
    UNKNOWN = "unknown"


@dataclass
class AWSResource:
    """Represents an AWS resource with free tier information."""

    resource_id: str
    service: str
    resource_type: str
    region: str
    current_usage: Dict[str, Any] = None
    free_tier_limit: Dict[str, Any] = None
    status: ResourceStatus = ResourceStatus.UNKNOWN

    def __post_init__(self):
        """Validate resource data."""
        if not self.resource_id:
            raise ValueError("Resource ID is required")
        if not self.service:
            raise ValueError("Service is required")
        if not self.resource_type:
            raise ValueError("Resource type is required")

        if self.current_usage is None:
            self.current_usage = {}
        if self.free_tier_limit is None:
            self.free_tier_limit = {}

    def is_within_free_tier(self) -> bool:
        """Check if resource usage is within free tier limits."""
        if not self.free_tier_limit:
            return False

        # Simple check - in real implementation, this would be more complex
        for key, limit in self.free_tier_limit.items():
            if key in self.current_usage:
                usage = self.current_usage[key]
                if isinstance(limit, (int, float)) and isinstance(usage, (int, float)):
                    if usage > limit:
                        return False
        return True

    def update_status(self):
        """Update the resource status based on current usage."""
        if self.is_within_free_tier():
            self.status = ResourceStatus.FREE
        else:
            self.status = ResourceStatus.CHARGED
