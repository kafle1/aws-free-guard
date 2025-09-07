"""Main entry point for AWS Free Guard CLI."""

import os
from pathlib import Path

from src.cli.commands import cli


def load_env_file():
    """Load environment variables from .env file."""
    env_path = Path(__file__).parent.parent.parent / ".env"
    if env_path.exists():
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    os.environ[key] = value


def main():
    """Main entry point."""
    # Load environment variables from .env file if it exists
    load_env_file()
    
    cli()


if __name__ == "__main__":
    main()
