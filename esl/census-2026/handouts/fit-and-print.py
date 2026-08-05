#!/usr/bin/env python3
"""Render the handout HTML to PDF, scaling any page that would overflow A4.

Each .page is measured against the printable area. Pages that fit are left
alone; pages that overflow get a `zoom` factor just small enough to fit, so
one logical page always lands on exactly one sheet.
"""

import pathlib, re, sys
from playwright.sync_api import sync_playwright

CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
PX_PER_MM = 96 / 25.4
PAGE_W_MM, PAGE_H_MM = 210 - 2 * 13, 297 - 2 * 10   # matches @page in _common.py
SAFETY = 0.985                                       # leave a hair of slack
MIN_ZOOM = 0.70                                      # below this, fix the content

MEASURE_CSS = f"""
<style id="measure">
  body {{ width: {PAGE_W_MM}mm; margin: 0; }}
  .page {{ page-break-after: auto; }}
</style>
"""


def fit(html_path: pathlib.Path, pdf_path: pathlib.Path):
    html = html_path.read_text()
    target_px = PAGE_H_MM * PX_PER_MM

    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
        page = browser.new_page(viewport={'width': int(PAGE_W_MM * PX_PER_MM), 'height': 1200})
        page.emulate_media(media='print')
        page.set_content(html.replace('<style>', MEASURE_CSS + '<style>', 1))

        n = page.evaluate("document.querySelectorAll('.page').length")
        zooms = [1.0] * n

        for _ in range(6):
            heights = page.evaluate(
                "Array.from(document.querySelectorAll('.page'))"
                ".map(function(e){return e.getBoundingClientRect().height})")
            done = True
            for i, h in enumerate(heights):
                if h > target_px + 0.5:
                    zooms[i] = max(MIN_ZOOM, zooms[i] * (target_px / h) * SAFETY)
                    done = False
            if done:
                break
            page.evaluate(
                """(z) => document.querySelectorAll('.page').forEach(
                       (e, i) => e.style.zoom = z[i])""", zooms)

        browser.close()

    # bake the zooms into the file we actually print
    out, idx = [], 0
    for chunk in re.split(r'(<div class="page">)', html):
        if chunk == '<div class="page">':
            z = zooms[idx]
            out.append(chunk if z >= 0.999 else f'<div class="page" style="zoom:{z:.4f}">')
            idx += 1
        else:
            out.append(chunk)
    fitted = ''.join(out)

    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
        page = browser.new_page()
        page.emulate_media(media='print')
        page.set_content(fitted)
        page.pdf(path=str(pdf_path), prefer_css_page_size=True, print_background=False)
        browser.close()

    scaled = [(i + 1, round(z, 3)) for i, z in enumerate(zooms) if z < 0.999]
    print(f'{pdf_path.name}: {n} pages'
          + (f' | scaled to fit: {scaled}' if scaled else ' | no scaling needed'))
    return zooms


if __name__ == '__main__':
    here = pathlib.Path(__file__).parent
    names = sys.argv[1:] or ['census-esl-handouts-1-4', 'census-esl-handouts-5-6']
    for name in names:
        fit(here / f'{name}.html', here / f'{name}.pdf')
