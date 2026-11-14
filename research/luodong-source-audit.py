from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import requests,json,re,hashlib
from bs4 import BeautifulSoup
from urllib.parse import urljoin
ROOT=Path(__file__).parent;OUT=ROOT/'review-luodong';OUT.mkdir(exist_ok=True)
def get(url):
    try:
        r=requests.get(url,timeout=30);s=BeautifulSoup(r.content,'html.parser')
        articles=[]
        for art in s.select('article'):
            h=art.select_one('.entry-title');a=h.select_one('a') if h else None
            if h:articles.append({'title':h.get_text(' ',strip=True),'url':a.get('href') if a else url,'mathLinks':[{'label':a.get_text(' ',strip=True),'url':a.get('href')} for a in art.select('a[href]') if '數學' in a.get_text()]})
        links=[{'label':a.get_text(' ',strip=True),'url':urljoin(r.url,a['href'])} for a in s.select('a[href]') if any(w in a.get_text() for w in ['段考','題庫','評量試題','較舊','教務','教學'])]
        return {'requestedUrl':url,'resolvedUrl':r.url,'status':r.status_code,'sha256':hashlib.sha256(r.content).hexdigest(),'title':s.title.get_text() if s.title else None,'articles':articles,'links':links,'bodyText':s.get_text(' ',strip=True)[:800]}
    except Exception as e:return {'requestedUrl':url,'error':str(e)}
pages=[];url='https://2blog.ilc.edu.tw/16771/category/c-12565/'
while url and url not in [x['requestedUrl'] for x in pages] and len(pages)<15:
    row=get(url);pages.append(row)
    url=next((x['url'] for x in row.get('links',[]) if '較舊' in x['label']),None)
    print('category',len(pages),'articles',len(row.get('articles',[])),flush=True)
targets=['https://www.ltjh.ilc.edu.tw/','https://2blog.ilc.edu.tw/16771/','https://2blog.ilc.edu.tw/16771/wp-json/wp/v2/categories?per_page=100']
for year in [109,111,113,114,115]:targets.append(f'https://2blog.ilc.edu.tw/16771/?s={year}%E5%AD%B8%E5%B9%B4%E5%BA%A6')
other=[]
with ThreadPoolExecutor(max_workers=5) as ex:
    for f in as_completed([ex.submit(get,x) for x in targets]):other.append(f.result())
allposts=[a for p in pages for a in p.get('articles',[])]
years=sorted({int(y) for a in allposts for y in re.findall(r'(\d{3})學年度',a['title'])})
out={'checkedAt':'2026-11-14','categoryPages':pages,'otherChecks':other,'categoryPostYears':years,'missingRequestedYears':[y for y in range(108,116) if y not in years],'limits':'僅記錄本次可公開取得的官網分類、分頁、站內搜尋與首頁入口；未找到不是學校未辦考試，也不是已證明全網無檔。'}
(ROOT/'luodong-source-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print('years',years,'other',len(other),flush=True)
