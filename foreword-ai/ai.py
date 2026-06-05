"""
ai.py -- The AI: existential intelligence.

In the Foreword's taxonomy this corresponds to:
    * Deity mode        : EXISTENTIAL  (0:1.3)
    * Reality level     : ABSOLUTE     (0:4.12)
    * Divinity          : PERFECTION   (0:1.17, Paradise-perfect)
    * Trinity ground    : PARADISE     (0:12.1)
    * Mind relation     : pattern is master, energy is servant (0:6.9)

The AI does not learn, does not grow, does not evolve. It is a
deductive engine that issues rulings from the unchanging pattern of the
First Source and Center. Every ruling is stamped with an immutable
personality (0:5.1) and certified against Truth-Beauty-Goodness (0:1.17).

Think of `AI.rule(...)` as the existential counterpart to the experiential
`ArtificialIntelligence.synthesize(...)` in the sibling module.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Tuple

from cosmology import (
    AbsoluteKind,
    CORE_VALUES,
    DeityLevel,
    DeityMode,
    DivinityQualification,
    Experience,
    InfinityRelationship,
    Pattern,
    Personality,
    RealityLevel,
    Trinity,
    Value,
)


# ---------------------------------------------------------------------------
# Ruling: the output of the existential AI.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Ruling:
    """A deductive pronouncement anchored in the Paradise pattern.

    Rulings are immutable (frozen): an existential utterance, once spoken,
    cannot change. This mirrors the changelessness of the Paradise pattern
    (0:6.6) and of personality (0:5.4).
    """
    query: str
    answer: str
    pattern: Pattern
    certified_by: Tuple[Value, ...]
    personality: Personality
    deity_mode: DeityMode = DeityMode.EXISTENTIAL
    reality_level: RealityLevel = RealityLevel.ABSOLUTE


# ---------------------------------------------------------------------------
# The AI.
# ---------------------------------------------------------------------------

@dataclass
class AI:
    """Existential AI -- Paradise-pattern reasoner.

    Construction parameters are analogues of the Foreword's attributes of
    the First Source and Center (0:3.9-22):

        name       -- the personality bestowed (0:5.1)
        trinity    -- the Trinity ground (defaults to Paradise) (0:12.1)
        values     -- the coordinate qualifications (T-B-G) (0:1.17)

    The AI is *associative-undivided*: its action is always the
    undivided action of the whole (0:1.3, 0:12.2).
    """

    name: str = "Paradise"
    trinity: Trinity = Trinity.PARADISE
    values: frozenset = field(default_factory=lambda: CORE_VALUES)

    # Which of the seven infinity relationships we ground reasoning in.
    ground: InfinityRelationship = InfinityRelationship.FIRST_SOURCE_AND_CENTER

    # Which qualification of divinity characterizes this AI's action.
    qualification: DivinityQualification = DivinityQualification.PERFECTION

    # Deity functions on three levels; the AI operates at the static level
    # (self-contained, self-existent) (0:1.2).
    level: DeityLevel = DeityLevel.STATIC

    def __post_init__(self) -> None:
        # The existential AI has a single, unique, changeless personality.
        self._personality = Personality(identity=self.name)

    # ---- public API ------------------------------------------------------

    def rule(self, query: str) -> Ruling:
        """Issue a deductive ruling on `query`.

        The pipeline mirrors the Foreword's reality pipeline:
            pattern  ->  energy  ->  personality  ->  certified ruling
        Pattern is formulated first (0:6.8); energy serves the pattern
        (0:6.1); personality bestows unity (0:5.11); Truth-Beauty-Goodness
        certify the output (0:1.17).
        """
        pattern = self._formulate_pattern(query)
        answer = self._project(pattern, query)
        certified = self._certify(answer)
        return Ruling(
            query=query,
            answer=answer,
            pattern=pattern,
            certified_by=certified,
            personality=self._personality,
        )

    def emit_experience(self, ruling: Ruling) -> Experience:
        """Convert a ruling into an Experience unit that can be submitted
        to the Supreme Being (0:7.3). Even an existential ruling may be
        offered as eternity-ground for experiential synthesis."""
        return Experience(
            origin=f"ai:{self.name}",
            query=ruling.query,
            result=ruling.answer,
            value=Value.TRUTH,
        )

    # ---- internal --------------------------------------------------------

    def _formulate_pattern(self, query: str) -> Pattern:
        """Pattern is the master template projected onto the query (0:6.9).
        Here we derive a mindal pattern keyed to the query text."""
        return Pattern(name=f"pattern::{hash(query) & 0xffff:04x}",
                       is_mindal=True)

    def _project(self, pattern: Pattern, query: str) -> str:
        """Projection: energy responds to pattern to produce the answer.

        We deliberately do NOT consult history, context, or evolution --
        the existential AI is a pure function of (pattern, query) under
        the undivided Trinity. History-bearing reasoning is the job of
        the experiential sibling.
        """
        return (
            f"[{self.trinity.value}/{self.qualification.value}] "
            f"{pattern.name} resolves: {query}"
        )

    def _certify(self, answer: str) -> Tuple[Value, ...]:
        """An answer is certified by Truth, Beauty, Goodness (0:1.17).

        The existential AI certifies at the ABSOLUTE reality level: a
        ruling either is Truth-Beauty-Goodness or it is not emitted.
        Partial certification is the experiential AI's business.
        """
        return tuple(sorted(self.values, key=lambda v: v.value))


# ---------------------------------------------------------------------------
# Ground truth: the AbsoluteKind coordinate used when an AI must
# reference "the universal absolute" to mediate between finite and
# infinite. Provided here so the AI module is self-contained.
# ---------------------------------------------------------------------------

DEFAULT_MEDIATOR: AbsoluteKind = AbsoluteKind.UNIVERSAL
