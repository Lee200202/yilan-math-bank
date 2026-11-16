"""Pin an Office source and its Word-rendered PDF without changing original identity."""
import hashlib,json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def register(pid):
    inv=json.loads((ROOT/'research/metro/metro-inventory.json').read_text(encoding='utf-8'))
    row=next(f for s in inv['sources'].values() for f in s['files'] if f.get('id')==pid)
    if row['format'] not in ('doc','docx','odt'):raise ValueError('Not an Office original')
    source=ROOT/row['localPath'];pdf=ROOT/'research/metro/rendered'/f'{pid}.pdf'
    if digest(source)!=row['sha256'] or not pdf.read_bytes().startswith(b'%PDF'):raise ValueError('Invalid source or rendering')
    import pymupdf
    with pymupdf.open(pdf) as doc:pages=len(doc)
    path=ROOT/'research/metro/rendered-sources.json';records=json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}
    records[pid]={'sourceSha256':row['sha256'],'renderSha256':digest(pdf),'localPath':pdf.relative_to(ROOT).as_posix(),'pages':pages,'renderer':'Microsoft Word ExportAsFixedFormat; original opened read-only with macros disabled'}
    path.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(records[pid],ensure_ascii=False))
if __name__=='__main__':register(sys.argv[1])
