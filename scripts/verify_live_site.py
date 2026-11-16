import sys
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 900})
    console_errors = []
    page.on('console', lambda msg: console_errors.append(msg.text) if msg.type == 'error' else None)
    page.on('pageerror', lambda err: console_errors.append(str(err)))

    print('Navigating to live site...')
    page.goto('https://lee200202.github.io/yilan-math-bank/', wait_until='networkidle')

    # Click on coverage
    print('Testing Coverage View...')
    page.click("button[data-view='coverage']")
    page.wait_for_timeout(1000)
    page.screenshot(path='qa/takeover/live_coverage_view.png', full_page=True)
    cov_text = page.locator('main').inner_text()
    for l in cov_text.splitlines()[:15]:
        if l.strip():
            print('  Cov:', l.strip())

    # Click on library
    print('Testing Library View...')
    page.click("button[data-view='library']")
    page.wait_for_timeout(1000)
    page.screenshot(path='qa/takeover/live_library_view.png', full_page=True)
    lib_text = page.locator('main').inner_text()
    for l in lib_text.splitlines()[:15]:
        if l.strip():
            print('  Lib:', l.strip())

    # Search for a paper in Library, e.g. 誠正國中
    print('Searching for 誠正國中 in Library...')
    search_input = page.locator("input[placeholder*='搜尋'], input[type='search']")
    if search_input.count() > 0:
        search_input.first.fill('誠正國中')
        page.wait_for_timeout(500)
        page.screenshot(path='qa/takeover/live_search_chengzheng.png', full_page=True)

    print('Total console errors:', len(console_errors))
    for err in console_errors:
        print('  Error:', err)

    browser.close()
    print('Live verification completed successfully!')
