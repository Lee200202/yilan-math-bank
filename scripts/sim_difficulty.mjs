// How evenly does generate() spread the requested difficulty ratios over each question type?
// Usage: node scripts/sim_difficulty.mjs [engine-path] [runs]
import {readFileSync} from 'node:fs';
import {pathToFileURL, fileURLToPath} from 'node:url';

const enginePath = process.argv[2] || fileURLToPath(new URL('../public/engine.mjs', import.meta.url));
const {generate, availableCounts, TYPES} = await import(pathToFileURL(enginePath).href);
const bank = JSON.parse(readFileSync(new URL('../public/data/questions.json', import.meta.url), 'utf8'));
const byId = new Map(bank.map(q => [q.id, q]));
const runs = Number(process.argv[3] || 300);
let seed = 4242;
const random = () => { seed = (seed * 1664525 + 1013904223) % 4294967296; return seed / 4294967296; };
const scenarios = [
  {name: '簡單50／中等50', ratios: {easy: 50, medium: 50, hard: 0}, counts: {choice: 10, fill: 6, written: 4}},
  {name: '簡單40／中等40／困難20', ratios: {easy: 40, medium: 40, hard: 20}, counts: {choice: 10, fill: 6, written: 4}},
  {name: '簡單30／中等50／困難20', ratios: {easy: 30, medium: 50, hard: 20}, counts: {choice: 12, fill: 8, written: 4}},
];
const filters = {year: '', semester: '', grade: '8', exam: '', region: '', school: '', difficulty: '', scopeMode: 'exam', curriculumOnly: true, unitWeights: {}};
for (const sc of scenarios) {
  const sum = {};
  let ok = 0, worstGap = 0;
  for (let i = 0; i < runs; i++) {
    let r;
    try { r = generate(bank, filters, sc.counts, sc.ratios, 100, random); } catch (e) { continue; }
    ok++;
    for (const type of TYPES) {
      const mine = r.items.map(x => byId.get(x.id)).filter(q => q.type === type);
      if (!mine.length) continue;
      sum[type] ??= {easy: 0, medium: 0, hard: 0, n: 0};
      for (const q of mine) sum[type][q.difficulty]++;
      sum[type].n += mine.length;
      for (const level of ['easy', 'medium', 'hard']) {
        const share = 100 * mine.filter(q => q.difficulty === level).length / mine.length;
        worstGap = Math.max(worstGap, Math.abs(share - sc.ratios[level]));
      }
    }
  }
  const line = TYPES.map(t => sum[t] ? `${t}: 簡單${(100 * sum[t].easy / sum[t].n).toFixed(0)}% 中等${(100 * sum[t].medium / sum[t].n).toFixed(0)}% 困難${(100 * sum[t].hard / sum[t].n).toFixed(0)}%` : '').join('  |  ');
  console.log(`${sc.name}（${ok} 次）\n  ${line}\n  單卷各題型與目標比例的最大差距 ${worstGap.toFixed(0)} 個百分點`);
}
