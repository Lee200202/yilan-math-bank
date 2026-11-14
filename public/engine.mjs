export const TYPES = ['choice', 'fill', 'written'];
export const TYPE_NAMES = {choice:'選擇題',fill:'填充題',written:'非選擇題'};
export const LEVEL_NAMES = {easy:'簡單',medium:'中等',hard:'困難'};
export function eligible(q, f) {
  return q.reviewed && (!f.year || q.year===Number(f.year)) && (!f.semester || q.semester===Number(f.semester)) && (!f.grade || q.grade===Number(f.grade)) && (!f.exam || q.exam===Number(f.exam)) && (!f.school || q.school===f.school) && (!f.curriculumOnly || q.year>=108+q.grade-7);
}
export function shuffle(items, random=Math.random) {const a=[...items]; for(let i=a.length-1;i>0;i--){const j=Math.floor(random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
export function allocateScores(items, target=100) {
  if (!items.length || !Number.isInteger(target) || target<items.length || target>1000) throw new Error('總分須為整數，且至少等於總題數、最多 1000 分。');
  const weights=items.map(q=>q.type==='written'?2.5:1), sum=weights.reduce((a,b)=>a+b,0), remaining=target-items.length;
  const exact=weights.map(w=>w/sum*remaining), scores=exact.map(x=>Math.floor(x)+1);
  let rest=target-scores.reduce((a,b)=>a+b,0);
  const order=exact.map((v,i)=>({i,r:v-Math.floor(v)})).sort((a,b)=>b.r-a.r||a.i-b.i);
  for(let i=0;i<rest;i++) scores[order[i].i]++;
  return scores;
}
export function generate(bank, filters, counts, ratios, target=100, random=Math.random) {
  const total=TYPES.reduce((s,t)=>s+Number(counts[t]),0);
  if(!total || total>80 || TYPES.some(t=>!Number.isInteger(Number(counts[t])) || counts[t]<0)) throw new Error('請設定 1–80 題，題數須為非負整數。');
  if(Object.values(ratios).some(n=>!Number.isFinite(Number(n))||n<0)||Object.values(ratios).reduce((a,b)=>a+Number(b),0)!==100) throw new Error('三種難度比例合計須為 100%。');
  const pool=bank.filter(q=>eligible(q,filters)), selected=[], notices=[];
  for(const type of TYPES){
    const n=Number(counts[type]), available=pool.filter(q=>q.type===type);
    if(available.length<n) throw new Error(`${TYPE_NAMES[type]}只有 ${available.length} 題符合條件，請減少題數或放寬篩選。`);
    const exact=Object.keys(ratios).map(level=>({level,n:n*ratios[level]/100}));
    const quotas=exact.map(x=>({...x,count:Math.floor(x.n)}));
    let rem=n-quotas.reduce((s,x)=>s+x.count,0);
    [...quotas].sort((a,b)=>(b.n-b.count)-(a.n-a.count)).slice(0,rem).forEach(x=>x.count++);
    const picked=[];
    for(const {level,count} of quotas) picked.push(...shuffle(available.filter(q=>q.difficulty===level),random).slice(0,count));
    if(picked.length<n){notices.push(`${TYPE_NAMES[type]}的部分難度題量不足，已由其他難度補足。`);const ids=new Set(picked.map(q=>q.id));picked.push(...shuffle(available.filter(q=>!ids.has(q.id)),random).slice(0,n-picked.length));}
    selected.push(...shuffle(picked,random));
  }
  const scores=allocateScores(selected,target);
  return {items:selected.map((q,i)=>({id:q.id,score:scores[i]})),notices};
}
export function replaceQuestion(bank, session, index, filters, random=Math.random) {
  const old=bank.find(q=>q.id===session.items[index]?.id);if(!old)throw new Error('找不到要替換的題目。');
  const used=new Set(session.items.map(q=>q.id));
  const candidates=bank.filter(q=>eligible(q,filters)&&q.type===old.type&&q.difficulty===old.difficulty&&!used.has(q.id));
  if(!candidates.length)throw new Error('相同篩選、題型及難度已無未使用的題目。請調整篩選後重新組卷，或保留本題。');
  const next=shuffle(candidates,random)[0];
  return {...session,revision:(session.revision||1)+1,items:session.items.map((item,i)=>i===index?{...item,id:next.id}:item)};
}
export function validateSession(data,bank) {
  if(!data || data.format!=='lanjuan-1' || !Array.isArray(data.items) || !data.items.length || data.items.length>80)throw new Error('這不是有效的蘭卷組卷紀錄。');
  const ids=new Set(bank.map(q=>q.id)); const seen=new Set();
  for(const item of data.items){if(!ids.has(item.id))throw new Error(`題庫缺少題目 ${String(item.id).slice(0,100)}，無法完整還原。`);if(seen.has(item.id)||!Number.isInteger(item.score)||item.score<1||item.score>1000)throw new Error('組卷紀錄包含重複題目或無效配分。');seen.add(item.id);}
  const filters=data.filters||{};for(const k of ['year','semester','grade','exam','school'])if(filters[k] && !['string','number'].includes(typeof filters[k]))throw new Error('篩選資料格式錯誤。');
  return {format:'lanjuan-1',title:String(data.title||'數學練習卷').slice(0,60),createdAt:String(data.createdAt||''),revision:Number.isInteger(data.revision)?data.revision:1,filters:{year:filters.year||'',semester:filters.semester||'',grade:filters.grade||'',exam:filters.exam||'',school:filters.school||'',curriculumOnly:filters.curriculumOnly!==false},items:data.items.map(x=>({id:x.id,score:x.score}))};
}
