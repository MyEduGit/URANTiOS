#!/usr/bin/env python3
"""Generate the print-ready A4 handout file for Tier 1 (Handouts 1-4)."""

def bx(n):
    return '<span class="bx">' + '<i></i>' * n + '</span>'

def bxw(*counts):
    return '<span class="bx">' + '<i class="sp"></i>'.join('<i></i>' * n for n in counts) + '</span>'

MK = '<span class="mk"></span>'
TOTAL_PAGES = 8

CSS = """
@page { size: A4; margin: 12mm 14mm; }
* { box-sizing: border-box; }
body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
       font-size: 11pt; line-height: 1.4; color: #000; margin: 0; }
.page { page-break-after: always; }
.page:last-child { page-break-after: auto; }

.hdr { border-top: 3px solid #000; border-bottom: 1px solid #000;
       padding: 2.5mm 0 2mm; margin-bottom: 3.5mm; overflow: hidden; }
.hdr .series { font-size: 8.5pt; letter-spacing: .09em; text-transform: uppercase; }
.hdr h1 { font-size: 16.5pt; margin: 1mm 0 0; font-weight: 700; }
.cont { float: right; font-size: 9pt; letter-spacing: .08em;
        text-transform: uppercase; padding-top: 1.5mm; }

.sec { margin-top: 4mm; }
.sec > h2 { font-size: 11.5pt; font-weight: 700; text-transform: uppercase;
            letter-spacing: .07em; border-bottom: 1px solid #000;
            padding-bottom: 1mm; margin: 0 0 2.5mm; }
.sec > h2 .t { float: right; font-weight: 400; font-size: 9.5pt;
               letter-spacing: 0; text-transform: none; }
p { margin: 0 0 2mm; }
ol, ul { margin: 0 0 2mm; padding-left: 6mm; }
li { margin-bottom: 1.4mm; }
.q { font-weight: 600; }
.note { font-size: 9.5pt; }

.excerpt { border: 1.3px solid #000; padding: 3.5mm 4mm; margin: 0 0 3mm; }
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
td, th { vertical-align: top; padding: 1.1mm 2mm 1.1mm 0; }
.vocab th { font-size: 8.5pt; text-transform: uppercase; letter-spacing: .05em;
            text-align: left; border-bottom: 1px solid #000; padding-bottom: 1mm; }
.vocab td { padding-top: 1.6mm; padding-bottom: 1.6mm; }
.vocab tr td { border-bottom: 1px dotted #999; }
.vocab .w { width: 22%; }
.vocab .a { width: 6%; }
.vocab .m { width: 44%; }
.vocab .l { width: 28%; padding-right: 0; }
.tf td:first-child { width: 6%; }
.tf td:last-child { width: 16%; text-align: right; white-space: nowrap; }
.grid td { border: 1px solid #000; padding: 1.6mm 2mm; }
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

.take { border-top: 1.4px dashed #000; margin-top: 4.5mm; padding-top: 2.5mm; }
.take h2 { font-size: 10.5pt; text-transform: uppercase; letter-spacing: .07em;
           margin: 0 0 2mm; }
.take .cols { display: flex; gap: 5mm; }
.take .cols > div { flex: 1; border: 1.2px solid #000; padding: 2.5mm 3mm;
                    font-size: 9.5pt; }
.take .cols h3 { margin: 0 0 1.5mm; font-size: 9pt; text-transform: uppercase;
                 letter-spacing: .06em; }
.take .help b { display: inline-block; min-width: 46mm; }

.foot { border-top: 1px solid #000; margin-top: 3.5mm; padding-top: 1.5mm;
        font-size: 8pt; overflow: hidden; }
.foot .pg { float: right; }
.line { display: inline-block; border-bottom: 1px solid #000; height: 4.5mm;
        min-width: 26mm; vertical-align: bottom; }
.line.s { min-width: 15mm; }
.line.f { min-width: 100%; }
.line.l { min-width: 60mm; }
"""

def header(num, title, cont=False):
    tag = f'<span class="cont">Handout {num} &middot; page 2</span>' if cont else ''
    sub = '' if cont else f'<div class="series">Filling In the Form &nbsp;&middot;&nbsp; Handout {num}</div>'
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

def foot(page):
    return ('<div class="foot"><span class="pg">Page ' + str(page) + ' of '
            + str(TOTAL_PAGES) + '</span>Adapted from the Census Household Form, '
            '&copy; Commonwealth of Australia 2026, Australian Bureau of Statistics. '
            'Classroom practice material &mdash; not an official ABS product.</div>')

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

pages = []

# ══════════════════════════════════════════════════════════════════ HANDOUT 1
look1 = """
<div class="excerpt">
<p><b>It&rsquo;s time to complete your Census.</b></p>
<p>Census night is Tuesday 11 August 2026. Everybody at this address on Census
night must be included on this Census form, including visitors and babies.</p>
<p>The information you provide is used to make important decisions about
transport, schools, health care and infrastructure.</p>
<p class="src">Census Household Form, page 1</p>
</div>
<p class="q">What can you see? Talk with a partner. What is this paper?</p>
"""

words1 = vocab([
    ("census", "a &nbsp; you must do it &mdash; it is the law"),
    ("household", "b &nbsp; a count of all the people in Australia"),
    ("form", "c &nbsp; put a person&rsquo;s name on the form"),
    ("include", "d &nbsp; secret &mdash; nobody can see your name"),
    ("visitor", "e &nbsp; a paper with questions and boxes"),
    ("compulsory", "f &nbsp; all the people who live in one home"),
    ("confidential", "g &nbsp; send the form back"),
    ("return", "h &nbsp; a person who stays for a night, but does not live here"),
]) + """Write your own language in the last column.</p>
<div class="aside"><b>&#8595; More support:</b> do the first five words only.
&nbsp;&nbsp; <b>&#8593; More challenge:</b> write one sentence with
<i>compulsory</i> and one with <i>confidential</i>.</div>
"""

und1 = """
<p>Read the form again, and the Questions page. Circle <b>TRUE</b> or <b>FALSE</b>.</p>
<table class="tf">
<tr><td>1</td><td>Census night is Tuesday 11 August 2026.</td><td>TRUE / FALSE</td></tr>
<tr><td>2</td><td>Only Australian citizens are on the form.</td><td>TRUE / FALSE</td></tr>
<tr><td>3</td><td>Babies are on the form.</td><td>TRUE / FALSE</td></tr>
<tr><td>4</td><td>The Census is compulsory.</td><td>TRUE / FALSE</td></tr>
<tr><td>5</td><td>The ABS can tell your neighbour your answers.</td><td>TRUE / FALSE</td></tr>
<tr><td>6</td><td>You can do the Census on the internet.</td><td>TRUE / FALSE</td></tr>
<tr><td>7</td><td>Visitors are on the form.</td><td>TRUE / FALSE</td></tr>
</table>
"""

pages.append(header(1, "Census night is Tuesday 11 August")
             + sec("A", "Look", "3 min", look1)
             + sec("B", "Words", "12 min", words1)
             + sec("C", "Understand", "8 min", und1) + foot(1))

prac1 = """
<p><b>1. The date.</b> Complete the sentence.</p>
<p style="margin-left:6mm">Census night is <span class="line"></span>day,
<span class="line s"></span> August <span class="line s"></span> .</p>
<p><b>2. The calendar.</b> This is August 2026. Circle Census night.</p>
<table class="grid" style="width:78mm; text-align:center">
<tr><th>M</th><th>T</th><th>W</th><th>T</th><th>F</th><th>S</th><th>S</th></tr>
<tr><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr>
<tr><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td></tr>
</table>
<p style="margin-left:6mm">Today is <span class="line"></span> .
How many days until Census night? <span class="line s"></span></p>
<p><b>3. Listen and write the number.</b> Your teacher will say each number twice.</p>
<p style="margin-left:6mm">Census help line <span class="line l"></span><br>
Interpreter (TIS National) <span class="line l"></span><br>
Paper form request <span class="line l"></span></p>
<p><b>4. Ask three people in the class.</b> Then change partners and ask again.</p>
<p style="margin-left:6mm"><i>When is Census night?</i> &nbsp;&mdash;&nbsp;
<i>What is the Census?</i> &nbsp;&mdash;&nbsp; <i>Is it compulsory?</i></p>
"""

do1 = """
<p>On Census night, these people were at 12 Graham Avenue.
Tick <b>&#10003;</b> the people who <b>must be on this form</b>.</p>
<table class="grid">
<tr><td style="width:8%">1</td><td>Amal Haddad. She lives here. She slept here.</td>
    <td style="width:12%">&nbsp;</td></tr>
<tr><td>2</td><td>Sara, a friend from Melbourne. She slept here for one night.</td><td>&nbsp;</td></tr>
<tr><td>3</td><td>Sami, a baby. He was born last week. He lives here.</td><td>&nbsp;</td></tr>
<tr><td>4</td><td>Tomas. He works at night. He was at work, and he came home
    on Wednesday morning. He is not on another form.</td><td>&nbsp;</td></tr>
<tr><td>5</td><td>The postman. He came to the door on Wednesday at 9am.</td><td>&nbsp;</td></tr>
<tr><td>6</td><td>Nadia. She slept at her cousin&rsquo;s house. She is on her
    cousin&rsquo;s form.</td><td>&nbsp;</td></tr>
</table>
<div class="aside"><b>&#8593; More challenge:</b> why is number 4 on the form?
Find the rule on page 3 of the Census form.</div>
"""

pages.append(header(1, "Census night is Tuesday 11 August", cont=True)
             + sec("D", "Practise", "15 min", prac1)
             + sec("E", "Do it", "10 min", do1) + TAKE + foot(2))

# ══════════════════════════════════════════════════════════════════ HANDOUT 2
look2 = f"""
<div class="excerpt">
<p><b>How to write your answers</b></p>
<p>&bull;&nbsp; Use a blue or black pen only.</p>
<p>&bull;&nbsp; Mark response boxes, like this: {MK}&#10007;</p>
<p>&bull;&nbsp; Use CAPITAL letters and only use one letter per box.</p>
<p>&bull;&nbsp; Remember to leave a space between words, like this:</p>
<p style="margin-left:6mm">{bxw(6, 3)}</p>
<p>&bull;&nbsp; If you make a mistake, draw a line through the box.</p>
<p class="src">Census Household Form, page 1</p>
</div>
<p class="q">Look at the boxes. How many letters go in one box?</p>
"""

words2 = vocab([
    ("capital letters", "a &nbsp; A B C, not a b c"),
    ("box", "b &nbsp; a small square for one letter"),
    ("mark", "c &nbsp; put a cross in the box"),
    ("mistake", "d &nbsp; something wrong"),
    ("a space", "e &nbsp; one empty box between two words"),
    ("specify", "f &nbsp; write the answer in your own words"),
    ("leave blank", "g &nbsp; write nothing &mdash; this question is not for you"),
    ("Go to 19", "h &nbsp; do not answer the next questions &mdash; jump to question 19"),
]) + "Write your own language in the last column.</p>"

und2 = f"""
<p>Look at each example. Is it <b>right &#10003;</b> or <b>wrong &#10007;</b>?
If it is wrong, say why.</p>
<table class="grid">
<tr><td style="width:58%">{bxw(4,5)}</td>
    <td style="width:12%">&nbsp;</td><td>Why?</td></tr>
<tr><td>written in small letters: <i>john smith</i></td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>two letters in one box</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>no empty box between the two words</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>written in pencil</td><td>&nbsp;</td><td>&nbsp;</td></tr>
</table>
"""

pages.append(header(2, "How to write your answers")
             + sec("A", "Look", "3 min", look2)
             + sec("B", "Words", "12 min", words2)
             + sec("C", "Understand", "8 min", und2) + foot(3))

prac2 = f"""
<p><b>1. Write these words in the boxes.</b> One letter in one box. CAPITAL letters.</p>
<p><span class="lbl">MARY</span>{bx(8)}</p>
<p><span class="lbl">JOHN SMITH</span>{bx(16)}</p>
<p><span class="lbl">GRAHAM AVENUE</span>{bx(18)}</p>
<p><b>2. A mistake.</b> This person wrote <i>SMITT</i>. The name is <i>SMITH</i>.
Draw a line through the wrong box and write the correct letter.</p>
<p style="margin-left:6mm">{bx(8)}</p>
<p><b>3. Mark the box.</b> Put a cross {MK} next to the correct answer.</p>
<p style="margin-left:6mm">{MK} Use a blue or black pen &nbsp;&nbsp;&nbsp;
{MK} Use a pencil &nbsp;&nbsp;&nbsp; {MK} Use a red pen</p>
<p><b>4. Ask your partner.</b></p>
<p style="margin-left:6mm"><i>Do I write big letters or small letters?</i>
&nbsp;&mdash;&nbsp; <i>Do I mark one box or all the boxes?</i>
&nbsp;&mdash;&nbsp; <i>Could you show me where to write the answer?</i></p>
<div class="aside"><b>&#8595; More support:</b> do part 1 only. Copy the words slowly.
&nbsp;&nbsp; <b>&#8593; More challenge:</b> write your street name in the boxes,
then check it with a partner.</div>
"""

do2 = f"""
<p>Write these names from the Haddad household in the boxes.
The Census form asks for the first name and the family name in different boxes.</p>
<p><span class="lbl">First or given name &mdash; AMAL</span>{bx(14)}</p>
<p><span class="lbl">Surname or family name &mdash; HADDAD</span>{bx(14)}</p>
<p><span class="lbl">First or given name &mdash; TOMAS</span>{bx(14)}</p>
<p><span class="lbl">Surname or family name &mdash; SILVA</span>{bx(14)}</p>
<p class="crit">Check your work:
<span>&#9744; CAPITAL letters</span>
<span>&#9744; one letter per box</span>
<span>&#9744; a space between words</span></p>
<div class="warn"><b>This page is yours.</b> If you write your own name, keep this
page and take it home. Do not give it to the teacher.</div>
"""

pages.append(header(2, "How to write your answers", cont=True)
             + sec("D", "Practise", "15 min", prac2)
             + sec("E", "Do it", "10 min", do2) + TAKE + foot(4))

# ══════════════════════════════════════════════════════════════════ HANDOUT 3
look3 = f"""
<div class="excerpt">
<p><span class="qn">1</span><b>What is the address of this dwelling?</b>
<span style="font-size:9.5pt">Please use CAPITAL letters only.</span></p>
<p><span class="lbl">Apartment/Flat/Unit number (if any)</span>{bx(6)}</p>
<p><span class="lbl">Street number (examples: 1&ndash;9, LOT 37)</span>{bx(8)}</p>
<p><span class="lbl">Street name (examples: GRAHAM AVENUE, GEORGE STREET)</span>{bx(20)}</p>
<p><span class="lbl">Suburb/Locality</span>{bx(20)}</p>
<p><span class="lbl">State/Territory &nbsp;&nbsp; Postcode</span>{bx(3)}
&nbsp;&nbsp;&nbsp;{bx(4)}</p>
<p class="src">Census Household Form, Question 1</p>
</div>
<p class="q">Which box is the biggest? Why?</p>
"""

words3 = vocab([
    ("street number", "a &nbsp; the small town, or the part of a city, where you live"),
    ("street name", "b &nbsp; 12, or 3A, or LOT 37"),
    ("suburb / locality", "c &nbsp; four numbers, for example 2165"),
    ("state / territory", "d &nbsp; GRAHAM AVENUE, GEORGE STREET"),
    ("postcode", "e &nbsp; your home number in a big building"),
    ("unit / flat / apartment", "f &nbsp; NSW, VIC, QLD, SA, WA, TAS, NT, ACT"),
    ("dwelling", "g &nbsp; the Census word for a home"),
    ("usual address", "h &nbsp; the place where you live for six months or more"),
]) + "Write your own language in the last column.</p>"

und3 = """
<p>Look at this address. Write the name of each part.</p>
<table class="grid">
<tr><td style="width:45%">UNIT 4</td><td><span class="line l"></span></td></tr>
<tr><td>12</td><td><span class="line l"></span></td></tr>
<tr><td>GRAHAM AVENUE</td><td><span class="line l"></span></td></tr>
<tr><td>FAIRFIELD</td><td><span class="line l"></span></td></tr>
<tr><td>NSW</td><td><span class="line l"></span></td></tr>
<tr><td>2165</td><td><span class="line l"></span></td></tr>
</table>
"""

pages.append(header(3, "Where do you live?")
             + sec("A", "Look", "3 min", look3)
             + sec("B", "Words", "12 min", words3)
             + sec("C", "Understand", "8 min", und3) + foot(5))

prac3 = """
<p><b>1. States and territories.</b> Match the short form to the long name.</p>
<table class="plain">
<tr><td>NSW &nbsp; VIC &nbsp; QLD &nbsp; SA</td>
    <td>South Australia &nbsp;&bull;&nbsp; Queensland &nbsp;&bull;&nbsp; New South Wales
        &nbsp;&bull;&nbsp; Victoria</td></tr>
<tr><td>WA &nbsp; TAS &nbsp; NT &nbsp; ACT</td>
    <td>Tasmania &nbsp;&bull;&nbsp; Australian Capital Territory
        &nbsp;&bull;&nbsp; Western Australia &nbsp;&bull;&nbsp; Northern Territory</td></tr>
</table>
<p style="margin-left:6mm">Which one is your state? <span class="line"></span></p>
<p><b>2. Put it in order.</b> These lines are mixed up. Number them 1&ndash;5
in the correct order for the form.</p>
<p style="margin-left:6mm">
<span class="line s"></span> 3068 &nbsp;&nbsp;
<span class="line s"></span> VIC &nbsp;&nbsp;
<span class="line s"></span> 88 &nbsp;&nbsp;
<span class="line s"></span> CLIFTON HILL &nbsp;&nbsp;
<span class="line s"></span> QUEENS PARADE</p>
<p><b>3. Find the mistakes.</b> A neighbour wrote this. Three things are wrong.
Circle them and say why.</p>
<table class="grid" style="width:80%">
<tr><td style="width:45%">Street number</td><td>graham avenue</td></tr>
<tr><td>Street name</td><td>12</td></tr>
<tr><td>Suburb/Locality</td><td>FAIRFIELD</td></tr>
<tr><td>State/Territory</td><td>NEW SOUTH WALES</td></tr>
<tr><td>Postcode</td><td>2165</td></tr>
</table>
<p><b>4. Partner dictation.</b> Your teacher will give you a card with an address.
Say it to your partner. Your partner writes it. Then change.</p>
<div class="warn">Use the address on the card, <b>not</b> your own address.</div>
"""

do3 = f"""
<p>The Haddad household lives at <b>Unit 4, 12 Graham Avenue, Fairfield NSW 2165</b>.
Write their address in the Question 1 boxes.</p>
<p><span class="lbl">Apartment/Flat/Unit number (if any)</span>{bx(6)}</p>
<p><span class="lbl">Street number</span>{bx(8)}</p>
<p><span class="lbl">Street name</span>{bx(20)}</p>
<p><span class="lbl">Suburb/Locality</span>{bx(20)}</p>
<p><span class="lbl">State/Territory &nbsp;&nbsp;&nbsp; Postcode</span>{bx(3)}
&nbsp;&nbsp;&nbsp;{bx(4)}</p>
<p class="crit">Check your work:
<span>&#9744; CAPITAL letters</span>
<span>&#9744; one letter per box</span>
<span>&#9744; the right information in the right box</span></p>
<div class="aside"><b>&#8593; More challenge:</b> invent an address for a new
household. Give it to a partner to write in the boxes.
&nbsp;&nbsp; The form has a special rule: a person with no address writes
<b>NONE</b> in <i>Suburb/Locality</i>. Find it on page 6.</div>
"""

pages.append(header(3, "Where do you live?", cont=True)
             + sec("D", "Practise", "15 min", prac3)
             + sec("E", "Do it", "10 min", do3) + TAKE + foot(6))

# ══════════════════════════════════════════════════════════════════ HANDOUT 4
look4 = f"""
<div class="excerpt">
<p><span class="qn">2</span><b>Who spent the night of Tuesday 11 August 2026 in
this dwelling?</b> Mark all that apply.</p>
<p style="margin-left:5mm">{MK} Me &nbsp;&nbsp; {MK} Spouse/partner<br>
{MK} Babies, children and teenagers &nbsp;&nbsp; {MK} Other adult family members<br>
{MK} Unrelated housemates, flatmates or boarders<br>
{MK} Visitors or friends who spent the night</p>
<p><span class="qn">3</span><b>In total, how many people spent the night
&hellip; in this dwelling?</b> &nbsp;{bx(2)}</p>
<p><span class="qn">5</span><b>In total, how many people were away &hellip;
but usually live in this dwelling?</b> &nbsp;{MK} No one away &nbsp; OR &nbsp;{bx(2)}</p>
<p class="src">Census Household Form, Questions 2, 3 and 5</p>
</div>
"""

words4 = vocab([
    ("spent the night", "a &nbsp; slept here on Tuesday 11 August"),
    ("usually lives here", "b &nbsp; not here on Census night"),
    ("away", "c &nbsp; this is their home for six months or more"),
    ("visitor", "d &nbsp; husband, wife or partner"),
    ("spouse / partner", "e &nbsp; a person who stays one night"),
    ("housemate", "f &nbsp; a person who pays to live in one room in your home"),
    ("boarder", "g &nbsp; a person who shares the home, but is not family"),
    ("shift worker", "h &nbsp; a person who works at night"),
]) + "Write your own language in the last column.</p>"

und4 = """
<div class="rule">
<h3>Two rules</h3>
<p><b>PRESENT</b> &mdash; the person <b>slept here</b> on Tuesday 11 August.
It does not matter if they live here or not.<br>
<span class="note">Also present: a person who lives here, was at work all night,
and came home on Wednesday &mdash; if they are not on another form.</span></p>
<p style="margin:0"><b>AWAY</b> &mdash; the person <b>usually lives here</b>,
but slept somewhere else on Tuesday 11 August.</p>
</div>
<p>Which question? Write <b>2</b>, <b>3</b>, <b>4</b> or <b>5</b>.</p>
<table class="tf">
<tr><td>a</td><td>How many people slept here?</td><td><span class="line s"></span></td></tr>
<tr><td>b</td><td>How many people were away?</td><td><span class="line s"></span></td></tr>
<tr><td>c</td><td>Was a visitor here?</td><td><span class="line s"></span></td></tr>
<tr><td>d</td><td>Is someone on holiday overseas?</td><td><span class="line s"></span></td></tr>
</table>
"""

pages.append(header(4, "Who is in your house?")
             + sec("A", "Look", "3 min", look4)
             + sec("B", "Words", "12 min", words4)
             + sec("C", "Understand", "8 min", und4) + foot(7))

prac4 = """
<p>It is Tuesday 11 August 2026 at Unit 4, 12 Graham Avenue, Fairfield.
Write <b>P</b> (present), <b>A</b> (away) or <b>N</b> (not on this form).</p>
<table class="grid">
<tr><td style="width:6%">1</td><td>Amal Haddad, 41. She lives here. She slept here.</td>
    <td style="width:10%">&nbsp;</td></tr>
<tr><td>2</td><td>Yusuf Haddad, 44. Amal&rsquo;s husband. He slept here.</td><td>&nbsp;</td></tr>
<tr><td>3</td><td>Layla Haddad, 12. She lives here. She slept here.</td><td>&nbsp;</td></tr>
<tr><td>4</td><td>Rana Haddad, 68. Amal&rsquo;s mother. She lives here. She slept here.</td><td>&nbsp;</td></tr>
<tr><td>5</td><td>Nadia Haddad, 6. She lives here, but she slept at her
    cousin&rsquo;s house. She is on her cousin&rsquo;s form.</td><td>&nbsp;</td></tr>
<tr><td>6</td><td>Tomas Silva, 29. He is a boarder. He worked all night and came
    home on Wednesday morning. He is not on another form.</td><td>&nbsp;</td></tr>
<tr><td>7</td><td>Sara Okafor, 30. A friend from Melbourne. She slept here for one night.</td><td>&nbsp;</td></tr>
<tr><td>8</td><td>Karim Haddad, 25. Yusuf&rsquo;s cousin. He usually lives here,
    but he is on holiday in Lebanon.</td><td>&nbsp;</td></tr>
<tr><td>9</td><td>Rana&rsquo;s brother. He came for dinner and went home at 9pm.</td><td>&nbsp;</td></tr>
</table>
<p class="note"><b>Talk about it.</b> Numbers 6 and 9 were both here on Tuesday.
Why is one on the form, and one not? Ask your partner:
<i>Does this person usually live here?</i> &nbsp;
<i>Did this person sleep here?</i></p>
"""

do4 = f"""
<p>Now complete the form for the Haddad household.</p>
<p><b>Question 2</b> &mdash; who spent the night? Mark all that apply.</p>
<p style="margin-left:5mm">{MK} Me &nbsp;&nbsp; {MK} Spouse/partner &nbsp;&nbsp;
{MK} Babies, children and teenagers<br>{MK} Other adult family members &nbsp;&nbsp;
{MK} Unrelated housemates, flatmates or boarders<br>
{MK} Visitors or friends who spent the night</p>
<p><b>Question 3</b> &mdash; in total, how many people spent the night? &nbsp;{bx(2)}</p>
<p><b>Question 5</b> &mdash; in total, how many people were away? &nbsp;
{MK} No one away &nbsp; OR &nbsp;{bx(2)}</p>
<p class="crit">Check your work:
<span>&#9744; the numbers match your P and A answers</span>
<span>&#9744; every kind of person is marked in Question 2</span></p>
<div class="aside"><b>&#8593; More challenge:</b> the form has room for six people,
and the Haddads have exactly six people present. What must a household with eight
people do? Find the answer on page 3 of the form.</div>
"""

pages.append(header(4, "Who is in your house?", cont=True)
             + sec("D", "Practise", "15 min", prac4)
             + sec("E", "Do it", "10 min", do4) + TAKE + foot(8))

html = ('<meta charset="utf-8">\n'
        '<title>Filling In the Form &mdash; Handouts 1&ndash;4</title>\n'
        f'<style>{CSS}</style>\n'
        + '\n'.join(f'<div class="page">{p}</div>' for p in pages))

import pathlib
out = pathlib.Path('/home/user/URANTiOS/esl/census-2026/handouts/census-esl-handouts-1-4.html')
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(html)
print(f'{out} — {len(html)} bytes, {len(pages)} A4 pages')
