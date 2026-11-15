import test from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
test('public builds exclude unapproved drafts and reject edits made after source review',()=>{
 const code=String.raw`
import hashlib,json,pathlib,sys,tempfile
sys.path.insert(0,'scripts')
from release_policy import approved
with tempfile.TemporaryDirectory() as temp:
 root=pathlib.Path(temp);(root/'research').mkdir();source=root/'paper.json';source.write_bytes(b'{"verified":true}\r\n')
 policy=root/'research/release-transcripts.json';policy.write_text(json.dumps({'papers':{}}))
 assert approved(root,source) is False
 digest=hashlib.sha256(source.read_bytes().replace(b'\r\n',b'\n')).hexdigest()
 policy.write_text(json.dumps({'papers':{'paper':{'transcriptSha256':digest}}}))
 assert approved(root,source) is True
 source.write_text('{"verified":false}')
 try:approved(root,source)
 except ValueError:pass
 else:raise AssertionError('Edited paper entered public build without re-review')
print('ok')
`;
 assert.equal(execFileSync('python',['-c',code],{encoding:'utf8'}).trim(),'ok');
});
