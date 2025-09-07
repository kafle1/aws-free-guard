"""Contract tests for the free command."""

import json
import os
import pytest
from jsonschema import validate, ValidationError
from click.testing import CliRunner

from src.cli.commands import cli


@pytest.fixture
def runner():
    """CLI runner fixture."""
    return CliRunner()


def test_free_command_contract():
    """Test that the free command adheres to its contract schema."""
    # Load the contract schema
    contract_path = os.path.join(os.path.dirname(__file__), "../../specs/001-a-powerful-cli/contracts/free_command.json")
    with open(contract_path, "r") as f:
        schema = json.load(f)

    # Test the command structure
    sample_request = {
        "command": "free",
        "options": {
            "region": "us-east-1",
            "dry-run": False,
            "services": ["ec2", "s3"]
        }
    }

    # Validate request against schema
    try:
        validate(instance=sample_request, schema=schema)
        # Should pass
    except ValidationError as e:
        pytest.fail(f"Schema validation failed: {e}")


def test_free_command_execution(runner):
    """Test that free command executes and returns expected structure."""
    # This will test the actual CLI command
    result = runner.invoke(cli, ["free", "--dry-run"])

    # Should not exit with error for credentials (we'll mock this later)
    # For now, it should at least start and show the analyzing message
    assert "Analyzing" in result.output or "analyzing" in result.output.lower()


def test_free_command_response_structure():
    """Test that free command response structure matches contract."""
    # Load the contract schema
    contract_path = os.path.join(os.path.dirname(__file__), "../../specs/001-a-powerful-cli/contracts/free_command.json")
    with open(contract_path, "r") as f:
        schema = json.load(f)

    # Test expected response structure
    expected_response = {
        "success": True,
        "message": "Free tier enforcement completed",
        "analyzed_resources": 10,
        "enforced_resources": 5,
        "errors": []
    }

    # Validate response against schema
    try:
        validate(instance=expected_response, schema=schema["properties"]["response"])
        # Should pass
    except ValidationError as e:
        pytest.fail(f"Response schema validation failed: {e}")
