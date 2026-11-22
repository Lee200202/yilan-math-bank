// Measures how evenly every question type is spread over the chosen units ("自選單元" mode).
// Usage: node scripts/sim_unit_balance.mjs [runs] [path-to-other-engine.mjs]
// Reports, per generated paper, the largest |actual - ideal| of any (type, unit) cell, where
// ideal = type count * unit weight. A value < 1 means every cell is within rounding of the ideal split.
import {readFile} from 'node:fs/promises';
import {fileURLToPath,pathToFileURL} from 'node:url';
import path from 'node:path';
const root=fileURLToPath(new URL('../',import.meta.url));
const runs=Number(process.argv[2]||300);
const engine=await import(process.argv[3]?pathToFileURL(path.resolve(process.argv[3])).href:new URL('../public/engine.mjs',import.meta.url).href);
const bank=JSON.parse(await readFile(path.join(root,'public/data/questions.json'),'utf8'));
let seed=12345;const rnd=()=>{seed=(seed*1664525+1013904223)%4294967296;return seed/4294967296;};
const TYPES=['choice','fill','written'];
const byGrade=new Map();
for(const q of bank){if(!q.primaryUnitId||!q.reviewed||q.typesetVerified!==true||q.selectionHidden)continue;const k=`${q.grade}-${q.semester}`;if(!byGrade.has(k))byGrade.set(k,new Map());const m=byGrade.get(k);if(!m.has(q.primaryUnitId))m.set(q.primaryUnitId,{choice:0,fill:0,written:0});m.get(q.primaryUnitId)[q.type]++;}
let papers=0,fail=0,sumDev=0,worst=0,bad=0;const examples=[];
for(let r=0;r<runs;r++){
 const keys=[...byGrade.keys()],key=keys[Math.floor(rnd()*keys.length)],[grade,semester]=key.split('-').map(Number),units=[...byGrade.get(key)].filter(([,s])=>s.choice+s.fill+s.written>=15).map(([id])=>id);
 if(units.length<2)continue;
 const n=2+Math.floor(rnd()*Math.min(4,units.length-1)),chosen=engine.shuffle(units,rnd).slice(0,n);
 const weights=Object.fromEntries(chosen.map((id,i)=>[id,Math.floor(100/n)+(i<100%n?1:0)]));
 const counts={choice:6+Math.floor(rnd()*10),fill:3+Math.floor(rnd()*6),written:Math.floor(rnd()*3)};
 const filters={grade,semester,scopeMode:'units',unitWeights:weights};
 let res;try{res=engine.generate(bank,filters,counts,{easy:34,medium:33,hard:33},100,rnd);}catch(e){fail++;continue;}
 papers++;
 const byId=new Map(bank.map(q=>[q.id,q]));
 const total=TYPES.reduce((s,t)=>s+counts[t],0);let dev=0;
 for(const t of TYPES)for(const id of chosen){
  const actual=res.items.filter(i=>{const q=byId.get(i.id);return q.type===t&&q.primaryUnitId===id;}).length;
  const stock=byGrade.get(key).get(id)[t],ideal=counts[t]*weights[id]/100;
  // a unit that simply lacks that type cannot be asked to supply it: compare against what its stock allows
  const target=Math.min(ideal,stock);dev=Math.max(dev,Math.abs(actual-target));
 }
 sumDev+=dev;worst=Math.max(worst,dev);if(dev>=1.5){bad++;if(examples.length<3)examples.push({key,counts,n,dev:+dev.toFixed(2)});}
}
console.log(JSON.stringify({engine:process.argv[3]||'current',papers,generationFailures:fail,meanMaxDeviation:+(sumDev/papers).toFixed(3),worstDeviation:+worst.toFixed(2),papersWithDeviationOver1_5:bad,examples}));
