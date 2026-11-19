import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';

test('different papers in the same exam slot use their verified answer links', () => {
  const papers = JSON.parse(readFileSync(new URL('../public/data/papers.json', import.meta.url)));
  for (const [id, answer] of [
    ['1AhIbjzAwUEmFrWisDMwTc-OzZhFUpm91', '11wJvmTNS4dRpw6sGsJo-09w0r-UsG20A'],
    ['161rWGzcQYllb6Vl0DXXV1sjxuPMFzpDP', '17_4Eufq7lx0g7POM4C1GkzuxqFiY-THj'],
  ]) {
    const paper = papers.find(p => p.id === id);
    assert.ok(paper);
    assert.ok(paper.answerUrl?.includes(answer), `${id} must use its verified answer`);
  }
});
