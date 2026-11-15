#!/bin/sh
# Cross-platform coordinator build; never moves another assistant's failed files.
set -e
cd "$(dirname "$0")/.."
exec python scripts/merge_batch.py "$@"
