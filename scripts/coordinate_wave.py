"""Coordinator pipeline for finished helper transcriptions (one command instead of ~8).

  python scripts/coordinate_wave.py <wave> [<wave> ...]   e.g.  python scripts/coordinate_wave.py w4 w5

For every research/targets/<wave>-<k>.json entry whose outFile exists and is not yet approved (or changed):
  1. inline SVG CSS / bad root attributes            (scripts/inline_svg_css.py --write)
  2. validate each file                              (scripts/check_transcript.py)  -> failing files are listed and left out
  3. approve the passing files for release           (scripts/release_queue.py)
  4. rebuild data, font subset, tests, static build  (scripts/merge_batch.py)
  5. PDF export check of every new paper             (scripts/qa_metro.py; needs the local server, see below)
  6. widen clipped figure frames and recheck         (scripts/fix_svg_viewbox.py)
Writes handoff/batches/<date>-<wave>/targets.txt, pdf-acceptance.json and prints a summary.
It never commits, pushes or edits docs: you still look at a few exported pages (qa/metro/<id>-p1.png), write the
source-issues report, bump the version, commit and push (see skills/exam-bank-coordinator/SKILL.md).

Needs the preview server on http://127.0.0.1:4173 (start it with `node scripts/server.mjs`).
"""
import datetime
import hashlib
import json
import pathlib
import subprocess
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
PY = [sys.executable, '-X', 'utf8']


def run(args, check=True):
    return subprocess.run(PY + args, cwd=ROOT, capture_output=True, text=True, encoding='utf-8', check=False)


def sha(path):
    return hashlib.sha256(path.read_bytes().replace(b'\r\n', b'\n')).hexdigest()


def main(waves):
    policy = json.loads((ROOT / 'research/release-transcripts.json').read_text(encoding='utf-8'))['papers']
    entries = []
    for wave in waves:
        for f in sorted((ROOT / 'research/targets').glob(f'{wave}-[0-9]*.json')):
            if f.stem.endswith('skipped'):
                continue
            for t in json.loads(f.read_text(encoding='utf-8-sig')):
                out = ROOT / t['outFile']
                if out.exists() and (t['paperId'] not in policy or policy[t['paperId']]['transcriptSha256'] != sha(out)):
                    entries.append((t['paperId'], out))
    if not entries:
        print('Nothing new to process (no finished, unapproved transcription files).')
        return 0
    files = [str(p) for _, p in entries]
    print(f'{len(entries)} finished files found')
    print(run(['scripts/inline_svg_css.py', '--write', *files]).stdout.strip().splitlines()[-1])

    good, bad = [], []
    for pid, path in entries:
        r = run(['scripts/check_transcript.py', str(path)])
        (good if r.returncode == 0 else bad).append((pid, path, (r.stdout + r.stderr).strip()[:300]))
    for pid, _, msg in bad:
        print(f'  FAIL {pid}: {msg}')
    if not good:
        return 1
    ids = [pid for pid, _, _ in good]
    r = run(['scripts/release_queue.py', *ids])
    approved = json.loads(r.stdout)
    for rej in approved['rejected']:
        print('  NOT APPROVED', rej)
    ids = approved['accepted']

    batch = ROOT / 'handoff/batches' / f'{datetime.date.today():%Y%m%d}-{"-".join(waves)}'
    batch.mkdir(parents=True, exist_ok=True)
    (batch / 'targets.txt').write_text('\n'.join(ids) + '\n', encoding='utf-8')

    def build_and_qa():
        r = run(['scripts/merge_batch.py'])
        tail = [l for l in r.stdout.splitlines() if l.startswith(('ℹ pass', 'ℹ fail', 'Static build'))]
        print('  build:', ' | '.join(tail) if tail else r.stdout[-300:] + r.stderr[-500:])
        if r.returncode:
            raise SystemExit('merge_batch failed')
        try:
            urllib.request.urlopen('http://127.0.0.1:4173/', timeout=5)
        except Exception:
            raise SystemExit('Start the local server first: node scripts/server.mjs (port 4173)')
        run(['scripts/qa_metro.py', '--ids-file', str(batch / 'targets.txt'), '--report-file', str(batch / 'pdf-acceptance.json')])
        report = json.loads((batch / 'pdf-acceptance.json').read_text(encoding='utf-8'))
        failing = [p for p in report['papers'] if not p['ok']]
        return report, failing

    report, failing = build_and_qa()
    clipped = [p['id'] for p in failing if p.get('escapedDiagrams')]
    if clipped:
        print(f'  widening clipped figure frames in {len(clipped)} papers')
        run(['scripts/fix_svg_viewbox.py', *clipped])
        report, failing = build_and_qa()
    pages = sum(len(p['renderedPages']) for p in report['papers'])
    print(f'PDF check: {len(report["papers"])} papers, {pages} pages, errors={report["errors"][:2]}, bankUnchanged={report["bankUnchangedDuringRun"]}')
    for p in failing:
        print('  PDF FAIL', p['id'], p['questions'], '/', p['expected'], p['missingNumbers'], p.get('overflowBlocks'), [e['diagram'] for e in p.get('escapedDiagrams', [])])
    cov = json.loads((ROOT / 'public/data/coverage.json').read_text(encoding='utf-8'))
    print(f'questions {cov["reviewedQuestions"]}; papers {cov["paperWorkflow"]}')
    print(f'batch folder: {batch.relative_to(ROOT)}')
    print('Next: look at qa/metro/<id>-p1.png for a few figure-heavy papers, write SOURCE_ISSUES_REPORT.md, bump version, commit, push, live acceptance.')
    return 1 if (bad or failing) else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or ['w']))
