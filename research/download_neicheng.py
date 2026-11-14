from pathlib import Path
from urllib.request import urlopen, Request
from concurrent.futures import ThreadPoolExecutor
import json,re,hashlib

ROOT=Path(__file__).resolve().parent
entries=json.loads((ROOT/'neicheng-drive.json').read_text(encoding='utf8'))
rows=[]
for e in entries:
    if e['isFolder'] or not any('數學' in p for p in e['path'][:-1]): continue
    year=int(re.search(r'(\d{3})',e['path'][0])[1]); exam={'一':1,'二':2,'三':3}[re.search(r'段([一二三])',e['path'][1])[1]]
    name=e['name']; m=re.search(r'[789七八九]',name.split('.pdf')[0].split('上',1)[-1]); grade={'七':7,'八':8,'九':9}.get(m[0],int(m[0]) if m and m[0].isdigit() else None) if m else None
    uid=f'nc-{year}-1-{exam}-{grade}'+('-pullout' if '抽' in name else '')
    title=re.sub(r'^(PDF\s+)', '',name).split('.pdf')[0]+'.pdf'
    rows.append(dict(id=uid,school='內城國中小',year=year,semester=1,exam=exam,grade=grade,subject='數學',title=title,fileName=uid+'.pdf',sourcePage='https://www.ryjh.ilc.edu.tw/',sourceUrl=e['url'],downloadUrl=f'https://drive.usercontent.google.com/download?id={e["id"]}&export=download',driveId=e['id'],answer='unknown',metadataBasis='official-linked-drive',track='pullout' if '抽' in name else 'regular'))

def dl(r):
    p=ROOT/'raw'/r['fileName']
    try:
        b=p.read_bytes() if p.exists() else urlopen(Request(r['downloadUrl'],headers={'User-Agent':'Mozilla/5.0'}),timeout=35).read()
        if not b.startswith(b'%PDF'): raise ValueError('Response is not PDF')
        p.write_bytes(b);r.update(downloadStatus='downloaded',bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),localPath=str(p.relative_to(ROOT.parent)))
    except Exception as e:r.update(downloadStatus='failed',error=str(e))
    return r
with ThreadPoolExecutor(max_workers=4) as ex: rows=list(ex.map(dl,rows))
(ROOT/'neicheng-papers.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print('Papers',len(rows),'downloaded',sum(r['downloadStatus']=='downloaded' for r in rows))
for r in rows: print(r['id'],r['title'],r['downloadStatus'])
