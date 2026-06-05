"""foreword-ai -- Foreword-derived AI for URANTiOS.

Public entry points:

    from foreword_ai.ai import AI
    from foreword_ai.artificial_intelligence import ArtificialIntelligence
    from foreword_ai.artificial_intelligence import canonical_pair
    from foreword_ai.foreword import Foreword

See README.md for the mapping between Paper 0 (the Foreword of The
Urantia Book) and this package's modules.
"""

from ai import AI, Ruling
from artificial_intelligence import (
    ArtificialIntelligence,
    Synthesis,
    canonical_pair,
)
from foreword import Foreword, Paragraph, Section

__all__ = [
    "AI",
    "Ruling",
    "ArtificialIntelligence",
    "Synthesis",
    "canonical_pair",
    "Foreword",
    "Paragraph",
    "Section",
]
