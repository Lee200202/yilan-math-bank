"""Re-apply a finished release commit on top of the newest origin/main (when `git push` is rejected because others pushed).

Usage (from the release worktree, HEAD = my release commit):
    python -X utf8 scripts/reapply_release.py <ids-file-in-commit> <batch-prefix> <batch-label>
e.g. python -X utf8 scripts/reapply_release.py handoff/batches/20261119-o6w19-ids.txt 20261119-o6w19 20261119-v120

What it does: keeps my commit on branch `my-release`, detaches onto origin/main, restores my transcripts / overrides /
batch reports from that branch, re-approves the ids, bumps the version, rebuilds (merge_batch), re-applies the CLAIMS update
and the VERIFICATION.md section from my commit, regenerates the handoff snapshot and commits. Push afterwards:
    git push origin HEAD:main HEAD:codex/initial-site
Nothing is deleted or force-pushed; if it fails halfway, `git checkout my-release` returns to my commit.
"""
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PY = [sys.executable, '-X', 'utf8']


def sh(*args, check=True, capture=True):
    r = subprocess.run(list(args), cwd=ROOT, capture_output=capture, text=True, encoding='utf-8', errors='replace')
    if check and r.returncode:
        raise SystemExit('FAILED: %s\n%s%s' % (' '.join(args), r.stdout[-800:], r.stderr[-800:]))
    return r.stdout


def main(ids_file, prefix, label):
    sh('git', 'branch', '-f', 'my-release', 'HEAD')
    sh('git', 'fetch', '-q', 'origin')
    sh('git', 'checkout', '-q', '--detach', 'origin/main')
    ids = [i.strip() for i in sh('git', 'show', f'my-release:{ids_file}').split() if i.strip()]
    (ROOT / 'scratch/ids.txt').write_text('\n'.join(ids) + '\n', encoding='utf-8', newline='\n')
    batch_files = [f for f in sh('git', 'ls-tree', '-r', '--name-only', 'my-release', 'handoff/batches').splitlines() if prefix in f]
    paths = ['research/metro/slot-overrides.json', 'research/metro/office_extract.py'] + batch_files
    paths += [f'research/metro/transcribed/{i}.json' for i in ids]
    sh('git', 'checkout', 'my-release', '--', *paths)
    res = json.loads(sh(*PY, 'scripts/release_queue.py', *ids))
    print('approved', len(res['accepted']), 'rejected', res['rejected'])
    html = (ROOT / 'public/index.html').read_text(encoding='utf-8')
    cur = re.search(r'\d+-metro-v(\d+)', html)
    old = cur.group(0)
    new = old.rsplit('v', 1)[0] + 'v%d' % (int(cur.group(1)) + 1)
    for base in ('public', 'scripts'):
        for p in (ROOT / base).rglob('*'):
            if p.is_file() and p.suffix in ('.mjs', '.html', '.css', '.js', '.py'):
                try:
                    t = p.read_text(encoding='utf-8')
                except Exception:
                    continue
                if old in t:
                    p.write_text(t.replace(old, new), encoding='utf-8', newline='')
    print('version', old, '->', new)
    out = sh(*PY, 'scripts/merge_batch.py', check=False)
    print([l for l in out.splitlines() if l.startswith(('ℹ pass', 'ℹ fail', 'Static build'))])
    claims_p = ROOT / 'handoff/CLAIMS.json'
    d = json.loads(claims_p.read_text(encoding='utf-8'))
    have = {x['paperId']: x for x in d['claims']}
    for i in ids:
        if i in have:
            have[i].update(status='published-text', batch=label)
        else:
            d['claims'].append({'agent': 'claude-helper', 'paperId': i, 'status': 'published-text', 'batch': label})
    claims_p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    mine = sh('git', 'show', 'my-release:VERIFICATION.md')
    k = mine.rfind('\n## v')
    section = mine[k:].rstrip('\n')
    section = re.sub(r'^## v\d+（\d+-metro-v\d+）', '## ' + 'v%d（%s）' % (int(cur.group(1)) + 1, new), section.lstrip('\n'), count=1)
    with open(ROOT / 'VERIFICATION.md', 'a', encoding='utf-8', newline='\n') as fh:
        fh.write('\n' + section + '\n')
    sh(*PY, 'scripts/handoff.py', '--write', check=False)
    add = ['public', 'scripts', 'tests', 'research/metro/slot-overrides.json', 'research/release-transcripts.json',
           'research/metro/office_extract.py', 'VERIFICATION.md', 'handoff'] + [f'research/metro/transcribed/{i}.json' for i in ids]
    sh('git', 'add', *add)
    sh('git', 'commit', '-q', '-m', f'Deploy {new.split("-")[-1]}: {label} ({len(ids)} papers)\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>')
    print(sh('git', 'log', '--oneline', '-1').strip())


if __name__ == '__main__':
    main(*sys.argv[1:4])
