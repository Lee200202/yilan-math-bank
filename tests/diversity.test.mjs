import {test} from 'node:test';
import assert from 'node:assert/strict';
import {generate, availableCounts, replaceQuestion, familyKeys} from '../public/engine.mjs';

const ratios = {easy: 34, medium: 33, hard: 33};
const seeded = seed => () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
const base = {school: '測試校', year: 114, semester: 1, grade: 8, exam: 2, reviewed: true, typesetVerified: true, difficulty: 'medium', primaryUnitId: 'u', unitIds: ['u']};
const filters = {semester: '1', grade: '8', exam: '2', school: '測試校', curriculumOnly: false};
let n = 0;
function written(paperId, number, text, extra = {}) {
  n++;
  return {...base, id: `${paperId}-written-${number}`, paperId, type: 'written', sourceSha256: `sha-${paperId}`, sourceNumber: number, number, blocks: [{type: 'text', text}], ...extra};
}
const stem = '直角三角形 ABC 中，已知兩股長分別為 3 與 4，回答下列問題：';

test('sub-questions of one problem are never combined while other questions are available', () => {
  // two problems, each split into two parts that share a stem, plus one stand-alone problem
  const bank = [
    written('p1', '1-1', stem + '求斜邊長。'), written('p1', '1-2', stem + '求面積。'),
    written('p2', '2(1)', '某班統計資料如下表，回答下列問題：求平均數。'), written('p2', '2(2)', '某班統計資料如下表，回答下列問題：求中位數。'),
    written('p3', '3', '解方程式 $x^2-5x+6=0$，並說明理由。'),
  ];
  for (let seed = 1; seed <= 200; seed++) {
    const picked = generate(bank, filters, {choice: 0, fill: 0, written: 3}, ratios, 100, seeded(seed)).items.map(i => bank.find(q => q.id === i.id));
    const families = picked.map(q => familyKeys(q)[0]);
    assert.equal(new Set(families).size, 3, `seed ${seed} repeated a stem: ${picked.map(q => q.id)}`);
  }
});

test('siblings are still used when the scope has no other questions of that type', () => {
  const bank = [written('p1', '1-1', stem + '求斜邊長。'), written('p1', '1-2', stem + '求面積。')];
  const picked = generate(bank, filters, {choice: 0, fill: 0, written: 2}, ratios, 100, seeded(7)).items;
  assert.equal(picked.length, 2);
});

test('identical content posted in two source files counts once', () => {
  const text = '解不等式 $2x-4<x+5$，並在數線上表示解集合。';
  const bank = [written('copy-a', '1', text), written('copy-b', '1', text, {sourceSha256: 'sha-other'}), written('p9', '2', '求圓的面積。')];
  assert.equal(availableCounts(bank, filters).written, 2);
});

test('identical text with a different figure is a different question', () => {
  const svgA = '<svg viewBox="0 0 10 10"><circle cx="5" cy="5" r="3"/></svg>', svgB = '<svg viewBox="0 0 10 10"><rect x="1" y="1" width="8" height="8"/></svg>';
  const make = (id, svg) => ({...written(id, '1', '如圖，求陰影面積。'), blocks: [{type: 'text', text: '如圖，求陰影面積。'}, {type: 'svg', svg}]});
  assert.equal(availableCounts([make('a', svgA), make('b', svgB)], filters).written, 2);
});

test('replacing a question prefers one that is not a sub-question of the rest of the paper', () => {
  const bank = [
    written('p1', '1-1', stem + '求斜邊長。'), written('p1', '1-2', stem + '求面積。'),
    written('p2', '2', '某店折扣活動如下，求最划算的方案。'), written('p3', '3', '解方程式 $x^2-5x+6=0$。'),
  ];
  const session = {items: [{id: 'p1-written-1-1', score: 10}, {id: 'p2-written-2', score: 10}]};
  for (let seed = 1; seed <= 100; seed++) {
    const next = replaceQuestion(bank, session, 1, filters, seeded(seed));
    assert.equal(next.items[1].id, 'p3-written-3', `seed ${seed} swapped in a sibling of question 1`);
  }
});
