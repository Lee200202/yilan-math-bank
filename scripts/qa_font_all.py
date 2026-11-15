"""Export every selectable question to PDF in batches through the real typesetter, so a font
subset that lost any glyph (or any overflow) fails loudly. Usage: python scripts/qa_font_all.py [base_url]"""
import json
import sys

from playwright.sync_api import sync_playwright

BASE = sys.argv[1] if len(sys.argv) > 1 else 'http://127.0.0.1:4173'
with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    page = browser.new_page()
    errors = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.goto(BASE + '/', wait_until='networkidle')
    page.wait_for_function('() => window.lanjuan')
    result = page.evaluate("""async () => {
      const bank = lanjuan.getBank(); const out = {batches: 0, questions: 0, pages: 0, failures: []};
      for (let i = 0; i < bank.length; i += 60) {
        const items = bank.slice(i, i + 60).map(q => ({id: q.id, score: 1}));
        const record = {format: 'lanjuan-1', title: '八年級上學期第一次段考練習', revision: 1, filters: {}, items};
        try { await lanjuan.createPdf(record); out.pages += lanjuan.lastPdfPages || 0; out.questions += items.length; }
        catch (e) { out.failures.push({from: i, error: String(e.message || e).slice(0, 200)}); }
        out.batches++;
      }
      return out; }""")
    browser.close()
print(json.dumps({**result, 'pageErrors': errors}, ensure_ascii=False))
sys.exit(1 if result['failures'] or errors else 0)
