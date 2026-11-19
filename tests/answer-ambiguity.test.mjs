import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';

test('different papers in the same exam slot use their verified answer links', () => {
  const papers = JSON.parse(readFileSync(new URL('../public/data/papers.json', import.meta.url)));
  for (const [id, answer] of [
    ['1AhIbjzAwUEmFrWisDMwTc-OzZhFUpm91', '11wJvmTNS4dRpw6sGsJo-09w0r-UsG20A'],
    ['161rWGzcQYllb6Vl0DXXV1sjxuPMFzpDP', '17_4Eufq7lx0g7POM4C1GkzuxqFiY-THj'],
    ['1MwiZk_NTiaWzJkV375OKM2aJlSEEC9Z0', '1dIySBEWi_hzCvikOHICmqAPwoSSHNrzv'],
    ['14cxdw_ivb8t4XK5xtAx_9LUyGMG-rcuO', '19Brj-32Irrzs1dqBv864kCuiZUSvbTes'],
    ['105J__1NnYMfjUaEX_KdQ43VpqmMko0s_', '1v-TZRKXXq6tu8fJFTareEnmsXOPaVgHf'],
    ['1Ax-L_cBTrRHTIjozUwWqXiz5B8eayLEr', '1ksYefdYhvbCnyAatz7xILd7GvIhdIv0W'],
    ['1ODYj-V7KzqhYr8EM7s2gkTI2Rb8qKDg3', '1Qn6bsoTzTAfvPK4qcH78e7KUKnaYkqDe'],
    ['16EeKUo1TFlipf950nPiry7mpCxdq6Cp-', '1i5ZEhOk5jvqIfMaOYhNln98ct4iSqXsS'],
    ['1x_Ioixv3cP69BEPRAJMCv9Btt2YkoGds', '11I_qdXuSSAoqTpKaPFzIl8r8-PnLk_iC'],
    ['174QCQASOMa3gnCdI0oS0BADxGv_cZO3P', '1yiJee3C3GPtVFBLJiMiOHVaPqsUHVf-6'],
  ]) {
    const paper = papers.find(p => p.id === id);
    assert.ok(paper);
    assert.ok(paper.answerUrl?.includes(answer), `${id} must use its verified answer`);
  }
  assert.ok(!papers.find(p => p.id === '1ZZUkKjnXYPQn5CwCnQPqN9ayYj__D6wS').answerUrl);
  const corrected = papers.find(p => p.id === '1x_Ioixv3cP69BEPRAJMCv9Btt2YkoGds');
  assert.match(corrected.answerNote, /第19題.*更正單/);
  assert.ok(corrected.correctionUrl.includes('1DPFTOWYDFmS4UcZRIG9sFGYXNiyc3Ruf'));
});
