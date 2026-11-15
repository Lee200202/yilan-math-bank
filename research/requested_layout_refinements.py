"""Reviewed compact diagrams: retain mathematical conditions, omit decorative players."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parent
baseball='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="-30 -15 380 300"><path d="M150 230L240 140L150 50L60 140Z" fill="none" stroke="#111" stroke-width="1.5"/><g fill="white" stroke="#111" stroke-width="1"><path d="M146 226H154V234H146Z"/><path d="M236 136H244V144H236Z"/><path d="M146 46H154V54H146Z"/><path d="M56 136H64V144H56Z"/></g><g font-family="serif" font-size="24" fill="#111"><text x="150" y="265" text-anchor="middle">本壘</text><text x="250" y="145">一壘</text><text x="150" y="25" text-anchor="middle">二壘</text><text x="50" y="145" text-anchor="end">三壘</text></g></svg>'''
p=R/'transcribed-requested-zh111-1-2-8.json';rows=json.loads(p.read_text(encoding='utf8'))
for q in rows:
    if q['id'].endswith('fill-6'):limit=95
    elif q['id'].endswith('fill-8'):limit=95
    elif q['id'].endswith('fill-10'):limit=65
    elif 'written-2-' in q['id']:limit=105
    else:continue
    for b in q['blocks']:
        if b['type']=='svg':
            b['maxHeight']=limit
            if 'written-2-' in q['id']:b['svg']=baseball
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')

poly=[(40,140),(80,40),(180,80),(140,180)];segments=[]
for c in range(-200,201,8):
    low=max(40,40-c);high=min(240,240-c)
    if high<=low:continue
    cuts=[]
    for (x1,y1),(x2,y2) in zip(poly,poly[1:]+poly[:1]):
        den=(y2-y1)-(x2-x1)
        if not den:continue
        t=(c-(y1-x1))/den
        if 0<=t<=1:cuts.append(x1+t*(x2-x1))
    cuts=sorted(set(round(x,6) for x in cuts))
    spans=[(low,high)] if len(cuts)<2 else [(low,min(high,cuts[0])),(max(low,cuts[-1]),high)]
    for a,b in spans:
        if b-a>.01:segments.append(f'M{a:.3f} {a+c:.3f}L{b:.3f} {b+c:.3f}')
p=R/'transcribed-requested-ld112-1-2-8.json';rows=json.loads(p.read_text(encoding='utf8'))
q=next(q for q in rows if q['id']=='ld-112-1-2-8-fill-15')
svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 290 285"><rect x="40" y="40" width="200" height="200" fill="white" stroke="#111" stroke-width="1.6"/>'
svg+='<path d="'+' '.join(segments)+'" fill="none" stroke="#555" stroke-width=".8"/>'
svg+='<path d="M40 140 80 40 180 80 140 180Z" fill="white" stroke="#111" stroke-width="1.6"/><g font-family="serif" font-size="21"><text x="23" y="35">A</text><text x="23" y="264">B</text><text x="243" y="264">C</text><text x="243" y="35">D</text><text x="20" y="145">P</text><text x="133" y="204">Q</text><text x="187" y="84">R</text><text x="75" y="31">S</text></g></svg>'
q['diagramSvg']=svg
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print('Compact baseball/triangle layouts and explicit vector hatching prepared')
