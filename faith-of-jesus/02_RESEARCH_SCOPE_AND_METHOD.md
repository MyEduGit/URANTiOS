# 02 — RESEARCH SCOPE AND METHOD

**Project:** THE FAITH OF JESUS: From Believing in Jesus to Believing With Jesus
**Repository:** URANTiOS / `faith-of-jesus/`
**Date of investigation:** July 2026

## Mission

Conduct the most comprehensive evidence-based investigation possible into "the
faith OF Jesus — not merely faith IN Jesus": Jesus' own personal religious
faith, trust, loyalty, prayer life, consciousness of God, surrender to the
Father's will, ethical conduct, courage, human spiritual development, and
faithfulness. The *pistis Christou* grammatical debate is treated as one
component of a much larger investigation, not its center.

## Corpora investigated

| Corpus | Method | Access level |
|---|---|---|
| A. The Urantia Book | Programmatic sweep of the complete local text (197 papers, 14,596 paragraphs, `urantia-book/Doc*.json`); pattern-matched extraction + manual augmentation; every citation verbatim by construction | FULL — highest confidence layer |
| B. Biblical texts | Greek text and translation comparison via public critical editions and translation databases fetched during the investigation; renderings marked verified vs. recalled | PARTIAL — web-verified where possible |
| C. Historical scholarship | Web research agents targeting primary texts (public-domain works fetched where available), publisher/bibliographic verification, survey articles | PARTIAL — paywalled academic literature recorded as UNVERIFIED where not accessed |
| D. Adventist corpus | egwwritings.org and Adventist archives for verbatim Ellen G. White / pioneer quotes; BRI materials | PARTIAL |
| E. Urantia secondary material | Foundation / Fellowship / UAI / TruthBook sites; Matthew Block source studies (claims independently spot-checked against Bundy's text where accessible) | PARTIAL |

## Method

1. **Corpus A first.** The Urantia Book text is local and complete, so its
   layer is exhaustive: a calibrated regex sweep over all 14,596 paragraphs
   across 20 thematic categories, then a focused core-filter for paragraphs
   about Jesus' own faith/religion/trust/prayer/will-alignment, then manual
   augmentation with essential narrative ranges (nine inevitabilities, baptism
   decisions, prayer discourses, Gethsemane, the cross). Output:
   `04_URANTIA_CORPUS.md` (Tier 1 verbatim core ~158 paragraphs; Tier 2
   exhaustive thematic reference index).
2. **Corpora B–E in parallel.** Five independent research agents (biblical/
   pistis Christou; Walter Bundy; Adventist history; historical theology;
   Urantia secondary literature), each bound by the no-fabrication standards
   below, each returning findings with per-claim verification labels and the
   URLs actually used.
3. **Synthesis last.** Claims are merged into the claims ledger
   (`14_CLAIMS_LEDGER.csv`), disagreements preserved, and the master synthesis
   (`16_MASTER_SYNTHESIS.md`) written only from ledgered material.

## Epistemic classification

Every substantive claim in these deliverables carries (explicitly or by
section-level declaration) one of:

- **FACT** — publicly verifiable, uncontested (e.g., publication data)
- **TEXTUAL OBSERVATION** — what a text verifiably says (quotation + locator)
- **SCHOLARLY INTERPRETATION** — a scholar's reading, attributed
- **THEOLOGICAL CLAIM** — a confessional/doctrinal position, attributed
- **URANTIA REVELATORY CLAIM** — what the Urantia text asserts on its own
  authority (authoritative *within* its frame; not used as external historical
  proof — see standards 8–9)
- **INFERENCE** — this project's reasoning from ledgered evidence
- **UNVERIFIED CLAIM** — reported but not confirmed against a primary source
  during this investigation

## Standards adopted (verbatim from the project charter)

1. Prefer primary sources, original texts, university presses, peer-reviewed
   journals, official denominational archives and stable repositories.
2. Never invent citations, quotations, page numbers, DOI numbers or URLs.
3. Verify quotations against the actual source.
4. Record inaccessible paywalled sources as unverified until accessed.
5. Do not bypass paywalls or obtain pirated books.
6. Distinguish the seven claim types above.
7. Preserve disagreements; do not manufacture consensus.
8. Treat The Urantia Book as the primary authority when explaining its own
   theology, but do not use it as external historical proof without saying so.
9. Do not force biblical scholarship to validate The Urantia Book.
10. Do not force The Urantia Book into Protestant justification categories.

## Known limitations (declared up front)

- Paywalled academic monographs and journal articles (most of the pistis
  Christou technical literature) were not purchased or pirated; positions are
  reported from accessible surveys, publisher pages, open-access copies, and
  reviews, and labeled accordingly.
- Conference recordings, podcasts, and unpublished Urantia manuscripts are
  catalogued by availability, not exhaustively transcribed.
- Romanian Adventist sources: availability was checked but coverage is thin;
  recorded honestly in `09_ADVENTIST_HISTORY.md`.
- Translation renderings not fetched live are marked as recalled-unverified in
  `05_BIBLICAL_PASSAGE_MATRIX.md`.
- Remaining gaps are consolidated in `12_CONTRADICTIONS_AND_UNRESOLVED_QUESTIONS.md`
  and the limitations section of `16_MASTER_SYNTHESIS.md`.
