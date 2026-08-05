#!/usr/bin/env python3
"""Session 1 (Wednesday 5 August): Handouts 1-4."""

import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from answers import ANSWERS
from _common import bx, bxw, MK, header, sec, vocab, TAKE, document


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
             + sec("C", "Understand", "8 min", und1))

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
             + sec("E", "Do it", "10 min", do1) + TAKE)

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
    ("capital letters", "a &nbsp; something wrong"),
    ("box", "b &nbsp; one empty box between two words"),
    ("mark", "c &nbsp; A B C, not a b c"),
    ("mistake", "d &nbsp; do not answer the next questions &mdash; jump to question 19"),
    ("a space", "e &nbsp; put a cross in the box"),
    ("specify", "f &nbsp; a small square for one letter"),
    ("leave blank", "g &nbsp; write nothing &mdash; this question is not for you"),
    ("Go to 19", "h &nbsp; write the answer in your own words"),
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
             + sec("C", "Understand", "8 min", und2))

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
             + sec("E", "Do it", "10 min", do2) + TAKE)

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
             + sec("C", "Understand", "8 min", und3))

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
             + sec("E", "Do it", "10 min", do3) + TAKE)

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
             + sec("C", "Understand", "8 min", und4))

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
             + sec("E", "Do it", "10 min", do4) + TAKE)

# interleave: each handout's two pages, then its answer page(s)
_p, pages = pages, []
for i, n in enumerate([1, 2, 3, 4]):
    pages += _p[i * 2:i * 2 + 2] + ANSWERS[n]

out = pathlib.Path(__file__).parent / 'census-esl-handouts-1-4.html'
out.write_text(document(pages, 'Filling In the Form &mdash; Handouts 1&ndash;4'))
print(f'{out} — {len(pages)} A4 pages')
