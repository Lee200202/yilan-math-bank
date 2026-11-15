import {test} from 'node:test';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {readFile} from 'node:fs/promises';
import {generate,eligible,eligiblePool,availableCounts,replaceQuestion,validateSession} from '../public/engine.mjs';

const U22='nani-8a-2-2',U31='nani-8a-3-1',U32='nani-8a-3-2';
const TYPES=['choice','fill','written'],LEVELS=['easy','medium','hard'];
const counts=(choice=0,fill=0,written=0)=>({choice,fill,written});
const ratios=(easy=0,medium=0,hard=0)=>({easy,medium,hard});
const seedRandom=seed=>()=>{seed|=0;seed=seed+0x6D2B79F5|0;let t=Math.imul(seed^seed>>>15,1|seed);t=t+Math.imul(t^t>>>7,61|t)^t;return ((t^t>>>14)>>>0)/4294967296;};
let seq=0;
// Hand-authored semantic fixtures, never represented as archived school questions.
function question(unit,type,difficulty,extra={}){
 const number=++seq;
 const text=unit===U22?'直角三角形兩股為3、4，求斜邊長。':unit===U31?'因式分解 $3x^2+6x$。':'用十字交乘法因式分解 $2x^2+5x+2$。';
 return {id:`fixture-${number}`,number,sourceSha256:createHash('sha256').update(`fixture-paper:${unit}`).digest('hex'),school:'配比測試校',year:114,semester:1,grade:8,exam:unit===U32?3:2,type,difficulty,primaryUnitId:unit,unitIds:[unit],reviewed:true,typesetVerified:true,blocks:[{type:'text',text}],...extra};
}
const balanced=()=>[U22,U31,U32].flatMap(u=>TYPES.flatMap(t=>LEVELS.flatMap(d=>[question(u,t,d),question(u,t,d)])));
const filters=weights=>({scopeMode:'units',unitWeights:weights,semester:'1',grade:'8',exam:'2',school:'配比測試校',curriculumOnly:false});
function picked(bank,result){const map=new Map(bank.map(q=>[q.id,q]));return result.items.map(q=>map.get(q.id));}
function tally(rows,key){return rows.reduce((a,q)=>(a[q[key]]=(a[q[key]]||0)+1,a),{});}
function session(result,f){return {format:'lanjuan-1',title:'八年級上學期第二次段考練習',createdAt:'2026-11-15',revision:3,filters:f,items:result.items};}

test('changing unit weights changes exact unit allocation while preserving type totals and scores',()=>{
 const bank=balanced(),wanted=counts(4,4,2);
 for(const seed of [1,7,42])for(const [a,b] of [[20,80],[80,20]]){
  const r=generate(bank,filters({[U22]:a,[U31]:b}),wanted,ratios(50,50),137,seedRandom(seed));
  const qs=picked(bank,r);
  assert.deepEqual(tally(qs,'primaryUnitId'),{[U22]:a/10,[U31]:b/10});
  assert.deepEqual(tally(qs,'type'),wanted);
  assert.deepEqual(tally(qs,'difficulty'),{easy:5,medium:5});
  assert.equal(r.items.reduce((s,q)=>s+q.score,0),137);
  assert.equal(new Set(r.items.map(q=>q.id)).size,10);
  assert.equal(r.notices.length,0);
 }
});

test('largest-remainder unit quotas and all requested question-type totals are exact',()=>{
 const bank=balanced(),r=generate(bank,filters({[U22]:50,[U31]:30,[U32]:20}),counts(3,3,1),ratios(100),100,seedRandom(8));
 assert.deepEqual(tally(picked(bank,r),'primaryUnitId'),{[U22]:4,[U31]:2,[U32]:1});
 assert.deepEqual(tally(picked(bank,r),'type'),counts(3,3,1));
});

test('two feasible cross-type questions achieve full-paper 50/50 difficulty across two units',()=>{
 const bank=[question(U22,'choice','easy'),question(U22,'choice','hard'),question(U31,'fill','easy'),question(U31,'fill','hard')];
 for(const seed of [1,2,3,91]){
  const r=generate(bank,filters({[U22]:50,[U31]:50}),counts(1,1),ratios(50,0,50),100,seedRandom(seed));
  assert.deepEqual(tally(picked(bank,r),'difficulty'),{easy:1,hard:1});assert.equal(r.notices.length,0);
 }
});

test('one unit can satisfy global 50/50 difficulty without rounding each type independently',()=>{
 const bank=[question(U32,'choice','easy'),question(U32,'choice','hard'),question(U32,'fill','easy'),question(U32,'fill','hard')];
 const r=generate(bank,filters({[U32]:100}),counts(1,1),ratios(50,0,50),100,seedRandom(6));
 assert.deepEqual(tally(picked(bank,r),'difficulty'),{easy:1,hard:1});assert.equal(r.notices.length,0);
});

test('exam mode also rounds difficulty once for the full paper',()=>{
 const bank=[question(U22,'choice','easy'),question(U22,'choice','hard'),question(U22,'fill','easy'),question(U22,'fill','hard')];
 const r=generate(bank,{...filters({}),scopeMode:'exam'},counts(1,1),ratios(50,0,50),100,seedRandom(11));
 assert.deepEqual(tally(picked(bank,r),'difficulty'),{easy:1,hard:1});assert.equal(r.notices.length,0);
});

test('a feasible assignment can require coordinated unit/type/difficulty choices',()=>{
 const bank=[question(U22,'choice','easy'),question(U22,'fill','hard'),question(U31,'choice','hard'),question(U31,'fill','medium')];
 const r=generate(bank,filters({[U22]:50,[U31]:50}),counts(1,1),ratios(50,50),100,seedRandom(17));
 assert.deepEqual(tally(picked(bank,r),'primaryUnitId'),{[U22]:1,[U31]:1});
 assert.deepEqual(tally(picked(bank,r),'difficulty'),{easy:1,medium:1});assert.equal(r.notices.length,0);
});

test('an alternative type/difficulty matrix is searched before declaring difficulty shortage',()=>{
 const bank=[question(U22,'choice','easy'),question(U22,'fill','hard'),question(U22,'choice','hard'),question(U31,'fill','easy'),question(U31,'fill','medium')];
 const r=generate(bank,filters({[U22]:50,[U31]:50}),counts(1,1),ratios(50,0,50),100,seedRandom(31));
 assert.deepEqual(tally(picked(bank,r),'primaryUnitId'),{[U22]:1,[U31]:1});
 assert.deepEqual(tally(picked(bank,r),'difficulty'),{hard:1,easy:1});assert.equal(r.notices.length,0);
});

test('difficulty shortage is explicit and fallback never leaves selected units or source filters',()=>{
 const bank=[question(U22,'fill','easy'),question(U22,'fill','easy'),question(U31,'fill','hard'),question(U31,'fill','hard'),question(U22,'fill','hard',{school:'其他校'}),question(U22,'fill','hard',{grade:9})];
 const r=generate(bank,filters({[U22]:100}),counts(0,2),ratios(0,0,100),100,seedRandom(2));
 assert.equal(r.items.length,2);assert.ok(picked(bank,r).every(q=>q.primaryUnitId===U22&&q.difficulty==='easy'&&q.school==='配比測試校'&&q.grade===8));
 assert.ok(r.notices.some(n=>n.includes('所選單元')&&n.includes('難度')));
});

test('incompatible unit/type quotas fail even when aggregate stock and outside-unit decoys are sufficient',()=>{
 const bank=[...Array.from({length:4},()=>question(U22,'choice','easy')),...Array.from({length:4},()=>question(U31,'fill','easy')),...Array.from({length:4},()=>question(U32,'choice','easy'))];
 const f=filters({[U22]:50,[U31]:50});assert.deepEqual(availableCounts(bank,f),counts(4,4));
 assert.throws(()=>generate(bank,f,counts(4,2),ratios(100),100,seedRandom(5)),/單元配比.*題型|無法同時滿足/);
});

test('an empty selected unit fails without borrowing from another selected unit',()=>{
 const bank=Array.from({length:8},()=>question(U22,'fill','easy'));
 assert.throws(()=>generate(bank,filters({[U22]:50,[U31]:50}),counts(0,4),ratios(100)),/無法同時滿足/);
});

test('an 80-question shortage respects forced unit capacity instead of searching impossible difficulty matrices',()=>{
 const bank=[...TYPES.flatMap(type=>Array.from({length:40},()=>question(U22,type,'easy'))),...TYPES.flatMap(type=>LEVELS.flatMap(level=>Array.from({length:40},()=>question(U31,type,level))))];
 const r=generate(bank,filters({[U22]:50,[U31]:50}),counts(27,27,26),ratios(33,34,33),100,seedRandom(7));
 assert.deepEqual(tally(picked(bank,r),'primaryUnitId'),{[U22]:40,[U31]:40});assert.deepEqual(tally(picked(bank,r),'type'),counts(27,27,26));
 assert.ok(picked(bank,r).filter(q=>q.difficulty==='easy').length>=40);assert.ok(r.notices.length>0);
});

test('unit and difficulty ratio validation rejects malformed or non-total percentages',()=>{
 const bank=balanced();
 for(const weights of [{[U22]:90},{[U22]:-1,[U31]:101},{[U22]:Infinity},{[U22]:NaN},[100]])assert.throws(()=>generate(bank,filters(weights),counts(0,1),ratios(100)),/100%/);
 for(const value of [null,[100],{unknown:100},{easy:50,hard:40},{easy:-1,hard:101}])assert.throws(()=>generate(bank,filters({[U22]:100}),counts(0,1),value),/100%/);
});

test('unit 3-2 from exam 3 remains selectable with exam=2, while unknown and zero-weight units stay excluded',()=>{
 const good=question(U32,'fill','easy'),unknown=question(undefined,'fill','easy'),zero=question(U22,'fill','easy');
 const f=filters({[U32]:100,[U22]:0});assert.equal(eligible(good,f),true);assert.equal(eligible(unknown,f),false);assert.equal(eligible(zero,f),false);
 const r=generate([good,unknown,zero],f,counts(0,1),ratios(100));assert.equal(r.items[0].id,good.id);
 assert.equal(eligible(good,{...f,scopeMode:'exam'}),false);
});

test('replacement retains primary unit, type, difficulty, every other ID, order, score and session settings',()=>{
 const bank=balanced(),f=filters({[U22]:50,[U32]:50}),s=session(generate(bank,f,counts(2,2),ratios(50,0,50),137,seedRandom(4)),f);
 s.items[0].score=19;const before=structuredClone(s),old=bank.find(q=>q.id===s.items[0].id);bank.push(question(old.primaryUnitId,old.type,old.difficulty));
 const next=replaceQuestion(bank,s,0,f,seedRandom(5)),replacement=bank.find(q=>q.id===next.items[0].id);
 assert.notEqual(replacement.id,old.id);for(const k of ['primaryUnitId','type','difficulty'])assert.equal(replacement[k],old[k]);
 assert.deepEqual(next.items.slice(1),before.items.slice(1));assert.deepEqual(next.items.map(q=>q.score),before.items.map(q=>q.score));
 assert.deepEqual(next.filters,before.filters);assert.equal(next.title,before.title);assert.equal(next.createdAt,before.createdAt);assert.equal(next.revision,before.revision+1);assert.deepEqual(s,before);
});

test('replacement cannot cross primary units or reuse a different ID for used content',()=>{
 const original=question(U22,'fill','easy'),alias={...original,id:'fixture-content-alias'},other=question(U31,'fill','easy'),f=filters({[U22]:50,[U31]:50});
 assert.throws(()=>replaceQuestion([original,alias,other],session({items:[{id:original.id,score:100}]},f),0,f),/已無未使用/);
});

test('PDF session validation preserves normalized unit weights and exact IDs/order/scores',()=>{
 const bank=balanced(),f={...filters({[U22]:'25',[U32]:'75'})},s=session(generate(bank,f,counts(2,2),ratios(50,0,50),100,seedRandom(9)),f);
 const restored=validateSession(JSON.parse(JSON.stringify(s)),bank);
 assert.equal(restored.filters.scopeMode,'units');assert.deepEqual(restored.filters.unitWeights,{[U22]:25,[U32]:75});assert.equal(restored.filters.exam,'2');
 assert.deepEqual(restored.items,s.items);assert.equal(restored.title,s.title);
 for(const bad of [{[U22]:80},{[U22]:-1,[U32]:101},{[U22]:NaN},{[U22]:Infinity},[100]])assert.throws(()=>validateSession({...s,filters:{...f,unitWeights:bad}},bank),/單元配比/);
});

test('source SHA/type/original-number aliases count once and cannot satisfy two requested slots',()=>{
 const q=question(U22,'fill','easy'),alias={...q,id:'fixture-alias-2',paperId:'different-metadata-alias'},bank=[q,alias],f=filters({[U22]:100});
 assert.equal(eligiblePool(bank,f).length,1);assert.deepEqual(availableCounts(bank,f),counts(0,1));
 assert.equal(generate(bank,f,counts(0,1),ratios(100)).items.length,1);
 assert.throws(()=>generate(bank,f,counts(0,2),ratios(100)),/無法同時滿足|只有/);
});

test('PDF session validation rejects distinct IDs that alias identical source content',()=>{
 const q=question(U22,'fill','easy'),alias={...q,id:'fixture-import-alias'},f=filters({[U22]:100});
 assert.throws(()=>validateSession(session({items:[{id:q.id,score:50},{id:alias.id,score:50}]},f),[q,alias]),/重複題目/);
});

test('small exhaustive subset oracle confirms joint feasibility before any difficulty fallback',()=>{
 const wanted=counts(1,1,1),f=filters({[U22]:67,[U31]:33});
 for(let seed=1;seed<=120;seed++){
  const random=seedRandom(seed),bank=Array.from({length:9},()=>question(random()<.6?U22:U31,TYPES[Math.floor(random()*3)],LEVELS[Math.floor(random()*3)]));
  let hardFeasible=false,difficultyFeasible=false;
  for(let a=0;a<bank.length-2;a++)for(let b=a+1;b<bank.length-1;b++)for(let c=b+1;c<bank.length;c++){
   const qs=[bank[a],bank[b],bank[c]],ut=tally(qs,'primaryUnitId'),tt=tally(qs,'type');
   if(ut[U22]!==2||ut[U31]!==1||TYPES.some(type=>tt[type]!==1))continue;
   hardFeasible=true;if(LEVELS.every(level=>tally(qs,'difficulty')[level]===1))difficultyFeasible=true;
  }
  if(!hardFeasible){assert.throws(()=>generate(bank,f,wanted,ratios(34,33,33),100,seedRandom(seed)),/無法同時滿足/,`seed ${seed}`);continue;}
  const r=generate(bank,f,wanted,ratios(34,33,33),100,seedRandom(seed)),qs=picked(bank,r);
  assert.deepEqual(tally(qs,'primaryUnitId'),{[U22]:2,[U31]:1},`unit totals, seed ${seed}`);assert.deepEqual(tally(qs,'type'),wanted);
  if(difficultyFeasible){assert.deepEqual(tally(qs,'difficulty'),{easy:1,medium:1,hard:1},`feasible difficulty, seed ${seed}`);assert.equal(r.notices.length,0);}
  else assert.ok(r.notices.some(n=>n.includes('所選單元')),`missing fallback notice, seed ${seed}`);
 }
});

test('published unit-labelled questions use the same exact-quota path when data is available',async t=>{
 const bank=JSON.parse(await readFile(new URL('../public/data/questions.json',import.meta.url),'utf8'));
 const eligibleRows=bank.filter(q=>q.reviewed&&q.typesetVerified&&!q.selectionHidden&&q.primaryUnitId);
 const units=[...new Set(eligibleRows.map(q=>q.primaryUnitId))].slice(0,2);
 if(units.length<2){t.skip('published question bank has fewer than two verified primary-unit groups');return;}
 const f={scopeMode:'units',unitWeights:{[units[0]]:50,[units[1]]:50},curriculumOnly:false};
 const first=eligibleRows.find(q=>q.primaryUnitId===units[0]),second=eligibleRows.find(q=>q.primaryUnitId===units[1]),wanted=counts();wanted[first.type]++;wanted[second.type]++;
 const r=generate(bank,f,wanted,ratios(100),100,seedRandom(13));assert.deepEqual(tally(picked(bank,r),'primaryUnitId'),{[units[0]]:1,[units[1]]:1});assert.deepEqual(tally(picked(bank,r),'type'),Object.fromEntries(Object.entries(wanted).filter(([,n])=>n)));
});
