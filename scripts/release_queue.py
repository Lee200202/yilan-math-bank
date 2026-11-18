"""Coordinator: select structurally complete transcripts under the user's active review policy."""
import argparse
import hashlib
import json
import pathlib
from prepare_metro import rows_from_transcript

ROOT=pathlib.Path(__file__).resolve().parents[1]


def approve(ids):
    papers={p['id']:p for p in json.loads((ROOT/'public/data/papers.json').read_text(encoding='utf-8'))}
    units={u['id'] for u in json.loads((ROOT/'research/nanyi-units.json').read_text(encoding='utf-8'))}
    paths={p.stem:p for folder in ('research/metro/transcribed','research/yilan/transcribed') for p in (ROOT/folder).glob('*.json')}
    policy=ROOT/'research/release-transcripts.json'
    data=json.loads(policy.read_text(encoding='utf-8')) if policy.exists() else {'schemaVersion':1,'papers':{}}
    accepted=[];rejected=[]
    for pid in ids:
        try:
            path=paths[pid];t=json.loads(path.read_text(encoding='utf-8'));paper=papers[pid]
            partial_ok = t.get('deliveryStatus') == 'partial' and t.get('sourceIncomplete') is True and bool(t.get('missingSourceUnits'))
            if not t.get('visualReviewComplete') or not t.get('questions') or t.get('deliveryStatus') == 'draft' or (t.get('deliveryStatus') == 'partial' and not partial_ok):
                raise ValueError('Author delivery is not a completed whole paper')
            issue=ROOT/f'handoff/source-issues/{pid}.json'
            if issue.exists():
                evidence=json.loads(issue.read_text(encoding='utf-8'))
                if evidence.get('printedSlot') and any(evidence['printedSlot'].get(k)!=paper[k] for k in ('year','semester','grade','exam')):
                    raise ValueError('Known printed-slot conflict remains unresolved')
            rows=rows_from_transcript(t,dict(paper),units,path.relative_to(ROOT).as_posix())
            if not rows:raise ValueError('No usable question units')
            data['papers'][pid]={'transcriptSha256':hashlib.sha256(path.read_bytes().replace(b'\r\n',b'\n')).hexdigest(),'basis':'User approved direct reuse of AI text, figure-focused review; see handoff/REVIEW_POLICY.md'}
            accepted.append(pid)
        except (ValueError,KeyError,TypeError) as e:rejected.append({'paperId':pid,'reason':str(e)})
    policy.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return {'accepted':accepted,'rejected':rejected}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('paper_ids',nargs='+')
    args=parser.parse_args()
    result=approve(args.paper_ids)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    raise SystemExit(1 if result['rejected'] else 0)
