#!/bin/bash
# Entrypoint script for fks_futures

set -e

# Default values
SERVICE_NAME=${SERVICE_NAME:-fks_futures}
SERVICE_PORT=${SERVICE_PORT:-8015}
HOST=${HOST:-0.0.0.0}

echo "Starting ${SERVICE_NAME} on ${HOST}:${SERVICE_PORT}"

# Run the service from src directory
exec python -m src.main
