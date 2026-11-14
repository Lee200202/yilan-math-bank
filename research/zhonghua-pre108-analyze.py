from pathlib import Path
import pymupdf,json,hashlib
ROOT=Path(__file__).parent;OUT=ROOT/'review-zhonghua-pre108';OUT.mkdir(exist_ok=True)
catalog=json.loads((ROOT/'zhonghua-pre108-catalog.json').read_text(encoding='utf8'))
SELECT=['1k-T9wedtWmZ4qTyP7Vomjl25Xpox6ymv','123lGBiDXT7Brx1TJah7SZy7MHrfWNKw9','1WSY16qjhQvFsIfCt4Bo48yXfgEE0DYJG']
for row in catalog:
    if row['id'] not in SELECT:continue
    path=ROOT.parent/row['localPath']
    if row['id'] in SELECT[:2]:
        rend=ROOT/'zhonghua_old_render';rend.mkdir(exist_ok=True)
        derived=rend/f"{row['id']}.pdf"
        d=pymupdf.open(path)
        for p in d:p.set_rotation(270)
        d.save(derived);d.close();path=derived
        row.update(renderPath=str(path.relative_to(ROOT.parent)).replace('\\','/'),renderSha256=hashlib.sha256(path.read_bytes()).hexdigest(),renderMethod='原掃描PDF頁面方向正規化（旋轉270度），保留原始PDF與SHA，未重繪或OCR。')
    if row['id']=='1WSY16qjhQvFsIfCt4Bo48yXfgEE0DYJG':
        path=ROOT/'zhonghua_old_render'/f"{row['id']}.pdf"
        row.update(renderPath=str(path.relative_to(ROOT.parent)).replace('\\','/'),renderSha256=hashlib.sha256(path.read_bytes()).hexdigest(),renderMethod='Microsoft Word唯讀開啟、巨集停用之背景獨立實例ExportAsFixedFormat；原DOC與SHA不變')
    d=pymupdf.open(path)
    row['metadataBasis']='卷首人工視覺核對學年、七年級、上學期第一次段考。'
    if row['year']==105:
        row.pop('metadataWarning',None)
        row['sourceNote']='官方檔案誤置於第3次資料夾；檔名與實際卷首均為105上學期第一次。依卷首核定。'
    row.update(pages=len(d),textChars=sum(len(p.get_text()) for p in d),hasTextLayer=sum(len(p.get_text()) for p in d)>100)
    for i,p in enumerate(d):
        p.get_pixmap(matrix=pymupdf.Matrix(1.4,1.4)).save(OUT/f"{row['year']}-p{i}.png")
        (OUT/f"{row['year']}-p{i}.txt").write_text(p.get_text(),encoding='utf8')
    print(row['year'],len(d),d[0].rect)
for row in catalog:
    if row['kind']=='question' and row['grade'] is None:
        row['kind']='unclassified'
        row['metadataWarning']='未明列適用年級的共同命題補充卷，已下載保存但不混入年級組卷。'
(ROOT/'zhonghua-pre108-catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf8')
