"""Browser test of 記憶點 (questions from downloaded PDFs are not drawn again).
Usage: python scripts/test_memory.py [base_url]   (default http://127.0.0.1:4173)"""
import random
import sys

from playwright.sync_api import sync_playwright

base = (sys.argv[1] if len(sys.argv) > 1 else 'http://127.0.0.1:4173').rstrip('/')
results = []


def check(name, ok, detail=''):
    results.append(ok)
    print(('PASS ' if ok else 'FAIL ') + name, detail)


def ids(page):
    return page.evaluate('() => lanjuan.getSession().items.map(i => i.id)')


def generate(page):
    page.locator('#generate-button').click()
    page.wait_for_timeout(500)
    return ids(page)


with sync_playwright() as pw:
    browser = pw.chromium.launch(channel='chrome', headless=True)
    ctx = browser.new_context(accept_downloads=True, viewport={'width': 1440, 'height': 1000})
    page = ctx.new_page()
    errors = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.goto(f'{base}/?fresh={random.randint(1, 10**9)}', wait_until='networkidle')
    page.wait_for_function('() => window.lanjuan')
    check('memory panel is on the page', page.locator('#memory-section, .memory-section').count() == 1)
    check('starts with no memory points', page.locator('[data-mem]').count() == 0)

    page.select_option('#grade', '8')
    page.wait_for_timeout(300)
    first = generate(page)
    with page.expect_download() as dl:
        page.locator('#pdf-button').click()
    dl.value.path()
    page.wait_for_timeout(800)
    check('downloading a PDF creates 記憶點 1', page.locator('[data-mem]').count() == 1 and '記憶點 1' in page.locator('#memory-list').inner_text(), page.locator('#memory-list').inner_text().replace('\n', ' ')[:80])
    page.locator('#pdf-button').click()  # same paper again must not create another point
    page.wait_for_timeout(1500)
    check('downloading the same paper twice keeps one point', page.locator('[data-mem]').count() == 1)

    repeats = 0
    for _ in range(25):
        repeats += len(set(generate(page)) & set(first))
    check('25 new papers never reuse a remembered question', repeats == 0, f'{repeats} reused')

    # swapping avoids remembered questions too
    swaps = 0
    for _ in range(15):
        page.locator('[data-swap]').first.click()
        page.wait_for_timeout(250)
        swaps += len(set(ids(page)) & set(first))
    check('swapping a question never brings one back', swaps == 0, f'{swaps} reused')

    # a second point
    second = generate(page)
    with page.expect_download() as dl2:
        page.locator('#pdf-button').click()
    dl2.value.path()
    page.wait_for_timeout(800)
    check('a different paper becomes 記憶點 2', page.locator('[data-mem]').count() == 2)
    both = set(first) | set(second)
    leak = sum(len(set(generate(page)) & both) for _ in range(15))
    check('two checked points are both avoided', leak == 0, f'{leak} reused')

    # reload keeps memory
    page.reload(wait_until='networkidle')
    page.wait_for_function('() => window.lanjuan')
    check('memory survives a reload', page.locator('[data-mem]').count() == 2 and page.locator('[data-mem]:checked').count() == 2)

    # unticking a point stops avoiding it (the summary text updates)
    page.locator('[data-mem="1"]').uncheck()
    page.wait_for_timeout(300)
    check('unticking removes the point from the avoid list', '記憶點' in page.locator('#memory-summary').inner_text() and page.locator('[data-mem]:checked').count() == 1)

    # delete and clear
    page.locator('[data-mem-del="1"]').click()
    page.wait_for_timeout(200)
    check('deleting a point works', page.locator('[data-mem]').count() == 1)
    page.once('dialog', lambda d: d.accept())
    page.locator('#memory-clear').click()
    page.wait_for_timeout(300)
    check('clear removes every point', page.locator('[data-mem]').count() == 0)
    check('no script errors', not errors, errors[:2])
    browser.close()

print('ALL PASS' if all(results) else 'FAILURES PRESENT')
sys.exit(0 if all(results) else 1)
