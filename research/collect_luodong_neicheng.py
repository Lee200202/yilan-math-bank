"""Collect public official exam links; never infer absent papers as present."""
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.parse import quote, unquote, urlsplit
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import hashlib, json, re, time

ROOT = Path(__file__).resolve().parent
RAW = ROOT / 'raw'
RAW.mkdir(exist_ok=True)

def fetch(url):
    return urlopen(Request(quote(url, safe=':/%?=&'), headers={'User-Agent':'Mozilla/5.0'}), timeout=40).read()

def soup(url):
    return BeautifulSoup(fetch(url).decode('utf-8'), 'html.parser')

def luodong():
    url = 'https://2blog.ilc.edu.tw/16771/category/c-12565/'
    rows=[]; pages=[]; seen=set()
    while url and url not in seen:
        seen.add(url); pages.append(url); s=soup(url)
        for art in s.select('article'):
            h=art.select_one('.entry-title a'); title=h.get_text(' ',strip=True)
            y=re.search(r'(\d{3})學年度',title)
            if not y or not 108 <= int(y[1]) <=115: continue
            semester=1 if '第一學期' in title else 2 if '第二學期' in title else None
            ex=re.search(r'第([一二三])次',title); exam={'一':1,'二':2,'三':3}.get(ex[1]) if ex else None
            for a in art.select('.entry-content a[href]'):
                if '數學' not in a.get_text(): continue
                context=re.sub(r'\s','',a.parent.get_text())
                g=re.search(r'([七八九])年級',context)
                grade={'七':7,'八':8,'九':9}.get(g[1]) if g else None
                uid=f'ld-{y[1]}-{semester}-{exam}-{grade}'
                rows.append(dict(id=uid,school='羅東國中',year=int(y[1]),semester=semester,grade=grade,exam=exam,subject='數學',sourcePage=h['href'],sourceUrl=a['href'],title=title,answer='unknown',metadataBasis='official-page',fileName=uid+Path(urlsplit(a['href']).path).suffix))
        nxt=next((a['href'] for a in s.find_all('a',href=True) if '較舊的文章' in a.get_text()),None)
        years=[int(m) for m in re.findall(r'(\d{3})學年度',s.get_text())]
        if years and max(years)<108: break
        url=nxt
    return rows,pages

def neicheng():
    root='1k1_c5hebr8RsSehpDlyWQCRSD92Vz3RU'
    todo=[(root,[])]; seen=set(); entries=[]
    while todo:
        fid, parents=todo.pop(0)
        if fid in seen: continue
        seen.add(fid);url=f'https://drive.google.com/drive/folders/{fid}'
        s=soup(url)
        for row in s.select('[role="row"][data-id]'):
            did=row['data-id']; name=row.get_text(' ',strip=True)
            # Drive displays visible filenames as aria-label on the grid name cell.
            cell=row.select_one('td[data-column-field="6"] .WQJtxb') or row.select_one('[role="gridcell"]')
            if cell: name=cell.get_text(' ',strip=True)
            if not name: continue
            folder='資料夾' in str(row) or 'folder' in str(row).lower()
            e=dict(id=did,name=name,parent=fid,path=parents+[name],isFolder=folder,url=f'https://drive.google.com/drive/folders/{did}' if folder else f'https://drive.google.com/file/d/{did}/view')
            entries.append(e)
            if folder: todo.append((did,parents+[name]))
    return entries

def download(row):
    try:
        dest=RAW/row['fileName']
        b=dest.read_bytes() if dest.exists() else fetch(row['sourceUrl'])
        dest.write_bytes(b)
        row.update(downloadStatus='downloaded',bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),localPath=str(dest.relative_to(ROOT.parent)))
        if dest.suffix.lower()=='.pdf' and not b.startswith(b'%PDF'): row['downloadStatus']='invalid-pdf'
    except Exception as e: row.update(downloadStatus='failed',error=str(e))
    return row

if __name__=='__main__':
    rows,pages=luodong()
    print('Luodong links',len(rows),flush=True)
    with ThreadPoolExecutor(max_workers=4) as ex: rows=list(ex.map(download,rows))
    (ROOT/'luodong-papers.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
    (ROOT/'luodong-pages.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2),encoding='utf8')
    print('Luodong downloaded',sum(r['downloadStatus']=='downloaded' for r in rows),flush=True)
    try:
        entries=neicheng()
        (ROOT/'neicheng-drive.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2),encoding='utf8')
        print('Neicheng entries',len(entries),flush=True)
    except Exception as e: print('Neicheng error',repr(e),flush=True)
