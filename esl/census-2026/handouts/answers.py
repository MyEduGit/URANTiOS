#!/usr/bin/env python3
"""Answer pages. Every answer carries a short reason and a fuller one."""

from _common import header

def _table(rows):
    out = ('<table class="ans"><tr><th class="i"></th><th class="an">Answer</th>'
           '<th class="s">Why &mdash; simple</th>'
           '<th class="d">Why &mdash; in detail</th></tr>')
    for i, a, s, d in rows:
        out += (f'<tr><td class="i">{i}</td><td class="an">{a}</td>'
                f'<td class="s">{s}</td><td class="d">{d}</td></tr>')
    return out + '</table>'

def answers_page(num, title, blocks, part=None, of=None):
    """blocks: list of (section heading, rows)."""
    label = f'Handout {num} &mdash; Answers'
    if part:
        label += f' ({part} of {of})'
    head = (f'<div class="hdr"><div class="series">Filling In the Form '
            f'&nbsp;&middot;&nbsp; {label}</div><h1>{title}</h1></div>')
    intro = ('<p class="note"><b>Try the exercises first, then check.</b> '
             'Mark your own work. Every answer here has a short reason and a '
             'longer one &mdash; read the short one first.</p>')
    body = ''
    for heading, rows in blocks:
        body += f'<h2 class="ansh">{heading}</h2>' + _table(rows)
    return head + (intro if not part or part == 1 else '') + body


# ═══════════════════════════════════════════════════════════════════════════
# HANDOUT 1
# ═══════════════════════════════════════════════════════════════════════════
H1_B = [
 ("B. Words", [
  ("1 census", "b", "A count of all the people.",
   "The Census counts everyone in Australia on one night, so governments know how many people live where, and what they need."),
  ("2 household", "f", "Everyone in one home.",
   "A household is all the people who live together in one home. One form covers one household."),
  ("3 form", "e", "The paper with the questions.",
   "This form has 65 questions across 26 pages. You write your answers in the small boxes."),
  ("4 include", "c", "Put the person on the form.",
   "If you include someone, you write their name and answer the questions for them in their own column."),
  ("5 visitor", "h", "A guest who sleeps here.",
   "A visitor does not live here. But if they slept here on Census night, they go on this form, not their own."),
  ("6 compulsory", "a", "You must do it.",
   "The Census is required by law &mdash; the Census and Statistics Act 1905. Page 2 of the form says so."),
  ("7 confidential", "d", "Kept secret.",
   "The ABS must keep your information secure and cannot release it in a way that is likely to identify you."),
  ("8 return", "g", "Send it back.",
   "Post the paper form in the Reply Paid envelope &mdash; or do it online instead and recycle the paper."),
 ]),
 ("C. Understand", [
  ("1", "TRUE", "The form says this date.",
   "Census night is printed on the front page: Tuesday 11 August 2026."),
  ("2", "FALSE", "Everyone is counted.",
   "The Census counts everyone in Australia, including non-citizens and international visitors. Only foreign diplomats are left out."),
  ("3", "TRUE", "Babies count too.",
   "The front page says &lsquo;including visitors and babies&rsquo;. Age makes no difference."),
  ("4", "TRUE", "It is the law.",
   "Page 2 says the Census is compulsory, under the Census and Statistics Act 1905."),
  ("5", "FALSE", "Nobody can see your answers.",
   "The ABS is legally required not to release information in a way that is likely to identify an individual."),
  ("6", "TRUE", "You can use the internet.",
   "Go to census.abs.gov.au, then enter the Census number and temporary password from the front of the form."),
  ("7", "TRUE", "Visitors are included.",
   "Anyone who slept in the dwelling on Census night goes on the form, even for one night only."),
 ]),
 ("D. Practise", [
  ("1", "Tuesday, 11 August 2026", "The day, the date, the year.",
   "Say it as one phrase. In Australia the day comes before the month: 11 August, not August 11."),
  ("2", "11 is in the T column", "Second row, second column.",
   "The calendar columns are M T W T F S S. The first T is Tuesday, the second is Thursday."),
  ("3", "1800 181 227 &middot; 131 450 &middot; 1800 130 250",
   "Help &middot; interpreter &middot; extra form.",
   "Australians say these in groups: <i>eighteen hundred, one-eight-one, two-two-seven</i>. Ask for it digit by digit if you need to."),
  ("4", "No fixed answer", "Your own words.",
   "Aim for a full sentence: <i>Census night is Tuesday the eleventh of August.</i> Ask three different people."),
 ]),
 ("E. Do it", [
  ("1 Amal", "&#10003;", "She slept here.",
   "She lives here and spent the night. This is the simplest case on the form."),
  ("2 Sara", "&#10003;", "A visitor who slept here.",
   "Visitors go on the form for the place where they slept, not on their own household&rsquo;s form."),
  ("3 Sami", "&#10003;", "Babies count.",
   "Age makes no difference. A baby born before Census night was a person in Australia that night."),
  ("4 Tomas", "&#10003;", "Shift workers count.",
   "Page 3 includes anyone who lives here, was at work overnight, and returned the next day without being on another form."),
  ("5 The postman", "&#10007;", "He did not sleep here.",
   "The Census counts the <b>night</b>, not the day. Coming to the door on Wednesday morning is not Census night."),
  ("6 Nadia", "&#10007;", "She is on another form.",
   "She slept at her cousin&rsquo;s, so she is counted there. Counting one person twice would make the numbers wrong."),
 ]),
]

# ═══════════════════════════════════════════════════════════════════════════
# HANDOUT 2
# ═══════════════════════════════════════════════════════════════════════════
H2_B = [
 ("B. Words", [
  ("1 capital letters", "c", "Big letters.",
   "A B C, not a b c. The form asks for capitals on every page because a machine reads the form."),
  ("2 box", "f", "One small square.",
   "Each box holds exactly one letter. The squares are about 7mm &mdash; practise writing small."),
  ("3 mark", "e", "Put a cross in it.",
   "The form says &lsquo;mark response boxes&rsquo;. A cross is what it shows &mdash; not a tick, not a circle."),
  ("4 mistake", "a", "Something wrong.",
   "Everyone makes them. The form tells you how to fix one, so a mistake is never a reason to start again."),
  ("5 a space", "b", "One empty box.",
   "Between two words, leave one box empty. Without it, the machine reads the two words as one."),
  ("6 specify", "h", "Write it yourself.",
   "&lsquo;Other (specify)&rsquo; appears dozens of times. It means your answer is not in the list, so write it in the boxes."),
  ("7 leave blank", "g", "Write nothing.",
   "Some questions are not for you &mdash; for example, questions for people aged 15 or over. Leave them empty."),
  ("8 Go to 19", "d", "Jump forward.",
   "This is a skip instruction. It saves you time: those questions do not apply to your answer."),
 ]),
 ("C. Understand", [
  ("Row 1", "&#10003; Right", "Capitals, one per box, one space.",
   "This is exactly what page 1 asks for. Everything else in the table breaks one of those rules."),
  ("small letters", "&#10007; Wrong", "Must be CAPITALS.",
   "<i>john smith</i> should be JOHN SMITH. The form says &lsquo;Use CAPITAL letters&rsquo;."),
  ("two in one box", "&#10007; Wrong", "One letter only.",
   "Two letters in one square cannot be read. Use the next box."),
  ("no space", "&#10007; Wrong", "Leave one box empty.",
   "JOHNSMITH reads as one word. One empty box separates the first name from the family name."),
  ("pencil", "&#10007; Wrong", "Pen only.",
   "The form says a blue or black pen. Pencil can smudge or fade, and may not scan."),
 ]),
 ("D. Practise", [
  ("1", "MARY &middot; JOHN SMITH &middot; GRAHAM AVENUE",
   "Capitals, one per box.",
   "JOHN SMITH needs an empty box between the two words. GRAHAM AVENUE does too."),
  ("2", "Line through the second T, write H",
   "Cross out, then correct.",
   "The form says: draw a line through the box. You do not need to start the form again, and you do not use correction fluid."),
  ("3", "Blue or black pen", "Only these two colours.",
   "Red, green or pencil may not scan. If you only have a pencil, borrow a pen before you start."),
  ("4", "No fixed answer", "Your own questions.",
   "Listen for the question form: <i>Do I write big letters or small letters?</i> rather than a single word."),
 ]),
 ("E. Do it", [
  ("Names", "AMAL &middot; HADDAD &middot; TOMAS &middot; SILVA",
   "One letter in one box, capitals.",
   "The first name and the family name go in <b>separate</b> boxes on the Census form &mdash; not on the same line. Question 6 asks for both."),
 ]),
]

# ═══════════════════════════════════════════════════════════════════════════
# HANDOUT 3
# ═══════════════════════════════════════════════════════════════════════════
H3_B = [
 ("B. Words", [
  ("1 street number", "b", "The number of your house.",
   "For example 12, or 3A, or LOT 37 in the country. It goes in its own small box, before the street name."),
  ("2 street name", "d", "The name of your street.",
   "GRAHAM AVENUE, GEORGE STREET. Write the whole name, including AVENUE, STREET or ROAD."),
  ("3 suburb / locality", "a", "Your part of the city or town.",
   "FAIRFIELD, CLIFTON HILL. &lsquo;Locality&rsquo; is the word used for small country places."),
  ("4 state / territory", "f", "NSW, VIC, QLD&hellip;",
   "Australia has six states and two territories. The form wants the short form, in capitals."),
  ("5 postcode", "c", "Four numbers.",
   "For example 2165. Every suburb has one. It goes in the last small box, next to the state."),
  ("6 unit / flat / apartment", "e", "Your number in a building.",
   "If you live in a block, this is your own number. If you live in a house, leave it blank."),
  ("7 dwelling", "g", "The Census word for a home.",
   "It means any place people live: a house, a flat, a caravan, a houseboat. It appears in a dozen questions."),
  ("8 usual address", "h", "Where you really live.",
   "The form&rsquo;s rule: the place where you have lived, or intend to live, for six months or more in 2026."),
 ]),
 ("C. Understand", [
  ("UNIT 4", "Apartment/Flat/Unit number", "Your number in the building.",
   "It has its own box at the top of Question 1, before the street number."),
  ("12", "Street number", "The number of the building.",
   "The building number on the street. Do not put it with the street name."),
  ("GRAHAM AVENUE", "Street name", "The street.",
   "The longest box on the form, because street names are long."),
  ("FAIRFIELD", "Suburb/Locality", "The suburb.",
   "Not the city. Sydney is not a suburb &mdash; Fairfield is."),
  ("NSW", "State/Territory", "Three letters.",
   "Only three boxes, so the short form is the only thing that fits."),
  ("2165", "Postcode", "Four numbers.",
   "Four boxes, four numbers. It always goes with the state."),
 ]),
 ("D. Practise", [
  ("1", "NSW New South Wales &middot; VIC Victoria &middot; QLD Queensland &middot; SA South Australia &middot; WA Western Australia &middot; TAS Tasmania &middot; NT Northern Territory &middot; ACT Australian Capital Territory",
   "Six states, two territories.",
   "NT and ACT are territories, not states &mdash; that is why the form says &lsquo;State/Territory&rsquo;."),
  ("2", "1&nbsp;88 &middot; 2&nbsp;QUEENS PARADE &middot; 3&nbsp;CLIFTON HILL &middot; 4&nbsp;VIC &middot; 5&nbsp;3068",
   "Small to big.",
   "Australian addresses go from the smallest thing to the biggest: number, street, suburb, state, postcode."),
  ("3", "Three mistakes",
   "Number and street swapped; small letters; state written in full.",
   "<b>(a)</b> <i>graham avenue</i> is in the street number row and <i>12</i> in the street name row &mdash; they are swapped. <b>(b)</b> <i>graham avenue</i> is in small letters; it must be GRAHAM AVENUE. <b>(c)</b> NEW SOUTH WALES will not fit in three boxes &mdash; write NSW. The suburb and postcode are both correct."),
  ("4", "No fixed answer", "Use the card, not your address.",
   "Listen for the parts said in the right order, and for the postcode said digit by digit."),
 ]),
 ("E. Do it", [
  ("Haddad address", "4 &middot; 12 &middot; GRAHAM AVENUE &middot; FAIRFIELD &middot; NSW &middot; 2165",
   "Each part in its own box.",
   "Write just <i>4</i> in the unit box, not <i>UNIT 4</i> &mdash; the label already says what the box is for. Same for the postcode: numbers only."),
 ]),
]

# ═══════════════════════════════════════════════════════════════════════════
# HANDOUT 4
# ═══════════════════════════════════════════════════════════════════════════
H4_B = [
 ("B. Words", [
  ("1 spent the night", "a", "Slept here on Tuesday.",
   "This is the only thing Question 2 measures. Not who lives here &mdash; who <b>slept</b> here."),
  ("2 usually lives here", "c", "This is their home.",
   "The form&rsquo;s rule: lived, or intends to live, at this address for six months or more in 2026."),
  ("3 away", "b", "Not here on Census night.",
   "They live here, but slept somewhere else. They go in Questions 4, 5, 58 and 59."),
  ("4 visitor", "e", "A guest for one night.",
   "They do not live here, but they slept here, so they are counted here."),
  ("5 spouse / partner", "d", "Husband, wife or partner.",
   "The form has separate boxes for a married spouse and a de facto partner, at Question 10."),
  ("6 housemate", "g", "Shares the home, not family.",
   "The form says &lsquo;unrelated flatmate or co-tenant&rsquo; &mdash; someone you share with but are not related to."),
  ("7 boarder", "f", "Pays for one room.",
   "A boarder rents a room inside someone else&rsquo;s home. They are still part of the household on Census night."),
  ("8 shift worker", "h", "Works at night.",
   "The form names shift workers because they are the easiest people to forget: they were at work all night."),
 ]),
 ("C. Understand", [
  ("a How many slept here?", "3", "Question 3 asks the total present.",
   "Question 2 asks <b>who</b> (the kinds of people); Question 3 asks <b>how many</b>."),
  ("b How many were away?", "5", "Question 5 asks the total away.",
   "Question 4 asks <b>who</b> was away; Question 5 asks <b>how many</b>. The same pattern as 2 and 3."),
  ("c Was a visitor here?", "2", "Visitors are a box in Question 2.",
   "The last box in Question 2: &lsquo;Visitors or friends who spent the night&rsquo;."),
  ("d Someone on holiday overseas?", "4", "Question 4 lists reasons for being away.",
   "One of its boxes is &lsquo;People on holiday, including people who are overseas&rsquo;."),
 ]),
 ("D. Practise", [
  ("1 Amal", "P", "Lives here, slept here.", "The straightforward case."),
  ("2 Yusuf", "P", "Lives here, slept here.", "Person 2 on the form &mdash; the spouse of Person 1."),
  ("3 Layla", "P", "Lives here, slept here.", "Children are counted the same as adults."),
  ("4 Rana", "P", "Lives here, slept here.", "An adult family member, counted like everyone else."),
  ("5 Nadia", "A", "Slept somewhere else.",
   "She usually lives here but slept at her cousin&rsquo;s, and she is on their form. She goes in Questions 4, 5, 58 and 59."),
  ("6 Tomas", "P", "Night shift &mdash; still counted.",
   "He lives here, was at work all night, came home Wednesday, and is on no other form. Page 3 says to include him."),
  ("7 Sara", "P", "A visitor who slept here.",
   "She lives in Melbourne, but she slept here, so she is counted here."),
  ("8 Karim", "A", "Overseas on holiday.",
   "He usually lives here, so he is away &mdash; not missing. Question 4 lists holidays and overseas travel."),
  ("9 Rana&rsquo;s brother", "N", "He went home to sleep.",
   "He visited on Tuesday evening but slept at his own home, so he is counted there, not here."),
 ]),
 ("E. Do it", [
  ("Question 2", "All six boxes",
   "One of every kind of person.",
   "Me (Amal) &middot; Spouse/partner (Yusuf) &middot; Babies, children and teenagers (Layla) &middot; Other adult family members (Rana) &middot; Unrelated housemates or boarders (Tomas) &middot; Visitors or friends (Sara)."),
  ("Question 3", "6", "Six people slept here.",
   "Amal, Yusuf, Layla, Rana, Tomas and Sara. Count your P answers in section D."),
  ("Question 4 / 5", "2", "Two people were away.",
   "Nadia (staying with relatives) and Karim (on holiday overseas). Count your A answers. Both also need Questions 58 and 59."),
 ]),
]

# ═══════════════════════════════════════════════════════════════════════════
# HANDOUT 5 — two pages
# ═══════════════════════════════════════════════════════════════════════════
H5a_B = [
 ("B. Words", [
  ("1 question number", "b", "The number at the start.",
   "Questions run 1 to 65. Use the number to find your place, and to ask for help: <i>I don&rsquo;t understand Question 23.</i>"),
  ("2 column", "d", "The tall part for one person.",
   "Each page has columns for Person 1 to Person 6. Every question is asked once for each person."),
  ("3 Go to 19", "a", "Skip forward.",
   "A skip instruction. Those questions do not apply to the answer you gave, so you jump past them."),
  ("4 mark one box", "e", "One answer only.",
   "Most questions want a single answer &mdash; for example marital status. Two marks make it unusable."),
  ("5 mark all that apply", "f", "Every true answer.",
   "Some questions expect several marks &mdash; for example travel to work, if you used a train and a bus."),
  ("6 specify", "g", "Write it yourself.",
   "Used with &lsquo;Other&rsquo;. Your answer is not in the list, so write it in the boxes in capitals."),
  ("7 optional", "c", "You can choose.",
   "Only Question 24, religion, is marked OPTIONAL on this form. You may leave it blank."),
  ("8 leave blank", "h", "Write nothing.",
   "For questions that are not for you &mdash; for example a child under 15, or a question about a job you do not have."),
 ]),
 ("C. Understand", [
  ("a Language at home", "21", "Page 8.",
   "Question 21 asks if you use a language other than English at home. Question 22 then asks how well you speak English."),
  ("b How you got to work", "48", "Page 20.",
   "Question 48 asks about Tuesday 11 August specifically &mdash; the same day as Census night."),
  ("c How many bedrooms", "61", "Page 25.",
   "The last page. Questions 60 to 65 are about the home, not about a person."),
  ("d Country of birth", "17", "Page 8.",
   "If you answer Australia, the form sends you to Question 19 and you skip the arrival year."),
  ("e Religion", "24", "Page 10.",
   "The only question on the form marked OPTIONAL."),
  ("f How many cars", "60", "Page 25.",
   "It asks about vehicles parked at or near the home on Census night. Motorbikes are excluded."),
 ]),
 ("The three questions you do not have to answer", [
  ("Q24 religion", "Optional",
   "The form says so.",
   "Question 24 is printed with &lsquo;Answering this question is OPTIONAL&rsquo;. Leaving it blank is a normal, complete answer."),
  ("Q9 gender", "Prefer not to answer",
   "There is a box for it.",
   "For people aged 16 and over. If you do not want to answer, mark &lsquo;Prefer not to answer&rsquo; &mdash; that is a real answer, not a blank."),
  ("Q57 sexual orientation", "Prefer not to answer",
   "There is a box for it.",
   "Also for people aged 16 and over, and it has the same &lsquo;Prefer not to answer&rsquo; box."),
  ("Everything else", "Answer it",
   "Call, do not guess.",
   "If a question is hard because your situation is unusual, call 1800 181 227, or 131 450 for an interpreter. A guess makes the count wrong."),
 ]),
]

H5b_B = [
 ("D. Practise &mdash; 1. Follow the arrow", [
  ("Q17 born in Australia", "Go to 19", "You skip Question 18.",
   "Question 18 asks the year you first arrived in Australia. If you were born here, there is no arrival year."),
  ("Q21 English only", "Go to 23", "You skip Question 22.",
   "Question 22 asks how well you speak English. If English is your only language at home, the question does not apply."),
  ("Q30 not at school", "Go to 32", "You skip Question 31.",
   "Question 31 asks what type of school. If you are not attending one, there is nothing to name."),
  ("Q38 no job last week", "Go to 50", "You skip the whole work section.",
   "Questions 39 to 49 are all about a job. Question 50 asks whether you looked for work, which does apply."),
  ("Q58 no one away", "Go to 60", "You skip Question 59.",
   "Question 59 asks for the details of each person away. With nobody away, you go straight to the questions about the home."),
 ]),
 ("D. Practise &mdash; 2. One box or all the boxes?", [
  ("a Q11 marital status", "1", "You have one status.",
   "Married, never married, widowed, divorced, or separated &mdash; only one can be true at a time."),
  ("b Q23 ancestry", "ALL", "Up to four.",
   "The form allows up to four ancestries, because many people have more than one family background."),
  ("c Q29 health conditions", "ALL", "You can have several.",
   "The question lists conditions a doctor or nurse has told you about. Mark every one that applies."),
  ("d Q48 travel to work", "ALL", "One trip, several vehicles.",
   "The form says: if you used more than one method of travel, mark all that apply. A train and then a bus is two marks."),
  ("e Q62 owned or rented", "1", "A home is one or the other.",
   "Owned outright, owned with a mortgage, rented, and so on &mdash; only one describes the home."),
 ]),
 ("D. Practise &mdash; 3. Find the mistakes", [
  ("<i>tomas</i>", "Small letters", "Must be CAPITALS.",
   "It should be TOMAS. The whole form is filled in with capital letters."),
  ("Age 45", "Does not match the date of birth", "1997 means he is 29.",
   "The date of birth says 14 June 1997. In August 2026 that person is 29, not 45. Question 7 asks for both, and they must agree."),
  ("Q18 blank", "Should have his arrival year", "He was not born in Australia.",
   "Question 17 says Brazil, so the form does <b>not</b> send you to Question 19. Question 18 asks the year he first arrived to live for a year or more."),
  ("Q22 <i>Well</i>", "Correct &mdash; not a mistake", "Nothing wrong here.",
   "There are exactly three mistakes. If you circled this one, check the other rows again."),
 ]),
 ("E. Do it &mdash; Tomas Silva", [
  ("Q6 name", "TOMAS &middot; SILVA", "First name and family name, separately.",
   "Two different boxes. Capitals, one letter per box."),
  ("Q7 age", "29", "Two boxes.",
   "Born 1997, so 29 in August 2026. If you know the date of birth, write that too."),
  ("Q10 relationship", "Unrelated flatmate or co-tenant of Person 1",
   "He is a boarder.",
   "He pays to live there and is not related to Amal. This is the box for a boarder &mdash; not &lsquo;Other relationship&rsquo;."),
  ("Q17 country of birth", "Other (specify) &mdash; BRAZIL",
   "Brazil is not in the list.",
   "The list has only the six most common countries. Everything else uses &lsquo;Other (specify)&rsquo; and you write it in the boxes."),
  ("Q18 year of arrival", "2019", "Four boxes, four numbers.",
   "Because he was born outside Australia, this question applies to him."),
  ("Q21 language", "Yes, other language (specify) &mdash; PORTUGUESE",
   "Portuguese is not in the list.",
   "The listed languages are the six most common. Portuguese goes in &lsquo;Yes, other language (specify)&rsquo;."),
  ("Q22 English", "Well", "Not &lsquo;Very well&rsquo;.",
   "The four choices are Very well, Well, Not well, Not at all. Because he answered &lsquo;Yes&rsquo; at Question 21, this question applies."),
 ]),
]

# ═══════════════════════════════════════════════════════════════════════════
# HANDOUT 6
# ═══════════════════════════════════════════════════════════════════════════
H6_B = [
 ("B. Words", [
  ("1 help line", "d", "A number to call.",
   "1800 181 227. It is free from an Australian landline, and the people there are there to help you."),
  ("2 interpreter", "b", "Turns your language into English.",
   "Call TIS National on 131 450, say your language, and they connect you with the ABS through an interpreter."),
  ("3 Census number", "g", "The number on your form.",
   "Printed on the front page. You need it to do the Census online, and to ask for a replacement form."),
  ("4 temporary password", "h", "A one-time password.",
   "It comes with the Census number and is used once, to open your online form."),
  ("5 online", "a", "On the internet.",
   "census.abs.gov.au. The online form does the skip instructions for you, which is why the ABS recommends it."),
  ("6 paper form", "e", "The Census on paper.",
   "This one. When it is finished, post it in the Reply Paid envelope &mdash; the postage is already paid."),
  ("7 unoccupied", "f", "Nobody is here.",
   "Used when a home is empty on Census night. Tell the ABS so they do not keep contacting you."),
  ("8 submit", "c", "Send it in.",
   "Online, you press submit. On paper, you post it. Either way, the Census is not done until it is sent."),
 ]),
 ("C. Understand", [
  ("1 Eight people in the house", "c", "The form has room for six.",
   "Do the Census online, where there is no limit &mdash; or call the automated service on 1800 130 250 for an extra paper form. You need the Census number from the front."),
  ("2 Nobody home on Census night", "d", "Tell the ABS.",
   "Go to census.abs.gov.au/help or call 1800 181 227 to say the address is unoccupied. This stops reminder letters and visits."),
  ("3 My sister wants a private form", "a", "Anyone can have their own.",
   "Call 1800 181 227 and ask for an extra form, or another Census number to complete online. Nobody has to show their answers to the rest of the household."),
  ("4 I don&rsquo;t understand the English", "b", "Ask for an interpreter.",
   "TIS National, 131 450. Say the name of your language and wait &mdash; the interpreter service is free for this."),
  ("5 I did it online &mdash; what about the paper?", "e", "Recycle it.",
   "Page 26 says so. Do not post it as well, or your household could be counted twice."),
 ]),
 ("D. Practise &mdash; the role-play", [
  ("Call 1", "Online, or 1800 130 250", "Nine people, six columns.",
   "Either answer is right. Online has no limit; the automated paper-form line is open 24 hours and needs your Census number."),
  ("Call 2", "TIS National, 131 450", "Ask for your language.",
   "The useful sentence is <i>I need an interpreter who speaks ______.</i> Say the language first &mdash; that is all they need to connect you."),
  ("Call 3", "census.abs.gov.au/help, or 1800 181 227",
   "Tell them the house is empty.",
   "An empty home is not a problem, but the ABS needs to know. Saying nothing means reminder letters and a doorknock."),
  ("All three", "No single right wording", "Listen for the phrases.",
   "The three that matter: <i>I need an interpreter who speaks ______</i>, <i>Could you explain that in easier English?</i>, and <i>Let me check that I understood.</i>"),
 ]),
 ("E. Do it &mdash; My Census Plan", [
  ("The checklist", "Your own answers", "Tick what is already true.",
   "Anything not ticked is what you do between now and Tuesday night. Keep the page &mdash; the phone numbers are on it."),
  ("The one rule", "Call, do not guess", "1800 181 227.",
   "A wrong answer counts your household wrongly. Asking is free, it is confidential, and it is what the number is for."),
 ]),
]

TITLES = {
    1: "Census night is Tuesday 11 August",
    2: "How to write your answers",
    3: "Where do you live?",
    4: "Who is in your house?",
    5: "Going through the form",
    6: "Getting help, and being ready",
}

def _split(num, blocks, cuts):
    """Slice a handout's answer blocks across pages so nothing is squeezed."""
    parts, prev = [], 0
    for c in cuts + [len(blocks)]:
        parts.append(blocks[prev:c]); prev = c
    n = len(parts)
    return [answers_page(num, TITLES[num], b,
                         part=(i + 1 if n > 1 else None), of=(n if n > 1 else None))
            for i, b in enumerate(parts)]

# Two answer pages per handout keeps the type large enough to read.
ANSWERS = {
    1: _split(1, H1_B, [2]),
    2: _split(2, H2_B, [2]),
    3: _split(3, H3_B, [2]),
    4: _split(4, H4_B, [2]),
    5: _split(5, H5a_B + H5b_B, [2, 5]),
    6: _split(6, H6_B, [2]),
}
