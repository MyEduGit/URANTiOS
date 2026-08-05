#!/usr/bin/env python3
"""Render the teacher-pack markdown to printable A4 PDFs."""

import pathlib, sys
import markdown
from playwright.sync_api import sync_playwright

CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'

CSS = """
@page { size: A4; margin: 0; }
body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
       font-size: 10.5pt; line-height: 1.45; color: #000; margin: 0; }
h1 { font-size: 19pt; margin: 0 0 4mm; padding-bottom: 2mm;
     border-bottom: 3px solid #000; }
h2 { font-size: 13pt; margin: 7mm 0 2.5mm; padding-bottom: 1mm;
     border-bottom: 1px solid #000; page-break-after: avoid; }
h3 { font-size: 11pt; margin: 5mm 0 2mm; page-break-after: avoid; }
p, li { margin: 0 0 2.2mm; }
ul, ol { padding-left: 6mm; margin: 0 0 3mm; }
table { border-collapse: collapse; width: 100%; margin: 0 0 4mm;
        font-size: 9.5pt; page-break-inside: avoid; }
th { text-align: left; border-bottom: 1.4px solid #000; padding: 1.4mm 3mm 1.4mm 0;
     font-size: 8.5pt; text-transform: uppercase; letter-spacing: .05em; }
td { border-bottom: 1px dotted #999; padding: 1.4mm 3mm 1.4mm 0; vertical-align: top; }
code { font-family: "SF Mono", Menlo, Consolas, monospace; font-size: 9pt; }
hr { border: none; border-top: 1px solid #000; margin: 6mm 0; }
blockquote { border-left: 3px solid #000; margin: 0 0 3mm; padding-left: 4mm; }
strong { font-weight: 700; }
a { color: #000; text-decoration: none; }
"""


def convert(md_path: pathlib.Path, pdf_path: pathlib.Path):
    html = markdown.markdown(md_path.read_text(), extensions=['tables', 'sane_lists'])
    doc = f'<meta charset="utf-8"><style>{CSS}</style>{html}'
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
        page = browser.new_page()
        page.emulate_media(media='print')
        page.set_content(doc)
        page.pdf(path=str(pdf_path), format='A4', print_background=False,
                 margin={'top': '16mm', 'bottom': '14mm', 'left': '18mm', 'right': '18mm'},
                 display_header_footer=True,
                 header_template='<div></div>',
                 footer_template=(
                     '<div style="font-size:8pt;width:100%;padding:0 18mm;'
                     'font-family:Helvetica,Arial,sans-serif;color:#000;'
                     'border-top:1px solid #000;padding-top:2mm;">'
                     '<span style="float:right">Page <span class="pageNumber"></span>'
                     ' of <span class="totalPages"></span></span>'
                     'Adapted from the Census Household Form, '
                     '&copy; Commonwealth of Australia 2026, '
                     'Australian Bureau of Statistics.</div>'))
        browser.close()
    print(f'{pdf_path.name}')


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        src = pathlib.Path(arg)
        convert(src, src.with_suffix('.pdf'))
