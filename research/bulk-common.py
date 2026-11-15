from pathlib import Path
from html import escape
from collections import Counter
import hashlib,json
R=Path(__file__).resolve().parent
def tx(x,y,s,size=17):return f'<text x="{x}" y="{y}" font-size="{size}">{escape(s)}</text>'
def ln(x,y,u,v,dash=None):return f'<line x1="{x}" y1="{y}" x2="{u}" y2="{v}" stroke="#111" stroke-width="1.4"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def pa(d,fill='none'):return f'<path d="{d}" fill="{fill}" stroke="#111" stroke-width="1.4"/>'
def SV(content,w=320,h=210):return {'type':'svg','svg':f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-12 -14 {w+24} {h+28}" role="img"><g fill="#111" font-family="serif" font-size="17" stroke-linecap="round" stroke-linejoin="round">{content}</g></svg>'}
def OPT(*a):return {'type':'options','items':list(a)}
def PTS(p,segs,offsets=None,w=320,h=220,extra=''):
 return SV(''.join(ln(*p[a],*p[b]) for a,b in segs)+''.join(tx(x+(offsets or {}).get(k,(-7,-10))[0],y+(offsets or {}).get(k,(-7,-10))[1],k) for k,(x,y) in p.items())+extra,w,h)
def start(pid,year):
 global PID,YEAR,SHA,C,T
 PID=pid;YEAR=year;SHA=hashlib.sha256((R.parent/'public/papers'/f'{pid}.pdf').read_bytes()).hexdigest();C=[];T=[]
def Q(kind,n,page,rect,level,*blocks,sub=None,section=None,issue=None,keyprefix=''):
 key=f'{kind}-'+(keyprefix+'-' if keyprefix else '')+f'{n}'+(f'-{sub}' if sub is not None else '')
 qid=f'zh-bulk-{PID}-{key}';num=str(n)+(f'({sub})' if sub is not None else '')
 sourceNumber=(f'{section}、' if section else '')+num
 meta={'id':qid,'paperId':PID,'sourceId':qid,'sourceNumber':sourceNumber,'parentNumber':n,'subnumber':sub,'sourceSha256':SHA,'page':page,'rect':rect,'type':kind,'number':num,'difficulty':level,'reviewed':True}
 typed={'id':qid,'sourceId':qid,'sourceNumber':sourceNumber,'parentNumber':n,'subnumber':sub,'blocks':[{'type':'text','text':b} if isinstance(b,str) else b for b in blocks],'sourceSha256':SHA,'verified':True}
 if issue:meta.update(usable=False,sourceIssue=issue);typed.update(usable=False,sourceIssue=issue)
 C.append(meta);T.append(typed)
def save(expected,types,evidence):
 assert len(C)==expected and dict(Counter(q['type'] for q in C))==types and len({q['id'] for q in C})==expected
 old_path=R/f'completeness-bulk-{PID}.json'
 old_proof=json.loads(old_path.read_text('utf8')) if old_path.exists() else {}
 (R/f'curated-bulk-{PID}.json').write_text(json.dumps(C,ensure_ascii=False,indent=2),'utf8')
 (R/f'transcribed-bulk-{PID}.json').write_text(json.dumps(T,ensure_ascii=False,indent=2),'utf8')
 proof={'paperId':PID,'sourcePrintedYear':YEAR,'sourceSha256':SHA,'expectedQuestions':expected,'expectedTypes':types,'actualQuestions':len(C),'actualTypes':dict(Counter(q['type'] for q in C)),'difficultyCounts':dict(Counter(q['difficulty'] for q in C)),'sourceMapping':[{'id':q['id'],'sourceNumber':q['sourceNumber'],'page':q['page'],'type':q['type'],'usable':q.get('usable',True)} for q in C],'evidence':evidence,'issues':[{'id':q['id'],'issue':q['sourceIssue']} for q in C if 'sourceIssue' in q]}
 proof['transcriptionSha256']=hashlib.sha256((R/f'transcribed-bulk-{PID}.json').read_bytes()).hexdigest()
 proof['visualReviewComplete']=bool(old_proof.get('visualReviewComplete') and old_proof.get('transcriptionSha256')==proof['transcriptionSha256'])
 if proof['visualReviewComplete']:
  for key in ['visualReviewEvidence','renderCheck','allIdsAndSourceHashesMatch']:
   if key in old_proof:proof[key]=old_proof[key]
 (R/f'completeness-bulk-{PID}.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2),'utf8');print(PID,len(C),types,flush=True)
