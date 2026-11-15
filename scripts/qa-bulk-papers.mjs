import {createRequire} from 'node:module';
import {readFile,mkdir,writeFile,readdir} from 'node:fs/promises';
const require=createRequire(import.meta.url),{chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const base=process.env.QA_URL||'http://127.0.0.1:4173';await mkdir('qa/bulk',{recursive:true});
const published=JSON.parse(await readFile('public/data/papers.json','utf8'));
const ids=(await readdir('research')).filter(f=>/^curated-bulk-.*\.json$/.test(f)).map(f=>f.slice(13,-5));
const papers=published.filter(p=>ids.includes(p.id)),reports=[],errors=[];
const browser=await chromium.launch({channel:'chrome',headless:true}),page=await browser.newPage({viewport:{width:1440,height:1000}});page.on('pageerror',e=>errors.push(e.message));
for(const p of papers){
 if(!p.transcriptionStatus.startsWith('complete'))throw new Error('Whole-paper visual review pending: '+p.id);
 await page.goto(base+'?paper='+encodeURIComponent(p.id),{waitUntil:'networkidle'});await page.waitForFunction(()=>window.lanjuan);
 const card=page.locator(`[data-paper-id="${p.id}"]`);await card.locator('[data-preview-paper]').click();
 await page.evaluate(async()=>{await MathJax.startup.promise;await MathJax.typesetPromise();});
 const initial=await page.evaluate(()=>lanjuan.getSession());if(initial.items.length!==p.questionCount)throw new Error('Incorrect complete preview: '+p.id);
 const rendered=await page.evaluate(()=>({raster:document.querySelectorAll('#paper-preview img,#paper-preview svg image').length,source:document.querySelectorAll('#paper-preview .question-source').length}));if(rendered.raster||rendered.source)throw new Error('Non-text question output: '+p.id);
 const result=await page.evaluate(async()=>{const bytes=await lanjuan.createPdf();let bin='';for(let i=0;i<bytes.length;i+=32768)bin+=String.fromCharCode(...bytes.subarray(i,i+32768));return {base64:btoa(bin),pages:lanjuan.lastPdfPages,layout:lanjuan.lastLayout};});
 if(result.layout.some(b=>b.yBottom<31.9||b.yTop>806))throw new Error('PDF overflow: '+p.id);
 const file=`qa/bulk/${p.id}.pdf`;await writeFile(file,Buffer.from(result.base64,'base64'));await page.locator('#restore-input').setInputFiles(file);await page.waitForFunction(n=>lanjuan.getSession().items.length===n,p.questionCount);
 const restored=await page.evaluate(()=>lanjuan.getSession());if(JSON.stringify(restored.items)!==JSON.stringify(initial.items))throw new Error('PDF restore changed original questions or scores: '+p.id);
 await page.screenshot({path:`qa/bulk/${p.id}.png`,fullPage:true});reports.push({id:p.id,school:p.school,year:p.year,questions:p.questionCount,pages:result.pages,file,preview:true,pdfRestore:true,rasterImages:0});console.log(p.id,p.questionCount,result.pages+' pages');
}
await page.goto(base+'?grade=8&semester=1&exam=2&year=&school=&curriculum=all',{waitUntil:'networkidle'});await page.waitForFunction(()=>window.lanjuan);
const priority=await page.evaluate(()=>({available:document.querySelector('#available-count').textContent,scope:document.querySelector('#scope-description').textContent,count:lanjuan.getBank().filter(q=>q.grade===8&&q.semester===1&&q.exam===2).length}));
for(const difficulty of ['easy','medium','hard']){await page.locator('#difficulty').selectOption(difficulty);await page.locator('#choice-count').fill('0');await page.locator('#fill-count').fill('3');await page.locator('#written-count').fill('0');await page.locator('#generate-button').click();const ok=await page.evaluate(level=>lanjuan.getSession().items.length===3&&lanjuan.getSession().items.every(i=>lanjuan.getBank().find(q=>q.id===i.id).difficulty===level),difficulty);if(!ok)throw new Error('Difficulty filter mismatch: '+difficulty);}
const before=await page.evaluate(()=>lanjuan.getSession());await page.locator('[data-swap]').first().click();const after=await page.evaluate(()=>lanjuan.getSession());if(before.items[0].id===after.items[0].id||before.items.some((q,i)=>q.score!==after.items[i].score)||(before.items.slice(1).some((q,i)=>q.id!==after.items[i+1].id)))throw new Error('Replacement changed unrelated questions or scores');
await page.setViewportSize({width:390,height:844});if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw new Error('Mobile overflow');if(await page.locator('.editor-difficulty').first().isHidden())throw new Error('Difficulty labels hidden on mobile');await page.screenshot({path:'qa/bulk/mobile.png',fullPage:true});
await writeFile('qa/bulk/report.json',JSON.stringify({base,priority,papers:reports,errors,checks:['all full-paper previews','text and vector output','all full-paper PDFs','PDF round-trip restores IDs and scores','all three strict difficulty levels','single-question replacement','mobile fits and difficulty visible']},null,2));await browser.close();if(errors.length)throw new Error(errors.join('\n'));console.log(JSON.stringify({papers:reports.length,priority,errors}));
