"""Metro-area (Taipei / New Taipei / Taoyuan / Taichung / Kaohsiung) public junior-high
math exam inventory.

Each source is traversed completely (all list pages / all Drive sub-folders), every
math file is recorded with its parsed slot, and question files are downloaded and
hash-checked. Output: research/metro/metro-inventory.json (+ raw files, gitignored).

Seeds were re-verified on 2026-11-15; guide URLs that were empty or unrelated are
recorded in metro-source-notes.json instead of being crawled.
"""
import concurrent.futures
import datetime
import hashlib
import json
import os
import pathlib
import re
import sys
import time
import unicodedata
from urllib.parse import quote, urljoin, unquote

import requests
from bs4 import BeautifulSoup

R = pathlib.Path(__file__).resolve().parent
ROOT = R.parents[1]
RAW = R / "raw"
RAW.mkdir(exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (compatible; public-exam-inventory/1.0)"}
S = requests.Session()
S.headers.update(UA)
CN = {"一": 1, "二": 2, "三": 3, "七": 7, "八": 8, "九": 9}


def get(url, attempts=3, **kw):
    for i in range(attempts):
        try:
            r = S.get(quote(url, safe=":/?=&%,#()"), timeout=60, **kw)
            r.raise_for_status()
            return r
        except Exception:
            if i == attempts - 1:
                raise
            time.sleep(2 + i * 3)


def html(url):
    r = get(url)
    r.encoding = "utf-8" if b"utf-8" in r.content[:3000].lower() else (r.apparent_encoding or "utf-8")
    return r, BeautifulSoup(r.text, "html.parser")


def norm(s):
    return unicodedata.normalize("NFKC", s or "")


def is_math(name):
    n = norm(name)
    return "數學" in n or re.search(r"(^|[^算])數(?!位|據|線)", n) is not None or "math" in n.lower()


def kind_of(name):
    n = norm(name)
    if "答案卷" in n or "答案紙" in n or "答案欄" in n or "作答卷" in n or "手寫卷" in n:
        return "answer_sheet"
    if "解答" in n or "答案" in n or "詳解" in n:
        return "answer"
    return "question"


def grade_from(text):
    t = norm(text)
    m = re.search(r"([789七八九])年級", t) or re.search(r"國([一二三123789])", t) or re.search(r"([789])G", t) or re.search(r"([七八九])[上下]", t)
    if m:
        g = m.group(1)
        g = CN.get(g, None) or int(g)
        return g + 6 if g <= 3 else g
    m = re.search(r"([一二三123])年級", t)
    if m:
        g = m.group(1)
        return (CN.get(g) or int(g)) + 6
    m = re.search(r"\(([789])\)|（([789])）|([789])數|數學[_ -]?([789])\b|-([789])[A-Z]?(?=數|\.|$)", t)
    if m:
        return int(next(x for x in m.groups() if x))
    return None


def slot_from(text):
    """Best-effort year/semester/exam/grade parsing from a combined name+path string."""
    t = norm(text)
    year = sem = exam = grade = None
    m = re.search(r"(1[01]\d)-([12])-([123])-([789])", t)
    if m:
        year, sem, exam, grade = map(int, m.groups())
        return dict(year=year, semester=sem, exam=exam, grade=grade)
    m = re.search(r"(1[01]\d)s([12])-([123])", t)  # 大業: 113s1-1
    if m:
        return dict(year=int(m.group(1)), semester=int(m.group(2)), exam=int(m.group(3)), grade=grade_from(t))
    m = re.search(r"(1[01]\d)\s*學年(?:度)?", t) or re.search(r"(?<!\d)(1[01]\d)(?=[-_ ]?[12上下]|學)", t) or re.search(r"(?<!\d)(1[01]\d)年(?!級)", t) or re.search(r"(?<!\d)(1[01]\d)[.]?[789]G", t)
    if m:
        year = int(m.group(1))
    m = re.search(r"第\s*([一二12])\s*學期|([上下])學期|[七八九]([上下])|(?<!\d)1[01]\d\s*-?\s*([12])(?=[-_ ]|學期|定期|$|[^\d])|1[01]\d([上下])", t)
    if m:
        g = next(x for x in m.groups() if x)
        sem = {"一": 1, "二": 2, "上": 1, "下": 2}.get(g) or int(g)
    m = re.search(r"第\s*([一二三123])\s*次", t) or re.search(r"(?<!\d)1[01]\d-[12]-([123])(?!\d)", t) or re.search(r"(?:^|[/ ])([一二三])段", t) or re.search(r"段([123])(?!\d)", t)
    if m:
        g = m.group(1)
        exam = CN.get(g) or int(g)
    grade = grade_from(t)
    return dict(year=year, semester=sem, exam=exam, grade=grade)


def record(region, school, name, url, page, path=""):
    s = slot_from(f"{path} {name}")
    return {
        "region": region, "school": school, "name": norm(name).strip(), "sourceUrl": url,
        "sourcePage": page, "path": path, "kind": kind_of(name), **s,
    }


# ---------------------------------------------------------------- sources

def kaohsiung_meinong():
    page = "https://hakka.mtjh.kh.edu.tw/exam/exam-section.htm"
    r, soup = html(page)
    rows = []
    for a in soup.find_all("a", href=True):
        href = urljoin(r.url, a["href"].strip())
        fname = unquote(href.rsplit("/", 1)[-1])
        if not re.search(r"\.(pdf|docx?|odt)$", fname, re.I) or "數學" not in fname:
            continue
        rec = record("kaohsiung", "美濃國中", fname, href, page)
        # Older entries live at /exam/<YYYS>/<exam>/<一|二|三>數學.doc
        m = re.search(r"/exam/(1[01]\d)([12])/0?([123])/([一二三])數學", unquote(href))
        if m and rec["year"] is None:
            rec.update(year=int(m.group(1)), semester=int(m.group(2)), exam=int(m.group(3)),
                       grade=CN[m.group(4)] + 6, slotBasis="official URL path /exam/<學年學期>/<次別>/<年級>")
        rows.append(rec)
    return rows, {"listPages": [page]}


def kaohsiung_dawan():
    base = "https://www.dwm.kh.edu.tw/view/index.php?WebID=344&MainType=0&SubType=104&MainMenuId=64182&SubMenuId=64183"
    rows, pages = [], []
    for n in range(1, 80):
        url = base + (f"&TypeChange=&page={n}" if n > 1 else "")
        r, soup = html(url)
        pages.append(url)
        files = [a for a in soup.find_all("a", href=True) if "/upload/344/104_64183/" in a["href"]]
        if not files:
            break
        for a in files:
            href = urljoin(r.url, a["href"])
            fname = unquote(href.rsplit("/", 1)[-1])
            if is_math(fname):
                rows.append(record("kaohsiung", "大灣國中", fname, href, url))
        if not any("下一頁" in a.get_text() for a in soup.find_all("a")):
            break
    return rows, {"listPages": pages}


def new_taipei_xikun():
    index = "https://www.ckjhs.ntpc.edu.tw/p/403-1000-196.php"
    pages = [index]
    sem_pages = {}
    for n in range(1, 10):
        url = index if n == 1 else f"https://www.ckjhs.ntpc.edu.tw/p/403-1000-196-{n}.php"
        try:
            r, soup = html(url)
        except Exception:
            break
        found = 0
        for a in soup.find_all("a", href=True):
            t = a.get_text(" ", strip=True)
            if ",r196" in a["href"] and "定期評量" in t:
                sem_pages[urljoin(r.url, a["href"])] = t
                found += 1
        pages.append(url)
        if not found:
            break
    rows = []
    for url, title in sem_pages.items():
        r, soup = html(url)
        for a in soup.find_all("a", href=True):
            t = a.get_text(" ", strip=True)
            if "downloadfile" in a["href"] and re.search(r"\.(pdf|docx?|odt)$", t, re.I) and is_math(t):
                rec = record("new_taipei", "溪崑國中", t, urljoin(r.url, a["href"]), url, title)
                rows.append(rec)
    return rows, {"listPages": pages, "semesterPages": sem_pages}


def drive_list(fid):
    r = get(f"https://drive.google.com/drive/folders/{fid}")
    m = re.search(r"window\['_DRIVE_ivd'\] = '((?:\\.|[^'])*)';", r.text)
    if not m:
        raise ValueError("no anonymous listing")
    enc = m.group(1).replace("\\x", "\\u00").replace("\\'", "'")
    data = json.loads(json.loads('"' + enc + '"'))
    return [{"id": x[0], "name": x[2], "mime": x[3]} for x in (data[0] or [])]


def drive_tree(region, school, roots, page, accept_zip=False):
    rows, folders = [], []
    stack = [(fid, label) for fid, label in roots]
    while stack:
        fid, path = stack.pop()
        try:
            items = drive_list(fid)
            folders.append({"id": fid, "path": path, "status": "listed" if items else "empty-folder", "items": len(items)})
        except Exception as e:  # noqa: BLE001
            folders.append({"id": fid, "path": path, "status": "list-failed", "error": str(e)[:160]})
            continue
        for it in items:
            if it["mime"] == "application/vnd.google-apps.folder":
                stack.append((it["id"], f"{path}/{it['name']}"))
            elif is_math(it["name"]) or is_math(path.rsplit("/", 1)[-1]) or (accept_zip and it["name"].lower().endswith(".zip")):
                rec = record(region, school, it["name"], f"https://drive.google.com/file/d/{it['id']}/view", page, path)
                rec["driveId"] = it["id"]
                rec["mime"] = it["mime"]
                rows.append(rec)
    return rows, {"driveFolders": folders}


def taichung_xiangshang():
    page = "https://hsjh.tc.edu.tw/p/403-1103-1921-1.php"
    r, soup = html(page)
    roots = []
    for a in soup.find_all("a", href=True):
        t = a.get_text(" ", strip=True)
        m = re.search(r"drive/folders/([\w-]+)", a["href"])
        if m and "學期" in t:
            roots.append((m.group(1), t.replace("(另開視窗)", "")))
    return drive_tree("taichung", "向上國中", roots, page, accept_zip=True)


def taoyuan_ziqiang():
    page = "https://www.tcjh.tyc.edu.tw/nss/p/index"
    return drive_tree("taoyuan", "自強國中", [("1BQFNJxFEFHDd76cIHCe0FjmXRJ2Cg7oD", "歷屆段考試題")], page)


def taipei_xingfu():
    page = "https://www.hfjh.tp.edu.tw/office/div_200/section_210/%E6%AE%B5%E8%80%83%E9%A1%8C%E5%BA%AB/"
    r, soup = html(page)
    roots, seen = [], set()
    for a in soup.find_all("a", href=True):
        m = re.search(r"drive/folders/([\w-]+)", a["href"])
        if m and m.group(1) not in seen:
            seen.add(m.group(1))
            roots.append((m.group(1), "段考題庫/" + a.get_text(strip=True)))
    return drive_tree("taipei", "興福國中", roots, page)


def new_taipei_zhongzheng():
    """RPage list 段考考古題專區 (403-1000-114[-n].php) -> one post per exam -> attachments."""
    posts, pages = {}, []
    for n in range(0, 40):
        url = "https://www.ccjhs.ntpc.edu.tw/p/403-1000-114.php" if n == 0 else f"https://www.ccjhs.ntpc.edu.tw/p/403-1000-114-{n}.php?Lang=zh-tw"
        try:
            r, soup = html(url)
        except Exception:
            break
        pages.append(url)
        found = 0
        for a in soup.find_all("a", href=True):
            t = a.get_text(" ", strip=True)
            if re.search(r"/p/40[46]-1000-\d+", a["href"]) and ("段考" in t or "定期評量" in t):
                href = urljoin(r.url, a["href"]).split("?")[0]
                if href not in posts:
                    posts[href] = t
                    found += 1
        if not found and n > 1:
            break
    rows = []
    for url, title in posts.items():
        try:
            r, soup = html(url)
        except Exception:
            continue
        for a in soup.find_all("a", href=True):
            t = a.get_text(" ", strip=True)
            if "downloadfile" in a["href"] and re.search(r"\.(pdf|docx?|odt)$", t, re.I) and is_math(t):
                rows.append(record("new_taipei", "中正國中", t, urljoin(r.url, a["href"]), url, title))
    return rows, {"listPages": pages, "posts": posts}


def rpage_archive(region, school, domain, list_ids, extra_lists=()):
    """Generic RPage archive: list pages /p/403-1000-<id>[-n].php -> posts (,r<id>) -> attachments.
    Attachment names often omit year/exam, so the post title is kept as the slot path."""
    posts, pages = {}, []
    lists = [(lid, f"https://{domain}/p/403-1000-{lid}.php") for lid in list_ids] + list(extra_lists)
    for lid, first in lists:
        for n in range(0, 40):
            url = first if n == 0 else first.replace(".php", f"-{n}.php")
            try:
                r, soup = html(url)
            except Exception:
                break
            pages.append(url)
            found = 0
            for a in soup.find_all("a", href=True):
                t = a.get_text(" ", strip=True)
                if re.search(rf"/p/40[46]-1000-\d+,r{lid}\.php", a["href"]):
                    href = urljoin(r.url, a["href"]).split("?")[0]
                    if href not in posts:
                        posts[href] = t
                        found += 1
            if not found and n > 0:
                break
    rows = []
    for url, title in posts.items():
        try:
            r, soup = html(url)
        except Exception:
            continue
        for a in soup.find_all("a", href=True):
            t = a.get_text(" ", strip=True) or a.get("title", "")
            href = urljoin(r.url, a["href"])
            is_file = "downloadfile" in href or re.search(r"/var/file/.+\.(pdf|docx?|odt)$", href, re.I)
            if is_file and re.search(r"\.(zip|7z|rar)$", t, re.I) and not re.search(r"答案|解答|詳解", t):
                rows.append(record(region, school, t, href, url, title))  # whole-exam archive
            elif is_file and re.search(r"\.(pdf|docx?|odt)$", t, re.I) and (is_math(t) or "數學" in title):
                if not is_math(t) and not re.search(r"數", t):
                    continue
                rows.append(record(region, school, t, href, url, title))
    return rows, {"listPages": pages, "posts": posts}


def taipei_chengzheng():
    """NSS page: each exam item is a JS toggle revealing per-grade all-subject zips."""
    from playwright.sync_api import sync_playwright
    page_url = "https://www.ccjh.tp.edu.tw/nss/p/546421"
    rows, items = [], []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(page_url, wait_until="networkidle", timeout=60000)
        labels = page.evaluate("""() => [...document.querySelectorAll('a')].map(a => a.textContent.trim()).filter(t => /^\\d{4}[一二三]段試題/.test(t))""")
        for label in labels:
            page.locator("a", has_text=label).first.click()
            page.wait_for_timeout(1200)
            links = page.evaluate("""() => [...document.querySelectorAll('a')].filter(a => /uploads\\/.+\\.zip$/i.test(a.href)).map(a => [a.textContent.replace(/\\s+/g,' ').trim(), a.href])""")
            m = re.match(r"(\d{3})(\d)([一二三])段", label)
            path = f"{m.group(1)}學年度第{m.group(2)}學期第{m.group(3)}次段考" if m else label
            items.append({"label": label, "zips": links})
            for text, href in links:
                name = re.sub(r"^attach_file\s*", "", text).split(" (")[0].strip()
                if "題目" not in name:
                    continue
                rec = record("taipei", "誠正國中", name, href, page_url, path)
                rows.append(rec)
            page.goto(page_url, wait_until="networkidle", timeout=60000)
        browser.close()
    return rows, {"listPage": page_url, "items": items}


def drive_source(region, school, page, roots):
    return lambda: drive_tree(region, school, roots, page, accept_zip=True)


SOURCES = {
    "taipei-chengzheng": taipei_chengzheng,
    "new_taipei-sanhe": lambda: rpage_archive("new_taipei", "三和國中", "www.shjh.ntpc.edu.tw", [76]),
    "new_taipei-fuhe": lambda: rpage_archive("new_taipei", "福和國中", "www.fhjh.ntpc.edu.tw", [78]),
    "new_taipei-wufeng": lambda: rpage_archive("new_taipei", "五峰國中", "www.wfjh.ntpc.edu.tw", [77]),
    "new_taipei-lujiang": lambda: rpage_archive("new_taipei", "鷺江國中", "www.ljjh.ntpc.edu.tw", [107]),
    "new_taipei-xinzhuang": lambda: rpage_archive("new_taipei", "新莊國中", "www.hcjh.ntpc.edu.tw", [177, 173, 167, 146, 138, 124, 90, 80, 79, 78]),
    "new_taipei-yonghe": drive_source("new_taipei", "永和國中", "https://www.jhjhs.ntpc.edu.tw/p/412-1000-175.php",
                                      [("1hcJh6StDal_wXcRSnNNkG6__g6QKv2wU", "段考試題雲端連結"), ("1kstc2Aj9LZOWmUq1GB1ZnoACje792LAK", "段考試題")]),
    "taichung-dahua": drive_source("taichung", "大華國中", "https://dhjh.tc.edu.tw/p/403-1154-1470-1.php",
                                   [("1-tsvXgbmG2n-7eFTLjl8TpStjK_OSt7J", "歷屆段考試題")]),
    "taichung-daye": drive_source("taichung", "大業國中", "https://sites.google.com/mail.dyjh.tc.edu.tw/test-memory-new/%E6%AD%B7%E5%B1%86%E8%A9%A6%E9%A1%8C%E4%B8%8B%E8%BC%89",
                                  [("1-FQ00lD4Q7jDy0vWiUxjyq2ovdLWQO5g", "大業歷屆段考試題")]),
    "new_taipei-zhongzheng": new_taipei_zhongzheng,
    "taipei-xingfu": taipei_xingfu,
    "kaohsiung-meinong": kaohsiung_meinong,
    "kaohsiung-dawan": kaohsiung_dawan,
    "new_taipei-xikun": new_taipei_xikun,
    "taichung-xiangshang": taichung_xiangshang,
    "taoyuan-ziqiang": taoyuan_ziqiang,
}


# ---------------------------------------------------------------- download

def sniff(b):
    if b.startswith(b"%PDF"):
        return "pdf"
    if b[:2] == b"PK":
        return "docx" if b"word/" in b[:4000] or b"[Content_Types]" in b[:4000] else "zip"
    if b[:4] == bytes.fromhex("d0cf11e0"):
        return "doc"
    if b[:6] == b"7z\xbc\xaf\x27\x1c":
        return "7z"
    if b[:4] == b"Rar!":
        return "rar"
    return None


def download(row):
    key = hashlib.sha1(row["sourceUrl"].encode()).hexdigest()[:16]
    row["id"] = f"metro-{row['region']}-{key}"
    existing = list(RAW.glob(row["id"] + ".*"))
    if existing:
        b = existing[0].read_bytes()
    else:
        urls = [row["sourceUrl"]]
        if row.get("driveId"):
            urls = [f"https://drive.google.com/uc?export=download&id={row['driveId']}",
                    f"https://drive.usercontent.google.com/download?id={row['driveId']}&export=download&confirm=t"]
        b, errors = None, []
        for u in urls:
            try:
                data = get(u).content
                if sniff(data):
                    b = data
                    break
                errors.append({"url": u, "error": "not a pdf/word original", "bytes": len(data)})
            except Exception as e:  # noqa: BLE001
                errors.append({"url": u, "error": str(e)[:160]})
        if b is None:
            row.update(downloadStatus="download-failed", downloadErrors=errors)
            return row
    fmt = sniff(b)
    path = RAW / f"{row['id']}.{fmt}"
    if not path.exists():
        path.write_bytes(b)
    row.update(downloadStatus="downloaded", format=fmt, bytes=len(b), sha256=hashlib.sha256(b).hexdigest(),
               localPath=str(path.relative_to(ROOT)).replace("\\", "/"))
    return row


def zip_member_name(info):
    if info.flag_bits & 0x800:
        return info.filename
    try:
        raw = info.filename.encode("cp437")
    except UnicodeEncodeError:
        return info.filename
    for enc in ("cp950", "utf-8"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            pass
    return info.filename


def expand_zips(rows):
    """Whole-school exam archives (all subjects in one zip): keep the zip as evidence and
    publish each math member as its own record, traceable to zip URL + member path."""
    import zipfile
    out = []
    for row in rows:
        if row["name"].lower().endswith((".7z", ".rar")):
            row["kind"] = "archive"
            row["archiveStatus"] = "not-extracted: no 7z/rar extractor installed in this environment"
            out.append(row)
            continue
        if not row["name"].lower().endswith(".zip"):
            out.append(row)
            continue
        row["kind"] = "archive"
        out.append(row)
        if row.get("downloadStatus") != "downloaded":
            continue
        with zipfile.ZipFile(ROOT / row["localPath"]) as z:
            members = []
            for info in z.infolist():
                name = zip_member_name(info)
                if info.is_dir() or not re.search(r"\.(pdf|docx?|odt)$", name, re.I) or not is_math(name.rsplit("/", 1)[-1]):
                    continue
                members.append(name)
                b = z.read(info)
                fmt = sniff(b) or name.rsplit(".", 1)[-1].lower()
                sha = hashlib.sha256(b).hexdigest()
                mid = f"{row['id']}-{sha[:8]}"
                path = RAW / f"{mid}.{fmt}"
                if not path.exists():
                    path.write_bytes(b)
                rec = record(row["region"], row["school"], name.rsplit("/", 1)[-1], f"{row['sourceUrl']}#{name}", row["sourcePage"], f"{row['path']}/{row['name']}/{name}")
                rec.update(id=mid, archiveId=row["id"], archiveMember=name, downloadStatus="extracted-from-archive",
                           format=fmt, bytes=len(b), sha256=sha, localPath=str(path.relative_to(ROOT)).replace("\\", "/"))
                out.append(rec)
            row["mathMembers"] = members
    return out


def reslot(inv):
    for src in inv["sources"].values():
        for row in src["files"]:
            if row.get("slotBasis"):
                continue
            row.update(slot_from(f"{row.get('path','')} {row['name']}"))
            if row["kind"] != "archive":
                row["kind"] = kind_of(row["name"])


def main():
    if sys.argv[1:] == ["--reslot"]:
        out_path = R / "metro-inventory.json"
        inv = json.loads(out_path.read_text(encoding="utf-8"))
        reslot(inv)
        out_path.write_text(json.dumps(inv, ensure_ascii=False, indent=1), encoding="utf-8")
        return
    only = sys.argv[1:] or list(SOURCES)
    out_path = R / os.environ.get("METRO_INV", "metro-inventory.json")
    inv = json.loads(out_path.read_text(encoding="utf-8")) if out_path.exists() else {"sources": {}}
    for key in only:
        print("crawl", key, flush=True)
        rows, evidence = SOURCES[key]()
        seen, uniq = set(), []
        for row in rows:
            if row["sourceUrl"] in seen:
                continue
            seen.add(row["sourceUrl"])
            uniq.append(row)
        with concurrent.futures.ThreadPoolExecutor(6) as ex:
            uniq = list(ex.map(download, uniq))
        uniq = expand_zips(uniq)
        inv["sources"][key] = {
            "crawledAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "evidence": evidence, "files": uniq,
        }
        ok = sum(r.get("downloadStatus") == "downloaded" for r in uniq)
        print(f"  {len(uniq)} math files, {ok} downloaded, questions={sum(r['kind']=='question' for r in uniq)}", flush=True)
        out_path.write_text(json.dumps(inv, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
