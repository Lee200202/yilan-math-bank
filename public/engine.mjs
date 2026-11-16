export const TYPES = ['choice', 'fill', 'written'];
export const TYPE_NAMES = {choice:'選擇題',fill:'填充題',written:'非選擇題'};
export const LEVEL_NAMES = {easy:'簡單',medium:'中等',hard:'困難'};
export const REGIONS = {yilan:'宜蘭縣',taipei:'臺北市',new_taipei:'新北市',taoyuan:'桃園市',taichung:'臺中市',kaohsiung:'高雄市'};
export const regionOf = q => q.region || 'yilan';
export function eligible(q, f) {
  const byUnit=f.scopeMode==='units';
  return q.reviewed && q.typesetVerified===true && !q.selectionHidden && (!f.year || q.year===Number(f.year)) && (!f.semester || q.semester===Number(f.semester)) && (!f.grade || q.grade===Number(f.grade)) && (byUnit||!f.exam || q.exam===Number(f.exam)) && (!f.region || regionOf(q)===f.region) && (!f.school || q.school===f.school) && (!f.difficulty || q.difficulty===f.difficulty) && (!f.curriculumOnly || q.year>=108+q.grade-7) && (!byUnit||Number(f.unitWeights?.[q.primaryUnitId])>0);
}
const contentKey=q=>q.sourceSha256?`${q.sourceSha256}:${q.type}:${q.sourceNumber||q.number}`:q.id;
// Visible content (text, options, table cells and figures). Two questions with identical content are the same
// question even when they come from different source files (a school re-posts the same exam).
const visibleContent=q=>Array.isArray(q.blocks)&&q.blocks.length?JSON.stringify(q.blocks).replace(/\s+/g,''):null;
export function eligiblePool(bank,filters){const seen=new Set();return bank.filter(q=>{if(!eligible(q,filters))return false;const keys=[contentKey(q)],body=visibleContent(q);if(body)keys.push(`${q.type}:${body}`);if(keys.some(k=>seen.has(k)))return false;keys.forEach(k=>seen.add(k));return true;});}
// Sub-questions of one problem ("1-1" and "1-2", "6(1)" and "6(3)", "承上題") share a stem. A paper that carries two of
// them reads as the same question twice, so generation treats them as one family and only combines them when the
// requested scope has no other question of that type and difficulty left.
const plainText=q=>(q.blocks||[]).map(b=>(b.text||'')+(b.items||[]).join('')+(b.rows||[]).flat().join('')).join('').replace(/[\s　（）()．.，,、。：:；;]/g,'');
// "6(1)" and "1-1" are parts of problems 6 and 1; "二-2" is item 2 of section 二 and is a problem of its own.
const baseNumber=n=>{const s=String(n??'').replace(/(?:\(\d+\))+$/,'');return /^\d+(?:-\d+)+$/.test(s)?s.split('-')[0]:s;};
export function familyKeys(q){
  const number=baseNumber(q.sourceNumber||q.number),keys=[],opening=plainText(q).slice(0,50);
  if(q.sourceParentId)keys.push(`parent|${q.sourceParentId}`);else if(q.paperId&&number)keys.push(`${q.paperId}|${q.type}|#${number}`);
  // The same exam is often posted twice with small edits, so an identical opening also marks a repeat across papers.
  if(opening.length>=24)keys.push(`${q.type}|~${opening}`);
  return keys;
}
function diversify(selected,pool,byUnit,random){
  const result=[...selected];
  for(let i=0;i<result.length;i++){
    const keys=familyKeys(result[i]),others=result.filter((_,j)=>j!==i),blocked=new Set(others.flatMap(familyKeys));
    if(!keys.some(k=>blocked.has(k)))continue;
    const inUse=new Set(result.map(q=>q.id)),q=result[i];
    const fresh=pool.filter(c=>!inUse.has(c.id)&&c.type===q.type&&(!byUnit||c.primaryUnitId===q.primaryUnitId)&&!familyKeys(c).some(k=>blocked.has(k)));
    // Same difficulty keeps the requested ratio; a different one is used only so that the paper never repeats a problem.
    const sameLevel=fresh.filter(c=>c.difficulty===q.difficulty);
    const options=sameLevel.length?sameLevel:fresh;
    if(options.length)result[i]=shuffle(options,random)[0];
  }
  return result;
}
export function availableCounts(bank,filters){const pool=eligiblePool(bank,filters);return Object.fromEntries(TYPES.map(type=>[type,pool.filter(q=>q.type===type).length]));}
export function suggestedCounts(bank,filters,requested){
  const stock=availableCounts(bank,filters);
  const result=Object.fromEntries(TYPES.map(type=>[type,Math.min(stock[type],Math.max(0,Number(requested[type])||0))]));
  if(!Object.values(result).some(Boolean))for(const type of TYPES)result[type]=Math.min(stock[type],type==='written'?2:5);
  return result;
}
export function shuffle(items, random=Math.random) {const a=[...items]; for(let i=a.length-1;i>0;i--){const j=Math.floor(random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
function quotas(weights,n){const rows=Object.entries(weights).map(([key,value])=>({key,exact:n*Number(value)/100,count:Math.floor(n*Number(value)/100)}));const rest=n-rows.reduce((s,r)=>s+r.count,0);[...rows].sort((a,b)=>(b.exact-b.count)-(a.exact-a.count)).slice(0,rest).forEach(r=>r.count++);return rows;}
const LEVELS=Object.keys(LEVEL_NAMES);
function network(){
 const graph=[];
 const node=()=>{graph.push([]);return graph.length-1;};
 const edge=(a,b,cap,cost=0)=>{const forward={to:b,cap,cost,rev:graph[b].length,initial:cap},reverse={to:a,cap:0,cost:-cost,rev:graph[a].length};graph[a].push(forward);graph[b].push(reverse);return forward;};
 const push=(a,e,n)=>{e.cap-=n;graph[e.to][e.rev].cap+=n;};
 function minCost(source,sink,total){
  let flow=0;
  while(flow<total){
   const distance=Array(graph.length).fill(Infinity),previous=Array(graph.length);distance[source]=0;
   for(let pass=0;pass<graph.length-1;pass++){let changed=false;for(let a=0;a<graph.length;a++)if(Number.isFinite(distance[a]))graph[a].forEach((e,i)=>{if(e.cap>0&&distance[e.to]>distance[a]+e.cost){distance[e.to]=distance[a]+e.cost;previous[e.to]=[a,i];changed=true;}});if(!changed)break;}
   if(!Number.isFinite(distance[sink]))break;
   let n=total-flow;for(let v=sink;v!==source;){const [a,i]=previous[v];n=Math.min(n,graph[a][i].cap);v=a;}
   for(let v=sink;v!==source;){const [a,i]=previous[v];push(a,graph[a][i],n);v=a;}flow+=n;
  }
  return flow;
 }
 // Feasibility checks use Dinic rather than rerunning a cost solver for every matrix.
 function maxFlow(source,sink,total){
  let flow=0;
  while(flow<total){
   const depth=Array(graph.length).fill(-1),queue=[source];depth[source]=0;
   for(let i=0;i<queue.length;i++)for(const e of graph[queue[i]])if(e.cap>0&&depth[e.to]<0){depth[e.to]=depth[queue[i]]+1;queue.push(e.to);}
   if(depth[sink]<0)break;const current=Array(graph.length).fill(0);
   function send(a,n){if(a===sink)return n;for(;current[a]<graph[a].length;current[a]++){const e=graph[a][current[a]];if(e.cap>0&&depth[e.to]===depth[a]+1){const sent=send(e.to,Math.min(n,e.cap));if(sent){push(a,e,sent);return sent;}}}return 0;}
   let n;while(flow<total&&(n=send(source,total-flow)))flow+=n;
  }
  return flow;
 }
 return {node,edge,minCost,maxFlow};
}
const stockMatrix=pool=>TYPES.map(type=>LEVELS.map(level=>pool.filter(q=>q.type===type&&q.difficulty===level).length));
// Difficulty is rounded once across the entire paper. This transport plan
// distributes that quota between question types without imposing per-type ratios.
// The whole-paper difficulty quota is still honoured first (it is rounded once, and a shortage is the only reason to
// miss it). Within that quota every question type receives the same easy/medium/hard proportions as the paper:
// 50% easy + 50% medium means choice, fill and written are each about half easy and half medium, instead of all the
// easy questions landing in the multiple-choice section. Each extra question placed in a (type, level) cell costs the
// marginal increase of its squared distance from that cell's ideal share, so the plan is the most even split.
function typeLevelPlan(stock,counts,target,total){
 const net=network(),source=net.node(),sink=net.node(),types=TYPES.map(()=>net.node()),levels=LEVELS.map(()=>net.node());
 const UNIT=1000,OFFSET=400000,SHORTAGE=1e9,units=[];
 types.forEach((tn,t)=>{
  const n=Number(counts[TYPES[t]]);net.edge(source,tn,n);
  levels.forEach((ln,l)=>{
   const ideal=total?n*target[l]/total:0,edges=[];
   for(let k=1;k<=Math.min(stock[t][l],n);k++)edges.push(net.edge(tn,ln,1,Math.round((2*k-1-2*ideal)*UNIT)+OFFSET));
   units.push({t,l,edges});
  });
 });
 levels.forEach((ln,l)=>{net.edge(ln,sink,target[l]);net.edge(ln,sink,total,SHORTAGE);});
 if(net.minCost(source,sink,total)!==total)return null;
 const plan=TYPES.map(()=>LEVELS.map(()=>0));
 units.forEach(({t,l,edges})=>{plan[t][l]=edges.filter(e=>e.cap===0).length;});
 return plan;
}
function difficultyNotices(selected,counts,target,total,byUnit){
 const actual=LEVELS.map(level=>selected.filter(q=>q.difficulty===level).length);
 if(actual.every((n,l)=>n===target[l]))return [];
 return TYPES.filter(type=>Number(counts[type])&&LEVELS.some((level,l)=>actual[l]<target[l]&&selected.filter(q=>q.type===type&&q.difficulty===level).length<target[l]*Number(counts[type])/total)).map(type=>`${TYPE_NAMES[type]}的部分難度題量不足，已${byUnit?'在所選單元內以其他難度':'由其他難度'}補足。`);
}
// The unit/type margins remain hard constraints. Enumerating the small 3x3
// type/difficulty matrix lets unit-capacity flow checks find a jointly feasible
// global difficulty quota rather than silently changing a feasible ratio.
function unitSelection(pool,filters,counts,target,total,random){
 const weights=filters.unitWeights;
 if(!weights||typeof weights!=='object'||Array.isArray(weights)||Object.keys(weights).length>100||Object.values(weights).some(v=>!Number.isFinite(Number(v))||Number(v)<0||Number(v)>100)||Math.abs(Object.values(weights).reduce((s,v)=>s+Number(v),0)-100)>1e-6)throw new Error('勾選單元並設定配比，合計須為 100%。');
 const units=shuffle(quotas(weights,total).filter(u=>u.count),random),unitIds=new Set(units.map(u=>u.key)),activePool=pool.filter(q=>unitIds.has(q.primaryUnitId)),stock=stockMatrix(activePool);
 const problem=()=>new Error('目前單元配比與題型題數無法同時滿足；請調整單元比例、減少題數或放寬來源。');
 const preferred=typeLevelPlan(stock,counts,target,total);if(!preferred)throw problem();
 const buckets=units.map(unit=>TYPES.map(type=>LEVELS.map(level=>shuffle(activePool.filter(q=>q.primaryUnitId===unit.key&&q.type===type&&q.difficulty===level),random))));
 function select(matrix,overflow=false){
  const net=network(),source=net.node(),sink=net.node(),types=TYPES.map(()=>net.node()),cells=TYPES.map(()=>LEVELS.map(()=>net.node())),used=[];
  types.forEach((tn,t)=>{net.edge(tn,sink,Number(counts[TYPES[t]]));cells[t].forEach((cn,l)=>{net.edge(cn,tn,matrix[t][l]);if(overflow)net.edge(cn,tn,total,1);});});
  units.forEach((unit,u)=>{const un=net.node();net.edge(source,un,unit.count);buckets[u].forEach((row,t)=>row.forEach((items,l)=>{if(items.length)used.push({items,edge:net.edge(un,cells[t][l],items.length)});}));});
  const flow=overflow?net.minCost(source,sink,total):net.maxFlow(source,sink,total);
  return flow===total?used.flatMap(b=>b.items.slice(0,b.edge.initial-b.edge.cap)):null;
 }
 let selected=select(preferred,true);if(!selected)throw problem();
 function difficultyCapacityFeasible(){
  const net=network(),source=net.node(),sink=net.node(),levels=LEVELS.map(()=>net.node());
  units.forEach((unit,u)=>{const un=net.node();net.edge(source,un,unit.count);levels.forEach((ln,l)=>net.edge(un,ln,buckets[u].reduce((n,row)=>n+row[l].length,0)));});
  levels.forEach((ln,l)=>net.edge(ln,sink,target[l]));return net.maxFlow(source,sink,total)===total;
 }
 if(LEVELS.some((level,l)=>selected.filter(q=>q.difficulty===level).length!==target[l])&&difficultyCapacityFeasible()){
  const order=TYPES.map((_,t)=>t).sort((a,b)=>Number(counts[TYPES[a]])-Number(counts[TYPES[b]])),matrix=TYPES.map(()=>[0,0,0]);
  const initial=JSON.stringify(preferred);
  function search(row,remaining){
   const t=order[row],n=Number(counts[TYPES[t]]),future=order.slice(row+1);
   if(!future.length){
    if(remaining.reduce((a,b)=>a+b,0)!==n||remaining.some((v,l)=>v<0||v>stock[t][l]))return null;
    matrix[t]=[...remaining];return JSON.stringify(matrix)===initial?null:select(matrix);
   }
   const futureStock=LEVELS.map((_,l)=>future.reduce((s,t)=>s+Math.min(stock[t][l],Number(counts[TYPES[t]])),0));
   const values=(lo,hi,preferred)=>Array.from({length:Math.max(0,hi-lo+1)},(_,i)=>lo+i).sort((a,b)=>Math.abs(a-preferred)-Math.abs(b-preferred));
   const easyMin=Math.max(0,n-stock[t][1]-stock[t][2],remaining[0]-futureStock[0]),easyMax=Math.min(n,stock[t][0],remaining[0]);
   for(const easy of values(easyMin,easyMax,preferred[t][0])){
    const mediumMin=Math.max(0,n-easy-stock[t][2],remaining[1]-futureStock[1]),mediumMax=Math.min(n-easy,stock[t][1],remaining[1]);
    for(const medium of values(mediumMin,mediumMax,preferred[t][1])){
     const hard=n-easy-medium;if(hard>remaining[2]||remaining[2]-hard>futureStock[2])continue;
     matrix[t]=[easy,medium,hard];const next=remaining.map((v,l)=>v-matrix[t][l]);if(next.some(v=>v<0))continue;
     const result=search(row+1,next);if(result)return result;
    }
   }
   return null;
  }
  selected=search(0,target)||selected;
 }
 return {selected:TYPES.flatMap(type=>shuffle(selected.filter(q=>q.type===type),random)),notices:difficultyNotices(selected,counts,target,total,true)};
}
export function allocateScores(items, target=100) {
  if (!items.length || !Number.isInteger(target) || target<items.length || target>1000) throw new Error('總分須為整數，且至少等於總題數、最多 1000 分。');
  const choiceCount=items.filter(q=>q.type==='choice').length,otherCount=items.length-choiceCount;
  if(!otherCount){if(target%choiceCount){const options=[Math.floor(target/choiceCount)*choiceCount,Math.ceil(target/choiceCount)*choiceCount].filter(n=>n>=items.length&&n<=1000);throw new Error(`選擇題須同分；${choiceCount} 題的總分須為 ${choiceCount} 的倍數，可改為 ${options.join(' 或 ')} 分，或加入其他題型。`);}return items.map(()=>target/choiceCount);}
  const weight=q=>q.type==='written'?2.5:1,totalWeight=items.reduce((s,q)=>s+weight(q),0);
  const idealChoice=1+(target-items.length)/totalWeight;
  const choiceScore=choiceCount?Math.max(1,Math.min(Math.round(idealChoice),Math.floor((target-otherCount)/choiceCount))):0;
  const otherTarget=target-choiceCount*choiceScore,otherWeight=items.filter(q=>q.type!=='choice').reduce((s,q)=>s+weight(q),0);
  const scores=items.map(q=>q.type==='choice'?choiceScore:Math.floor(1+(otherTarget-otherCount)*weight(q)/otherWeight));
  let rest=target-scores.reduce((a,b)=>a+b,0);
  const rank=q=>LEVELS.indexOf(q.difficulty)<0?1:LEVELS.indexOf(q.difficulty);
  // Give at most one remainder point to each fill question: hard first, then
  // medium, then easy. Later equal-level questions receive the extra point.
  const order=items.map((q,i)=>({q,i})).filter(r=>r.q.type!=='choice').sort((a,b)=>(a.q.type==='written')-(b.q.type==='written')||rank(b.q)-rank(a.q)||b.i-a.i);
  for(let i=0;i<rest;i++)scores[order[i].i]++;
  return scores;
}
export function orderPracticeQuestions(items){return [...items].sort((a,b)=>TYPES.indexOf(a.type)-TYPES.indexOf(b.type)||(a.type==='fill'?LEVELS.indexOf(a.difficulty)-LEVELS.indexOf(b.difficulty):0));}
export function generate(bank, filters, counts, ratios, target=100, random=Math.random) {
  const total=TYPES.reduce((s,t)=>s+Number(counts[t]),0);
  if(!total || total>80 || TYPES.some(t=>!Number.isInteger(Number(counts[t])) || counts[t]<0)) throw new Error('請設定 1–80 題，題數須為非負整數。');
  if(!ratios||typeof ratios!=='object'||Array.isArray(ratios)||Object.keys(ratios).some(k=>!LEVELS.includes(k))||Object.values(ratios).some(n=>!Number.isFinite(Number(n))||n<0)||Object.values(ratios).reduce((a,b)=>a+Number(b),0)!==100) throw new Error('三種難度比例合計須為 100%。');
  const pool=eligiblePool(bank,filters), selected=[];
  const difficultyTarget=quotas(Object.fromEntries(LEVELS.map(level=>[level,Number(ratios[level])||0])),total).map(r=>r.count);
  if(filters.scopeMode==='units'){const result=unitSelection(pool,filters,counts,difficultyTarget,total,random),distinct=diversify(result.selected,pool,true,random),ordered=orderPracticeQuestions(distinct),scores=allocateScores(ordered,target);return {items:ordered.map((q,i)=>({id:q.id,score:scores[i]})),notices:distinct.every((q,i)=>q===result.selected[i])?result.notices:difficultyNotices(distinct,counts,difficultyTarget,total,true)};}
  for(const type of TYPES){
    const n=Number(counts[type]), available=pool.filter(q=>q.type===type);
    if(available.length<n) throw new Error(`${TYPE_NAMES[type]}只有 ${available.length} 題符合條件，請減少題數或放寬篩選。`);
  }
  const plan=typeLevelPlan(stockMatrix(pool),counts,difficultyTarget,total);
  if(!plan)throw new Error('目前題型與難度資料無法完成組卷。');
  TYPES.forEach((type,t)=>selected.push(...shuffle(LEVELS.flatMap((level,l)=>shuffle(pool.filter(q=>q.type===type&&q.difficulty===level),random).slice(0,plan[t][l])),random)));
  const distinct=diversify(selected,pool,false,random),notices=difficultyNotices(distinct,counts,difficultyTarget,total,false);
  const ordered=orderPracticeQuestions(distinct),scores=allocateScores(ordered,target);
  return {items:ordered.map((q,i)=>({id:q.id,score:scores[i]})),notices};
}
export function replaceQuestion(bank, session, index, filters, random=Math.random) {
  const old=bank.find(q=>q.id===session.items[index]?.id);if(!old)throw new Error('找不到要替換的題目。');
  const used=new Set(session.items.map(q=>q.id));
  const usedContent=new Set(bank.filter(q=>used.has(q.id)).map(contentKey));
  const candidates=eligiblePool(bank,filters).filter(q=>q.type===old.type&&q.difficulty===old.difficulty&&!used.has(q.id)&&!usedContent.has(contentKey(q))&&(filters.scopeMode!=='units'||q.primaryUnitId===old.primaryUnitId));
  if(!candidates.length)throw new Error('相同篩選、題型及難度已無未使用的題目。請調整篩選後重新組卷，或保留本題。');
  // Prefer a question that is not a sub-question of something already on the paper.
  const blocked=new Set(bank.filter(q=>used.has(q.id)&&q.id!==old.id).flatMap(familyKeys));
  const fresh=candidates.filter(q=>!familyKeys(q).some(k=>blocked.has(k)));
  const next=shuffle(fresh.length?fresh:candidates,random)[0];
  return {...session,revision:(session.revision||1)+1,items:session.items.map((item,i)=>i===index?{...item,id:next.id}:item)};
}
export function validateSession(data,bank) {
  if(!data || data.format!=='lanjuan-1' || !Array.isArray(data.items) || !data.items.length || data.items.length>80)throw new Error('這不是有效的蘭卷組卷紀錄。');
  const ids=new Map(bank.map(q=>[q.id,q])); const seen=new Set(),seenContent=new Set();
  for(const item of data.items){if(!ids.has(item.id))throw new Error(`題庫缺少題目 ${String(item.id).slice(0,100)}，無法完整還原。`);const key=contentKey(ids.get(item.id));if(seen.has(item.id)||seenContent.has(key)||!Number.isInteger(item.score)||item.score<1||item.score>1000)throw new Error('組卷紀錄包含重複題目或無效配分。');seen.add(item.id);seenContent.add(key);}
  const filters=data.filters||{};for(const k of ['year','semester','grade','exam','school','difficulty','region'])if(filters[k] && !['string','number'].includes(typeof filters[k]))throw new Error('篩選資料格式錯誤。');
  if(filters.region&&!Object.hasOwn(REGIONS,filters.region))throw new Error('縣市條件無效。');
  if(filters.difficulty&&!Object.hasOwn(LEVEL_NAMES,filters.difficulty))throw new Error('組卷難度條件無效。');
  const unitWeights=filters.unitWeights||{};if(filters.scopeMode==='units'&&(typeof unitWeights!=='object'||Array.isArray(unitWeights)||Object.keys(unitWeights).length>100||Object.values(unitWeights).some(v=>!Number.isFinite(Number(v))||Number(v)<0||Number(v)>100)||Math.abs(Object.values(unitWeights).reduce((s,v)=>s+Number(v),0)-100)>1e-6))throw new Error('單元配比資料無效。');
  const difficultyRatios=filters.difficultyRatios||{easy:40,medium:40,hard:20};if(typeof difficultyRatios!=='object'||Array.isArray(difficultyRatios)||Object.keys(difficultyRatios).length!==3||Object.keys(LEVEL_NAMES).some(k=>!Number.isFinite(Number(difficultyRatios[k]))||Number(difficultyRatios[k])<0)||Object.values(difficultyRatios).reduce((s,v)=>s+Number(v),0)!==100)throw new Error('難度比例資料無效。');
  return {format:'lanjuan-1',title:String(data.title||'數學練習卷').slice(0,60),createdAt:String(data.createdAt||''),revision:Number.isInteger(data.revision)?data.revision:1,filters:{year:filters.year||'',semester:filters.semester||'',grade:filters.grade||'',exam:filters.exam||'',region:filters.region||'',school:filters.school||'',difficulty:filters.difficulty||'',difficultyRatios:Object.fromEntries(Object.entries(difficultyRatios).map(([k,v])=>[k,Number(v)])),scopeMode:filters.scopeMode==='units'?'units':'exam',unitWeights:Object.fromEntries(Object.entries(unitWeights).map(([k,v])=>[k,Number(v)])),curriculumOnly:filters.curriculumOnly!==false},items:data.items.map(x=>({id:x.id,score:x.score}))};
}
