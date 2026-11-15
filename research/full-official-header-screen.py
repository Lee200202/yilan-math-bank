"""Read first-page text layers of all original question files. Flags only; no automatic metadata edits."""
import json,pathlib,re,collections,hashlib,unicodedata
import pymupdf as fitz
R=pathlib.Path(__file__).resolve().parent;ROOT=R.parent
audit=json.loads((R/'full-official-crawl-audit.json').read_text(encoding='utf8'))
over=json.loads((R/'paper-metadata-overrides.json').read_text(encoding='utf8'))
word=[]
for filename in ['bulk-render-manifest.json','full-official-word-header-render-manifest.json']:
    if (R/filename).exists():word+=json.loads((R/filename).read_text(encoding='utf-8-sig'))
wm={r['id']:r for r in word if r.get('renderPath') and r.get('status')!='failed'}
digits={'○':'0','〇':'0','零':'0','Ｏ':'0','O':'0','o':'0','一':'1','二':'2','三':'3','四':'4','五':'5','六':'6','七':'7','八':'8','九':'9'}
def chinese_num(s):return int(''.join(digits.get(c,c) for c in s))
def parse(text):
    t=re.sub(r'\s+','',unicodedata.normalize('NFKC',text[:650]));slot={};matches={}
    m=re.search(r'([0-9一二三四五六七八九○〇零Oo]{3})學年(?:度)?',t)
    if m:
        try:
            y=chinese_num(m[1])
            if 90<=y<=130:slot['year']=y;matches['year']=m[0]
        except ValueError:pass
    m=re.search(r'第([一二12])學期|([上下])學期',t)
    if m:slot['semester']=({'一':1,'二':2,'1':1,'2':2}[m[1]] if m[1] else 1 if m[2]=='上' else 2);matches['semester']=m[0]
    m=re.search(r'第([一二三123])次',t)
    if m:slot['exam']={'一':1,'二':2,'三':3,'1':1,'2':2,'3':3}[m[1]];matches['exam']=m[0]
    m=re.search(r'([一二三七八九123789])年級',t)
    if m:slot['grade']={'一':7,'二':8,'三':9,'七':7,'八':8,'九':9,'1':7,'2':8,'3':9,'7':7,'8':8,'9':9}[m[1]];matches['grade']=m[0]
    return slot,matches
rows=[]
for q in audit['allMathFiles']:
    if q['kind']!='question':continue
    declared={k:q.get(k) for k in ['year','semester','exam','grade']};effective={**declared,**{k:v for k,v in over.get(q['id'],{}).items() if k in declared}}
    row={'id':q['id'],'school':q['school'],'name':q['name'],'originalPath':q.get('localPath'),'originalSha256':q.get('sha256'),'declaredSlot':declared,'effectiveSlot':effective,'sourceUrl':q['sourceUrl'],'metadataOverride':over.get(q['id'])}
    src=ROOT/q['localPath'];pdf=src
    if src.suffix.lower()!='.pdf':
        if q['id'] in wm:
            pdf=ROOT/wm[q['id']]['renderPath'];row['renderPath']=wm[q['id']]['renderPath'];row['renderSha256']=wm[q['id']].get('renderSha256')
        else:row['status']='word-not-yet-rendered';rows.append(row);continue
    try:
        d=fitz.open(pdf);text=d[0].get_text(sort=True);slot,matched=parse(text);row.update(pages=len(d),firstPageTextChars=len(text),headerText=text[:650],textLayerSlotCandidate=slot,matchedPhrases=matched,textExtractionMethod='first-page text geometrically sorted by position; not source stream order')
        row['potentialConflicts']=[{'field':k,'expected':effective[k],'headerTextCandidate':v} for k,v in slot.items() if effective.get(k) is not None and effective[k]!=v]
        if row['potentialConflicts']:row['status']='text-header-conflict-needs-visual-review'
        elif not text.strip() or not slot:row['status']='scanned-or-header-text-unresolved'
        elif len(slot)<4:row['status']='partial-header-text-consistent'
        else:row['status']='full-header-text-consistent'
        d.close()
    except Exception as e:row['status']='read-failed';row['error']=str(e)
    rows.append(row)
report={'checkedDate':'2026-11-15','scope':'255 official original question files from the completed fresh source listing','policy':'Regex results are review candidates only. No source metadata was changed by this screen. Only separately inspected visual findings may be added to paper-metadata-overrides.json.','originalQuestionFiles':len(rows),'statuses':dict(collections.Counter(r['status'] for r in rows)),'potentialConflicts':[r for r in rows if r['status']=='text-header-conflict-needs-visual-review'],'rows':rows}
(R/'full-official-header-screen.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'files':len(rows),'statuses':report['statuses'],'conflictIds':[r['id'] for r in report['potentialConflicts']]},ensure_ascii=False))
