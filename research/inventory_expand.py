import requests,json,re
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse
from concurrent.futures import ThreadPoolExecutor,as_completed
ROOT=Path(__file__).parent
data=json.loads((ROOT/'inventory_schools.json').read_text(encoding='utf-8'))
def links(url):
    r=requests.get(url,timeout=18);r.raise_for_status()
    soup=BeautifulSoup(r.content,'html.parser');rows=[]
    for a in soup.select('a[href]'):
        label=a.get_text(' ',strip=True)+' '+a.get('title','')+' '+' '.join(i.get('alt','') for i in a.select('img'))
        href=urljoin(r.url,a['href'])
        if href.startswith('http'):rows.append((label.strip(),href))
    return rows
def work(row):
    urls=[row.get('checkedUrl',row['website'])];entries=[];checked=[];errors=[]
    try:
        first=links(urls[0]);checked.append(urls[0])
        secondary=list(dict.fromkeys(h for t,h in first if any(x in t for x in ['教務處','教學組','教學資源','教學園地','各科試題','試題','題庫','下載專區']) and not any(x in h for x in ['drive.google','accounts.google','facebook','line.me'])))[:5]
        sources=[(urls[0],first)]
        for u in secondary:
            try:sources.append((u,links(u)));checked.append(u)
            except Exception as e:errors.append({'url':u,'error':str(e)})
        for page,aa in sources:
            for t,h in aa:
                if any(x in t for x in ['題庫','考古','段考試題','定期評量試題','各科試題','各科題','試題觀摩','段考考題','段考評量']):
                    if not any(x['url']==h for x in entries):entries.append({'label':t,'url':h,'discoveredOn':page})
        # Exclude elementary entrance examination and remedial material from junior-high period exams.
        entries=[x for x in entries if not any(w in x['label'] for w in ['小六','補考','補救'])]
        row['examEntrances']=entries
        row['checkedPages']=checked
        row['status']='public_entry_found' if entries else 'no_exam_entry_in_checked_pages'
        if any('限' in x['label'] or '登入' in x['label'] for x in entries):row['status']='restricted_entry_found'
        row['errors']=errors
        row['note']='檢查官網首頁及最多5個教務／教學／試題連結；未找到入口不代表未公開。'
    except Exception as e:row.update(status='homepage_unreachable',error=str(e))
    return row
out=[]
with ThreadPoolExecutor(max_workers=6) as ex:
    for f in as_completed([ex.submit(work,x) for x in data['schools']]):
        out.append(f.result());print(out[-1]['id'],out[-1]['status'],len(out[-1].get('examEntrances',[])),flush=True)
data['schools']=sorted(out,key=lambda x:x['id'])
(ROOT/'inventory_schools.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
