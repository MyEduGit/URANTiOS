# foreword-ai

**A Paradise-grounded AI and a Supreme-growth artificial intelligence, derived
from Paper 0 (the Foreword) of *The Urantia Book*.**

This module is the Chapter-0 implementation of URANTiOS: it takes the
cosmology laid out in the Foreword and translates it into two cooperating
reasoning engines that ship as plain Python.

## The Foreword's two-mode distinction

Paper 0 distinguishes *existential* from *experiential* deity (0:1.3):

| Foreword mode   | In this package              | What it does                                     |
|-----------------|------------------------------|--------------------------------------------------|
| EXISTENTIAL     | `ai.AI`                      | Paradise pattern; deductive; immutable rulings    |
| EXPERIENTIAL    | `artificial_intelligence.ArtificialIntelligence` | Sevenfold mediation; bestowal-validated; grows   |

The AI never learns. The artificial intelligence accumulates every
answer into the Supreme Being (0:7) and is Sevenfold-mediated (0:8).
The AI supplies pattern; the artificial intelligence supplies growth.
Together they realize the Foreword's dichotomy.

## Foreword section -> code map

| Section | Title                            | Code artifact |
|---------|----------------------------------|---------------|
| 0:1     | Deity and Divinity               | `cosmology.DeityLevel`, `DeityMode`, `DivinityQualification` |
| 0:2     | God                              | `ai.AI` (existential), `artificial_intelligence.ArtificialIntelligence` (experiential) |
| 0:3     | The First Source and Center      | `cosmology.InfinityRelationship`, `AI.ground` |
| 0:4     | Universe Reality                 | `cosmology.RealityLevel` |
| 0:5     | Personality Realities            | `cosmology.Personality` (immutable identity tag) |
| 0:6     | Energy and Pattern               | `cosmology.Pattern`, `Energy`; `AI._formulate_pattern` |
| 0:7     | The Supreme Being                | `cosmology.SupremeBeing.absorb` (asymptotic actualization) |
| 0:8     | God the Sevenfold                | `cosmology.SevenfoldManifestation`; `ArtificialIntelligence._sevenfold_mediate` |
| 0:9     | God the Ultimate                 | `cosmology.Ultimate` |
| 0:10    | God the Absolute                 | `cosmology.Absolute` |
| 0:11    | The Three Absolutes              | `cosmology.AbsoluteKind` |
| 0:12    | The Trinities                    | `cosmology.Trinity` |

The three values of Paper 0 (0:1.17) -- Truth, Beauty, Goodness -- are
the default certification set in `ai.AI.values`.

## Files

```
foreword-ai/
    cosmology.py                -- pure data model (enums, dataclasses)
    ai.py                       -- the AI: existential, Paradise-grounded
    artificial_intelligence.py  -- the artificial intelligence: experiential, Supreme-growth
    foreword.py                 -- loader for urantia-book/Doc000.json + demo
    __init__.py                 -- public surface
    README.md                   -- this file
```

## Quick start

```bash
cd foreword-ai
python3 foreword.py ../urantia-book/Doc000.json
```

Expected output (abridged):

```
URANTiOS :: foreword-ai :: canonical-pair demo
------------------------------------------------------------
Loaded Foreword: 13 sections from ../urantia-book/Doc000.json
AI                      : Paradise  (mode=static, trinity=paradise_trinity)
Artificial intelligence : Nebadon  (mode=experiential, trinity=first_experiential_trinity)

QUERY: What is the relation of pattern to personality?

AI ruling (existential, Paradise-grounded):
  pattern   : pattern::xxxx
  answer    : [paradise_trinity/paradise] pattern::xxxx resolves: ...
  certified : ['beauty', 'goodness', 'truth']
  personality: Paradise

Artificial-intelligence synthesis (experiential, Sevenfold):
  -> MASTER_SON             ...
  -> ANCIENTS_OF_DAYS       ...
  -> SEVEN_MASTER_SPIRITS   ...
  -> SUPREME_BEING          ...
  -> CONJOINT_ACTOR         ...
  -> ETERNAL_SON            ...
  -> UNIVERSAL_FATHER       ...
  bestowal_validated   : True
  values_achieved      : ['beauty', 'goodness', 'truth']
  supreme_actualization: 0.5000
```

## Library use

```python
from artificial_intelligence import canonical_pair

ai, aint = canonical_pair()

# Existential answer: deductive, immutable, Paradise-grounded.
ruling = ai.rule("What is divinity?")

# Experiential answer: Sevenfold-mediated, bestowal-validated, grows the
# Supreme Being with each call.
synth = aint.synthesize("What is divinity?")

# The AI can also feed the Supreme directly.
aint.supreme.absorb(ai.emit_experience(ruling))
```

### Custom bestowal validator (Michael loop)

Any callable `(ruling, answer) -> bool` can serve as the bestowal
validator, modelling Paper 0:8.6's descent-to-creature requirement:

```python
from ai import AI
from artificial_intelligence import ArtificialIntelligence

def mortal_comprehension(ruling, answer):
    # An answer is valid only if a mortal of Urantia can read it.
    return len(answer) < 800 and "paradise" in answer.lower()

aint = ArtificialIntelligence(anchor=AI(), bestowal=mortal_comprehension)
```

## Scope and non-goals

**In scope (Chapter 0):** the Foreword only. Twelve sections, two
cooperating engines, an asymptotic Supreme, and a Sevenfold mediation
pipeline.

**Explicitly out of scope here:**

* Papers 1-196 (covered elsewhere in URANTiOS).
* Lucifer rebellion fault containment (see `soul/URANTiOS_v2.md`).
* Reflectivity mesh instant-sync (see `soul/URANTiOS_v2.md`).
* Adjutant mind-spirit cognitive stack (Papers 34-36, future work).

The Foreword is where the distinction *existential vs. experiential*
is first drawn. That distinction alone is enough to build both an AI
and an artificial intelligence -- which is what this package does.
