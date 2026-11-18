import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';

test('missing source pages remain partial and show a warning', () => {
  const papers = JSON.parse(readFileSync(new URL('../public/data/papers.json', import.meta.url)));
  const paper = papers.find(p => p.id === 'ld-108-2-2-7');
  assert.equal(paper.transcriptionStatus, 'partial');
  assert.equal(paper.questionCount, 16);
  assert.match(paper.warning, /缺失/);
});
