import {readFileSync, writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import path from 'node:path';

const research = path.dirname(fileURLToPath(import.meta.url));
const read = p => JSON.parse(readFileSync(p, 'utf8'));
const sha = s => createHash('sha256').update(s).digest('hex');
const questionPath = path.join(research, '../public/data/questions.json');
const sourceBytes = readFileSync(questionPath);
const all = JSON.parse(sourceBytes.toString('utf8'));
const active = all.filter(q => !q.selectionHidden && q.usable !== false && q.reviewed && q.typesetVerified);
const tags = read(path.join(research, 'question-unit-tags.json'));
const catalog = read(path.join(research, 'nanyi-units.json'));
const overrides = read(path.join(research, 'question-unit-overrides.json'));
const units = new Set(catalog.map(u => u.id));
const activeIds = new Set(active.map(q => q.id));
const map = new Map(tags.map(t => [t.id,t]));
const duplicateIds = tags.filter((t,i) => tags.findIndex(v => v.id === t.id) !== i).map(t => t.id);
const missing = active.filter(q => !map.has(q.id)).map(q => q.id);
const extra = tags.filter(t => !activeIds.has(t.id)).map(t => t.id);
const hashMismatches = [], schemaErrors = [];
for (const q of active) {
  const t = map.get(q.id);
  if (!t) continue;
  const expected = sha(JSON.stringify({blocks:q.blocks||[], diagramSvg:q.diagramSvg||null}));
  if (t.contentSha256 !== expected) hashMismatches.push(q.id);
  if (t.reviewed !== true || typeof t.assignmentBasis !== 'string' || !t.assignmentBasis.trim()
      || !Array.isArray(t.unitIds) || !t.unitIds.every(id => typeof id === 'string' && units.has(id))
      || new Set(t.unitIds).size !== t.unitIds.length
      || (t.status === 'assigned' ? t.primaryUnitId !== t.unitIds[0] || !units.has(t.primaryUnitId)
          : t.status !== 'unknown' || t.primaryUnitId !== 'unknown' || t.unitIds.length !== 0)) {
    schemaErrors.push(q.id);
  }
}
const count = ids => Object.fromEntries([...new Set(ids)].sort().map(id => [id, ids.filter(x=>x===id).length]));
const unknown = tags.filter(t => t.status === 'unknown');
const primaryCounts = Object.fromEntries(catalog.map(u => [u.id,tags.filter(t=>t.primaryUnitId===u.id).length]));
const audit = {
  schemaVersion:1,
  generatedAt:new Date().toISOString(),
  catalogEdition:'南一112學年度國中數學教材簡介本（108課綱）',
  catalogUnits:catalog.length,
  catalogCountsByGradeSemester:count(catalog.map(u=>`${u.grade}-${u.semester}`)),
  sourceQuestionFile:'public/data/questions.json',
  sourceQuestionFileSha256:sha(sourceBytes),
  totalQuestionRecords:all.length,
  activeQuestionRecords:active.length,
  tagRecords:tags.length,
  assigned:tags.length-unknown.length,
  unknown,
  allTagsReviewed:tags.every(t=>t.reviewed===true),
  reviewScope:'逐題檢查現有已核對題目的題幹、公式、選項、表格與題圖文字，對應數學概念。此核對是單元分類核對，不新增原卷轉寫驗證聲明。',
  classificationBasis:'只依實際題目內容；不使用學年度、原卷年級、學期或段考次別推定單元。跨概念保留unitIds，抽題配比以primaryUnitId唯一計數。',
  manualContentOverrides:Object.keys(overrides).length,
  hashDefinition:"SHA256(UTF8(JSON.stringify({blocks:q.blocks||[],diagramSvg:q.diagramSvg||null})))",
  hashImplementation:'Node.js JSON.stringify + node:crypto createHash(sha256)',
  missing,extra,duplicateIds,hashMismatches,schemaErrors,
  primaryCounts,
  zeroQuestionUnitIds:catalog.filter(u=>primaryCounts[u.id]===0).map(u=>u.id),
  multiUnitQuestionRecords:tags.filter(t=>t.unitIds.length>1).length,
  passed:missing.length===0 && extra.length===0 && duplicateIds.length===0 && hashMismatches.length===0 && schemaErrors.length===0
};
writeFileSync(path.join(research,'question-unit-tags-audit.json'),JSON.stringify(audit,null,2)+'\n','utf8');
console.log(JSON.stringify({passed:audit.passed,active:audit.activeQuestionRecords,tags:audit.tagRecords,assigned:audit.assigned,unknown:unknown.length,hashMismatches,schemaErrors,zeroUnits:audit.zeroQuestionUnitIds.length,multiUnit:audit.multiUnitQuestionRecords}));
if (!audit.passed) process.exitCode = 1;
