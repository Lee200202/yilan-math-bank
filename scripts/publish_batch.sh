#!/bin/sh
# After merge_batch.sh + QA: commit exactly the transcriptions that went into the build,
# bump the cache version, push main and codex/initial-site.
# Usage: sh scripts/publish_batch.sh "commit subject"
set -e
cd "$(dirname "$0")/.."
python - <<'EOF'
import json, subprocess
p = json.load(open('public/data/papers.json', encoding='utf-8'))
built = {x['completionEvidence'] for x in p if str(x.get('completionEvidence') or '').startswith('research/')}
st = subprocess.run(['git', 'status', '--porcelain', '--untracked-files=all', 'research/metro/transcribed', 'research/yilan/transcribed'],
                    capture_output=True, text=True, encoding='utf-8').stdout.splitlines()
files = [l[3:] for l in st if l[3:] in built]
open('research/targets/batch.txt', 'w', newline='\n').write('\n'.join(files) + '\n')
print(len(files), 'transcriptions in this batch')
EOF
OLD=$(grep -o "20261115-metro-v[0-9]*" public/index.html | head -1)
N=$(echo "$OLD" | sed 's/.*-v//')
NEW="20261115-metro-v$((N + 1))"
sed -i "s/$OLD/$NEW/g" public/index.html public/app.mjs public/units-ui.mjs scripts/qa-requested-papers.mjs
git add $(cat research/targets/batch.txt) public README.md VERIFICATION.md tests scripts research/targets/*.json research/TRANSCRIBE_GUIDE.md 2>/dev/null
git commit -q -m "$1 ($NEW)" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push -q origin HEAD:main
git push -q origin HEAD:codex/initial-site
git log --oneline -1
python -c "import json;c=json.load(open('public/data/coverage.json',encoding='utf-8'));print(c['reviewedQuestions'],c['paperWorkflow'])"
