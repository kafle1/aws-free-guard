"""Integration tests for the free command user flow."""

import pytest
from click.testing import CliRunner
from src.cli.commands import cli


@pytest.fixture
def runner():
    """CLI runner fixture."""
    return CliRunner()


def test_free_command_basic_flow(runner):
    """Test basic free command execution flow."""
    result = runner.invoke(cli, ["free"])

    # Should succeed and show enforcement results
    assert result.exit_code == 0
    assert "analyzing" in result.output.lower() or "free" in result.output.lower()


def test_free_command_dry_run(runner):
    """Test free command with dry-run option."""
    result = runner.invoke(cli, ["free", "--dry-run"])

    # Should succeed with dry-run
    assert result.exit_code == 0
    assert "analyzing" in result.output.lower() or "dry run" in result.output.lower()


def test_free_command_with_region(runner):
    """Test free command with specific region."""
    result = runner.invoke(cli, ["--region", "us-east-1", "free"])

    # Should succeed with region
    assert result.exit_code == 0
    assert "us-east-1" in result.output or "region" in result.output.lower()


def test_free_command_help(runner):
    """Test free command help output."""
    result = runner.invoke(cli, ["free", "--help"])

    # Help should work even without full implementation
    assert result.exit_code == 0
    assert "free" in result.output.lower()
    assert "dry-run" in result.output or "region" in result.output
