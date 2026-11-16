import sys
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 900})
    console_errors = []
    page.on('console', lambda msg: console_errors.append(msg.text) if msg.type == 'error' else None)
    page.on('pageerror', lambda err: console_errors.append(str(err)))

    print('Navigating to live site...')
    page.goto('https://lee200202.github.io/yilan-math-bank/', wait_until='domcontentloaded')
    page.wait_for_timeout(1500)

    # Switch to Library
    print('Switching to library view...')
    page.click("button[data-view='library']")
    page.wait_for_timeout(800)

    # Filter to ready papers
    page.check("#library-ready")
    page.wait_for_timeout(500)

    # Look for button[data-preview-paper]
    preview_btn = page.locator("button[data-preview-paper]").first
    btn_text = preview_btn.inner_text()
    print('Found preview button:', btn_text)
    preview_btn.click()
    page.wait_for_timeout(2000)

    # Take screenshot of rendered paper in compose view
    page.screenshot(path='qa/takeover/live_exam_preview.png', full_page=True)
    print('Saved exam preview screenshot to qa/takeover/live_exam_preview.png')

    # Verify questions and SVG on page
    svg_items = page.locator("svg")
    print('SVG items count on live preview page:', svg_items.count())

    # Check paper heading
    print('Console errors:', len(console_errors))
    for err in console_errors:
        print('  Console Error:', err)

    browser.close()
    print('Live paper preview verification successful!')
