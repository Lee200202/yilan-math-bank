// Monte-Carlo check of generate(): looks for repeated questions inside one generated paper.
// Usage: node scripts/sim_generate.mjs [runs]
import {readFileSync} from 'node:fs';
import {generate, availableCounts, TYPES} from '../public/engine.mjs';

const bank = JSON.parse(readFileSync(new URL('../public/data/questions.json', import.meta.url), 'utf8'));
const byId = new Map(bank.map(q => [q.id, q]));
const runs = Number(process.argv[2] || 400);
const norm = q => q.blocks.map(b => (b.text || '') + (b.items || []).join('') + (b.rows || []).flat().join('')).join('').replace(/[\s　（）()．.，,、。：:；;]/g, '');
const opening = q => norm(q).slice(0, 50);
let seed = 12345;
const random = () => { seed = (seed * 1664525 + 1013904223) % 4294967296; return seed / 4294967296; };
const pick = a => a[Math.floor(random() * a.length)];
const stats = {runs: 0, dupId: 0, dupText: 0, dupOpening: 0, samePaperWritten: 0, errors: 0};
const examples = [];
for (let i = 0; i < runs; i++) {
  const filters = {year: '', semester: pick(['', '1', '2']), grade: pick(['', '7', '8', '9']), exam: pick(['', '1', '2', '3']), region: pick(['', 'yilan', 'taipei', 'new_taipei', 'taoyuan', 'taichung', 'kaohsiung']), school: '', difficulty: '', scopeMode: 'exam', curriculumOnly: true, unitWeights: {}};
  const stock = availableCounts(bank, filters);
  const want = {choice: Math.min(stock.choice, 5), fill: Math.min(stock.fill, 5), written: Math.min(stock.written, 2 + Math.floor(random() * 4))};
  if (!Object.values(want).some(Boolean)) continue;
  let result;
  try { result = generate(bank, filters, want, {easy: 40, medium: 40, hard: 20}, 100, random); } catch (e) { stats.errors++; continue; }
  stats.runs++;
  const qs = result.items.map(x => byId.get(x.id));
  if (new Set(result.items.map(x => x.id)).size !== qs.length) stats.dupId++;
  for (const type of TYPES) {
    const mine = qs.filter(q => q.type === type);
    if (new Set(mine.map(norm)).size !== mine.length) { stats.dupText++; examples.push(['text', type, filters, mine.map(q => q.id)]); }
    if (new Set(mine.map(opening)).size !== mine.length) { stats.dupOpening++; if (examples.length < 12) examples.push(['opening', type, filters, mine.map(q => q.id + ' | ' + opening(q))]); }
  }
  const written = qs.filter(q => q.type === 'written');
  if (new Set(written.map(q => q.paperId)).size !== written.length) stats.samePaperWritten++;
}
console.log(JSON.stringify(stats));
for (const e of examples.slice(0, 6)) console.log(JSON.stringify(e).slice(0, 700));
