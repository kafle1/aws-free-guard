"""Integration tests for the clean command user flow."""

import pytest
from click.testing import CliRunner
from src.cli.commands import cli


@pytest.fixture
def runner():
    """CLI runner fixture."""
    return CliRunner()


def test_clean_command_basic_flow(runner):
    """Test basic clean command execution flow."""
    # Command should prompt for confirmation and abort without input
    result = runner.invoke(cli, ["clean"])
    
    # Should exit with confirmation prompt
    assert result.exit_code == 1  # Aborted
    assert "delete resources" in result.output.lower()
    assert "continue" in result.output.lower()


def test_clean_command_dry_run(runner):
    """Test clean command with dry-run option."""
    result = runner.invoke(cli, ["clean", "--dry-run"])

    # Should succeed even with credential issues in dry-run mode
    assert result.exit_code == 0
    # The command runs but may show credential errors
    assert "cleaning" in result.output.lower()


def test_clean_command_with_confirm(runner):
    """Test clean command with confirm option."""
    result = runner.invoke(cli, ["clean", "--confirm"])

    # Should succeed with confirm flag
    assert result.exit_code == 0
    assert "cleaning" in result.output.lower() or "deleting" in result.output.lower()


def test_clean_command_help(runner):
    """Test clean command help output."""
    result = runner.invoke(cli, ["clean", "--help"])

    # Help should work even without full implementation
    assert result.exit_code == 0
    assert "clean" in result.output.lower()
    assert "dry-run" in result.output or "confirm" in result.output
