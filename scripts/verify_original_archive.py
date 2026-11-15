"""Validate the downloaded originals, independently of selected question crops."""
from pathlib import Path
import collections,hashlib,json,zipfile
import pymupdf

root=Path(__file__).resolve().parents[1]
papers=json.loads((root/'public/data/papers.json').read_text(encoding='utf-8'))
results=[]
for p in papers:
    file=root/'public'/p.get('originalFile',p['file']).removeprefix('./')
    data=file.read_bytes()
    assert data and hashlib.sha256(data).hexdigest()==p['sha256'],p['id']
    row={'id':p['id'],'format':file.suffix[1:],'bytes':len(data),'sha256':p['sha256'],'status':'verified'}
    if file.suffix.lower()=='.pdf':
        with pymupdf.open(file) as doc:
            assert len(doc)>0 and not doc.needs_pass,p['id']
            # Parse each page, including source papers with no transcription yet.
            for page in doc:page.get_text()
            row['pages']=len(doc)
    elif file.suffix.lower()=='.docx' or data.startswith(b'PK\x03\x04'):
        with zipfile.ZipFile(file) as doc:
            assert 'word/document.xml' in doc.namelist() and doc.testzip() is None,p['id']
            row['actualFormat']='docx'
    elif file.suffix.lower()=='.doc':
        assert data.startswith((bytes.fromhex('d0cf11e0a1b11ae1'),b'{\\rtf',b'<?xml')),p['id']
    else:raise AssertionError(f'Unexpected original type: {file}')
    results.append(row)
out={'files':len(results),'formats':dict(collections.Counter(r['format'] for r in results)),'originalPdfPages':sum(r.get('pages',0) for r in results),'results':results}
(root/'qa').mkdir(exist_ok=True)
(root/'qa/original-archive-report.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='results'},ensure_ascii=False))
