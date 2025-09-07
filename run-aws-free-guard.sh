#!/bin/bash
# Load AWS credentials from .env file and run AWS Free Guard

# Load environment variables from .env file
if [ -f ".env" ]; then
    export $(cat .env | xargs)
fi

# Run AWS Free Guard with the loaded credentials
exec aws-free-guard "$@"
