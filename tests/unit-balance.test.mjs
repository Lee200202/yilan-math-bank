import {test} from 'node:test';
import assert from 'node:assert/strict';
import {generate} from '../public/engine.mjs';

// Synthetic bank: every unit has plenty of every type and difficulty, one source paper per unit/type so no question
// is treated as a repeat of another.
function makeBank(units, perCell = 8, skip = {}) {
  const bank = [];
  let n = 0;
  for (const unit of units) for (const type of ['choice', 'fill', 'written']) {
    if (skip[`${unit}:${type}`]) continue;
    for (const difficulty of ['easy', 'medium', 'hard']) for (let i = 0; i < perCell; i++) {
      n++;
      bank.push({id: `q${n}`, reviewed: true, typesetVerified: true, region: 'yilan', school: 'S', year: 110, semester: 1, grade: 8, exam: 1,
        paperId: `P-${unit}-${type}-${difficulty}-${i}`, sourceNumber: String(n), sourceSha256: `sha${n}`, primaryUnitId: unit, type, difficulty,
        blocks: [{type: 'text', text: `${unit} ${type} ${difficulty} 第${n}題 內容${n}`}]});
    }
  }
  return bank;
}
const seeded = seed => () => { seed = (seed * 1664525 + 1013904223) % 4294967296; return seed / 4294967296; };
const tally = (items, bank) => {
  const byId = new Map(bank.map(q => [q.id, q])), out = {};
  for (const it of items) { const q = byId.get(it.id), k = `${q.type}|${q.primaryUnitId}`; out[k] = (out[k] || 0) + 1; }
  return out;
};
const filtersFor = weights => ({grade: 8, semester: 1, scopeMode: 'units', unitWeights: weights});
const RATIOS = {easy: 34, medium: 33, hard: 33};

test('four equal units: every question type is split evenly over the four units (not all choice from one unit)', () => {
  const units = ['u1', 'u2', 'u3', 'u4'], bank = makeBank(units);
  for (let seed = 1; seed <= 25; seed++) {
    const {items} = generate(bank, filtersFor(Object.fromEntries(units.map(u => [u, 25]))), {choice: 12, fill: 8, written: 4}, RATIOS, 100, seeded(seed));
    const t = tally(items, bank);
    for (const u of units) {
      assert.equal(t[`choice|${u}`], 3, `choice in ${u}, seed ${seed}: ${JSON.stringify(t)}`);
      assert.equal(t[`fill|${u}`], 2, `fill in ${u}, seed ${seed}`);
      assert.equal(t[`written|${u}`], 1, `written in ${u}, seed ${seed}`);
    }
  }
});

test('counts that do not divide evenly differ by at most one question between units', () => {
  const units = ['u1', 'u2', 'u3', 'u4'], bank = makeBank(units);
  for (let seed = 1; seed <= 25; seed++) {
    const {items} = generate(bank, filtersFor(Object.fromEntries(units.map(u => [u, 25]))), {choice: 11, fill: 7, written: 3}, RATIOS, 100, seeded(seed * 31));
    const t = tally(items, bank);
    for (const type of ['choice', 'fill', 'written']) {
      const counts = units.map(u => t[`${type}|${u}`] || 0);
      assert.ok(Math.max(...counts) - Math.min(...counts) <= 1, `${type} ${counts} (seed ${seed})`);
    }
    const totals = units.map(u => ['choice', 'fill', 'written'].reduce((sum, ty) => sum + (t[`${ty}|${u}`] || 0), 0));
    assert.equal(totals.reduce((a, b) => a + b, 0), 21);
    assert.ok(Math.max(...totals) - Math.min(...totals) <= 1, `unit totals ${totals}`);
  }
});

test('unequal weights split each type in proportion (50/30/20 of 10 choice = 5/3/2)', () => {
  const units = ['a', 'b', 'c'], bank = makeBank(units);
  for (let seed = 1; seed <= 15; seed++) {
    const {items} = generate(bank, filtersFor({a: 50, b: 30, c: 20}), {choice: 10, fill: 0, written: 0}, RATIOS, 100, seeded(seed * 17));
    const t = tally(items, bank);
    assert.deepEqual([t['choice|a'], t['choice|b'], t['choice|c']], [5, 3, 2], `seed ${seed}`);
  }
});

test('a unit that has no questions of a type does not break the split: the other units supply it, unit totals stay exact', () => {
  const units = ['u1', 'u2', 'u3'], bank = makeBank(units, 8, {'u3:written': true});
  for (let seed = 1; seed <= 20; seed++) {
    const {items} = generate(bank, filtersFor({u1: 34, u2: 33, u3: 33}), {choice: 9, fill: 6, written: 3}, RATIOS, 100, seeded(seed * 13));
    const t = tally(items, bank);
    assert.equal(t['written|u3'] || 0, 0);
    assert.equal((t['written|u1'] || 0) + (t['written|u2'] || 0), 3);
    // The unit totals are a hard limit and u3 cannot supply written questions, so its share has to be made up of
    // choice and fill: those two types may drift from their ideal split by one question, but not more.
    for (const type of ['choice', 'fill']) {
      const ideal = (type === 'choice' ? 9 : 6) / 3;
      for (const u of units) assert.ok(Math.abs((t[`${type}|${u}`] || 0) - ideal) <= 1.5, `${type} in ${u}: ${JSON.stringify(t)} (seed ${seed})`);
    }
    // unit totals follow the weights (21 questions: 34/33/33% -> 7/7/7)
    const totals = units.map(u => ['choice', 'fill', 'written'].reduce((s, ty) => s + (t[`${ty}|${u}`] || 0), 0));
    assert.equal(totals.reduce((a, b) => a + b, 0), 18);
    assert.ok(Math.max(...totals) - Math.min(...totals) <= 1, `totals ${totals}`);
  }
});

test('difficulty ratio and total counts are still honoured while balancing units', () => {
  const units = ['u1', 'u2', 'u3', 'u4'], bank = makeBank(units, 10), byId = new Map(bank.map(q => [q.id, q]));
  const {items} = generate(bank, filtersFor(Object.fromEntries(units.map(u => [u, 25]))), {choice: 12, fill: 8, written: 4}, {easy: 50, medium: 50, hard: 0}, 100, seeded(99));
  assert.equal(items.length, 24);
  const levels = items.map(i => byId.get(i.id).difficulty);
  assert.equal(levels.filter(l => l === 'easy').length, 12);
  assert.equal(levels.filter(l => l === 'medium').length, 12);
  assert.equal(levels.filter(l => l === 'hard').length, 0);
  assert.equal(new Set(items.map(i => i.id)).size, 24);
});
