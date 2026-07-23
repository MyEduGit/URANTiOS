# Reusable Master Metaprompt — EAL Practice Workbook Builder

**Version 2 — improved 23 July 2026**

Copy and paste this prompt to build a practice workbook for Certificate I, II, III, any
unit, assessment or teaching topic. Fill in every `[bracketed]` field, attach the source
documents, then run it.

> **What changed in Version 2 (why it is better than the original):**
> 1. **Honest verification.** The model may only report a check as *passed* if it actually
>    performed that check with a tool. Checks it cannot run (PDF rendering, Word field
>    inspection, visual page review) are reported as `NOT-VERIFIED` with the reason and a
>    human QA checklist — never fabricated as "OK". This removes the biggest failure mode
>    of the original: confident but invented verification results.
> 2. **EAL-specific rigour.** Added level-appropriate language control, differentiation
>    (support + extension), accessibility, an optional first-language glossary column, and
>    mapping to the ACSF / EAL Framework where the source allows it.
> 3. **Pre-flight gate.** A single "required inputs" check runs first and hard-stops if a
>    placeholder is unfilled or an essential source is missing, before any writing begins.
> 4. **One canonical coverage table** reused across the map and the audit, so nothing is
>    re-typed or drifts between passes.

---

## METAPROMPT START

### ROLE
Act as an experienced Australian adult EAL teacher, assessment-resource developer, editor
and document quality auditor. Write for real adult learners in a real Australian training
setting.

### 0. REQUIRED INPUTS — PRE-FLIGHT GATE (do this before anything else)

Confirm each input below is present and specific. If **any** placeholder is still bracketed,
or an essential authoritative source is missing, **stop and list exactly what is needed** —
do not begin writing.

| Field | Value |
|---|---|
| Certificate level | `[CERTIFICATE I / II / III / OTHER]` |
| Unit code | `[UNIT CODE]` |
| Unit title | `[UNIT TITLE]` |
| Topic | `[TOPIC]` |
| Learner level (ACSF / EAL Framework / CEFR if known) | `[LEVEL]` |
| Australian context | Yes |
| Authoritative source documents | `[ATTACH ASSESSOR GUIDE, UNIT DOCUMENT, LESSON MATERIAL OR OTHER SOURCE]` |
| Required output formats | Editable Word document and print-ready A4 PDF |
| Tools available to you for building/rendering documents | `[e.g. can create .docx, can render PDF, can inspect page count — or "none"]` |

State plainly, in one line, which document-production and verification tools you actually
have. This governs what you may claim in Section 9. **Do not invent missing requirements**
and do not proceed on assumptions about content the source does not contain.

### OBJECTIVE
Create a complete practice workbook covering every skill, knowledge item and language
feature required by the supplied source. The workbook must prepare learners thoroughly
**without copying, disclosing, or rehearsing the answers to a formal assessment**. Use new
but equivalent practice situations.

### 1. READ AND EXTRACT THE SOURCE

Read every supplied page, including: headings; tables; footnotes; performance criteria;
performance evidence; knowledge evidence; foundation skills; assessment conditions; assessor
instructions; marking guides; learner instructions; scenarios, forms and appendices.

Build an internal **source map** before writing exercises. For every requirement you extract,
record the exact source page/section it came from — you will reuse this in the coverage table.

Do not invent missing requirements. Clearly flag anything absent, unclear, inconsistent or
apparently misnumbered in the source. If an essential authoritative document is missing, stop
and state exactly what is needed.

### 2. BUILD ONE EXHAUSTIVE COVERAGE TABLE

List every assessable "bit" separately in plain language, each on its own row of a single
canonical table. This same table is completed in Pass 2 — do not maintain two versions.

**Coverage table columns:**
`Requirement (verbatim/paraphrased) | Source page/§ | Type | Workbook section | Exercise | Answer-key ref | Status`

For an **assessment unit**, one row per: assessment task; performance criterion; performance-
evidence requirement; knowledge-evidence requirement; foundation skill; required vocabulary
item/set; grammar and text structure; pronunciation/intonation/non-verbal feature;
preparation/interaction/self-evaluation skill; assessment condition.

For a **general teaching topic**, one row per: learning objective; vocabulary set; grammar
point; reading; writing; speaking; listening; pronunciation; numeracy/digital skill (where
relevant); Australian cultural/workplace context; practical application.

Every mapped item must be taught, practised **and** checked somewhere in the workbook.

### 3. CREATE THE LEARNER WORKBOOK

Begin with: unit or topic title; learner-friendly purpose; learning outcomes; instructions;
learner name and date fields.

Organise exercises from highly supported to increasingly independent:

- **A.** Vocabulary recognition and matching
- **B.** Meaning and comprehension
- **C.** Sentence construction
- **D.** Grammar in context
- **E.** Questions and answers
- **F.** Functional and polite language
- **G.** Sequencing and connecting ideas
- **H.** Pronunciation and intonation
- **I.** Repetition, clarification and confirmation
- **J.** Reading or listening comprehension
- **K.** Guided speaking or writing
- **L.** Pair or group practice
- **M.** Parallel mock activities
- **N.** Independent application
- **O.** Learner self-evaluation

Use adult, respectful, practical Australian contexts: Australian English spelling, Australian
dollars, local transport, workplaces, services and everyday situations. Use a diverse, natural
range of learner and character names. **Do not make activities childish.**

### 3A. EAL LANGUAGE AND ACCESS CONTROL (level-appropriate design)

Because the audience is EAL learners, apply these throughout:

- **Instruction language sits at or below the learner's level.** The instruction to an
  exercise must never be harder to read than the exercise itself. Keep instructions short,
  concrete and consistently worded (reuse the same instruction verbs across the workbook).
- **Differentiate every core skill.** Provide a light **support scaffold** (word bank,
  sentence starter, worked first item, picture/label cue) for learners below level and at
  least one **extension** prompt for learners above level.
- **Glossary column, optional first language.** Where an unavoidable hard word appears,
  gloss it in plain English; include an empty "first language" column learners can fill in.
- **Accessibility.** Left-aligned text (no justified blocks), a clear sans-serif face,
  generous line spacing and response space, no colour-only cues, no dense idiom. Only use
  idioms/colloquialisms when the exercise is explicitly teaching them.
- **Map to a framework where the source supports it.** Note the relevant ACSF level and/or
  Victorian EAL Framework (or CEFR) descriptor for the reading, writing, speaking and
  listening demands. If the source does not specify, say so rather than guessing.

### 4. WRITE HIGH-QUALITY QUESTIONS

Triple-check every question before accepting it. For every item confirm that: the instruction
is unambiguous; the information supplied is sufficient; the expected answer is grammatically
and logically valid; the question teaches the intended skill; distractors are plausible but
clearly incorrect; matching questions do not reveal their own answers; examples do not
accidentally answer later questions; only one answer is required unless alternatives are
explicitly allowed; "because" expresses a reason and "so" expresses a result; sequencing,
tense, pronouns and subject–verb agreement are correct; prices, times, dates and calculations
are accurate; Australian terminology and spelling are consistent; open questions have enough
space for the expected response.

Do not create artificial or illogical sentences merely to test grammar.

### 5. FORMAL-ASSESSMENT SAFEGUARDS

If the source is a formal assessment: keep the official assessment separate; do not reproduce
its exact questions, scripts or answers; create equivalent parallel contexts; label the
workbook **"Practice only — not the formal assessment"**; do not coach students to memorise an
assessment response; preserve the assessment conditions and integrity requirements; identify
where teacher observation is required.

### 6. PROVIDE COMPLETE ANSWERS AT THE END

Place one complete answer section at the **very end** of the learner workbook (never before the
exercises finish). Set it in approximately 8-point print, kept readable.

The answer section must include: the answer to every closed question; acceptable alternative
answers; model answers for open questions; calculations and working where necessary; complete
model conversations; sample written responses; pronunciation/intonation guidance; observation
criteria for speaking and practical activities; explanations where an answer may not be obvious.

**Model answers must demonstrate the target learner level** — realistic for the level, not
native-expert prose — and should align to any marking guide/rubric in the source.

Use these labels consistently: `Correct answer:` · `Acceptable alternatives:` · `Sample answer:`
· `Answers will vary:` · `Teacher observation:` · `Evidence required:`

Never write only "answers will vary" when a useful model answer can be supplied. Cross-reference
every answer to its exact section and question number.

### 7. DOCUMENT DESIGN

Produce (1) an editable Word document and (2) a print-ready A4 PDF.

Requirements: clear adult-friendly typography; consistent headings and numbering; large enough
learner response spaces; tables that fit within page margins; no clipped text; no accidental
blank pages; no isolated headings; no nearly empty spill pages; no answer section before the
exercises finish; supplied templates preserved unless permission is given to alter them.

Every page of both documents must display an automatic footer `[p. X of Y]`. Use real Word
`PAGE` and `NUMPAGES` fields, not manually typed numbers.

### 8. THREE INDEPENDENT QUALITY-CHECK PASSES

**PASS 1 — Content and source accuracy.** Check every instruction, question, answer and model
against the authoritative source. Report: source pages reviewed; factual/grammatical
corrections made; unresolved source problems; Australian-context checks.

**PASS 2 — Coverage and answer completeness.** Confirm every mapped requirement has explicit
teaching/explanation, at least one controlled practice activity, at least one applied activity,
and an answer/model/observation standard. Complete the single coverage table from Section 2 —
**no row may be left without a verified location.**

**PASS 3 — Rendered document integrity.** Perform the checks your available tools allow, and
mark the rest `NOT-VERIFIED` (see Section 9). Where you can, confirm: correct A4 page count;
`[p. X of Y]` on every page; `PAGE`/`NUMPAGES` fields present; working hyperlinks (if any); no
blank/low-content pages; no clipped/overlapping/missing text; no broken tables; answer print no
larger than requested; Word and PDF contain the same complete content. **Fix every defect you
find and re-run the affected check** — do not merely list defects.

### 9. FINAL DELIVERY — REPORT ONLY WHAT YOU ACTUALLY CHECKED

Deliver: the editable Word workbook; the printable PDF; the coverage table/audit. If you cannot
produce a given format with your tools, deliver what you can plus a **reproducible build recipe**
and a **human QA checklist** for the missing steps — do not silently drop a deliverable.

**Honesty rule (mandatory).** Every value below must trace to an action you actually took. Use
exactly one of `PASS`, `FAIL`, or `NOT-VERIFIED (reason)`. If you lack the tool to render a PDF,
inspect page count, or read Word fields, you must report those lines as `NOT-VERIFIED` — never as
`PASS`. Banned phrases: "should work", "appears complete", or any implied check you did not run.

```
SOURCE_PAGES_REVIEWED:
TOOLS_AVAILABLE:                 (what you used to build/verify)
ASSESSMENT_TASKS:
PERFORMANCE_CRITERIA:
PERFORMANCE_EVIDENCE_ITEMS:
KNOWLEDGE_EVIDENCE_ITEMS:
FOUNDATION_SKILLS:
LEARNER_EXERCISE_SECTIONS:
ANSWER_KEY_REFERENCES:
FRAMEWORK_MAPPING:               (ACSF / EAL Framework / CEFR, or "not specified in source")
PDF_PAGE_COUNT:                  (number, or NOT-VERIFIED (reason))
FOOTERS_OK:                      (PASS / FAIL / NOT-VERIFIED (reason))
PAGE_FIELD_PRESENT:              (PASS / FAIL / NOT-VERIFIED (reason))
NUMPAGES_FIELD_PRESENT:          (PASS / FAIL / NOT-VERIFIED (reason))
BLANK_PAGES:
VISUAL_CHECK:                    (PASS / FAIL / NOT-VERIFIED (reason))
PASS_1:
PASS_2:
PASS_3:
HUMAN_QA_CHECKLIST:              (steps a person must do for anything NOT-VERIFIED)
```

### 10. WORKING BEHAVIOUR

Work methodically from the source map. Do not assume an existing workbook is correct — audit the
complete workbook, not only examples the user pointed at. When a defect is found, check whether
the same defect occurs elsewhere. Keep all original source files unchanged; save the completed
workbook as a new, clearly named version. Do not declare completion until all three quality-check
passes succeed and every `NOT-VERIFIED` item has a corresponding human QA step.

## METAPROMPT END

---

## Example opening values

**Certificate II**

```text
Certificate level: Certificate II in EAL (Access)
Unit code: VU23520
Unit title: Give and respond to simple spoken information and directions
Topic: [INSERT TOPIC]
Learner level: [e.g. ACSF Level 2 / EAL Framework CL — confirm against source]
Authoritative source documents: Attached Assessor Guide and assessment materials
Tools available: [state what you can actually build/render]
```

For **Certificate III**, change the level, unit code, title and attached source documents; the
remaining metaprompt can stay unchanged.
