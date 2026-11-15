import test from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {readFileSync} from 'node:fs';
import {questionHTML} from '../public/typesetter.mjs';

test('figure-only choice options render their labels once with vector content',()=>{
 const svg='<svg viewBox="0 0 120 30"><path d="M1 1L10 10"/><text>(A)</text><text>(B)</text><text>(C)</text><text>(D)</text></svg>';
 const html=questionHTML({blocks:[{type:'text',text:'選出正確圖形。'},{type:'optionFigures',svg}]});
 assert.equal((html.match(/\(A\)/g)||[]).length,1);
 assert.ok(html.includes('figure-options'));
 assert.ok(html.includes('<path'));
 assert.ok(!html.includes('<img'));
});

test('transcript gate rejects empty labels and undrawn option panels',()=>{
 const code=String.raw`
import sys
sys.path.insert(0,'scripts')
from prepare_metro import validate_choice_blocks as check
bad=[
 [{'type':'options','items':['(A)','(B)','(C)','(D)']}],
 [{'type':'options','items':['1','2','3','']}],
 [{'type':'optionFigures','svg':'<svg><text>(A)</text><text>(B)</text><text>(C)</text><text>(D)</text></svg>'}],
 [{'type':'optionFigures','svg':'<svg><path d="M1 1L2 2"/><text>(A)</text></svg>'}]
]
for blocks in bad:
 try: check(blocks)
 except ValueError: pass
 else: raise AssertionError(blocks)
check([{'type':'options','items':['$1$','$2$','$3$','$4$']}])
check([{'type':'optionFigures','svg':'<svg><path d="M1 1L2 2"/><text>(A)</text><text>(B)</text><text>(C)</text><text>(D)</text></svg>'}])
print('ok')
`;
 assert.equal(execFileSync('python',['-c',code],{encoding:'utf8'}).trim(),'ok');
});

test('Kai PDF source uses even glyph offsets so small fontkit subsets do not lose glyph outlines',()=>{
 const font=readFileSync('public/fonts/TW-Kai-subset.ttf'), tables={};
 for(let i=0;i<font.readUInt16BE(4);i++){const p=12+i*16;tables[font.toString('ascii',p,p+4)]={offset:font.readUInt32BE(p+8),length:font.readUInt32BE(p+12)};}
 const long=font.readInt16BE(tables.head.offset+50)===1,step=long?4:2;
 for(let p=tables.loca.offset;p<tables.loca.offset+tables.loca.length;p+=step){const offset=long?font.readUInt32BE(p):font.readUInt16BE(p)*2;assert.equal(offset%2,0,'Odd glyph offsets corrupt short PDF loca subsets');}
});

test('official source downloader encodes Chinese paths and preserves existing percent escapes',()=>{
 const code=String.raw`
import sys
from unittest.mock import patch, MagicMock
sys.path.insert(0,'scripts')
from fetch_paper import download
response=MagicMock()
response.__enter__.return_value.read.return_value=b'%PDF-test'
with patch('urllib.request.urlopen',return_value=response) as opener:
 assert download('https://example.test/數學%20試卷.pdf')==b'%PDF-test'
 url=opener.call_args.args[0].full_url
 assert url=='https://example.test/%E6%95%B8%E5%AD%B8%20%E8%A9%A6%E5%8D%B7.pdf',url
print('ok')
`;
 assert.equal(execFileSync('python',['-c',code],{encoding:'utf8'}).trim(),'ok');
});
