"""Inspection only: list Word paragraph text and decoded Equation.3 objects.

Uses GPL-2.0-or-later mtef.py/mtef2mathml.py from TomJoey/mathTypeWord;
those files are separately downloaded to scratch and are not bundled.
This is a diagnostic, not a verified transcription.
"""
import io,json,pathlib,sys,zipfile,xml.etree.ElementTree as ET
sys.path.insert(0,'scratch/lo-portable-test/deps')
import olefile,mtef,mtef2mathml
src=pathlib.Path('scratch/lo-portable-test/render/ld-108-1-2-9.docx')
z=zipfile.ZipFile(src)
rel=ET.fromstring(z.read('word/_rels/document.xml.rels'))
relmap={x.attrib['Id']:x.attrib['Target'] for x in rel}
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
M='{http://schemas.openxmlformats.org/officeDocument/2006/math}'
O='{urn:schemas-microsoft-com:office:office}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
root=ET.fromstring(z.read('word/document.xml'));paras=[];success=0;failed=[]
def walk(n):
    global success
    if n.tag==W+'object':
        o=n.find('.//'+O+'OLEObject')
        if o is None:return '[object]'
        ident=o.attrib.get(R+'id');target=relmap.get(ident,'')
        try:
            if not target.startswith('embeddings/'):return '[non-equation object]'
            with olefile.OleFileIO(io.BytesIO(z.read('word/'+target))) as ole:
                stream=ole.openstream('Equation Native').read()
            parser,nodes=mtef.parse_equation_native(stream)
            math,warns=mtef2mathml.to_mathml(parser,nodes)
            if parser.warnings or warns:failed.append({'id':ident,'warning':str([parser.warnings,warns])})
            success+=1
            return ' ⟦'+ET.tostring(math,encoding='unicode')+'⟧ '
        except Exception as exc:
            failed.append({'id':ident,'error':str(exc)})
            return ' [UNREADABLE:'+str(ident)+'] '
    if n.tag in (W+'t',M+'t'):return n.text or ''
    if n.tag==W+'tab':return '\t'
    return ''.join(walk(child) for child in n)
for para in root.iter(W+'p'):
    value=walk(para).strip()
    if value:paras.append(value)
out=pathlib.Path('scratch/lo-portable-test/reference-objects.txt')
out.write_text('\n'.join(paras),encoding='utf8')
print(json.dumps({'paragraphs':len(paras),'ole_decoded':success,'issues':failed},ensure_ascii=False))
