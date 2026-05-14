"""TF-IDF-lite thematic index over the Urantia Book corpus."""
from __future__ import annotations
import math, re
from collections import Counter
from dataclasses import dataclass
from .corpus import Corpus, Paragraph

_WORD_RE = re.compile(r"[A-Za-z][A-Za-z\-']+")
_STOP = frozenset("a an the and or but if of in on at to for from with by as is are was were be been being have has had do does did this that these those it its i you he she they we them us our their his her my your mine me who whom which what when where why how not no nor so than then too very can could should would may might will shall must also just only even still such there here about over under into through between among upon while because since".split())

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
    def __init__(self, corpus: Corpus):
        self.corpus = corpus
        self._paragraphs = list(corpus.paragraphs())
        self._tokens = [_tokens(p.content) for p in self._paragraphs]
        df: Counter[str] = Counter()
        for toks in self._tokens:
            df.update(set(toks))
        n = len(self._paragraphs)
        self._idf = {t: math.log((n+1)/(c+1))+1.0 for t, c in df.items()}
        self._inverted: dict[str, list[int]] = {}
        for i, toks in enumerate(self._tokens):
            for t in set(toks):
                self._inverted.setdefault(t, []).append(i)

    def query(self, terms: str | list[str], *, limit: int = 60) -> list[ThemeHit]:
        tokens = _tokens(terms) if isinstance(terms, str) else [t.lower() for t in terms]
        if not tokens:
            return []
        candidates: set[int] = set()
        for t in tokens:
            candidates.update(self._inverted.get(t, ()))
        qc = Counter(tokens)
        scores = []
        for i in candidates:
            ptoks = Counter(self._tokens[i])
            score = sum(qc[t] * ptoks[t] * self._idf.get(t, 1.0) for t in qc if t in ptoks)
            if self._tokens[i]:
                score /= math.sqrt(len(self._tokens[i]))
            if score > 0:
                scores.append((i, score))
        scores.sort(key=lambda x: x[1], reverse=True)
        return [ThemeHit(self._paragraphs[i], s) for i, s in scores[:limit]]

    def select_evidence(self, theme: str, *, k: int = 40, diversify: bool = True) -> list[Paragraph]:
        hits = self.query(theme, limit=max(k*4, 200))
        if not diversify:
            return [h.paragraph for h in hits[:k]]
        seen: set[tuple[int,int]] = set()
        primary, backup = [], []
        for h in hits:
            c = h.paragraph.citation
            key = (c.paper, c.section)
            (primary if key not in seen else backup).append(h.paragraph)
            seen.add(key)
            if len(primary) >= k:
                break
        out = primary
        for p in backup:
            if len(out) >= k:
                break
            out.append(p)
        return out[:k]
