"""Move three visually audited labels clear of vertices; preserve all geometry."""
from pathlib import Path
import hashlib,json
R=Path(__file__).parent
plans={
 'zh-111-1-2-8-fill-6':('transcribed-requested-zh111-1-2-8.json',[('188','221','220','184','D')]),
 'zh-114-2-1-9-fill-9':('transcribed-zhonghua-late.json',[('100','166','70','155','C')]),
 'zh-113-1-1-9-fill-9':('transcribed-zhonghua-late.json',[('65','64','77','85','E'),('65','147','77','136','F'),('234','147','212','136','G'),('234','64','212','85','H')]),
}
def digest(q):return hashlib.sha256(json.dumps({'blocks':q['blocks'],'diagramSvg':q.get('diagramSvg')},ensure_ascii=False,separators=(',',':')).encode('utf8')).hexdigest()
tags=json.loads((R/'question-unit-tags.json').read_text(encoding='utf8'));tag_map={t['id']:t for t in tags}
reviewed=json.loads((R/'question-unit-reviewed-content.json').read_text(encoding='utf8'))
files={name:json.loads((R/name).read_text(encoding='utf8')) for name,_ in plans.values()}
for id,(name,moves) in plans.items():
 q=next(q for q in files[name] if q['id']==id);before=digest(q)
 assert tag_map[id]['contentSha256']==before and reviewed[id]==before,id
 for ox,oy,nx,ny,label in moves:
  old=f'<text x="{ox}" y="{oy}" font-size="15">{label}</text>';new=f'<text x="{nx}" y="{ny}" font-size="15">{label}</text>'
  block=next(b for b in q['blocks'] if b['type']=='svg')
  assert old in block['svg'] or new in block['svg'],(id,label)
  block['svg']=block['svg'].replace(old,new)
 after=digest(q);tag_map[id]['contentSha256']=after;reviewed[id]=after
 tag_map[id]['layoutReview']='2026-11-15：僅移動圖中字標，保留所有線、交點、尺寸與題文；主要單元未變。'
 print(id,after)
for name,data in files.items():(R/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
(R/'question-unit-tags.json').write_text(json.dumps(tags,ensure_ascii=False,indent=2),encoding='utf8')
(R/'question-unit-reviewed-content.json').write_text(json.dumps(reviewed,ensure_ascii=False,indent=2),encoding='utf8')
