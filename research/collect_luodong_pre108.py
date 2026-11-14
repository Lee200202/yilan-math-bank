from pathlib import Path
from urllib.request import Request,urlopen
from urllib.parse import urlsplit,quote
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from bs4 import BeautifulSoup
import json,re,hashlib

R=Path(__file__).resolve().parent;RAW=R/'raw';RAW.mkdir(exist_ok=True)
audit=json.loads((R/'luodong-api-audit.json').read_text(encoding='utf8'))
posts=next(x['json'] for x in audit if '/wp/v2/posts?' in x['url'])
rows=[]
for p in posts:
 title=BeautifulSoup(p['title']['rendered'],'html.parser').get_text()
 m=re.search(r'(\d{3})學年度',title)
 if not m or int(m[1]) not in [105,106,107]:continue
 year=int(m[1]);semester=1 if '第一學期' in title else 2 if '第二學期' in title else None
 em=re.search(r'第([一二三])次',title);exam={'一':1,'二':2,'三':3}.get(em[1]) if em else None
 s=BeautifulSoup(p['content']['rendered'],'html.parser')
 for a in s.select('a[href]'):
  if '數學' not in a.get_text():continue
  context=re.sub(r'\s','',a.parent.get_text())
  gm=re.search(r'([七八九])年級',context);grade={'七':7,'八':8,'九':9}.get(gm[1]) if gm else None
  uid=f'ld-{year}-{semester}-{exam}-{grade}';url=a['href'];ext=Path(urlsplit(url).path).suffix.lower()
  rows.append(dict(id=uid,school='羅東國中',year=year,semester=semester,grade=grade,exam=exam,subject='數學',sourcePage=p['link'],sourceUrl=url,title=title,answer='unknown',metadataBasis='official-page-header-unverified',fileName=uid+ext,curriculum108=False,rightsStatus='not-stated',sourcePostId=p['id']))

def dl(r):
 dest=RAW/r['fileName']
 try:
  b=dest.read_bytes() if dest.exists() else urlopen(Request(quote(r['sourceUrl'],safe=':/%?=&'),headers={'User-Agent':'Mozilla/5.0'}),timeout=35).read()
  if dest.suffix=='.pdf' and not b.startswith(b'%PDF'):raise ValueError('not a PDF')
  dest.write_bytes(b);r.update(downloadStatus='downloaded',bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),localPath=str(dest.relative_to(R.parent)))
 except Exception as e:r.update(downloadStatus='failed',error=str(e))
 return r
with ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(dl,rows))
seen={}
for r in rows:
 key=r.get('sha256',r['sourceUrl'])
 if key in seen:
  r['contentDuplicateOf']=seen[key]
  r['metadataConflict']='官網不同學期／年級使用相同檔案內容，須以原卷卷首核對，不可僅按發布頁計入該年度。'
 else:seen[key]=r['id']
(R/'luodong-pre108-papers.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
report={'checkedAt':'2026-11-14','source':'官方WordPress posts API的既存完整回應（research/luodong-api-audit.json），按原文標題及年級標頭擷取數學下載連結。','requestedYears':[105,106,107],'links':len(rows),'downloaded':sum(r['downloadStatus']=='downloaded' for r in rows),'byYear':dict(Counter(r['year'] for r in rows)),'formats':dict(Counter(Path(r['fileName']).suffix for r in rows)),'uniqueDownloadedHashes':len({r['sha256'] for r in rows if r.get('sha256')}),'duplicates':[{'id':r['id'],'duplicateOf':r['contentDuplicateOf'],'sourceUrl':r['sourceUrl']} for r in rows if r.get('contentDuplicateOf')],'limitations':'來源標頭按官網保留；除了另行視覺核對之題目，尚未逐份核對原卷卷首。'}
(R/'luodong-pre108-download-review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(report,ensure_ascii=False))
