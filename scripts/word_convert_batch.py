"""Convert every still-pending legacy .doc paper to .docx with the installed Word (scripts/word_convert.py), one at a time.

Usage: python -X utf8 scripts/word_convert_batch.py <out_dir> [--limit N] [--timeout S]
Output: <out_dir>/<paperId>.docx ; the original file and its SHA are untouched (transcripts still pin the ORIGINAL file's SHA).
Skips papers whose output already exists. Writes <out_dir>/_report.json (ok / failed with the last logged step).
Do not run two copies at once, and do not run while the user has Word documents open they care about: this only starts its
own hidden Word instance, but a second instance may be confusing.
"""
import json
import pathlib
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import word_convert  # noqa: E402


def candidates():
    papers = json.loads((ROOT / 'public/data/papers.json').read_text(encoding='utf-8'))
    inv = json.loads((ROOT / 'research/metro/metro-inventory.json').read_text(encoding='utf-8'))
    local = {f['id']: f['localPath'] for s in inv['sources'].values() for f in s['files'] if f.get('localPath')}
    main_root = ROOT.parent / 'yilan-math-bank'
    rows = []
    for p in papers:
        if p['format'] != 'doc' or p.get('transcriptionStatus', '').startswith('complete'):
            continue
        src = None
        if p['id'] in local and (ROOT / local[p['id']]).exists():
            src = ROOT / local[p['id']]
        elif p['id'] in local and (main_root / local[p['id']]).exists():
            src = main_root / local[p['id']]
        elif p['region'] == 'yilan':
            for base in (ROOT, main_root):
                c = base / 'public/papers' / f'{p["id"]}.doc'
                if c.exists():
                    src = c
                    break
        if src:
            rows.append((p, src))
    return rows


def main():
    out = pathlib.Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    limit = int(sys.argv[sys.argv.index('--limit') + 1]) if '--limit' in sys.argv else 10 ** 9
    timeout = int(sys.argv[sys.argv.index('--timeout') + 1]) if '--timeout' in sys.argv else 90
    rep_path = out / '_report.json'
    report = json.loads(rep_path.read_text(encoding='utf-8')) if rep_path.exists() else {}
    done = 0
    for p, src in candidates():
        dst = out / f'{p["id"]}.docx'
        if dst.exists() and dst.stat().st_size > 0:
            continue
        if done >= limit:
            break
        t0 = time.time()
        ok, msg = word_convert.convert(src, dst, timeout)
        report[p['id']] = {'ok': ok, 'seconds': round(time.time() - t0, 1), 'msg': msg[:200], 'school': p['school'], 'year': p['year'],
                           'semester': p['semester'], 'grade': p['grade'], 'exam': p['exam'], 'region': p['region']}
        rep_path.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding='utf-8')
        print(('OK  ' if ok else 'FAIL'), p['id'], report[p['id']]['seconds'], 's', '' if ok else msg[:120], flush=True)
        done += 1
    print('converted this run:', done, '| total ok:', sum(1 for v in report.values() if v['ok']), '| failed:', sum(1 for v in report.values() if not v['ok']))


if __name__ == '__main__':
    main()
