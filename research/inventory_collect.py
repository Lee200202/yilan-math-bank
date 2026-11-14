"""Official MOE school inventory and bounded homepage examination-link discovery."""
import requests,json,re
from pathlib import Path
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor,as_completed
from urllib.parse import urljoin
ROOT=Path(__file__).parent
SOURCES=['https://stats.moe.gov.tw/files/opendata/j1_new.json','https://stats.moe.gov.tw/files/opendata/aj_new.json']
allrows=[]
for source in SOURCES:
    rows=requests.get(source,timeout=45).json()
    selected=[x for x in rows if '宜蘭' in str(x) and int(x.get('學年度','0'))==115]
    if not selected:
        selected=[x for x in rows if '宜蘭' in str(x) and int(x.get('學年度','0'))==114]
    for row in selected:
        allrows.append({'id':row['代碼'],'name':row['學校名稱'],'website':row['網址'],'schoolYear':int(row['學年度']),'type':'附設國中部' if 'aj_' in source else '國民中學','inventorySource':source})
def inspect(row):
    url=row['website'].replace('http://','https://')
    # Legacy MOE URLs may point to old nested pages; root remains school controlled.
    urls=list(dict.fromkeys([url,re.match(r'https://[^/]+',url).group(0)+'/']))
    try:
        for u in urls:
            r=requests.get(u,timeout=18)
            if r.status_code==200:break
        row['checkedUrl']=r.url; row['httpStatus']=r.status_code
        soup=BeautifulSoup(r.content,'html.parser')
        found=[]
        for a in soup.select('a[href]'):
            label=a.get_text(' ',strip=True); href=urljoin(r.url,a['href'])
            if any(w in label for w in ['題庫','考古','段考試題','定期評量試題','各科試題','各科題','試題觀摩','段考考題']):
                if href.startswith('http') and not any(x['url']==href for x in found):found.append({'label':label,'url':href})
        row['examEntrances']=found
        row['status']='public_entry_found' if found else 'no_exam_entry_on_homepage'
        row['note']='僅完成官網首頁入口查找；未找到入口不代表學校未公開考卷。'
    except Exception as e:row.update(status='homepage_unreachable',error=str(e))
    return row
out=[]
with ThreadPoolExecutor(max_workers=6) as ex:
    for f in as_completed([ex.submit(inspect,x) for x in allrows]):
        out.append(f.result())
        (ROOT/'inventory_schools.json').write_text(json.dumps({'checkedAt':'2026-11-14','sources':SOURCES,'scope':'MOE latest available school roster; bounded homepage examination-link discovery, not an exhaustive absence check','schools':sorted(out,key=lambda x:x['id'])},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps([{'id':x['id'],'name':x['name'],'status':x['status'],'links':x.get('examEntrances',[])} for x in sorted(out,key=lambda x:x['id'])],ensure_ascii=True))
