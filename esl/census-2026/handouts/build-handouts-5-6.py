#!/usr/bin/env python3
"""Session 2 (Monday 10 August): Handouts 5 and 6, plus the readiness checklist."""

import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _common import bx, MK, CSS, header, sec, vocab, make_foot, TAKE, document

foot = make_foot(5)
pages = []

# ══════════════════════════════════════════════════════════════════ HANDOUT 5
look5 = f"""
<div class="excerpt">
<p><b>The Census form has 65 questions and 26 pages. You do not answer all of them.</b></p>
<table style="font-size:10pt; margin:0">
<tr><td style="width:26%"><b>Pages 3&ndash;5</b></td>
    <td>Who is in the house &mdash; Questions 2 to 12</td></tr>
<tr><td><b>Pages 6&ndash;13</b></td>
    <td>Each person: address, country, language, health &mdash; Questions 13 to 29</td></tr>
<tr><td><b>Pages 14&ndash;21</b></td>
    <td>Each person: school, work, travel &mdash; Questions 30 to 51</td></tr>
<tr><td><b>Pages 22&ndash;23</b></td>
    <td>Each person: unpaid work and care &mdash; Questions 52 to 57</td></tr>
<tr><td><b>Page 24</b></td><td>People who were away &mdash; Questions 58 and 59</td></tr>
<tr><td><b>Page 25</b></td><td>The home itself &mdash; Questions 60 to 65</td></tr>
</table>
<p class="src">Census Household Form, pages 3&ndash;25</p>
</div>
<p class="q">Open the form. Find the six columns: Person 1, Person 2, Person 3&hellip;
Each person has their own column. Every question is asked six times.</p>
"""

words5 = vocab([
    ("question number", "a &nbsp; do not answer this question &mdash; jump forward"),
    ("column", "b &nbsp; the number at the start of each question: 1, 2, 3&hellip;"),
    ("Go to 19", "c &nbsp; you can choose &mdash; you do not have to answer"),
    ("mark one box", "d &nbsp; the tall part of the page for one person"),
    ("mark all that apply", "e &nbsp; choose one answer only"),
    ("specify", "f &nbsp; choose every answer that is true"),
    ("optional", "g &nbsp; write the answer in your own words"),
    ("leave blank", "h &nbsp; write nothing here"),
]) + "Write your own language in the last column.</p>"

und5 = """
<p><b>Find it fast.</b> Use the form. Write the question number.</p>
<table class="tf">
<tr><td>a</td><td>Which language do you use at home?</td><td><span class="line s"></span></td></tr>
<tr><td>b</td><td>How did you get to work?</td><td><span class="line s"></span></td></tr>
<tr><td>c</td><td>How many bedrooms?</td><td><span class="line s"></span></td></tr>
<tr><td>d</td><td>Which country were you born in?</td><td><span class="line s"></span></td></tr>
<tr><td>e</td><td>What is your religion?</td><td><span class="line s"></span></td></tr>
<tr><td>f</td><td>How many cars?</td><td><span class="line s"></span></td></tr>
</table>
<div class="rule">
<h3>Three questions you do not have to answer</h3>
<p style="margin:0"><b>Question 24 &mdash; religion.</b> The form says
<b>OPTIONAL</b>. You can leave it blank.<br>
<b>Question 9 &mdash; gender</b> and <b>Question 57 &mdash; sexual orientation</b>
both have a box that says <b>Prefer not to answer</b>. They are for people aged
16 and over.<br>
<span class="note">Every other question should be answered. If a question is
difficult, call 1800 181 227 &mdash; do not guess.</span></p>
</div>
"""

pages.append(header(5, "Going through the form")
             + sec("A", "Look", "5 min", look5)
             + sec("B", "Words", "12 min", words5)
             + sec("C", "Understand", "10 min", und5) + foot(1))

prac5 = f"""
<p><b>1. Follow the arrow.</b> The form tells you when to skip questions.
Where do you go next?</p>
<table class="grid">
<tr><td style="width:62%">Question 17: you were born in <b>Australia</b></td>
    <td>Go to question <span class="line s"></span></td></tr>
<tr><td>Question 21: you speak <b>English only</b> at home</td>
    <td>Go to question <span class="line s"></span></td></tr>
<tr><td>Question 30: you are <b>not</b> at school</td>
    <td>Go to question <span class="line s"></span></td></tr>
<tr><td>Question 38: you did <b>not</b> have a job last week</td>
    <td>Go to question <span class="line s"></span></td></tr>
<tr><td>Question 58: <b>no one</b> was away</td>
    <td>Go to question <span class="line s"></span></td></tr>
</table>
<p><b>2. One box or all the boxes?</b> Write <b>1</b> or <b>ALL</b>.</p>
<table class="tf">
<tr><td>a</td><td>Question 11 &mdash; marital status</td><td><span class="line s"></span></td></tr>
<tr><td>b</td><td>Question 23 &mdash; ancestry</td><td><span class="line s"></span></td></tr>
<tr><td>c</td><td>Question 29 &mdash; long-term health conditions</td><td><span class="line s"></span></td></tr>
<tr><td>d</td><td>Question 48 &mdash; how you got to work</td><td><span class="line s"></span></td></tr>
<tr><td>e</td><td>Question 62 &mdash; is this home owned or rented?</td><td><span class="line s"></span></td></tr>
</table>
<p><b>3. Find the mistakes.</b> Someone filled in this part for Tomas. Three
things are wrong. Circle them.</p>
<table class="grid" style="width:88%">
<tr><td style="width:52%">Q6 &nbsp; First name</td><td>tomas</td></tr>
<tr><td>Q7 &nbsp; Date of birth</td><td>14 / 06 / 1997 &nbsp;&nbsp; Age: 45</td></tr>
<tr><td>Q17 &nbsp; Country of birth</td><td>Brazil &mdash; and Q18 left blank</td></tr>
<tr><td>Q22 &nbsp; How well do you speak English?</td><td>Well</td></tr>
</table>
"""

do5 = f"""
<p>Complete this part of the form for <b>Person 6 &mdash; Tomas Silva</b>, the boarder.
He is 29. He was born in Brazil and came to Australia in 2019. At home he speaks
Portuguese. He speaks English well.</p>
<p><span class="lbl">Q6 &nbsp; First or given name</span>{bx(14)}</p>
<p><span class="lbl">Q6 &nbsp; Surname or family name</span>{bx(14)}</p>
<p><span class="lbl">Q7 &nbsp; Age &nbsp;&nbsp; years</span>{bx(3)}</p>
<p><span class="lbl">Q10 &nbsp; Relationship to Person 1</span>
{MK} Child of Person 1 &nbsp;&nbsp; {MK} Unrelated flatmate or co-tenant of Person 1
&nbsp;&nbsp; {MK} Other relationship (specify)</p>
<p><span class="lbl">Q17 &nbsp; Country of birth</span>
{MK} Australia &nbsp; {MK} England &nbsp; {MK} New Zealand &nbsp; {MK} India
&nbsp; {MK} Other (specify) {bx(10)}</p>
<p><span class="lbl">Q18 &nbsp; Year first arrived in Australia</span>{bx(4)}</p>
<p><span class="lbl">Q21 &nbsp; Language other than English at home</span>
{MK} No, English only &nbsp;&nbsp; {MK} Yes, other language (specify) {bx(12)}</p>
<p><span class="lbl">Q22 &nbsp; How well does the person speak English?</span>
{MK} Very well &nbsp; {MK} Well &nbsp; {MK} Not well &nbsp; {MK} Not at all</p>
<p class="crit">Check your work:
<span>&#9744; CAPITAL letters</span>
<span>&#9744; one box only</span>
<span>&#9744; nothing left blank by mistake</span></p>
"""

pages.append(header(5, "Going through the form", cont=True)
             + sec("D", "Practise", "18 min", prac5)
             + sec("E", "Do it", "12 min", do5) + TAKE + foot(2))

# ══════════════════════════════════════════════════════════════════ HANDOUT 6
look6 = """
<div class="excerpt">
<p><b>Need help to complete your Census?</b></p>
<p>We are here to help. Go to www.census.abs.gov.au/help for frequently asked
questions, self-service options and information about getting help in person.
You can also call us on <b>1800 181 227</b>.</p>
<p><b>Language support.</b> To access in-language support, you can contact the
Translating and Interpreting Service (TIS National) on <b>131 450</b>.</p>
<p><b>National Relay Service.</b> If you are deaf, hard of hearing and/or have a
speech or communication difficulty, you can contact us through the National
Relay Service.</p>
<p class="src">Census Household Form, page 26</p>
</div>
"""

words6 = vocab([
    ("help line", "a &nbsp; a person who changes your language into English"),
    ("interpreter", "b &nbsp; a telephone number to call for help"),
    ("Census number", "c &nbsp; the number on the front of your form"),
    ("temporary password", "d &nbsp; a short password, to use one time"),
    ("online", "e &nbsp; on the internet"),
    ("paper form", "f &nbsp; the Census on paper, in an envelope"),
    ("unoccupied", "g &nbsp; nobody lives here / nobody is here"),
    ("submit", "h &nbsp; send your finished form to the ABS"),
]) + "Write your own language in the last column.</p>"

und6 = """
<p><b>What should they do?</b> Match the problem to the answer.</p>
<table class="plain">
<tr><td>1 &nbsp; There are eight people in the house.</td>
    <td>a &nbsp; Call 1800 181 227 and ask for another form or another Census number.</td></tr>
<tr><td>2 &nbsp; Nobody will be home on Census night.</td>
    <td>b &nbsp; Call TIS National on 131 450.</td></tr>
<tr><td>3 &nbsp; My sister wants her own private form.</td>
    <td>c &nbsp; Do the Census online, or call 1800 130 250 for an extra paper form.</td></tr>
<tr><td>4 &nbsp; I don&rsquo;t understand the English.</td>
    <td>d &nbsp; Go to census.abs.gov.au/help or call 1800 181 227 to tell them.</td></tr>
<tr><td>5 &nbsp; I did the Census online. What about the paper form?</td>
    <td>e &nbsp; Recycle it.</td></tr>
</table>
<p class="note">Answers: <span class="line s"></span>
<span class="line s"></span> <span class="line s"></span>
<span class="line s"></span> <span class="line s"></span></p>
"""

pages.append(header(6, "Getting help, and being ready")
             + sec("A", "Look", "4 min", look6)
             + sec("B", "Words", "12 min", words6)
             + sec("C", "Understand", "10 min", und6) + foot(3))

prac6 = """
<div class="rule">
<h3>Useful sentences</h3>
<p style="margin:0">
<i>Hello. I need some help with my Census form.</i><br>
<i>I need an interpreter who speaks</i> <span class="line s"></span> .<br>
<i>Could you say that again, please?</i> &nbsp;&nbsp;
<i>Could you explain that in easier English?</i><br>
<i>Could you show me where to write the answer?</i><br>
<i>Do I mark one box, or all the boxes?</i> &nbsp;&nbsp;
<i>Is this question compulsory or optional?</i><br>
<i>Let me check that I understood. You said</i> <span class="line s"></span> .<br>
<i>Thank you. That&rsquo;s all I need.</i></p>
</div>
<p><b>Role-play.</b> Student A calls the help line. Student B answers.
Do it three times, with three different partners. Each time, use fewer notes.</p>
<table class="grid">
<tr><th style="width:50%">Student A &mdash; you are calling</th>
    <th>Student B &mdash; you work at the help line</th></tr>
<tr><td><b>Call 1.</b> There are nine people in your house on Census night.</td>
    <td>Tell them to do it online, or call 1800 130 250 for an extra form.</td></tr>
<tr><td><b>Call 2.</b> You do not understand the questions in English.</td>
    <td>Tell them about TIS National, 131 450.</td></tr>
<tr><td><b>Call 3.</b> You will be away on holiday on Census night, and the
    house will be empty.</td>
    <td>Tell them to go to census.abs.gov.au/help, or call 1800 181 227.</td></tr>
</table>
<div class="aside"><b>&#8595; More support:</b> read the sentences from the box.
&nbsp;&nbsp; <b>&#8593; More challenge:</b> close the handout. Student B asks one
extra question that is not on the card.</div>
"""

do6 = """
<p>This is your plan for next week. Tick each one when it is true.
<b>Take this page home.</b></p>
<div class="ck">
<p class="big" style="margin:0 0 1.5mm">Before Tuesday</p>
<ul>
<li>I know Census night is <b>Tuesday 11 August 2026</b>.</li>
<li>I have my Census form, or my Census number and password for online.</li>
<li>I know who will sleep in my home on Tuesday night.</li>
<li>I have a blue or black pen.</li>
<li>If I need an interpreter, I know to call <b>131 450</b>.</li>
</ul>
<p class="big" style="margin:0 0 1.5mm">On Tuesday night and after</p>
<ul>
<li>I count <b>everyone</b> who sleeps in my home &mdash; family, babies, visitors.</li>
<li>I write in <b>CAPITAL letters</b>, one letter in one box.</li>
<li>I answer for every person, in their own column.</li>
<li>I do the Census <b>online</b>, or post the paper form in the Reply Paid envelope.</li>
<li>If I do it online, I recycle the paper form.</li>
<li>If I am not sure about something, I call <b>1800 181 227</b>. I do not guess.</li>
</ul>
</div>
"""

pages.append(header(6, "Getting help, and being ready", cont=True)
             + sec("D", "Practise", "20 min", prac6)
             + sec("E", "Do it &mdash; my Census plan", "10 min", do6) + TAKE + foot(4))

# ══════════════════════════════════════════════════════════════ CHECKLIST A4
checklist = """
<div class="hdr"><div class="series">Filling In the Form</div>
<h1>My Census Plan &mdash; Tuesday 11 August 2026</h1></div>
<div class="ck">
<h2>Before Tuesday</h2>
<ul>
<li><span class="big">Census night is Tuesday 11 August 2026.</span></li>
<li>I have my Census form &mdash; or my <b>Census number</b> and <b>password</b> to do it online.</li>
<li>I know who will <b>sleep</b> in my home on Tuesday night.</li>
<li>I have a <b>blue or black pen</b>.</li>
<li>More than six people in the house? I do it online, or call <b>1800 130 250</b> for another form.</li>
<li>Nobody home on Tuesday? I tell the ABS: <b>census.abs.gov.au/help</b> or <b>1800 181 227</b>.</li>
</ul>
<h2>On Tuesday night</h2>
<ul>
<li>I count <b>everyone</b> who sleeps here &mdash; family, babies, visitors, boarders.</li>
<li>I do <b>not</b> count people who came to visit and went home.</li>
<li>I count someone who lives here, worked all night, and came home on Wednesday.</li>
<li>People who live here but slept somewhere else go in <b>Questions 58 and 59</b>.</li>
</ul>
<h2>Filling it in</h2>
<ul>
<li><b>CAPITAL LETTERS.</b> One letter in one box. A space between words.</li>
<li>Each person has their <b>own column</b>. Person 1 is the householder.</li>
<li>I follow the arrows: <b>Go to 19</b> means skip forward.</li>
<li>Question 24 (religion) is <b>optional</b>. I can leave it blank.</li>
<li>If I make a mistake, I draw a line through the box.</li>
</ul>
<h2>Finishing</h2>
<ul>
<li>I do it <b>online</b> at census.abs.gov.au &mdash; or post the paper form in the Reply Paid envelope.</li>
<li>If I do it online, I <b>recycle</b> the paper form.</li>
<li>If I am not sure, I <b>call &mdash; I do not guess</b>.</li>
</ul>
</div>
<div class="rule" style="margin-top:5mm">
<h3>Numbers to keep</h3>
<p style="margin:0" class="big">Census help &nbsp; 1800 181 227<br>
Interpreter &mdash; TIS National &nbsp; 131 450<br>
Extra paper form &nbsp; 1800 130 250</p>
<p style="margin:2mm 0 0" class="note">Deaf, hard of hearing, or a speech or
communication difficulty? Contact the ABS through the <b>National Relay Service</b>.</p>
</div>
"""

pages.append(checklist + foot(5))

out = pathlib.Path(__file__).parent / 'census-esl-handouts-5-6.html'
out.write_text(document(pages, 'Filling In the Form &mdash; Handouts 5&ndash;6 and Census Plan'))
print(f'{out} — {len(pages)} A4 pages')
