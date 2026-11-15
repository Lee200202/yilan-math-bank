"""Verify a frozen batch's exact data, source files and every-page review before publishing.

Read-only. A different machine must reproduce missing ignored QA artifacts rather than
claiming an old report verifies its newly generated PDFs.
"""
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def verify(path):
    manifest = read(path)
    for artifact in manifest['artifacts']:
        if sha(artifact['file']) != artifact['sha256']:
            raise ValueError(f'Artifact changed after acceptance: {artifact["file"]}')
    machine = read(manifest['machineReport'])
    if machine['errors'] or not machine['bankUnchangedDuringRun']:
        raise ValueError('Browser QA failed or bank changed during the run')
    if sha('public/typesetter.mjs') != machine['typesetterSha256'] or sha('public/fonts/TW-Kai-subset.ttf') != machine['fontSha256']:
        raise ValueError('PDF implementation or font changed after export')
    targets = {pathlib.Path(line).stem for line in (ROOT / manifest['targetList']).read_text(encoding='utf-8').splitlines() if line.strip()}
    rows = {p['id']: p for p in machine['papers']}
    if targets != rows.keys():
        raise ValueError('Not every batch paper has a PDF acceptance row')
    papers = {p['id']: p for p in read('public/data/papers.json')}
    bank = {q['id']: q for q in read('public/data/questions.json')}
    visual = {p['id']: p for p in manifest['visualReviews']}
    for pid, result in rows.items():
        if not result['ok'] or not result['embeddedGlyphsDecoded']:
            raise ValueError(f'PDF checks failed: {pid}')
        paper = papers[pid]
        source = paper['completionEvidence']
        if sha(source) != result['transcriptSha256']:
            raise ValueError(f'Transcript changed after PDF export: {pid}')
        transcript = read(source)
        if transcript['sourceSha256'] != paper['sha256']:
            raise ValueError(f'Original provenance changed: {pid}')
        for question in transcript['questions']:
            if question.get('usable', True):
                qid = f'{pid}-{question["type"]}-{question["sourceNumber"]}'
                if bank[qid]['blocks'] != question['blocks']:
                    raise ValueError(f'Built bank is stale: {qid}')
        review = visual[pid]
        if review['status'] != 'pass' or review['pages'] != result['renderedPages']:
            raise ValueError(f'Every final page must have a matching visual review: {pid}')
        for page in result['renderedPages']:
            if sha(page['file']) != page['sha256']:
                raise ValueError(f'Render changed after visual review: {page["file"]}')
        if sha(f'qa/metro/{pid}.pdf') != result['pdfSha256']:
            raise ValueError(f'PDF changed after review: {pid}')
    print(f'Frozen batch verified: {len(rows)} papers, {sum(len(r["renderedPages"]) for r in rows.values())} reviewed pages. No files staged or pushed.')


if __name__ == '__main__':
    verify(sys.argv[1])
