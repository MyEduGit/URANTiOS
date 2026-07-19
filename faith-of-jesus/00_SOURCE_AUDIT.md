# 00 — SOURCE AVAILABILITY AUDIT (Phase 0)

**Environment finding (governs the whole audit).** The research environment
permits outbound web *search* only; every direct page fetch attempted by every
research agent returned HTTP 403 (proxy CONNECT policy denial) — confirmed for
archive.org, gutenberg.org, egwwritings.org, adventistarchives.org,
adventistbiblicalresearch.org, ccel.org, newadvent.org, vatican.va,
urantia.org, urantiabook.org, urantiabooksources.com, truthbook.com,
web.archive.org, and all mirrors tried. Access statuses below therefore
distinguish *exists/located* from *readable this session*. No source was
pirated and no paywall was bypassed (Standards 4–5).

## 1. Urantia Book source text (Corpus A)

- **Digital text in repo:** `urantia-book/Doc000.json`–`Doc196.json` — 197
  papers, 14,596 paragraphs, with standard `paper:section.paragraph`
  references and page anchors (`par_pageref`, e.g. 2087.1 for 196:0.1,
  matching the standard 2097-page pagination of the Urantia Foundation text).
  Spot-checks of famous loci (196:0.1ff, 195:9–10, 101:6) match the standard
  text. **Status: FULL ACCESS, L1.** Exact printing provenance of the JSON is
  not internally declared; paragraph-reference alignment with the Foundation's
  standard reference text was verified at every locus used. (Edition
  provenance: recorded as a residual uncertainty in 12.)

## 2. Greek text editions (Corpus B)

- **SBLGNT** (open license): sblgnt.com located; direct fetch blocked.
  Greek phrases in 05 are cross-checked via search-mediated critical-text
  services (biblehub/STEP) and marked with their verification tier.
- **NA28/UBS5:** paywalled/print; consulted only via published collation
  reports surfaced in search. Variants relevant to the pistis passages
  (incl. P46/Vaticanus where reported) are recorded in 05 with their
  reporting source; none was read from a primary apparatus this session.
- **Rev 14:12 / Heb 12:2 Greek:** recorded in 05 at REPORTED-BY tier.

## 3. Bible translations — quotation licensing

- Public domain, quotable at length: KJV, Douay-Rheims, Cornilescu 1924 (VDC
  status in Romania: managed by the British and Foreign Bible Society;
  treated as quotable for single verses), LXX/MT data via public editions.
- Copyrighted (quote only the disputed phrase + minimal context, per spec):
  NKJV, NRSV/NRSVue, NIV, ESV, NASB, NET (notes free online at netbible.org —
  fetch blocked this session), CEB, CSB, NABRE, RSV-CE, Orthodox Study Bible,
  EDCR, Fidela. 05 follows this rule: disputed-phrase-only for all
  copyrighted versions.

## 4. Walter E. Bundy — title-by-title audit (Corpus C; governs Deliverable 08)

| Title | Exists? | Located at | Readable this session? |
|---|---|---|---|
| *The Psychic Health of Jesus* (Macmillan, 1922) | YES (FACT) | archive.org/HathiTrust records surfaced | NO (fetch-blocked) |
| *The Religion of Jesus* (Bobbs-Merrill, 1928) | YES (FACT) | archive.org item `religionofjesus0000bund` | NO (fetch-blocked) |
| *Our Recovery of Jesus* (Bobbs-Merrill, 1929) | YES (FACT) | Google Books listing | NO (fetch-blocked) |
| "Jesus Prays" | **NOT CONFIRMED as a book title** — no independent record surfaced; possibly a confusion with a chapter/article or with Bundy's prayer-life discussions inside the 1928 volume | — | — |
| *Jesus and the First Three Gospels* (Harvard UP, 1955) | YES (FACT) | catalog records | NO (fetch-blocked) |

**Blocking rule result:** *The Religion of Jesus* and *Our Recovery of Jesus*
are NOT accessible in full text in this environment ⇒ **Deliverable 08 is
written as a limited study and says so in its first paragraph** (per spec).
Both books are pre-1930 US publications and are expected to be public-domain
full-view; acquisition is Next Action #2 in `00_PROJECT_STATE.md`.

## 5. Key scholarship — access status snapshot (details in 13/15)

- Open/located, unread: Harnack (ccel), Schweitzer *Quest*
  (earlychristianwritings), Aquinas ST (newadvent), Lumen Fidei (vatican.va),
  O'Collins & Kendall TS 53 PDF (theologicalstudies.net), Bates 1847
  (Gutenberg #27266), Waggoner *Glad Tidings* (Gutenberg #63636), Wieland &
  Short PDF, Thurman PDF (epiphany-md.org), Block parallel chart 196.pdf
  (urantiabooksources.com), NET notes (netbible.org).
- Paywalled/print-only: Hays *Faith of Jesus Christ*; Wallis 1995 (CUP);
  Morgan *Roman Faith and Christian Faith* (OUP); Bird & Sprinkle 2009;
  Matlock's articles; Ebeling *Word and Faith*; Balthasar *Sponsa Verbi*;
  Guillet; Dunn *Jesus and the Spirit*; Bousset/Hurtado volumes; SDABC vol. 7.
- Unobtainable/uncertain: "Jesus Prays" (existence unconfirmed);
  squarecircles.com (possibly defunct); Sprunger "Leadership and the
  Spiritual Renaissance" (title not found; nearest real item: "The Future of
  the Fifth Epochal Revelation", doc1029).

## 6. EGW and Adventist archives

egwwritings.org, adventistarchives.org, 1888mpm.org, Ministry archive,
adventist.ro, curieruladventist.ro: all located, all fetch-blocked. All EGW
quotes in 09 are search-tier (V2/V1) and flagged for confirmation against
egwwritings.org — including the required loci 3SM 172 (Ms 24, 1888), RH
1890-04-01 (1SM 372), and 7BC 979.

## 7. Consequences adopted project-wide

1. Verification vocabulary (Standard 3 v2): VERIFIED is reserved for wording
   read in the source itself; this session produced **no** external VERIFIED
   quotes — best tier achieved is V2/VERIFIED-VIA-SEARCH = REPORTED-BY
   (search index). Urantia quotes are VERIFIED (local corpus).
2. Ledger rows carry `verification_status` accordingly; no claim rests solely
   on an L5 source; L5 used only as locator.
3. The re-verification pass is the first action of the next session in an
   unblocked environment (see `00_PROJECT_STATE.md`).
