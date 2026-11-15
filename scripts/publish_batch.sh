#!/bin/sh
# The v13/v14 automatic broad git-add/push workflow is retired.
set -e
cd "$(dirname "$0")/.."
echo "Automatic publication retired: use AI_HANDOFF.md and verify the batch acceptance manifest."
echo "Run python scripts/verify_release.py handoff/batches/<batch>/acceptance.json before an explicit commit/push."
exit 2
