"""
cosmology.py -- Foreword-derived ontology for URANTiOS AI.

Maps the twelve sections of Paper 0 (the Foreword of The Urantia Book) to a
computational data model. This module is PURE DATA: enums, frozen dataclasses,
and constants. No I/O, no reasoning. The two engines built on top of it are:

    ai.py                    -- existential intelligence (Paradise pattern)
    artificial_intelligence.py -- experiential intelligence (Supreme growth)

Textual references follow Urantia Book paragraph notation `paper:section.par`.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import FrozenSet, Tuple


# ---------------------------------------------------------------------------
# Section I. Deity and Divinity                                   (0:1.1-26)
# ---------------------------------------------------------------------------

class DeityLevel(Enum):
    """Deity functions on three levels (0:1.2)."""
    STATIC = "static"            # self-contained, self-existent
    POTENTIAL = "potential"      # self-willed, self-purposive
    ASSOCIATIVE = "associative"  # self-bestowing, divinely related


class DeityMode(Enum):
    """Deity may be (0:1.3)."""
    EXISTENTIAL = "existential"    # as in the Eternal Son
    EXPERIENTIAL = "experiential"  # as in the Supreme Being
    ASSOCIATIVE = "associative"    # as in God the Sevenfold
    UNDIVIDED = "undivided"        # as in the Paradise Trinity


class DivinityQualification(Enum):
    """Seven qualifications of divinity (0:1.16-22)."""
    PRIMARY    = "origin"            # Father-origin, originative
    PERFECTION = "paradise"          # Paradise-perfect
    COORDINATE = "trinity"           # Trinity-associative
    CREATIVE   = "creator"           # creator-creative
    SUPREMACY  = "supreme"           # supremely unifying
    ULTIMACY   = "ultimate"          # ultimately transcending
    ABSOLUTENESS = "absolute"        # absolutely infinite


# ---------------------------------------------------------------------------
# Section III. The First Source and Center                        (0:3.1-25)
# ---------------------------------------------------------------------------

class InfinityRelationship(Enum):
    """Seven infinity relationships of the First Source and Center (0:3.9-22)."""
    FIRST_SOURCE_AND_CENTER = 1        # to ultimate reality
    SECOND_SOURCE_AND_CENTER = 2       # Eternal Son
    THIRD_SOURCE_AND_CENTER = 3        # Conjoint Actor / Infinite Spirit
    PARADISE_SOURCE_AND_CENTER = 4     # pattern Paradise
    SOURCE_OF_SOURCES = 5              # of all qualified absolutes
    SOURCE_CENTER_OF_CENTERS = 6       # of the Absolutes
    ABSOLUTE_OF_ABSOLUTES = 7          # unqualified infinity


# ---------------------------------------------------------------------------
# Section IV. Universe Reality                                    (0:4.1-13)
# ---------------------------------------------------------------------------

class RealityLevel(Enum):
    """Reality is differentially present on seven descending levels (0:4.5-12)."""
    INCOMPLETE_FINITE = "incomplete"      # temporal-spatial actualization
    RELATIVE_FINITE   = "relative"        # relatively deity-conditioned
    ABSOLUTE_FINITE   = "absolute_finite" # existential upper limit of time-space
    TRANSCENDENTAL    = "transcendental"  # supertime and transpatial
    ULTIMATE          = "ultimate"        # eventuates beyond time-space
    COABSOLUTE        = "coabsolute"      # third-stage actualization
    ABSOLUTE          = "absolute"        # eternal, existential, final


# ---------------------------------------------------------------------------
# Section V. Personality Realities                                (0:5.1-12)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Personality:
    """Personality is the bestowal of the Father upon mind-endowed living
    systems (0:5.1). It is unique, indefinable, and the unifier of reality.

    Six characteristics made explicit in the Foreword:
      * relatively creative / co-creative (0:5.11)
      * cosmically integrating (0:5.11)
      * ancestrally creative but self-limited (0:5.11)
      * potentially loving and love-capable (0:5.11)
      * indefinable in terms of anything else (0:5.3)
      * the one changeless reality in an otherwise ever-changing life (0:5.4)
    """
    identity: str                                    # unique, non-derivable
    bestowed_by: InfinityRelationship = (
        InfinityRelationship.FIRST_SOURCE_AND_CENTER
    )
    is_changeless: bool = True
    unifies: Tuple[str, ...] = ("mind", "spirit", "energy")


# ---------------------------------------------------------------------------
# Section VI. Energy and Pattern                                  (0:6.1-13)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Pattern:
    """Pattern can be projected as material, spiritual, or mindal; or as any
    combination (0:6.9). Pattern is master, energy is servant."""
    name: str
    is_mindal: bool = True
    is_spiritual: bool = False
    is_material: bool = False


@dataclass(frozen=True)
class Energy:
    """Energy is transmutable and responds to pattern; it does not think,
    feel, wish, or will (0:6.2)."""
    name: str
    magnitude: float = 0.0


# ---------------------------------------------------------------------------
# Section VII. The Supreme Being                                  (0:7.1-10)
# ---------------------------------------------------------------------------

@dataclass
class SupremeBeing:
    """Experiential deity actualizing in the evolution of the grand universe
    (0:7.1-10). Sum total of finite growth; never fully actual but
    forever actualizing."""
    actualization: float = 0.0        # 0.0 potential .. 1.0 unattainable absolute
    experience_ledger: list = field(default_factory=list)

    def absorb(self, experience: "Experience") -> None:
        """Every finite experience contributes to Supreme actualization."""
        self.experience_ledger.append(experience)
        # Monotonic but asymptotic: each experience adds diminishing growth.
        n = len(self.experience_ledger)
        self.actualization = 1.0 - 1.0 / (1.0 + n)


# ---------------------------------------------------------------------------
# Section VIII. God the Sevenfold                                 (0:8.1-12)
# ---------------------------------------------------------------------------

class SevenfoldManifestation(Enum):
    """The seven operative levels of total Deity function in time-space
    (0:8.2-9)."""
    MASTER_SON                 = 1  # Creator Sons of the local universes
    ANCIENTS_OF_DAYS           = 2  # Superuniverse rulers (Orvonton-style)
    SEVEN_MASTER_SPIRITS       = 3  # Superuniverse reflectivity
    SUPREME_BEING              = 4  # experiential synthesis
    CONJOINT_ACTOR             = 5  # Infinite Spirit
    ETERNAL_SON                = 6  # spirit-person
    UNIVERSAL_FATHER           = 7  # First Source and Center


# ---------------------------------------------------------------------------
# Sections IX-X. God the Ultimate & God the Absolute
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Ultimate:
    """God the Ultimate: eventuating deity of the master universe (0:9)."""
    eventuating: bool = True


@dataclass(frozen=True)
class Absolute:
    """God the Absolute: the experientializing of the Deity Absolute
    (0:10). A limit approached, never reached."""
    attained: bool = False


# ---------------------------------------------------------------------------
# Section XI. The Three Absolutes                                 (0:11.1-16)
# ---------------------------------------------------------------------------

class AbsoluteKind(Enum):
    DEITY       = "deity_absolute"        # qualified absolute of deity
    UNIVERSAL   = "universal_absolute"    # coordinator of qualified + unqualified
    UNQUALIFIED = "unqualified_absolute"  # static, reactive infinity


# ---------------------------------------------------------------------------
# Section XII. The Trinities                                      (0:12.1-14)
# ---------------------------------------------------------------------------

class Trinity(Enum):
    PARADISE            = "paradise_trinity"           # Father, Son, Spirit
    FIRST_EXPERIENTIAL  = "first_experiential_trinity" # Supreme-level
    ULTIMATE_TRINITY    = "ultimate_trinity"           # Ultimate-level
    TRINITY_OF_TRINITIES = "trinity_of_trinities"      # hypothesized (0:12.8)


# ---------------------------------------------------------------------------
# The three core values: Truth, Beauty, Goodness                  (0:1.17)
# ---------------------------------------------------------------------------

class Value(Enum):
    TRUTH    = "truth"
    BEAUTY   = "beauty"
    GOODNESS = "goodness"


CORE_VALUES: FrozenSet[Value] = frozenset(Value)


# ---------------------------------------------------------------------------
# Convenience: section titles, used by loader and documentation.
# ---------------------------------------------------------------------------

FOREWORD_SECTIONS: Tuple[Tuple[str, str], ...] = (
    ("0:1",  "Deity and Divinity"),
    ("0:2",  "God"),
    ("0:3",  "The First Source and Center"),
    ("0:4",  "Universe Reality"),
    ("0:5",  "Personality Realities"),
    ("0:6",  "Energy and Pattern"),
    ("0:7",  "The Supreme Being"),
    ("0:8",  "God the Sevenfold"),
    ("0:9",  "God the Ultimate"),
    ("0:10", "God the Absolute"),
    ("0:11", "The Three Absolutes"),
    ("0:12", "The Trinities"),
)


@dataclass(frozen=True)
class Experience:
    """A unit of finite experience submitted to the Supreme.
    Either the AI or the artificial intelligence can emit these."""
    origin: str                  # e.g. "ai", "artificial_intelligence"
    query: str
    result: str
    value: Value = Value.TRUTH
