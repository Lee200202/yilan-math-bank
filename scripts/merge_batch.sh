#!/bin/sh
# Coordinator merge for helper transcriptions: check every new/changed whole-paper file,
# park failing ones outside the transcribed folders, rebuild data + font subset, run tests.
# Usage: sh scripts/merge_batch.sh
set -e
cd "$(dirname "$0")/.."
PARK=research/targets/parked
mkdir -p "$PARK"
FILES=$(git status --porcelain --untracked-files=all research/metro/transcribed research/yilan/transcribed | cut -c4-)
[ -z "$FILES" ] && { echo "no new files"; exit 0; }
for f in $FILES; do
  if ! python scripts/check_transcript.py "$f" >/dev/null 2>&1; then
    python scripts/check_transcript.py "$f" || true
    mv "$f" "$PARK/"
    echo "PARKED $f"
  fi
done
python scripts/prepare_data.py | tail -1 | cut -c1-90
python scripts/subset_font.py | tail -1 | cut -c1-60
python scripts/readme_metro.py >/dev/null
npm test 2>&1 | grep -E "^(ℹ (pass|fail)|✖)"
git status --porcelain --untracked-files=all research/metro/transcribed research/yilan/transcribed | wc -l
