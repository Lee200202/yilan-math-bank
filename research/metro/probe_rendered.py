"""Open candidate school archive pages in headless Chromium (handles JS-built RPage/NSS lists)
and record exam-related links. Usage: python research/metro/probe_rendered.py out.json"""
import json
import sys

from playwright.sync_api import sync_playwright

CANDIDATES = {
    'taipei': [
        'http://web.nmjh.tp.edu.tw/about-05_02.asp',
        'https://sites.google.com/jajh.tp.edu.tw/teaching/%E8%80%83%E8%A9%A6%E8%B3%87%E8%A8%8A/%E6%AD%B7%E5%B1%86%E8%A9%A6%E9%A1%8C',
        'http://eweb4.lkjh.tp.edu.tw/eweb/module/download/index.php?free_ids=423&home=ew00000000011&sn=293&sn_ids=420',
        'https://www.ccjh.tp.edu.tw/nss/p/546421',
    ],
    'new_taipei': [
        'https://www.hcjh.ntpc.edu.tw/p/403-1000-173.php',
        'https://www.shjh.ntpc.edu.tw/p/403-1000-76.php',
        'https://www.jhjhs.ntpc.edu.tw/p/412-1000-175.php',
        'https://www.fhjh.ntpc.edu.tw/p/403-1000-78.php',
        'https://www.wfjh.ntpc.edu.tw/p/403-1000-77.php',
        'https://www.ljjh.ntpc.edu.tw/p/403-1000-107.php',
    ],
    'taichung': [
        'https://sgjh.tc.edu.tw/p/404-1115-21572.php',
        'https://dhjh.tc.edu.tw/p/403-1154-1470-1.php',
        'https://sites.google.com/mail.dyjh.tc.edu.tw/test-memory-new/%E6%AD%B7%E5%B1%86%E8%A9%A6%E9%A1%8C%E4%B8%8B%E8%BC%89',
    ],
    'kaohsiung': [
        'https://www.cchs.kh.edu.tw/ischool/publish_page/3/?cid=558',
        'https://www.smjh.kh.edu.tw/index.php?WebID=63',
    ],
}
KEYS = ('數學', '段考', '試題', '定期評量', '考古', 'drive.google', '.pdf', 'downloadfile', '學年')

out = {}
with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    page = browser.new_page()
    for region, urls in CANDIDATES.items():
        for url in urls:
            row = {'region': region, 'url': url}
            try:
                page.goto(url, wait_until='networkidle', timeout=45000)
                page.wait_for_timeout(1500)
                links = page.evaluate("""() => [...document.querySelectorAll('a,iframe')].map(a => [(a.innerText||a.title||'').trim().slice(0,60), String(a.href||a.src||'')])""")
                hits = [l for l in links if any(k in (l[0] + ' ' + l[1]) for k in KEYS)]
                row.update(title=page.title()[:60], links=len(links), hits=hits[:60], hitCount=len(hits))
            except Exception as e:  # noqa: BLE001
                row['error'] = str(e)[:200]
            out[url] = row
            print(region, row.get('hitCount', row.get('error')), row.get('title', ''), url[:70], flush=True)
    browser.close()
open(sys.argv[1], 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))
