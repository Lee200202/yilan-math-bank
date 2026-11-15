"""Metro-area (臺北/新北/桃園/臺中/高雄) inventory and verified transcriptions.

* Every crawled math question file with a complete slot becomes a paper record (linked to
  the official file; not re-hosted) so the archive shows the full inventory.
* Papers with a whole-paper transcription are archived as PDF in public/papers and their
  questions join the bank. Every transcription is pinned to the source SHA256 and each
  question's unit review is pinned to its content SHA256.
"""
import hashlib
import json
import pathlib
import shutil

REGION_LABELS = {'taipei': '臺北市', 'new_taipei': '新北市', 'taoyuan': '桃園市', 'taichung': '臺中市', 'kaohsiung': '高雄市'}
SOURCE_NAMES = {
    'taipei-xingfu': ('臺北市立興福國民中學', 'https://www.hfjh.tp.edu.tw/office/div_200/section_210/%E6%AE%B5%E8%80%83%E9%A1%8C%E5%BA%AB/'),
    'new_taipei-xikun': ('新北市立溪崑國民中學', 'https://www.ckjhs.ntpc.edu.tw/p/403-1000-196.php'),
    'new_taipei-zhongzheng': ('新北市立中正國民中學', 'https://www.ccjhs.ntpc.edu.tw/p/403-1000-114.php'),
    'taipei-chengzheng': ('臺北市立誠正國民中學', 'https://www.ccjh.tp.edu.tw/nss/p/546421'),
    'new_taipei-sanhe': ('新北市立三和國民中學', 'https://www.shjh.ntpc.edu.tw/p/403-1000-76.php'),
    'new_taipei-fuhe': ('新北市立福和國民中學', 'https://www.fhjh.ntpc.edu.tw/p/403-1000-78.php'),
    'new_taipei-wufeng': ('新北市立五峰國民中學', 'https://www.wfjh.ntpc.edu.tw/p/403-1000-77.php'),
    'new_taipei-lujiang': ('新北市立鷺江國民中學', 'https://www.ljjh.ntpc.edu.tw/p/403-1000-107.php'),
    'new_taipei-xinzhuang': ('新北市立新莊國民中學', 'https://www.hcjh.ntpc.edu.tw/p/403-1000-173.php'),
    'new_taipei-yonghe': ('新北市立永和國民中學', 'https://www.jhjhs.ntpc.edu.tw/p/412-1000-175.php'),
    'taichung-dahua': ('臺中市立大華國民中學', 'https://dhjh.tc.edu.tw/p/403-1154-1470-1.php'),
    'taichung-daye': ('臺中市立大業國民中學', 'https://sites.google.com/mail.dyjh.tc.edu.tw/test-memory-new'),
    'taoyuan-ziqiang': ('桃園市立自強國民中學', 'https://drive.google.com/drive/folders/1BQFNJxFEFHDd76cIHCe0FjmXRJ2Cg7oD'),
    'taichung-xiangshang': ('臺中市立向上國民中學', 'https://hsjh.tc.edu.tw/p/403-1103-1921-1.php'),
    'kaohsiung-meinong': ('高雄市立美濃國民中學', 'https://hakka.mtjh.kh.edu.tw/exam/exam-section.htm'),
    'kaohsiung-dawan': ('高雄市立大灣國民中學', 'https://www.dwm.kh.edu.tw/view/index.php?WebID=344&MainType=0&SubType=104&MainMenuId=64182&SubMenuId=64183'),
}
BAD_SVG = ['<image', '<script', '<foreignobject', 'data:image']


def content_sha(blocks, diagram=None):
    content = json.dumps({'blocks': blocks, 'diagramSvg': diagram}, ensure_ascii=False, separators=(',', ':'))
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


def rows_from_transcript(t, paper, unit_ids, evidence):
    """Validate a whole-paper transcription and return its usable question rows.
    Also stamps the paper with counts, status and the printed-header basis.
    Shared by metro papers and Yilan whole-paper transcriptions."""
    pid = paper['id']
    printed = t['printedSlot']
    if any(printed[k] != paper[k] for k in ['year', 'semester', 'grade', 'exam']):
        raise ValueError(f'Printed header disagrees with slot: {pid} {printed}')
    if t['sourceSha256'] != paper['sha256']:
        raise ValueError(f'Transcription invalidated: {pid}')
    paper['metadataBasis'] = f'卷首：{t["printedHeader"]}'
    rows, seen = [], set()
    for q in t['questions']:
        if q['type'] not in ('choice', 'fill', 'written') or q['difficulty'] not in ('easy', 'medium', 'hard'):
            raise ValueError(f'Bad question type/difficulty: {pid} {q.get("sourceNumber")}')
        if not q.get('blocks'):
            raise ValueError(f'Empty question: {pid} {q["sourceNumber"]}')
        strings = [b.get('text', '') for b in q['blocks']] + [i for b in q['blocks'] for i in b.get('items', [])] + [c for b in q['blocks'] for r in b.get('rows', []) for c in r]
        if any(ord(ch) < 32 and ch != '\n' for s in strings for ch in s):
            raise ValueError(f'Control character (e.g. a TAB from a mangled \\t) in {pid} {q["sourceNumber"]}')
        if any(s.count('$') % 2 for s in strings):
            raise ValueError(f'Unbalanced $ in {pid} {q["sourceNumber"]}')
        for b in q['blocks']:
            if b['type'] not in ('text', 'options', 'table', 'svg'):
                raise ValueError(f'Unknown block in {pid}')
            if b['type'] == 'svg' and any(s in b['svg'].lower() for s in BAD_SVG):
                raise ValueError(f'Non-vector diagram in {pid}')
        if q['type'] == 'choice' and not any(b['type'] == 'options' for b in q['blocks']):
            raise ValueError(f'Choice question without options: {pid} {q["sourceNumber"]}')
        if q['primaryUnitId'] not in unit_ids or any(u not in unit_ids for u in q['unitIds']) or q['primaryUnitId'] not in q['unitIds']:
            raise ValueError(f'Unknown unit in {pid} {q["sourceNumber"]}')
        qid = f'{pid}-{q["type"]}-{q["sourceNumber"]}'
        if qid in seen:
            raise ValueError(f'Duplicate question number: {qid}')
        seen.add(qid)
        row = {
            'id': qid, 'paperId': pid, 'page': q['page'] - 1, 'type': q['type'], 'number': q['sourceNumber'],
            'sourceNumber': q['sourceNumber'], 'difficulty': q['difficulty'], 'reviewed': True,
            'region': paper['region'], 'school': paper['school'], 'sourceSha256': paper['sha256'],
            'difficultyBasis': q.get('difficultyBasis', '編輯依步驟數與概念整合估計，非官方答對率'),
            'sourceScan': False, 'year': paper['year'], 'semester': paper['semester'], 'grade': paper['grade'],
            'exam': paper['exam'], 'curriculum108': paper['curriculum108'], 'blocks': q['blocks'],
            'typesetVerified': True, 'primaryUnitId': q['primaryUnitId'], 'unitIds': q['unitIds'],
            'unitAssignmentBasis': q['unitAssignmentBasis'], 'contentSha256': content_sha(q['blocks']),
        }
        if q.get('usable', True) is not False:
            rows.append(row)
        elif not q.get('sourceIssue'):
            raise ValueError(f'Unusable question needs sourceIssue: {qid}')
    expected = t['expectedTypes']
    actual = {k: sum(q['type'] == k for q in t['questions']) for k in ('choice', 'fill', 'written')}
    if actual != {k: expected.get(k, 0) for k in actual}:
        raise ValueError(f'Whole-paper type count mismatch: {pid} {actual} != {expected}')
    paper['questionCount'] = len(rows)
    paper['sourceUnitCount'] = len(t['questions'])
    paper['excludedUnitCount'] = len(t['questions']) - len(rows)
    paper['transcriptionStatus'] = ('complete' if not paper['excludedUnitCount'] else 'complete-with-source-issues') if t.get('visualReviewComplete') else 'partial'
    paper['completionEvidence'] = evidence
    return rows


def build(root, unit_ids):
    root = pathlib.Path(root)
    inv = json.loads((root / 'research/metro/metro-inventory.json').read_text(encoding='utf-8'))
    tdir = root / 'research/metro/transcribed'
    transcripts = {f.stem: json.loads(f.read_text(encoding='utf-8')) for f in sorted(tdir.glob('*.json'))}
    papers, questions, summary = [], [], []
    for key, src in inv['sources'].items():
        files = src['files']
        seen_sha = set()
        school = files[0]['school'] if files else key
        region = key.split('-')[0]
        stats = {'source': key, 'region': region, 'regionLabel': REGION_LABELS[region], 'school': school,
                 'officialName': SOURCE_NAMES[key][0], 'entry': SOURCE_NAMES[key][1], 'crawledAt': src['crawledAt'],
                 'mathFiles': 0, 'questionFiles': 0, 'answerFiles': 0, 'unresolvedSlot': 0, 'downloadFailed': 0,
                 'years': set(), 'transcribedPapers': 0, 'questions': 0}
        stats['archivesNotExtracted'] = 0
        for f in files:
            if f['kind'] == 'archive':
                stats['archivesNotExtracted'] += bool(f.get('archiveStatus'))
                continue
            stats['mathFiles'] += 1
            if f['kind'] != 'question':
                stats['answerFiles'] += 1
                continue
            if not f.get('sha256'):
                stats['downloadFailed'] += 1
                continue
            if f['sha256'] in seen_sha:
                continue
            seen_sha.add(f['sha256'])
            if None in (f['year'], f['semester'], f['exam'], f['grade']):
                stats['unresolvedSlot'] += 1
                continue
            stats['questionFiles'] += 1
            stats['years'].add(f['year'])
            ext = f['name'].rsplit('.', 1)[-1].lower() if '.' in f['name'] else f.get('format', 'pdf')
            paper = {
                'id': f['id'], 'region': region, 'school': school, 'year': f['year'], 'semester': f['semester'],
                'grade': f['grade'], 'exam': f['exam'], 'title': f['name'], 'file': '', 'format': ext,
                'sha256': f['sha256'], 'bytes': f.get('bytes'), 'sourceUrl': f['sourceUrl'], 'sourcePage': f['sourcePage'],
                'curriculum108': f['year'] >= 108 + f['grade'] - 7, 'track': 'regular', 'questionCount': 0, 'warning': '',
                'answerUrl': None, 'metadataBasis': '官方檔名／資料夾；未逐份核對卷首',
                'transcriptionStatus': 'pending',
            }
            if f.get('archiveMember'):
                paper['sourceNote'] = f'校方以整包壓縮檔公開，本卷為其中「{f["archiveMember"]}」。'
            t = transcripts.get(f['id'])
            if t:
                if t['sourceSha256'] != f['sha256']:
                    raise ValueError(f'Metro transcription invalidated: {f["id"]}')
                local = root / f['localPath']
                if hashlib.sha256(local.read_bytes()).hexdigest() != f['sha256']:
                    raise ValueError(f'Metro source hash changed: {f["id"]}')
                if f.get('format') != 'pdf':
                    raise ValueError(f'Metro transcribed source must be a PDF original: {f["id"]}')
                dest = root / 'public/papers' / f'{f["id"]}.pdf'
                shutil.copyfile(local, dest)
                paper['file'] = f'./papers/{dest.name}'
                rows = rows_from_transcript(t, paper, unit_ids, f'research/metro/transcribed/{f["id"]}.json')
                questions += rows
                stats['transcribedPapers'] += 1
                stats['questions'] += len(rows)
            papers.append(paper)
        stats['years'] = sorted(stats['years'])
        summary.append(stats)
    missing = set(transcripts) - {p['id'] for p in papers}
    if missing:
        raise ValueError(f'Transcriptions without an inventoried source: {sorted(missing)}')
    return papers, questions, summary
