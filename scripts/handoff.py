"""Read-only status by default; --write refreshes the shared Git handoff snapshot."""
import argparse
import collections
import datetime
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]


def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True,
                          text=True, encoding='utf-8', errors='replace', check=True).stdout.strip()


def snapshot():
    papers = json.loads((ROOT / 'public/data/papers.json').read_text(encoding='utf-8'))
    questions = json.loads((ROOT / 'public/data/questions.json').read_text(encoding='utf-8'))
    # Same fresh-generation eligibility as public/engine.mjs (old grouped IDs are restore-only).
    usable = [q for q in questions if q.get('reviewed') and q.get('typesetVerified') and not q.get('selectionHidden')]
    version = re.search(r"const DATA_VERSION='([^']+)'", (ROOT / 'public/app.mjs').read_text(encoding='utf-8'))
    regions = {}
    for region in sorted({p['region'] for p in papers}):
        subset = [p for p in papers if p['region'] == region]
        regions[region] = {'papers': len(subset), 'statuses': dict(collections.Counter(
            p['transcriptionStatus'] for p in subset)), 'usableQuestions': sum(q.get('region', 'yilan') == region for q in usable)}
    queues = {}
    queued_ids = set()
    blocked_ids = {p.stem for p in (ROOT / 'handoff/source-issues').glob('*.json')}
    claims = json.loads((ROOT / 'handoff/CLAIMS.json').read_text(encoding='utf-8'))['claims']
    reserved = {c['paperId'] for c in claims if c.get('status') in ('claimed','transcribing','repairing-figures','assigned-external','reserved-for-external-dispatch','staged-for-coordinator-review')}
    for path in sorted((ROOT / 'research/targets').glob('*.json')):
        targets = json.loads(path.read_text(encoding='utf-8-sig'))
        if not isinstance(targets, list):
            continue
        incomplete = [t for t in targets if isinstance(t, dict) and 'outFile' in t and not (ROOT / t['outFile']).exists()]
        queued_ids.update(t['paperId'] for t in incomplete)
        waiting = [t for t in incomplete if t['paperId'] not in blocked_ids | reserved]
        queues[path.stem] = {'remaining': len(waiting), 'next': waiting[:3]}
    return {'generatedAt': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'head': git('rev-parse', 'HEAD'), 'dataVersion': version.group(1) if version else None,
            'paperCount': len(papers), 'questionRecords': len(questions), 'usableQuestions': len(usable),
            'statuses': dict(collections.Counter(p['transcriptionStatus'] for p in papers)),
            'regions': regions, 'queues': queues, 'blockedSources': sorted(blocked_ids),
            'reservedOrClaimed': sorted(reserved),
            'remainingByFormat': dict(collections.Counter(p.get('format', 'unknown') for p in papers if not p['transcriptionStatus'].startswith('complete'))),
            'notInPreparedQueues': [p['id'] for p in papers if not p['transcriptionStatus'].startswith('complete') and p['id'] not in queued_ids and p['id'] not in blocked_ids],
            'parked': [p.name for p in (ROOT / 'research/targets/parked').glob('*.json')],
            'workingChanges': git('status', '--short'),
            'warning': '此快照只代表本機資料；不代表 PDF 目視通過或正式站已更新，另讀 VERIFICATION.md。'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    data = snapshot()
    summary = f"版本 {data['dataVersion']} / {data['head'][:8]}\n原卷 {data['paperCount']}；可用題 {data['usableQuestions']}；狀態 {data['statuses']}\n"
    for name, queue in data['queues'].items():
        summary += (f"{name}: 未認領PDF候選 {queue['remaining']} 卷，接續 " + ', '.join(t['paperId'] for t in queue['next'])).rstrip() + '\n'
    print(summary)
    if args.write:
        folder = ROOT / 'handoff'
        folder.mkdir(exist_ok=True)
        (folder / 'state.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        papers = json.loads((ROOT / 'public/data/papers.json').read_text(encoding='utf-8'))
        remaining = [{k: p.get(k) for k in ('id', 'region', 'school', 'year', 'semester', 'grade', 'exam', 'format', 'questionCount', 'transcriptionStatus', 'sourceUrl', 'file')}
                     for p in papers if not p['transcriptionStatus'].startswith('complete')]
        (folder / 'pending-papers.json').write_text(json.dumps(remaining, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        (folder / 'STATUS.md').write_text('# 資料快照\n\n' + data['generatedAt'] + '\n\n```text\n' + summary + '```\n\n' + data['warning'] + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
