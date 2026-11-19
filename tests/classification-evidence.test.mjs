import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';

test('Neicheng exam classification retains the conflicting printed header', () => {
  const papers = JSON.parse(readFileSync(new URL('../public/data/papers.json', import.meta.url)));
  const p = papers.find(x => x.id === 'nc-109-1-2-7');
  assert.equal(p.exam, 2);
  assert.match(p.metadataBasis, /第一次/);
  assert.match(p.warning, /答案卷/);
  assert.match(p.warning, /第二次/);
  assert.equal(p.questionCount, 26);
});
