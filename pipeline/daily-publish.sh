#!/bin/bash
# Daily book publishing — local runner.
# Wraps `python -m bookwriter daily` with env setup.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

echo "=== URANTiOS Daily Book Publisher ==="
echo "Date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "Repo: $REPO_ROOT"
echo ""

# Load secrets if available
if [ -f "$HOME/.openclaw/secrets.env" ]; then
    set -a
    # shellcheck disable=SC1091
    source "$HOME/.openclaw/secrets.env"
    set +a
    echo "Loaded secrets from ~/.openclaw/secrets.env"
fi

# Run the daily publisher
cd "$REPO_ROOT"
exec python3 -m bookwriter daily "$@"
