import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createRequire} from 'node:module';
const require=createRequire(import.meta.url);
const {chromium}=require('C:/Program Files/WindowsApps/OpenAI.CodexPrimaryRuntime.v26-1112-737-0_26.1112.737.0_x64__3k8sg7r9htsxt/dependencies/node/node_modules/playwright');
const data=JSON.parse(await readFile('research/transcribed-zhonghua-late.json','utf8'));
const dir='research/transcribed-zhonghua-late-review';await mkdir(dir,{recursive:true});
const texts=[];function walk(x){if(typeof x==='string')texts.push(x);else if(Array.isArray(x))x.forEach(walk);else if(x&&typeof x==='object'){for(const [k,v] of Object.entries(x))if(k!=='svg')walk(v);}}
for(const q of data)walk(q.blocks);
const formulas=[...new Set(texts.flatMap(t=>[...t.matchAll(/\$([^$]+)\$/g)].map(x=>x[1])))];
const browser=await chromium.launch({headless:true,channel:'chrome'}), page=await browser.newPage({viewport:{width:1300,height:1200},deviceScaleFactor:1});
await page.goto('http://127.0.0.1:4173',{waitUntil:'networkidle'});await page.evaluate(()=>MathJax.startup.promise);
const texErrors=await page.evaluate(async formulas=>{const errors=[];for(const tex of formulas){try{const s=await MathJax.tex2svgPromise(tex);if(s.querySelector('[data-mjx-error],mjx-merror'))errors.push({tex,error:s.textContent});}catch(e){errors.push({tex,error:String(e)});}}return errors;},formulas);
const diagrams=data.flatMap(q=>q.blocks.filter(b=>b.type==='svg').map((b,index)=>({id:q.id,index,svg:b.svg})));
const bounds=[];const sheets=[];
for(let start=0;start<diagrams.length;start+=6){const chunk=diagrams.slice(start,start+6);await page.setContent(`<style>@font-face{font-family:QA;src:url(http://127.0.0.1:4173/NotoSansTC.ttf)}body{font-family:QA,sans-serif;padding:15px;background:white}.grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}.card{border:1px solid #aaa;padding:12px;height:350px;display:flex;flex-direction:column}.id{font:14px monospace;margin-bottom:8px}svg{width:100%;flex:1;min-height:0}svg text{font-family:QA,serif}</style><div class="grid">${chunk.map(d=>`<div class="card"><div class="id">${d.id}</div>${d.svg}</div>`).join('')}</div>`);await page.evaluate(()=>document.fonts.ready);const check=await page.evaluate(()=>[...document.querySelectorAll('.card svg')].map(e=>{const b=e.getBBox(),v=e.viewBox.baseVal;return {b:{x:b.x,y:b.y,width:b.width,height:b.height},v:{x:v.x,y:v.y,width:v.width,height:v.height},overflow:b.x<v.x-.1||b.y<v.y-.1||b.x+b.width>v.x+v.width+.1||b.y+b.height>v.y+v.height+.1};}));check.forEach((c,i)=>{if(c.overflow)bounds.push({id:chunk[i].id,index:chunk[i].index,...c});});const file=`svg-sheet-${start/6+1}.png`;await page.screenshot({path:`${dir}/${file}`,fullPage:true});sheets.push(file);}
await writeFile('research/transcribed-zhonghua-late-render-check.json',JSON.stringify({questions:data.length,formulas:formulas.length,texErrors,diagrams:diagrams.length,svgBounds:bounds,sheets},null,2));await browser.close();console.log(JSON.stringify({questions:data.length,formulas:formulas.length,texErrors,diagrams:diagrams.length,svgBounds:bounds,sheets},null,2));
