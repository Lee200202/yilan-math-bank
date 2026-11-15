"""Probe metro seed URLs from the external guide: status, title, attachment/link counts.

The guide's URLs come from another AI and must be re-verified before use.
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

SEEDS = {
    "new_taipei": [
        "https://www.hcjh.ntpc.edu.tw/p/403-1000-173.php",
        "https://www.ckjhs.ntpc.edu.tw/p/403-1000-196.php",
        "https://www.shjh.ntpc.edu.tw/p/403-1000-76.php",
        "https://www.ccjhs.ntpc.edu.tw/p/404-1000-12646.php?Lang=zh-tw",
        "https://www.jhjhs.ntpc.edu.tw/p/412-1000-175.php",
        "https://www.fhjh.ntpc.edu.tw/p/403-1000-78.php",
        "https://www.wfjh.ntpc.edu.tw/p/403-1000-77.php",
        "https://www.ljjh.ntpc.edu.tw/p/403-1000-107.php",
        "https://www.csjh.ntpc.edu.tw/p/404-1000-3962.php",
    ],
    "taipei": [
        "https://www.spjh.tp.edu.tw/nss/p/Pastexam",
        "https://www.ccjh.tp.edu.tw/nss/p/546421",
        "https://web.hhjh.tp.edu.tw/%E6%AA%94%E6%A1%88%E4%B8%8B%E8%BC%89/",
        "https://www.bjjh.tp.edu.tw/news/113-2_%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C%E8%A7%A3%E7%AD%94/",
    ],
    "taichung": [
        "https://hsjh.tc.edu.tw/p/403-1103-1921-1.php",
        "https://sgjh.tc.edu.tw/p/404-1115-21572.php",
        "https://dhjh.tc.edu.tw/p/403-1154-1470-1.php",
        "https://sites.google.com/mail.dyjh.tc.edu.tw/test-memory-new/%E6%AD%B7%E5%B1%86%E8%A9%A6%E9%A1%8C%E4%B8%8B%E8%BC%89",
    ],
    "kaohsiung": [
        "https://www.cchs.kh.edu.tw/ischool/publish_page/3/?cid=558",
        "https://hakka.mtjh.kh.edu.tw/exam/exam-section.htm",
        "https://www.dwm.kh.edu.tw/view/index.php?WebID=344&MainType=0&SubType=104&MainMenuId=64182&SubMenuId=64183",
        "https://www.smjh.kh.edu.tw/index.php?WebID=63",
    ],
    "taoyuan": [
        "https://www.wlsh.tyc.edu.tw/p/404-1000-21395.php",
        "https://hlmath.tw/school-examination/",
    ],
}

UA = {"User-Agent": "Mozilla/5.0 (compatible; exam-archive-research/1.0)"}
FILE_RE = re.compile(r"\.(pdf|docx?|odt)(\?|$)|/download\.php|downloadfile|/files/", re.I)


def probe(url):
    try:
        r = requests.get(url, headers=UA, timeout=25)
        r.encoding = r.apparent_encoding or r.encoding
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.title.get_text(strip=True) if soup.title else ""
        links = []
        for a in soup.find_all("a", href=True):
            href = urljoin(r.url, a["href"].strip())
            text = a.get_text(" ", strip=True) or a.get("title", "")
            links.append((text, href))
        files = [(t, h) for t, h in links if FILE_RE.search(h)]
        mathish = [(t, h) for t, h in links if "數" in t]
        return {
            "url": url, "final": r.url, "status": r.status_code, "title": title[:80],
            "links": len(links), "files": len(files), "math_links": len(mathish),
            "sample_files": files[:6], "sample_math": mathish[:10],
        }
    except Exception as e:  # noqa: BLE001
        return {"url": url, "error": repr(e)[:200]}


if __name__ == "__main__":
    out = {}
    for region, urls in SEEDS.items():
        out[region] = [probe(u) for u in urls]
    dest = Path(sys.argv[1])
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    for region, rows in out.items():
        for row in rows:
            print(region, row.get("status", row.get("error")), row.get("files"), row.get("math_links"), row.get("title", ""), row["url"][:70])
