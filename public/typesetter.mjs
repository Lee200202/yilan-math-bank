import {TYPES,TYPE_NAMES} from './engine.mjs';
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export function examTitle(filters={}){const grade={7:'七年級',8:'八年級',9:'九年級'}[filters.grade]||'國中';const term={1:'上學期',2:'下學期'}[filters.semester]||'';const exam={1:'第一次',2:'第二次',3:'第三次'}[filters.exam]||'';return `${grade}${term}${exam}段考練習`;}
export function questionHTML(q){const blocks=[...(q.blocks||[])];if(q.diagramSvg)blocks.push({type:'svg',svg:q.diagramSvg});return blocks.map(b=>{
  if(b.type==='text')return String(b.text).split('\n').filter(x=>x.trim()).map(x=>`<p>${esc(x)}</p>`).join('');
  if(b.type==='options')return `<div class="typed-options">${b.items.map((x,i)=>`<div><span class="option-letter">(${String.fromCharCode(65+i)})</span> ${esc(x)}</div>`).join('')}</div>`;
  if(b.type==='table')return `<table class="typed-table"><tbody>${b.rows.map((row,i)=>`<tr>${row.map(x=>`<${b.header&&i===0?'th':'td'}>${esc(x)}</${b.header&&i===0?'th':'td'}>`).join('')}</tr>`).join('')}</tbody></table>`;
  if(b.type==='svg')return `<div class="typed-diagram">${b.svg}</div>`;
  throw new Error('未知題目區塊：'+b.type);
}).join('');}
export async function typesetDOM(root){await MathJax.startup.promise;await MathJax.typesetPromise([root]);if(root.querySelector('[data-mjx-error],[data-mml-node="merror"]'))throw new Error('題目公式排版失敗，請通知維護者。');}

const I=[1,0,0,1,0,0];
function mul(a,b){return [a[0]*b[0]+a[2]*b[1],a[1]*b[0]+a[3]*b[1],a[0]*b[2]+a[2]*b[3],a[1]*b[2]+a[3]*b[3],a[0]*b[4]+a[2]*b[5]+a[4],a[1]*b[4]+a[3]*b[5]+a[5]];}
function transforms(value=''){let m=I;for(const part of value.matchAll(/([a-zA-Z]+)\(([^)]*)\)/g)){const a=part[2].trim().split(/[\s,]+/).filter(Boolean).map(Number);let n=I;switch(part[1]){case 'matrix':n=a;break;case 'translate':n=[1,0,0,1,a[0]||0,a[1]||0];break;case 'scale':n=[a[0],0,0,a[1]??a[0],0,0];break;case 'rotate':{const r=a[0]*Math.PI/180,rot=[Math.cos(r),Math.sin(r),-Math.sin(r),Math.cos(r),0,0];n=a.length>1?mul(mul([1,0,0,1,a[1],a[2]],rot),[1,0,0,1,-a[1],-a[2]]):rot;break;}case 'skewX':n=[1,0,Math.tan(a[0]*Math.PI/180),1,0,0];break;case 'skewY':n=[1,Math.tan(a[0]*Math.PI/180),0,1,0,0];break;default:throw new Error('不支援的向量轉換：'+part[1]);}m=mul(m,n);}return m;}
function parseSvg(source){const doc=new DOMParser().parseFromString(source,'image/svg+xml');if(doc.querySelector('parsererror'))throw new Error('題圖 SVG 格式錯誤。');if(doc.querySelector('image,script,foreignObject'))throw new Error('題圖含點陣圖或不允許的內容。');return doc.documentElement;}
function svgView(svg){const v=(svg.getAttribute('viewBox')||'').trim().split(/[\s,]+/).map(Number);if(v.length===4&&v.every(Number.isFinite))return v;return [0,0,parseFloat(svg.getAttribute('width'))||300,parseFloat(svg.getAttribute('height'))||180];}
// PDF has cubic Beziers. Expand SVG's smooth/quadratic commands before passing
// paths to pdf-lib, whose quadratic shorthand produces distorted math glyphs.
export function normalizeSvgPath(path){
 const tokens=String(path).match(/[AaCcHhLlMmQqSsTtVvZz]|[-+]?(?:\d*\.\d+|\d+\.?\d*)(?:e[-+]?\d+)?/gi)||[],counts={M:2,L:2,H:1,V:1,C:6,S:4,Q:4,T:2,A:7};let i=0,cmd='',x=0,y=0,sx=0,sy=0,qc=null,cc=null,previous='',out=[];
 const emit=(c,a=[])=>out.push(c+a.map(n=>Number(n.toFixed(5))).join(' '));
 while(i<tokens.length){if(/^[a-z]$/i.test(tokens[i]))cmd=tokens[i++];const upper=cmd.toUpperCase(),rel=cmd!==upper;if(upper==='Z'){emit('Z');x=sx;y=sy;qc=cc=null;previous='Z';cmd='';continue;}const count=counts[upper];if(!count||i+count>tokens.length)throw new Error('無效的向量路徑。');const a=tokens.slice(i,i+count).map(Number);i+=count;if(a.some(n=>!Number.isFinite(n)))throw new Error('無效的向量座標。');const xx=n=>n+(rel?x:0),yy=n=>n+(rel?y:0);let nx,ny;
  if(upper==='M'||upper==='L'){nx=xx(a[0]);ny=yy(a[1]);emit(upper,[nx,ny]);x=nx;y=ny;if(upper==='M'){sx=x;sy=y;cmd=rel?'l':'L';}qc=cc=null;}
  else if(upper==='H'){x=xx(a[0]);emit('L',[x,y]);qc=cc=null;}
  else if(upper==='V'){y=yy(a[0]);emit('L',[x,y]);qc=cc=null;}
  else if(upper==='C'){const c1=[xx(a[0]),yy(a[1])],c2=[xx(a[2]),yy(a[3])];nx=xx(a[4]);ny=yy(a[5]);emit('C',[...c1,...c2,nx,ny]);cc=c2;qc=null;x=nx;y=ny;}
  else if(upper==='S'){const c1=['C','S'].includes(previous)&&cc?[2*x-cc[0],2*y-cc[1]]:[x,y],c2=[xx(a[0]),yy(a[1])];nx=xx(a[2]);ny=yy(a[3]);emit('C',[...c1,...c2,nx,ny]);cc=c2;qc=null;x=nx;y=ny;}
  else if(upper==='Q'||upper==='T'){const control=upper==='Q'?[xx(a[0]),yy(a[1])]:['Q','T'].includes(previous)&&qc?[2*x-qc[0],2*y-qc[1]]:[x,y];nx=xx(a[upper==='Q'?2:0]);ny=yy(a[upper==='Q'?3:1]);emit('C',[x+(control[0]-x)*2/3,y+(control[1]-y)*2/3,nx+(control[0]-nx)*2/3,ny+(control[1]-ny)*2/3,nx,ny]);qc=control;cc=null;x=nx;y=ny;}
  else if(upper==='A'){nx=xx(a[5]);ny=yy(a[6]);emit('A',[...a.slice(0,5),nx,ny]);x=nx;y=ny;qc=cc=null;}
  previous=upper;
 }
 return out.join(' ');
}
const mathCache=new Map();
let fontDataPromise;
async function mathShape(tex){if(!mathCache.has(tex)){mathCache.set(tex,(async()=>{await MathJax.startup.promise;const node=await MathJax.tex2svgPromise(tex,{display:false});if(node.querySelector('[data-mjx-error],[data-mml-node="merror"]'))throw new Error('無法排版公式：'+tex);const svg=node.querySelector('svg'),v=svgView(svg);return {svg,v,width:v[2]/1000,ascent:Math.max(0,-v[1])/1000,descent:Math.max(0,v[1]+v[3])/1000};})());}return mathCache.get(tex);}
const richParts=text=>String(text).split(/(\$\$[\s\S]+?\$\$|\$[^$]+?\$)/g).filter(Boolean).map(s=>s.startsWith('$')?{math:s.replace(/^\$\$?|\$\$?$/g,'')}:{text:s});

/** All body text is native PDF text. Formula glyphs and diagrams are vector paths. */
export async function createTypesetPdf(record,bankMap){
  if(!record?.items?.length)throw new Error('請先生成試卷。');
  const P=PDFLib,{rgb}=P,pdf=await P.PDFDocument.create();pdf.registerFontkit(window.fontkit);
  if(!fontDataPromise)fontDataPromise=fetch('./NotoSansTC.ttf').then(r=>{if(!r.ok)throw new Error('中文字型載入失敗。');return r.arrayBuffer();});const font=await pdf.embedFont(await fontDataPromise,{subset:false});
  const glyphs=new Set(font.getCharacterSet());const assertGlyphs=text=>{for(const c of text)if(!glyphs.has(c.codePointAt(0)))throw new Error(`字型缺少「${c}」；請通知維護者核對題目。`);};
  const SIZE=11.5,W=595.28,H=841.89,M=36,BOTTOM=32,WIDTH=W-M*2,INK=rgb(0,0,0);let page,y,pageIndex=0;const layout=[];
  function addPage(){page=pdf.addPage([W,H]);pageIndex++;y=H-M;}
  function room(h){if(y-h<BOTTOM)addPage();}
  const native=(text,x,baseline,size=SIZE)=>{assertGlyphs(String(text));page.drawText(String(text),{x,y:baseline,size,font,color:INK});};
  function color(value){if(!value||value==='currentColor')return INK;if(value==='none')return undefined;const names={black:'#000000',white:'#ffffff',red:'#ff0000',gray:'#888888',grey:'#888888'};value=names[value]||value;if(value.startsWith('#')){let h=value.slice(1);if(h.length===3)h=h.split('').map(c=>c+c).join('');return rgb(parseInt(h.slice(0,2),16)/255,parseInt(h.slice(2,4),16)/255,parseInt(h.slice(4,6),16)/255);}const a=value.match(/[\d.]+/g);return a?.length>=3?rgb(Number(a[0])/255,Number(a[1])/255,Number(a[2])/255):INK;}
  function vector(svg,rootMatrix){
    const visit=(el,parent,inherit={fill:'black',stroke:'none','stroke-width':'1','font-size':'14','text-anchor':'start'})=>{
      const tag=el.localName;if(['defs','title','desc','metadata'].includes(tag))return;
      const style={...inherit};for(const k of ['fill','stroke','stroke-width','stroke-dasharray','font-size','text-anchor'])if(el.hasAttribute(k))style[k]=el.getAttribute(k);for(const s of (el.getAttribute('style')||'').split(';')){const [k,v]=s.split(':');if(k&&v)style[k.trim()]=v.trim();}
      let m=mul(parent,transforms(el.getAttribute('transform')||''));const n=(k,fallback=0)=>parseFloat(el.getAttribute(k))||fallback;const fill=color(style.fill),stroke=color(style.stroke),sw=Number.isFinite(parseFloat(style['stroke-width']))?parseFloat(style['stroke-width']):1;
      const state=()=>page.pushOperators(P.pushGraphicsState(),P.concatTransformationMatrix(...m));const end=()=>page.pushOperators(P.popGraphicsState());
      if(tag==='path'){
        state();page.pushOperators(P.concatTransformationMatrix(1,0,0,-1,0,0));page.drawSvgPath(normalizeSvgPath(el.getAttribute('d')||''),{x:0,y:0,scale:1,color:fill,borderColor:stroke&&sw?stroke:undefined,borderWidth:stroke&&sw?sw:undefined,borderDashArray:(style['stroke-dasharray']||'').split(/[\s,]+/).map(Number).filter(x=>x>0)});end();return;
      }
      if(tag==='rect'){state();page.drawRectangle({x:n('x'),y:n('y'),width:n('width'),height:n('height'),color:fill,borderColor:stroke,borderWidth:stroke?sw:0});end();return;}
      if(tag==='line'){state();page.drawLine({start:{x:n('x1'),y:n('y1')},end:{x:n('x2'),y:n('y2')},thickness:sw,color:stroke||INK,dashArray:(style['stroke-dasharray']||'').split(/[\s,]+/).map(Number).filter(x=>x>0)});end();return;}
      if(tag==='circle'||tag==='ellipse'){state();page.drawEllipse({x:n('cx'),y:n('cy'),xScale:n(tag==='circle'?'r':'rx'),yScale:n(tag==='circle'?'r':'ry'),color:fill,borderColor:stroke,borderWidth:stroke?sw:0});end();return;}
      if(tag==='polyline'||tag==='polygon'){const points=(el.getAttribute('points')||'').trim().split(/[\s,]+/).map(Number);const d=points.reduce((s,n,i)=>s+(i%2?' ':i?' L':'M')+n,'')+(tag==='polygon'?' Z':'');state();page.pushOperators(P.concatTransformationMatrix(1,0,0,-1,0,0));page.drawSvgPath(d,{x:0,y:0,scale:1,color:tag==='polygon'?fill:undefined,borderColor:stroke||INK,borderWidth:sw,borderDashArray:(style['stroke-dasharray']||'').split(/[\s,]+/).map(Number).filter(x=>x>0)});end();return;}
      if(tag==='text'){const text=el.textContent,size=10.5/Math.hypot(m[0],m[1]),w=font.widthOfTextAtSize(text,size),anchor=style['text-anchor'],offset=anchor==='middle'?-w/2:anchor==='end'?-w:0;state();if(text.trim()==='⋮'||text.trim()==='⋯'){for(let j=0;j<3;j++)page.drawEllipse({x:n('x')+offset+size*(text.trim()==='⋮'?.3:.15+j*.3),y:n('y')-size*(text.trim()==='⋮'?.15+j*.3:.3),xScale:size*.055,yScale:size*.055,color:fill||INK});}else{assertGlyphs(text);page.pushOperators(P.concatTransformationMatrix(1,0,0,-1,n('x')+offset,n('y')));page.drawText(text,{x:0,y:0,size,font,color:fill||INK});}end();return;}
      if(tag==='use'){const id=(el.getAttribute('href')||el.getAttributeNS('http://www.w3.org/1999/xlink','href')||'').slice(1);const target=svg.querySelector(`[id="${CSS.escape(id)}"]`);if(!target)throw new Error('題圖缺少向量定義。');visit(target,mul(m,[1,0,0,1,n('x'),n('y')]),style);return;}
      for(const child of el.children)visit(child,m,style);
    };visit(svg,rootMatrix);
  }
  async function tokens(text,size=SIZE){const ts=[];for(const part of richParts(text)){if(part.math!==undefined){const shape=await mathShape(part.math);ts.push({tex:part.math,shape,width:shape.width*size,ascent:shape.ascent*size,descent:shape.descent*size,size});}else{for(const ch of part.text){if(ch==='\n'){ts.push({newline:true});continue;}ts.push({text:ch,width:font.widthOfTextAtSize(ch,size),ascent:size*1.16,descent:size*.27,size});}}}return ts;}
  async function lines(text,width,size=SIZE){const ts=await tokens(text,size),result=[];let line=[],used=0;const flush=()=>{if(line.length){result.push({items:line,width:used,ascent:Math.max(size*1.16,...line.map(t=>t.ascent||0)),descent:Math.max(size*.27,...line.map(t=>t.descent||0))});line=[];used=0;}};
    for(const token of ts){if(token.newline){flush();continue;}if(token.width>width&&token.shape)throw new Error(`公式超過欄寬，須核對換行：${token.tex}`);if(used+token.width>width+.1&&line.length)flush();if(!line.length&&token.text===' ')continue;line.push(token);used+=token.width;}flush();return result;}
  function drawLine(line,x,top){const baseline=top-line.ascent;let xx=x;let run='',runX=x,runSize=SIZE;const flush=()=>{if(run){native(run,runX,baseline,runSize);run='';}};for(const t of line.items){if(t.shape){flush();vector(t.shape.svg,[t.size/1000,0,0,-t.size/1000,xx,baseline]);}else{if(!run){runX=xx;runSize=t.size;}run+=t.text;}xx+=t.width;}flush();}
  function lineHeight(line){return line.ascent+line.descent+1.6;}
  async function paragraph(text,x=M,width=WIDTH,size=SIZE){const ls=await lines(text,width,size);for(const line of ls){const h=lineHeight(line);room(h);drawLine(line,x,y);layout.push({page:pageIndex,x,width:line.width,yTop:y,yBottom:y-h,type:'text'});y-=h;}}
  async function options(items,x=M+14,width=WIDTH-14){const contents=await Promise.all(items.map((s,i)=>tokens(`(${String.fromCharCode(65+i)}) ${s}`)));const max=Math.max(...contents.map(ts=>ts.reduce((n,t)=>n+t.width,0)));let columns=max<=width/4-9?4:max<=width/2-9?2:1;const cw=(width-(columns-1)*12)/columns;
    for(let start=0;start<items.length;start+=columns){const row=await Promise.all(items.slice(start,start+columns).map((s,j)=>lines(`(${String.fromCharCode(65+start+j)}) ${s}`,cw)));const heights=row.map(ls=>ls.reduce((s,l)=>s+lineHeight(l),0)),h=Math.max(...heights);room(h);const top=y;row.forEach((ls,col)=>{let yy=top;for(const l of ls){drawLine(l,x+col*(cw+12),yy);yy-=lineHeight(l);}});layout.push({page:pageIndex,x,yTop:y,yBottom:y-h,type:'options'});y-=h;}
  }
  async function table(block,x=M+14,width=WIDTH-14){const cols=Math.max(...block.rows.map(r=>r.length)),cw=width/cols;for(let ri=0;ri<block.rows.length;ri++){const cells=await Promise.all(block.rows[ri].map(t=>lines(String(t),cw-10))),h=Math.max(22,...cells.map(ls=>ls.reduce((s,l)=>s+lineHeight(l),0)+8));room(h);for(let c=0;c<cols;c++){page.drawRectangle({x:x+c*cw,y:y-h,width:cw,height:h,borderColor:INK,borderWidth:.5});let yy=y-4;for(const line of cells[c]||[]){drawLine(line,x+c*cw+5,yy);yy-=lineHeight(line);}}layout.push({page:pageIndex,x,yTop:y,yBottom:y-h,type:'table'});y-=h;}y-=2;}
  async function diagram(source){const svg=parseSvg(source),v=svgView(svg),isChart=svg.querySelectorAll('text').length>15;let width=Math.min(WIDTH-14,v[2]*(isChart?1:.7)),height=width*v[3]/v[2];const max=isChart?200:150;if(height>max){width*=max/height;height=max;}const available=y-BOTTOM-3;if(height>available&&available>=height*.8){width*=available/height;height=available;}room(height+3);const scale=width/v[2];vector(svg,[scale,0,0,-scale,M+14-v[0]*scale,y+v[1]*scale]);layout.push({page:pageIndex,x:M+14,yTop:y,yBottom:y-height,type:'diagram'});y-=height+3;}
  async function estimateQuestion(q,item,number){let height=4,first=true;const blocks=[...q.blocks];if(q.diagramSvg)blocks.push({type:'svg',svg:q.diagramSvg});
    for(const block of blocks){if(block.type==='text'){height+=(await lines((first?`${number}.（${item.score}分）`:'')+block.text,first?WIDTH:WIDTH-14)).reduce((n,l)=>n+lineHeight(l),0);first=false;continue;}
      if(first){height+=(await lines(`${number}.（${item.score}分）`,WIDTH)).reduce((n,l)=>n+lineHeight(l),0);first=false;}
      if(block.type==='svg'){const svg=parseSvg(block.svg),v=svgView(svg),chart=svg.querySelectorAll('text').length>15,w=Math.min(WIDTH-14,v[2]*(chart?1:.7));height+=Math.min(w*v[3]/v[2],chart?200:150)+3;}
      else if(block.type==='table'){const cols=Math.max(...block.rows.map(r=>r.length)),cw=(WIDTH-14)/cols;for(const row of block.rows){const cells=await Promise.all(row.map(s=>lines(String(s),cw-10)));height+=Math.max(22,...cells.map(ls=>ls.reduce((n,l)=>n+lineHeight(l),0)+8));}height+=2;}
      else if(block.type==='options'){const width=WIDTH-14,contents=await Promise.all(block.items.map((s,i)=>tokens(`(${String.fromCharCode(65+i)}) ${s}`))),max=Math.max(...contents.map(ts=>ts.reduce((n,t)=>n+t.width,0))),cols=max<=width/4-9?4:max<=width/2-9?2:1,cw=(width-(cols-1)*12)/cols;for(let i=0;i<block.items.length;i+=cols){const row=await Promise.all(block.items.slice(i,i+cols).map((s,j)=>lines(`(${String.fromCharCode(65+i+j)}) ${s}`,cw)));height+=Math.max(...row.map(ls=>ls.reduce((n,l)=>n+lineHeight(l),0)));}}
    }return height;
  }
  addPage();const title=record.title||examTitle(record.filters);const titleLines=await lines(title,WIDTH,14);for(const line of titleLines){drawLine(line,M+(WIDTH-line.width)/2,y);y-=lineHeight(line);}y-=7;
  let section=0,index=0;
  for(const type of TYPES){const items=record.items.filter(item=>bankMap.get(item.id)?.type===type);if(!items.length)continue;const firstQ=bankMap.get(items[0].id),firstHeight=await estimateQuestion(firstQ,items[0],index+1);room(firstHeight<H-M-BOTTOM-24?firstHeight+24:60);section++;await paragraph(`${['一','二','三'][section-1]}、${TYPE_NAMES[type]}`,M,WIDTH,12.5);y-=2;
    for(const item of items){const q=bankMap.get(item.id);if(!q?.typesetVerified||!q.blocks?.length)throw new Error('本題尚未完成文字核對，請重新選題。');index++;const height=await estimateQuestion(q,item,index);room(height<=H-M-BOTTOM?height:38);const blocks=[...q.blocks];if(q.diagramSvg)blocks.push({type:'svg',svg:q.diagramSvg});let first=true;
      for(const block of blocks){if(block.type==='text'){await paragraph((first?`${index}.（${item.score}分）`:'')+block.text,first?M:M+14,first?WIDTH:WIDTH-14);first=false;}else{if(first){await paragraph(`${index}.（${item.score}分）`);first=false;}if(block.type==='options')await options(block.items);else if(block.type==='table')await table(block);else if(block.type==='svg')await diagram(block.svg);else throw new Error('未知題目區塊。');}}
      y-=4;
    }
    y-=3;
  }
  const payload=new TextEncoder().encode(JSON.stringify(record));let binary='';payload.forEach(b=>binary+=String.fromCharCode(b));pdf.setSubject('LANJUAN1:'+btoa(binary));pdf.setTitle(title);pdf.setCreator('蘭卷・文字重排版');pdf.setKeywords(['蘭卷','數學','文字重排']);
  return {bytes:await pdf.save(),layout,pages:pageIndex};
}
