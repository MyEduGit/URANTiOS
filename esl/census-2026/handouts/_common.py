#!/usr/bin/env python3
"""Shared layout, CSS and helpers for the Census ESL handout builders."""

def bx(n):
    return '<span class="bx">' + '<i></i>' * n + '</span>'

def bxw(*counts):
    return '<span class="bx">' + '<i class="sp"></i>'.join('<i></i>' * n for n in counts) + '</span>'

MK = '<span class="mk"></span>'

CSS = """
@page { size: A4; margin: 10mm 13mm; }
* { box-sizing: border-box; }
body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
       font-size: 10.6pt; line-height: 1.34; color: #000; margin: 0; }
.page { page-break-after: always; }
.page:last-child { page-break-after: auto; }

.hdr { border-top: 3px solid #000; border-bottom: 1px solid #000;
       padding: 2mm 0 1.6mm; margin-bottom: 2.6mm; overflow: hidden; }
.hdr .series { font-size: 8.5pt; letter-spacing: .09em; text-transform: uppercase; }
.hdr h1 { font-size: 16.5pt; margin: 1mm 0 0; font-weight: 700; }
.cont { float: right; font-size: 9pt; letter-spacing: .08em;
        text-transform: uppercase; padding-top: 1.5mm; }

.sec { margin-top: 3mm; }
.sec > h2 { font-size: 11.5pt; font-weight: 700; text-transform: uppercase;
            letter-spacing: .07em; border-bottom: 1px solid #000;
            padding-bottom: 0.8mm; margin: 0 0 2mm; }
.sec > h2 .t { float: right; font-weight: 400; font-size: 9.5pt;
               letter-spacing: 0; text-transform: none; }
p { margin: 0 0 1.6mm; }
ol, ul { margin: 0 0 2mm; padding-left: 6mm; }
li { margin-bottom: 1.1mm; }
.q { font-weight: 600; }
.note { font-size: 9.5pt; }

.excerpt { border: 1.3px solid #000; padding: 2.8mm 3.5mm; margin: 0 0 2.4mm; }
.excerpt .qn { font-weight: 700; font-size: 12pt; margin-right: 2mm; }
.excerpt p { margin: 0 0 1.8mm; }
.excerpt .src { font-size: 8pt; text-align: right; margin: 2mm 0 0; }
.lbl { font-size: 8.5pt; letter-spacing: .04em; display: block; margin: 2mm 0 0.8mm; }

.bx { display: inline-block; white-space: nowrap; vertical-align: middle; }
.bx i { display: inline-block; width: 7mm; height: 7mm; border: 1px solid #000;
        margin-right: -1px; vertical-align: middle; }
.bx i.sp { border: none; width: 3.5mm; margin-right: 0; }
.mk { display: inline-block; width: 4.6mm; height: 4.6mm; border: 1.2px solid #000;
      vertical-align: middle; margin-right: 2mm; }

table { border-collapse: collapse; width: 100%; margin: 0 0 2mm; }
td, th { vertical-align: top; padding: 0.9mm 2mm 0.9mm 0; }
.vocab th { font-size: 8.5pt; text-transform: uppercase; letter-spacing: .05em;
            text-align: left; border-bottom: 1px solid #000; padding-bottom: 1mm; }
.vocab td { padding-top: 1.2mm; padding-bottom: 1.2mm; }
.vocab tr td { border-bottom: 1px dotted #999; }
.vocab .w { width: 22%; }
.vocab .a { width: 6%; }
.vocab .m { width: 44%; }
.vocab .l { width: 28%; padding-right: 0; }
.tf td:first-child { width: 6%; }
.tf td:last-child { width: 16%; text-align: right; white-space: nowrap; }
.grid td { border: 1px solid #000; padding: 1.2mm 2mm; }
.grid th { border: 1px solid #000; padding: 1.6mm 2mm; text-align: left;
           font-size: 9.5pt; text-transform: uppercase; letter-spacing: .05em; }
.plain td:first-child { width: 47%; padding-right: 5mm; }

.aside { border: 1.2px dashed #000; padding: 2.5mm 3mm; margin: 2.5mm 0 0;
         font-size: 9.5pt; }
.warn { border: 1.2px solid #000; border-left-width: 4px; padding: 2.5mm 3mm;
        margin: 0 0 3mm; font-size: 9.5pt; }
.rule { border: 1.3px solid #000; padding: 3mm; margin: 0 0 3mm; }
.rule h3 { margin: 0 0 1.5mm; font-size: 10.5pt; text-transform: uppercase;
           letter-spacing: .06em; }

.crit { font-size: 9.5pt; margin-top: 2mm; }
.crit span { margin-right: 6mm; white-space: nowrap; }

.take { border-top: 1.4px dashed #000; margin-top: 3mm; padding-top: 2mm; }
.take h2 { font-size: 10.5pt; text-transform: uppercase; letter-spacing: .07em;
           margin: 0 0 2mm; }
.take .cols { display: flex; gap: 5mm; }
.take .cols > div { flex: 1; border: 1.2px solid #000; padding: 2.5mm 3mm;
                    font-size: 9.5pt; }
.take .cols h3 { margin: 0 0 1.5mm; font-size: 9pt; text-transform: uppercase;
                 letter-spacing: .06em; }
.take .help b { display: inline-block; min-width: 46mm; }

.foot { border-top: 1px solid #000; margin-top: 2.5mm; padding-top: 1.2mm;
        font-size: 8pt; overflow: hidden; }
.foot .pg { float: right; }
.line { display: inline-block; border-bottom: 1px solid #000; height: 4.5mm;
        min-width: 26mm; vertical-align: bottom; }
.line.s { min-width: 15mm; }
.line.f { min-width: 100%; }
.line.l { min-width: 60mm; }

/* readiness checklist */
.ck h2 { font-size: 11.5pt; text-transform: uppercase; letter-spacing: .06em;
         border-bottom: 1.4px solid #000; padding-bottom: 0.8mm; margin: 3.5mm 0 2mm; }
.ck li { margin-bottom: 2.1mm; list-style: none; }
.ck ul { padding-left: 0; }
.ck li:before { content: "\\2610"; font-size: 13pt; margin-right: 3mm; }
.big { font-size: 13pt; font-weight: 700; }

/* answer pages */
.ansh { font-size: 10pt; text-transform: uppercase; letter-spacing: .06em;
        border-bottom: 1px solid #000; padding-bottom: 0.6mm; margin: 2.6mm 0 1.2mm; }
.ans { font-size: 8.3pt; line-height: 1.28; }
.ans th { font-size: 7.6pt; text-transform: uppercase; letter-spacing: .05em;
          text-align: left; border-bottom: 1px solid #000; padding-bottom: 0.8mm; }
.ans td { border-bottom: 1px dotted #999; padding: 0.85mm 2mm 0.85mm 0; }
.ans .i { width: 15%; font-weight: 600; }
.ans .an { width: 17%; font-weight: 700; }
.ans .s { width: 23%; }
.ans .d { width: 45%; padding-right: 0; }
"""

def header(num, title, cont=False, series="Filling In the Form"):
    tag = f'<span class="cont">Handout {num} &middot; page 2</span>' if cont else ''
    sub = '' if cont else f'<div class="series">{series} &nbsp;&middot;&nbsp; Handout {num}</div>'
    return f'<div class="hdr">{tag}{sub}<h1>{title}</h1></div>'

def sec(letter, name, time, body):
    t = f'<span class="t">{time}</span>' if time else ''
    return f'<div class="sec"><h2>{t}{letter}. {name}</h2>{body}</div>'

def vocab(rows):
    """rows: (word, meaning) — meanings are deliberately out of order."""
    out = ('<table class="vocab"><tr><th class="w">Word</th><th class="a"></th>'
           '<th class="m">Meaning</th><th class="l">My language</th></tr>')
    for w, m in rows:
        out += (f'<tr><td class="w">{w}</td><td class="a"><span class="line s"></span></td>'
                f'<td class="m">{m}</td><td class="l">&nbsp;</td></tr>')
    return out + '</table><p class="note">Write the letter of the meaning. '

def make_foot(total):
    def foot(page):
        return ('<div class="foot"><span class="pg">Page ' + str(page) + ' of '
                + str(total) + '</span>Adapted from the Census Household Form, '
                '&copy; Commonwealth of Australia 2026, Australian Bureau of Statistics. '
                'Classroom practice material &mdash; not an official ABS product.</div>')
    return foot

TAKE = """
<div class="take">
<h2>&#9986; F. Take home</h2>
<div class="cols">
<div>
<h3>Exit ticket</h3>
Three words I can use now:<br>
<span class="line f"></span><br>
One thing I still need help with:<br>
<span class="line f"></span>
</div>
<div class="help">
<h3>Getting help</h3>
<b>Census help line</b> 1800 181 227<br>
<b>Interpreter &mdash; TIS National</b> 131 450<br>
<b>Online help</b> census.abs.gov.au/help<br>
<span style="font-size:9pt"><i>Could you say that again, please?</i><br>
<i>Could you explain that in easier English?</i><br>
<i>I need an interpreter who speaks</i> <span class="line s"></span> .</span>
</div>
</div>
</div>
"""

def document(pages, title):
    """Assembles the pages and stamps "Page x of y" on every one."""
    total = len(pages)
    body = []
    for i, p in enumerate(pages, 1):
        f = ('<div class="foot"><span class="pg">Page ' + str(i) + ' of ' + str(total)
             + '</span>Adapted from the Census Household Form, '
             '&copy; Commonwealth of Australia 2026, Australian Bureau of Statistics. '
             'Classroom practice material &mdash; not an official ABS product.</div>')
        body.append(f'<div class="page">{p}{f}</div>')
    return ('<meta charset="utf-8">\n'
            f'<title>{title}</title>\n'
            f'<style>{CSS}</style>\n' + '\n'.join(body))
