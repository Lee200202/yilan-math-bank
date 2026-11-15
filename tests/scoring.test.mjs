import {test} from 'node:test';
import assert from 'node:assert/strict';
import {allocateScores,generate,replaceQuestion} from '../public/engine.mjs';

const rank={easy:0,medium:1,hard:2},levels=Object.keys(rank);
let sequence=0;
const question=(type,difficulty='medium')=>({id:`scoring-fixture-${++sequence}`,number:sequence,sourceSha256:'scoring-fixture-paper',school:'配分測試校',year:114,semester:1,grade:8,exam:2,primaryUnitId:'fixture-unit',type,difficulty,reviewed:true,typesetVerified:true});
const itemsOf=(choice,fill,written)=>[
 ...Array.from({length:choice},(_,i)=>question('choice',levels[i%3])),
 ...Array.from({length:fill},(_,i)=>question('fill',levels[i%3])),
 ...Array.from({length:written},(_,i)=>question('written',levels[i%3])),
];
const randomFor=seed=>()=>{seed|=0;seed=seed+0x6D2B79F5|0;let t=Math.imul(seed^seed>>>15,1|seed);t=t+Math.imul(t^t>>>7,61|t)^t;return ((t^t>>>14)>>>0)/4294967296;};
function permute(rows,seed){const a=[...rows],random=randomFor(seed);for(let i=a.length-1;i>0;i--){const j=Math.floor(random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
function scored(rows,scores){assert.equal(scores.length,rows.length);return rows.map((q,i)=>({...q,score:scores[i]}));}
function assertAllocation(rows,scores,total){
 const qs=scored(rows,scores);assert.equal(scores.reduce((a,b)=>a+b,0),total);assert.ok(scores.every(n=>Number.isInteger(n)&&n>=1));
 const choice=qs.filter(q=>q.type==='choice');if(choice.length)assert.equal(new Set(choice.map(q=>q.score)).size,1,'every multiple-choice question must have the same score');
 const fill=qs.filter(q=>q.type==='fill');
 if(fill.length){assert.ok(Math.max(...fill.map(q=>q.score))-Math.min(...fill.map(q=>q.score))<=1,'fill scores must differ by at most one');
  for(const high of fill)for(const low of fill)if(rank[high.difficulty]>rank[low.difficulty])assert.ok(high.score>=low.score,`${high.difficulty} must receive remainder points before ${low.difficulty}`);
 }
 return qs;
}
function scoringSummary(qs){return Object.fromEntries(['choice','fill'].flatMap(type=>levels.map(level=>[`${type}:${level}`,qs.filter(q=>q.type===type&&q.difficulty===level).map(q=>q.score).sort((a,b)=>a-b)])));}
const filters=mode=>({scopeMode:mode,unitWeights:mode==='units'?{'fixture-unit':100}:{},grade:'8',semester:'1',exam:'2',school:'配分測試校',curriculumOnly:false});
function resolve(bank,result){const byId=new Map(bank.map(q=>[q.id,q]));return result.items.map(item=>({...byId.get(item.id),score:item.score}));}
function assertFillOrder(qs){
 const fill=qs.filter(q=>q.type==='fill');
 for(let i=1;i<fill.length;i++){
  assert.ok(rank[fill[i-1].difficulty]<=rank[fill[i].difficulty],'generated fill section must progress easy → medium → hard');
  assert.ok(fill[i-1].score<=fill[i].score,'fill section scores must never decrease');
 }
}

test('mixed score allocations preserve exact integer totals, uniform MC scores and fair fill scores across many paper sizes',()=>{
 for(const c of [0,1,2,3,7,13])for(const f of [0,1,2,5,8])for(const w of [0,1,3]){
  const rows=itemsOf(c,f,w),n=rows.length;if(!n)continue;
  for(const total of [...new Set([n,n+1,n+7,100,137].filter(t=>t>=n))]){
   if(c&&!f&&!w&&total%c)continue;
   const input=permute(rows,total+c+f),before=JSON.stringify(input);
   assertAllocation(input,allocateScores(input,total),total);assert.equal(JSON.stringify(input),before,'allocateScores must preserve item/index correspondence');
  }
 }
});

test('fill-only papers use floor/ceiling equal shares and hard → medium → easy remainder priority',()=>{
 for(let n=3;n<=21;n++)for(let extra=0;extra<=2*n;extra++){
  const rows=permute(itemsOf(0,n,0),n+extra),total=n+extra,qs=assertAllocation(rows,allocateScores(rows,total),total);
  const base=Math.floor(total/n),remainder=total%n;
  assert.ok(qs.every(q=>q.score===base||q.score===base+1));assert.equal(qs.filter(q=>q.score===base+1).length,remainder);
  const expectedHigh={easy:0,medium:0,hard:0};let left=remainder;
  for(const level of ['hard','medium','easy']){expectedHigh[level]=Math.min(left,rows.filter(q=>q.difficulty===level).length);left-=expectedHigh[level];}
  for(const level of levels)assert.equal(qs.filter(q=>q.difficulty===level&&q.score===base+1).length,expectedHigh[level]);
 }
});

test('four remainder points in six fill questions go to both hard and both medium questions',()=>{
 const rows=['easy','hard','medium','easy','medium','hard'].map(d=>question('fill',d));
 const qs=assertAllocation(rows,allocateScores(rows,100),100);
 for(const q of qs)assert.equal(q.score,q.difficulty==='easy'?16:17);
});

test('input permutations cannot change MC score or fill score distribution by difficulty',()=>{
 for(const spec of [[3,7,2],[7,8,1],[1,9,3],[0,11,0]])for(const total of [100,137]){
  const rows=itemsOf(...spec),reference=scoringSummary(assertAllocation(rows,allocateScores(rows,total),total));
  for(const seed of [1,2,19,73]){const input=permute(rows,seed);assert.deepEqual(scoringSummary(assertAllocation(input,allocateScores(input,total),total)),reference);}
 }
});

test('written questions retain their larger relative weight without breaking MC or fill constraints',()=>{
 const rows=itemsOf(3,7,2),qs=assertAllocation(rows,allocateScores(rows,1000),1000);
 const avg=type=>{const group=qs.filter(q=>q.type===type);return group.reduce((n,q)=>n+q.score,0)/group.length;};
 for(const type of ['choice','fill'])assert.ok(avg('written')/avg(type)>2.2&&avg('written')/avg(type)<2.8,'large-score allocation should retain the approximately 2.5 written weight');
});

test('new seven-fill papers sort by difficulty, then put higher scores last within the same difficulty',()=>{
 const bank=permute(levels.flatMap(d=>Array.from({length:6},()=>question('fill',d))),5);
 for(const mode of ['exam','units'])for(const seed of [1,7,29]){
  const r=generate(bank,filters(mode),{choice:0,fill:7,written:0},{easy:43,medium:43,hard:14},100,randomFor(seed)),qs=resolve(bank,r);
  assertAllocation(qs,qs.map(q=>q.score),100);assertFillOrder(qs);
  assert.deepEqual(qs.map(q=>q.difficulty),['easy','easy','easy','medium','medium','medium','hard']);
  assert.deepEqual(qs.map(q=>q.score),[14,14,14,14,14,15,15]);
 }
});

test('mixed exam and unit generation keeps totals, MC equality and nondecreasing fill sections',()=>{
 const bank=permute([...Array.from({length:6},()=>question('choice','easy')),...levels.flatMap(d=>Array.from({length:8},()=>question('fill',d))),...Array.from({length:5},()=>question('written','hard'))],91);
 for(const mode of ['exam','units'])for(const total of [100,137])for(const seed of [3,11,27]){
  const r=generate(bank,filters(mode),{choice:3,fill:7,written:2},{easy:34,medium:33,hard:33},total,randomFor(seed)),qs=resolve(bank,r);
  assert.equal(qs.length,12);for(const [type,n] of Object.entries({choice:3,fill:7,written:2}))assert.equal(qs.filter(q=>q.type===type).length,n);
  assertAllocation(qs,qs.map(q=>q.score),total);assertFillOrder(qs);
 }
});

test('replacing a fill question preserves every score, all other IDs and the existing order',()=>{
 const bank=levels.flatMap(d=>Array.from({length:9},()=>question('fill',d))),f=filters('units');
 const r=generate(bank,f,{choice:0,fill:7,written:0},{easy:43,medium:43,hard:14},100,randomFor(9));
 const session={format:'lanjuan-1',revision:2,title:'配分測試',filters:f,items:r.items},before=structuredClone(session);
 for(const index of [0,3,6]){
  const next=replaceQuestion(bank,session,index,f,randomFor(index+2));assert.notEqual(next.items[index].id,before.items[index].id);
  assert.deepEqual(next.items.map(q=>q.score),before.items.map(q=>q.score));assert.deepEqual(next.items.filter((_,i)=>i!==index),before.items.filter((_,i)=>i!==index));
  assertFillOrder(resolve(bank,next));assert.deepEqual(session,before);
 }
});

test('replacing a multiple-choice question keeps the common MC score and all other scores',()=>{
 const bank=[...Array.from({length:8},()=>question('choice','easy')),...levels.flatMap(d=>Array.from({length:8},()=>question('fill',d)))],f=filters('exam');
 const r=generate(bank,f,{choice:3,fill:7,written:0},{easy:40,medium:40,hard:20},100,randomFor(8));
 const session={format:'lanjuan-1',revision:1,filters:f,items:r.items},index=resolve(bank,r).findIndex(q=>q.type==='choice'),next=replaceQuestion(bank,session,index,f,randomFor(2));
 assert.notEqual(next.items[index].id,session.items[index].id);assert.deepEqual(next.items.map(q=>q.score),session.items.map(q=>q.score));assertAllocation(resolve(bank,next),next.items.map(q=>q.score),100);
});

test('MC-only papers use equal integer scores for multiple counts and divisible totals',()=>{
 for(const n of [1,2,3,6,7,11,19,80])for(const each of [1,2,7,11]){
  const total=n*each;if(total>1000)continue;
  const rows=permute(itemsOf(n,0,0),n+each),scores=allocateScores(rows,total);assert.deepEqual(scores,Array(n).fill(each));
 }
});

test('three MC questions at 100 points reject the impossible split and suggest 99/102 or another question type',()=>{
 assert.throws(()=>allocateScores(itemsOf(3,0,0),100),error=>/選擇題/.test(error.message)&&error.message.includes('99')&&error.message.includes('102')&&/其他題型|加入.*題|增加.*題/.test(error.message));
});

test('other indivisible MC-only totals also reject instead of silently changing scores or total',()=>{
 for(const n of [2,3,6,7,11,19,80]){
  const total=3*n+1,low=Math.floor(total/n)*n,high=low+n;
  assert.throws(()=>allocateScores(itemsOf(n,0,0),total),error=>/選擇題/.test(error.message)&&error.message.includes(String(low))&&error.message.includes(String(high)));
 }
});

test('generation exposes MC-only divisibility errors while 99 and 102 remain usable',()=>{
 const bank=Array.from({length:8},()=>question('choice','easy'));
 for(const mode of ['exam','units']){
  assert.throws(()=>generate(bank,filters(mode),{choice:3,fill:0,written:0},{easy:100,medium:0,hard:0},100),/99.*102/);
  for(const total of [99,102]){
   const r=generate(bank,filters(mode),{choice:3,fill:0,written:0},{easy:100,medium:0,hard:0},total,randomFor(total));assert.deepEqual(r.items.map(q=>q.score),Array(3).fill(total/3));assert.equal(r.items.reduce((n,q)=>n+q.score,0),total);
  }
 }
});
