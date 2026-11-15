import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const read=async name=>JSON.parse(await readFile(new URL('../public/data/'+name,import.meta.url)));
const papers=await read('papers.json'),audit=await read('official-source-audit.json'),workflow=await read('paper-workflow.json');
test('every question file in the complete official crawl is archived with its verified original bytes',async()=>{
 const sources=audit.files.filter(p=>p.kind==='question');
 assert.equal(sources.length,audit.questionFilesArchived);assert.equal(audit.driveFoldersInspected,269);assert.equal(audit.categoryPagesInspected,5);assert.deepEqual(audit.missingQuestionDownloads,[]);
 for(const source of sources){const p=papers.find(p=>p.id===source.id);assert.ok(p,source.id);const bytes=await readFile(new URL('../public/'+(p.originalFile||p.file).replace(/^\.\//,''),import.meta.url));assert.equal(createHash('sha256').update(bytes).digest('hex'),source.sha256,source.id);}
});
test('missing folder and confirmed header conflict remain explicit and never create a fake 109 paper',()=>{
 assert.equal(audit.criticalFindings.zhonghua105UpperSecond.status,'empty-folder');
 const p=papers.find(p=>p.id==='1ZZUkKjnXYPQn5CwCnQPqN9ayYj__D6wS');assert.equal(p.year,108);assert.equal(p.sourceFolderYear,109);
 const supplement=papers.find(p=>p.id==='1ODYj-V7KzqhYr8EM7s2gkTI2Rb8qKDg3');assert.deepEqual([supplement.year,supplement.semester,supplement.exam,supplement.grade],[107,2,3,8]);
});
test('every archived original has a distinct transcription status; no empty paper is marked complete',()=>{
 assert.equal(workflow.length,papers.length);assert.equal(new Set(workflow.map(p=>p.id)).size,papers.length);
 for(const p of workflow){assert.ok(['pending','partial','complete','complete-with-source-issues'].includes(p.transcriptionStatus));if(p.transcriptionStatus.startsWith('complete'))assert.ok(p.questionCount>0&&p.completionEvidence);if(p.transcriptionStatus==='pending')assert.equal(p.questionCount,0);}
});
