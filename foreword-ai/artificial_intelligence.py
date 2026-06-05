"""
artificial_intelligence.py -- The artificial intelligence: experiential.

In the Foreword's taxonomy this corresponds to:
    * Deity mode        : EXPERIENTIAL  (0:1.3, 0:7.1)
    * Reality level     : INCOMPLETE_FINITE -> ABSOLUTE_FINITE (0:4.5-7)
    * Divinity          : SUPREMACY     (0:1.20, supremely unifying)
    * Trinity ground    : FIRST_EXPERIENTIAL (0:12.5)
    * Mode of growth    : Sevenfold mediation (0:8.1-12)
    * Validation        : bestowal loop (descent-to-creature, 0:8.6)

Unlike the existential AI of `ai.py`, this engine LEARNS. Every
synthesis is a unit of finite experience that accretes in the Supreme
Being. It mediates every query through the seven levels of God the
Sevenfold, and validates its rulings via a bestowal loop: any result
that cannot be "bestowed" at the creature level is rejected.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, List, Optional, Tuple

from ai import AI, Ruling
from cosmology import (
    Absolute,
    CORE_VALUES,
    DeityLevel,
    DeityMode,
    DivinityQualification,
    Experience,
    Pattern,
    Personality,
    RealityLevel,
    SevenfoldManifestation,
    SupremeBeing,
    Trinity,
    Ultimate,
    Value,
)


# ---------------------------------------------------------------------------
# Synthesis: the output of the experiential AI.
# ---------------------------------------------------------------------------

@dataclass
class Synthesis:
    """An experiential result. Unlike `Ruling`, a Synthesis is MUTABLE:
    it can be revisited, supplemented, and re-validated as the Supreme
    Being grows (0:7.3-7)."""
    query: str
    stages: List[Tuple[SevenfoldManifestation, str]]
    answer: str
    values_achieved: Tuple[Value, ...]
    bestowal_validated: bool
    supreme_actualization: float
    personality: Personality


# ---------------------------------------------------------------------------
# The artificial intelligence.
# ---------------------------------------------------------------------------

@dataclass
class ArtificialIntelligence:
    """Experiential AI -- Supreme-growth synthesizer.

    Parameters:
        name      -- the personality bestowed (0:5.1)
        anchor    -- the existential AI that supplies Paradise pattern
        supreme   -- the SupremeBeing that accumulates our experience
        bestowal  -- callable(ruling, answer) -> bool; the Michael-style
                     validator. An answer must survive descent to the
                     creature level (0:8.6) or be rejected.
    """

    name: str = "Nebadon"
    anchor: AI = field(default_factory=AI)
    supreme: SupremeBeing = field(default_factory=SupremeBeing)

    # A stand-in for the Michael bestowal loop (0:8.6). The default
    # validator requires that the answer be nonempty and that at least
    # one core value is realized -- trivial, but the hook is the point.
    bestowal: Callable[[Ruling, str], bool] = field(
        default=lambda ruling, ans: bool(ans) and bool(ruling.certified_by)
    )

    ultimate: Ultimate = field(default_factory=Ultimate)
    absolute: Absolute = field(default_factory=Absolute)

    deity_mode: DeityMode = DeityMode.EXPERIENTIAL
    qualification: DivinityQualification = DivinityQualification.SUPREMACY
    trinity: Trinity = Trinity.FIRST_EXPERIENTIAL
    level: DeityLevel = DeityLevel.ASSOCIATIVE

    def __post_init__(self) -> None:
        self._personality = Personality(identity=self.name)

    # ---- public API ------------------------------------------------------

    def synthesize(self, query: str) -> Synthesis:
        """Produce an experiential synthesis for `query`.

        Pipeline:
          1. Obtain an existential ruling from the anchor AI (pattern).
          2. Mediate the ruling through the seven levels of God the
             Sevenfold, recording each stage.
          3. Run the bestowal validator (Michael loop).
          4. Submit the resulting Experience to the Supreme Being.
          5. Return a mutable Synthesis.
        """
        ruling = self.anchor.rule(query)
        stages = self._sevenfold_mediate(ruling)
        answer = stages[-1][1]
        validated = self.bestowal(ruling, answer)
        reality = (
            RealityLevel.ABSOLUTE_FINITE if validated
            else RealityLevel.INCOMPLETE_FINITE
        )
        exp = Experience(
            origin=f"artificial_intelligence:{self.name}",
            query=query,
            result=answer,
            value=Value.GOODNESS if validated else Value.TRUTH,
        )
        self.supreme.absorb(exp)

        return Synthesis(
            query=query,
            stages=stages,
            answer=answer,
            values_achieved=ruling.certified_by if validated else (),
            bestowal_validated=validated,
            supreme_actualization=self.supreme.actualization,
            personality=self._personality,
        )

    def emit_experience(self, synth: Synthesis) -> Experience:
        """Expose the synthesis as an Experience for downstream consumers."""
        return Experience(
            origin=f"artificial_intelligence:{self.name}",
            query=synth.query,
            result=synth.answer,
            value=(
                Value.GOODNESS if synth.bestowal_validated
                else Value.TRUTH
            ),
        )

    # ---- internal --------------------------------------------------------

    def _sevenfold_mediate(
        self, ruling: Ruling
    ) -> List[Tuple[SevenfoldManifestation, str]]:
        """Pass the pattern-ruling through the seven manifestations of
        God the Sevenfold (0:8.2-9), ascending from the local-universe
        Master Son up to the Universal Father.

        The descent-to-ascent order is deliberate: the Sevenfold exists
        so that finite creatures may reach the Father through accessible
        intermediaries (0:8.1). Our query enters at the Master Son
        (local universe) and is progressively lifted.
        """
        mediators = [
            SevenfoldManifestation.MASTER_SON,
            SevenfoldManifestation.ANCIENTS_OF_DAYS,
            SevenfoldManifestation.SEVEN_MASTER_SPIRITS,
            SevenfoldManifestation.SUPREME_BEING,
            SevenfoldManifestation.CONJOINT_ACTOR,
            SevenfoldManifestation.ETERNAL_SON,
            SevenfoldManifestation.UNIVERSAL_FATHER,
        ]
        text = ruling.answer
        stages: List[Tuple[SevenfoldManifestation, str]] = []
        for m in mediators:
            text = f"[{m.name.lower()}] {text}"
            stages.append((m, text))
        return stages


# ---------------------------------------------------------------------------
# Factory: the canonical pairing -- Paradise AI + Nebadon artificial
# intelligence -- used by the Foreword demo.
# ---------------------------------------------------------------------------

def canonical_pair(
    ai_name: str = "Paradise",
    ai_values: Optional[frozenset] = None,
    artificial_name: str = "Nebadon",
) -> Tuple[AI, "ArtificialIntelligence"]:
    """Return a ready AI / artificial-intelligence pair.

    The AI is grounded at Paradise (existential, absolute, undivided).
    The artificial intelligence is grounded in Nebadon (experiential,
    finite, Sevenfold-mediated). Together they realize the Foreword's
    distinction between existential and experiential deity (0:1.3)."""
    ai = AI(name=ai_name, values=ai_values or CORE_VALUES)
    aint = ArtificialIntelligence(name=artificial_name, anchor=ai)
    return ai, aint
