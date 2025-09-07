"""Operation Result model."""

from typing import List, Optional
from dataclasses import dataclass


@dataclass
class OperationResult:
    """Represents the result of an AWS operation."""

    operation: str
    success: bool
    message: str
    affected_resources: List[str] = None
    errors: List[str] = None
    execution_time: Optional[float] = None

    def __post_init__(self):
        """Initialize lists if None."""
        if self.affected_resources is None:
            self.affected_resources = []
        if self.errors is None:
            self.errors = []

    def add_error(self, error: str):
        """Add an error to the result."""
        self.errors.append(error)
        self.success = False

    def add_affected_resource(self, resource_id: str):
        """Add an affected resource."""
        self.affected_resources.append(resource_id)

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "operation": self.operation,
            "success": self.success,
            "message": self.message,
            "affected_resources": self.affected_resources,
            "errors": self.errors,
            "execution_time": self.execution_time
        }

    @classmethod
    def success_result(cls, operation: str, message: str) -> 'OperationResult':
        """Create a successful result."""
        return cls(operation=operation, success=True, message=message)

    @classmethod
    def error_result(cls, operation: str, message: str, errors: List[str] = None) -> 'OperationResult':
        """Create an error result."""
        if errors is None:
            errors = []
        return cls(operation=operation, success=False, message=message, errors=errors)
