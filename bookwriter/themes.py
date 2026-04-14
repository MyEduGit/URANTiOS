"""
Thematic index over the Urantia Book corpus.

Provides keyword-weighted selection of paragraphs relevant to a seed theme.
This gives the writer a compact evidence basket — keeping prompts small
while maximising citation density.
"""
from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass
from typing import Iterable

from .corpus import Corpus, Paragraph


_WORD_RE = re.compile(r"[A-Za-z][A-Za-z\-']+")
_STOP = frozenset(
    """
    a an the and or but if of in on at to for from with by as is are was were be been being
    have has had do does did this that these those it its i you he she they we them us our
    their his her my your mine me who whom which what when where why how not no nor so than
    then too very can could should would may might will shall must also just only even still
    such there here about over under into through between among upon while because since
    """.split()
)


def _tokens(text: str) -> list[str]:
    return [w.lower() for w in _WORD_RE.findall(text) if w.lower() not in _STOP]


@dataclass
class ThemeHit:
    paragraph: Paragraph
    score: float

    @property
    def ref(self) -> str:
        return self.paragraph.ref


class ThemeIndex:
    """TF-IDF-lite ranker over Urantia Book paragraphs.

    Built once over the 17k+ paragraphs of the corpus; queries are fast
    keyword lookups with IDF weighting.
    """

    def __init__(self, corpus: Corpus):
        self.corpus = corpus
        self._paragraphs: list[Paragraph] = list(corpus.paragraphs())
        self._tokens: list[list[str]] = [_tokens(p.content) for p in self._paragraphs]

        # Document frequencies
        df: Counter[str] = Counter()
        for toks in self._tokens:
            df.update(set(toks))
        self._df = df
        n = len(self._paragraphs)
        self._idf = {
            t: math.log((n + 1) / (c + 1)) + 1.0 for t, c in df.items()
        }

        # Inverted index for fast lookup
        self._inverted: dict[str, list[int]] = {}
        for i, toks in enumerate(self._tokens):
            for t in set(toks):
                self._inverted.setdefault(t, []).append(i)

    def query(
        self,
        terms: Iterable[str] | str,
        *,
        limit: int = 60,
        min_score: float = 0.0,
    ) -> list[ThemeHit]:
        """Rank paragraphs by relevance to the given terms."""
        if isinstance(terms, str):
            tokens = _tokens(terms)
        else:
            tokens = [t.lower() for t in terms]
        if not tokens:
            return []

        # Candidate paragraph indices: union of inverted hits
        candidate_idxs: set[int] = set()
        for t in tokens:
            candidate_idxs.update(self._inverted.get(t, ()))

        scores: list[tuple[int, float]] = []
        query_counter = Counter(tokens)
        for i in candidate_idxs:
            ptoks = self._tokens[i]
            ptok_counts = Counter(ptoks)
            # cosine-lite: sum(tf * idf) for shared terms
            score = 0.0
            for term, qcount in query_counter.items():
                if term in ptok_counts:
                    score += qcount * ptok_counts[term] * self._idf.get(term, 1.0)
            # length normalisation
            if ptoks:
                score /= math.sqrt(len(ptoks))
            if score > min_score:
                scores.append((i, score))

        scores.sort(key=lambda x: x[1], reverse=True)
        return [
            ThemeHit(paragraph=self._paragraphs[i], score=s)
            for i, s in scores[:limit]
        ]

    def select_evidence(
        self,
        theme: str,
        *,
        k: int = 40,
        diversify: bool = True,
    ) -> list[Paragraph]:
        """Pick the top-k paragraphs for a theme.

        When ``diversify`` is True, at most one paragraph per (paper, section)
        is kept until every distinct (paper, section) is exhausted — then the
        remaining paragraphs fill in. This gives broad coverage instead of
        clustering on a single section.
        """
        hits = self.query(theme, limit=max(k * 4, 200))
        if not diversify:
            return [h.paragraph for h in hits[:k]]

        seen: set[tuple[int, int]] = set()
        primary: list[Paragraph] = []
        backup: list[Paragraph] = []
        for h in hits:
            c = h.paragraph.citation
            key = (c.paper, c.section)
            if key in seen:
                backup.append(h.paragraph)
            else:
                seen.add(key)
                primary.append(h.paragraph)
            if len(primary) >= k:
                break
        out = primary
        # Top up if we still need more
        for p in backup:
            if len(out) >= k:
                break
            out.append(p)
        return out
