import test from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';

test('external Markdown intake stages a real whole paper without publishing, overwriting or trusting drafts',()=>{
 const code=String.raw`
import copy,json,pathlib,sys,tempfile
from unittest.mock import patch
sys.path.insert(0,'scripts')
import handoff_exchange as h
pid='1N7akUT_Cyuz05u1dNYDUr7ZRdfciAV_3'
t=json.loads(pathlib.Path('research/yilan/transcribed/'+pid+'.json').read_text(encoding='utf-8'))
real=h.papers();units=h.read('research/nanyi-units.json')
markdown='# Full paper\n\n'+chr(96)*3+'json\n'+json.dumps(t,ensure_ascii=False)+'\n'+chr(96)*3+'\n'
assert h.parse_md(markdown)['paperId']==pid
for bad in ['# no JSON',markdown+markdown]:
 try:h.parse_md(bad)
 except ValueError:pass
 else:raise AssertionError('Malformed MD accepted')
with tempfile.TemporaryDirectory() as tmp:
 pending=copy.deepcopy(real);pending[pid]['transcriptionStatus']='pending'
 with patch.object(h,'ROOT',pathlib.Path(tmp)),patch.object(h,'papers',lambda:pending),patch.object(h,'read',lambda _:units):
  draft=copy.deepcopy(t);draft['deliveryStatus']='partial'
  text=chr(96)*3+'json\n'+json.dumps(draft)+'\n'+chr(96)*3+'\n'
  try:h.stage(text,'partial.md')
  except ValueError:pass
  else:raise AssertionError('Partial delivery accepted')
  receipt=h.stage(markdown,'returned.md')
  assert receipt['published'] is False and receipt['status']=='staged-for-coordinator-review'
  folder=pathlib.Path(tmp)/'research/incoming-external'/pid
  assert (folder/(pid+'.json')).exists() and not (pathlib.Path(tmp)/'public').exists()
  try:h.stage(markdown,'duplicate.md')
  except ValueError:pass
  else:raise AssertionError('Existing delivery overwritten')
print('ok')
`;
 assert.equal(execFileSync('python',['-c',code],{encoding:'utf8'}).trim(),'ok');
});

test('external-chat inventory includes every unfinished school and all original formats',()=>{
 const code=String.raw`
import collections,sys
sys.path.insert(0,'scripts')
import handoff_exchange as h
rows=h.queue();papers=h.papers()
assert len(rows)==sum(not p['transcriptionStatus'].startswith('complete') for p in papers.values())
assert {r['school'] for r in rows}=={p['school'] for p in papers.values() if not p['transcriptionStatus'].startswith('complete')}
assert len({r['school'] for r in rows})>=19
assert all(r['sha256'] and r['originalUrl'] for r in rows)
assert {'pdf','doc','docx','odt'} <= {r['format'] for r in rows}
assert all(r['blocked'] for r in rows if (h.ROOT/'handoff/source-issues'/f"{r['id']}.json").exists())
print('ok')
`;
 assert.equal(execFileSync('python',['-c',code],{encoding:'utf8'}).trim(),'ok');
});
