// Per-type difficulty spread in unit mode. Usage: node scripts/sim_difficulty_units.mjs [runs]
import {readFileSync} from 'node:fs';
import {generate, TYPES} from '../public/engine.mjs';
const bank = JSON.parse(readFileSync(new URL('../public/data/questions.json', import.meta.url), 'utf8'));
const byId = new Map(bank.map(q => [q.id, q]));
let seed = 99;
const random = () => { seed = (seed * 1664525 + 1013904223) % 4294967296; return seed / 4294967296; };
const filters = {year: '', semester: '1', grade: '8', exam: '', region: '', school: '', difficulty: '', scopeMode: 'units', curriculumOnly: true,
  unitWeights: {'nanyi-8-1-1-1': 20, 'nanyi-8-1-1-2': 20, 'nanyi-8-1-1-3': 20, 'nanyi-8-1-2-1': 20, 'nanyi-8-1-2-3': 20}};
const counts = {choice: 10, fill: 6, written: 4}, ratios = {easy: 50, medium: 50, hard: 0};
const sum = {};
let ok = 0, fail = 0, shortage = 0;
for (let i = 0; i < Number(process.argv[2] || 200); i++) {
  let r;
  try { r = generate(bank, filters, counts, ratios, 100, random); } catch (e) { fail++; continue; }
  ok++; if (r.notices.length) shortage++;
  for (const type of TYPES) {
    const mine = r.items.map(x => byId.get(x.id)).filter(q => q.type === type);
    sum[type] ??= {easy: 0, medium: 0, hard: 0, n: 0};
    for (const q of mine) sum[type][q.difficulty]++;
    sum[type].n += mine.length;
  }
}
console.log(`單元模式 簡單50／中等50：成功 ${ok} 次、失敗 ${fail} 次、出現題量不足提示 ${shortage} 次`);
console.log(TYPES.map(t => sum[t] ? `${t}: 簡單${(100 * sum[t].easy / sum[t].n).toFixed(0)}% 中等${(100 * sum[t].medium / sum[t].n).toFixed(0)}% 困難${(100 * sum[t].hard / sum[t].n).toFixed(0)}%` : '').join('  |  '));
