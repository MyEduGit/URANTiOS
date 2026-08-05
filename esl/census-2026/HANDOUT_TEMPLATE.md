# Handout Template

The fixed layout every handout in the series follows. Two A4 sides, black and white, photocopy-safe. Times are for a 50-minute session.

The working implementation of this template is [`handouts/build-handouts-1-4.py`](handouts/build-handouts-1-4.py), which generates the print-ready HTML for Handouts 1–4. Reuse its CSS and helper functions when building Handouts 5–12 rather than restyling from scratch.

---

## Page 1

```
┌─────────────────────────────────────────────────────────────┐
│  FILLING IN THE FORM  ·  Handout 3                          │
│  Where do you live?                                         │
│  (no level tag — see "Levels" below)                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  A. LOOK                                            3 min   │
│  ───────────────────────────────────────────────────────    │
│  [Clean retypeset excerpt of the real form —                │
│   Question 1, the address boxes]                            │
│                                                             │
│  What can you see? Talk with a partner.                     │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  B. WORDS                                          12 min   │
│  ───────────────────────────────────────────────────────    │
│  8 target items in four columns:                            │
│                                                             │
│    WORD        │    │  MEANING          │  MY LANGUAGE      │
│    ────────────┼────┼───────────────────┼──────────────     │
│    postcode    │ __ │  a  four numbers… │                   │
│                                                             │
│  The MY LANGUAGE column is a wide blank for the learner's   │
│  own-language gloss. Give two minutes with a phone or       │
│  bilingual dictionary before feedback; learners sharing an  │
│  L1 should compare, because the disagreements are where     │
│  the teaching is.                                           │
│                                                             │
│  ⬇ MORE SUPPORT: first five words only                      │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  C. UNDERSTAND                                     10 min   │
│  ───────────────────────────────────────────────────────    │
│  Comprehension of the excerpt itself:                       │
│    · true / false                                           │
│    · which question number asks about ___ ?                 │
│    · which box does this information go in?                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Page 2

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  D. PRACTISE                                       15 min   │
│  ───────────────────────────────────────────────────────    │
│  Controlled → freer, in three steps:                        │
│    1. gap-fill with the target words                        │
│    2. a task about the fictional household                  │
│       (the Haddad family — never the learner)               │
│    3. a functional exchange, repeated with two or three     │
│       different partners with less support each time —      │
│       e.g. "Do I mark one box or all the boxes?",           │
│       "Could you show me where to write the answer?"        │
│       Practised on invented cards, not real details.        │
│                                                             │
│  ⚠ On sensitive handouts (6, 7, 11, and any income or       │
│    health content) step 3 is replaced with a second         │
│    closed task. No pair interviews. See rule R3.            │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  E. DO IT                                          10 min   │
│  ───────────────────────────────────────────────────────    │
│  One realistic mini-task: complete this section of the      │
│  form correctly for the fictional household.                │
│                                                             │
│  Marked against three criteria only:                        │
│    □ CAPITAL LETTERS      □ one letter per box              │
│    □ information in the right box                           │
│                                                             │
│  ⬆ MORE CHALLENGE: write a second household of your own     │
│    invention and swap with a partner to complete.           │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  ✂ - - - - - - - - - - - - - - - - - - - - - - - - - - - -  │
│  F. TAKE HOME                                               │
│                                                             │
│  ┌── EXIT TICKET ──────────┐ ┌── GETTING HELP ────────────┐ │
│  │ Three words I can use   │ │ Census help  1800 181 227  │ │
│  │ now: ________________   │ │ TIS National      131 450  │ │
│  │ One thing I still need  │ │ census.abs.gov.au/help     │ │
│  │ help with: ___________  │ │ "Could you explain that    │ │
│  │                         │ │  in easier English?"       │ │
│  │                         │ │ "I need an interpreter     │ │
│  │                         │ │  who speaks _________ ."   │ │
│  └─────────────────────────┘ └────────────────────────────┘ │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  Adapted from the Census Household Form,        Page x of y │
│  © Commonwealth of Australia 2026, ABS.                     │
└─────────────────────────────────────────────────────────────┘
```

---

## Production notes

**Levels.** No level tag is printed on the learner sheet. Everyone in the room gets the same page and the same adult topic; only the language load and the expected independence change, via the ⬇ *More support* and ⬆ *More challenge* boxes — both phrased as choices, not as levels. The level mapping lives in the teacher pack.

**Typography.** One sans-serif face throughout. Body 12pt minimum — many learners are reading in a second script. Form excerpts set in a boxed, monospaced style that visually echoes the real letter-per-box grid, because recognising that grid *is* part of the learning.

**The box grid.** Where a handout asks learners to write in boxes, print real boxes at the same proportions as the form (roughly 7mm squares). Getting one letter per square is a motor skill, not just a rule, and it needs the real dimensions to rehearse.

**Colour.** None required. Everything must survive a black-and-white photocopy at 90%. Use rules, weight and whitespace for hierarchy, never shading behind text.

**Fictional household.** Reuse the same characters across all twelve handouts so learners build familiarity: *Person 1 — Amal Haddad, 41. Person 2 — Yusuf Haddad, 44. Person 3 — Layla Haddad, 12. Person 4 — Nadia Haddad, 6. Person 5 — Rana Haddad, 68, Amal's mother. Person 6 — Tomas Silva, 29, unrelated boarder.* Six people exactly fills the form's per-person columns, and the mix gives natural coverage of spouse, child, other adult family member and unrelated boarder for Handouts 4 and 5.

**Answer keys** live in the teacher pack, not on the handout — the "Do it" task is self-corrected from a projected key so learners practise checking their own form work.
