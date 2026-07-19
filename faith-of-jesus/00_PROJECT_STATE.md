# 00 — PROJECT STATE

**Project:** THE FAITH OF JESUS: From Believing in Jesus to Believing With Jesus
**Spec:** v2.0 (supersedes v1; v1 deliverables retro-aligned)
**Branch:** `claude/sharp-gauss-ajvbks` · PR #22 (draft)
**Last updated:** 2026-07-19 (session 1)

## Status by deliverable

| File | Status | Notes |
|---|---|---|
| 00_PROJECT_STATE.md | LIVE | this file |
| 00_SOURCE_AUDIT.md | DONE (session 1) | environment fetch-block documented; Bundy access audit included |
| 01_EXECUTIVE_RULING.md | DONE — WRITTEN LAST | per spec, after 16 |
| 02_RESEARCH_SCOPE_AND_METHOD.md | DONE | v2 standards incorporated |
| 03_TERMINOLOGY_AND_ONTOLOGY.md | DONE | 8-term ontology + ladder |
| 04_URANTIA_CORPUS.md | DONE | Tier 1 core (~158 pars) + v2 addendum (101:8 complete; 42 transferability pars) + Tier 2 exhaustive index |
| 05_BIBLICAL_PASSAGE_MATRIX.md | DONE | pistis-agent findings; renderings labeled verified/recalled |
| 06_PISTIS_CHRISTOU_DEBATE.md | DONE | scholars, argument bundles, history, assessment |
| 07_JESUS_PERSONAL_RELIGION.md | DONE | RQ 1–5; Aquinas locus engaged |
| 08_WALTER_BUNDY_COMPARISON.md | DONE — **LIMITED STUDY** | Bundy full text NOT accessible in this environment (archive.org fetch-blocked); written under the spec's blocking rule; first paragraph declares limitation |
| 09_ADVENTIST_HISTORY.md | DONE | V1/V2/PARAPHRASE tiers preserved |
| 10_HISTORICAL_THEOLOGY.md | DONE | incl. Aquinas, Balthasar, O'Collins, Lumen Fidei ¶18, Bousset/Hurtado |
| 11_PRACTICAL_PSYCHOLOGY_OF_JESUS_FAITH.md | DONE | RQ 9 + reproducible practice |
| 12_CONTRADICTIONS_AND_UNRESOLVED_QUESTIONS.md | DONE | disagreements + gaps consolidated |
| 13_ANNOTATED_BIBLIOGRAPHY.md | DONE | by corpus, with access status |
| 14_CLAIMS_LEDGER.csv | DONE | v2 fields |
| 15_SOURCES.csv | DONE | L1–L5 + access status |
| 16_MASTER_SYNTHESIS.md | DONE | 17-section structure |
| SEARCH_LOG.csv | DONE | agent search coverage log |

## Blocked / degraded items

1. **Environment fetch-block (global):** the research environment allowed web
   *search* but returned HTTP 403 on every direct page fetch (all agents,
   all domains, including archive.org, egwwritings.org, ccel.org, vatican.va,
   newadvent.org). Consequence: every external quotation is REPORTED-BY
   (search-result mediated), tiered V2/V1/PARAPHRASE; none is
   primary-VERIFIED per Standard 3. **Next session in an unblocked
   environment: re-fetch and upgrade the ledger's verification_status
   fields.**
2. **Deliverable 08 (Bundy):** BLOCKED condition triggered — *The Religion of
   Jesus* and *Our Recovery of Jesus* were located (archive.org / Google
   Books) but not readable. 08 is written as a limited study per spec.
   Contamination rule 13 could not be exercised (no Bundy text to read
   Block-blind); documented inside 08.
3. Romanian Adventist corpus: located, unread (see 09 §2.5).

## Next actions (priority order)

1. Re-run verification pass from an environment with page-fetch access:
   upgrade V2/V1 quotes to VERIFIED (Ms 24 1888; Waggoner Glad Tidings;
   Aquinas ST III q.7 a.3; Lumen Fidei ¶18; Harnack; Bultmann; Bundy texts).
2. Bundy full-text acquisition (archive.org full-view scan or library) →
   rewrite 08 as full line-by-line comparison under contamination rule 13.
3. Romanian-language pass on curieruladventist.ro / adventist.ro (project
   owner reads Romanian).
4. Access Ebeling "Jesus and Faith", Balthasar "Fides Christi", O'Collins &
   Kendall TS 53 (1992), Wallis 1995 — the four highest-value unread
   scholarly items.
5. Optional: integrate with Mircea's journal article for publication targets
   (see `../FAITH_OF_JESUS_RESEARCH.md` §5).

## Session log

- **Session 1 (2026-07-19):** Spec v1 received; foundation deliverables
  built; spec v2.0 received mid-session and adopted; five parallel research
  agents executed (Urantia secondary, Adventist, historical theology, pistis
  Christou, Bundy); all 16+3 deliverables produced; limitations honestly
  recorded. All work committed to PR #22.
