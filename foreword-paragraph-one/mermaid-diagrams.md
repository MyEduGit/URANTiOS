# Mermaid Diagrams — Seven Aspects of Human Perception

Renderable in GitHub, Obsidian, or any Mermaid-compatible viewer.

---

## 1. Consciousness Tier Hierarchy (Top-Down)

```mermaid
graph TD
    SUPER["🔆 SUPERCONSCIOUS"]
    CON["🧠 CONSCIOUS"]
    SUB["🌊 SUBCONSCIOUS"]
    UNC["⬛ UNCONSCIOUS"]

    SUPER --> A7["7 · Revelatory Reception<br/><i>Orvonton corps … translate</i>"]
    CON --> A1["1 · Mind<br/><i>IN THE MINDS of the mortals</i>"]
    CON --> A2["2 · Meaning-Seeking<br/><i>meaning of … God, divinity, deity</i>"]
    CON --> A6["6 · Symbolic Mediation<br/><i>word symbols … meanings attached</i>"]
    SUB --> A3["3 · Relational Perception<br/><i>relationships of divine personalities</i>"]
    SUB --> A5["5 · Ideational Confusion<br/><i>ideational confusion</i>"]
    UNC --> A4["4 · Conceptual Poverty<br/><i>conceptual poverty</i>"]

    A7 -.->|"revelation<br/>descends"| A1
    A1 -->|"seeks"| A2
    A2 -->|"requires"| A6
    A1 -->|"dimly senses"| A3
    A3 -.->|"generates"| A5
    A5 -.->|"rooted in"| A4
    A6 -.->|"bridges"| A7

    style SUPER fill:#FFD700,stroke:#B8860B,color:#000
    style CON fill:#87CEEB,stroke:#4682B4,color:#000
    style SUB fill:#DDA0DD,stroke:#8B008B,color:#000
    style UNC fill:#696969,stroke:#2F4F4F,color:#FFF
    style A7 fill:#FFF8DC,stroke:#DAA520
    style A1 fill:#E0F0FF,stroke:#4682B4
    style A2 fill:#E0F0FF,stroke:#4682B4
    style A6 fill:#E0F0FF,stroke:#4682B4
    style A3 fill:#F0E0F0,stroke:#8B008B
    style A5 fill:#F0E0F0,stroke:#8B008B
    style A4 fill:#A0A0A0,stroke:#2F4F4F,color:#FFF
```

---

## 2. Radial / Sunburst View

```mermaid
mindmap
  root((MORTAL MIND))
    CONSCIOUS
      1 Mind
        Field of awareness
        Substrate of thought
      2 Meaning-Seeking
        God
        Divinity
        Deity
      6 Symbolic Mediation
        Word symbols
        Meanings attached
        English language
    SUBCONSCIOUS
      3 Relational Perception
        Divine personalities
        Numerous appellations
        Relationships
      5 Ideational Confusion
        Signal noise
        Misattribution
        Category error
    UNCONSCIOUS
      4 Conceptual Poverty
        Unknown unknowns
        Absent frameworks
        Missing vocabulary
    SUPERCONSCIOUS
      7 Revelatory Reception
        Orvonton corps
        Truth revealers
        Authorized translation
```

---

## 3. Flow Diagram — From Poverty to Reception

```mermaid
flowchart LR
    A4["4 · Conceptual<br/>Poverty"] -->|"breeds"| A5["5 · Ideational<br/>Confusion"]
    A5 -->|"obscures"| A3["3 · Relational<br/>Perception"]
    A3 -->|"feeds back to"| A5
    A5 -->|"experienced as"| A2["2 · Meaning-<br/>Seeking"]
    A2 -->|"frustrated, turns to"| A6["6 · Symbolic<br/>Mediation"]
    A6 -->|"opens channel for"| A7["7 · Revelatory<br/>Reception"]
    A7 -->|"illuminates"| A1["1 · Mind"]
    A1 -->|"renews"| A2
    A7 -.->|"dissolves"| A4

    style A4 fill:#696969,color:#FFF
    style A5 fill:#DDA0DD
    style A3 fill:#DDA0DD
    style A2 fill:#87CEEB
    style A6 fill:#87CEEB
    style A7 fill:#FFD700
    style A1 fill:#87CEEB
```

---

## 4. Sankey-Style: Revelation → Mortal Cognition

```mermaid
flowchart TD
    SOURCE["SOURCE<br/>Paradise Truth"] ==>|"authorized"| A7["7 · Revelatory<br/>Reception"]
    A7 ==>|"translated into"| A6["6 · Symbolic<br/>Mediation"]
    A6 ==>|"words carry meaning to"| A1["1 · Mind"]
    A1 ==>|"activates"| A2["2 · Meaning-<br/>Seeking"]
    A1 ==>|"partially reaches"| A3["3 · Relational<br/>Perception"]
    A2 -->|"blocked by"| A5["5 · Ideational<br/>Confusion"]
    A3 -->|"blocked by"| A5
    A5 -->|"caused by"| A4["4 · Conceptual<br/>Poverty"]

    style SOURCE fill:#FFFACD,stroke:#DAA520
    style A7 fill:#FFD700,stroke:#B8860B
    style A6 fill:#98FB98,stroke:#228B22
    style A1 fill:#87CEEB,stroke:#4682B4
    style A2 fill:#87CEEB,stroke:#4682B4
    style A3 fill:#DDA0DD,stroke:#8B008B
    style A5 fill:#FF6347,stroke:#B22222,color:#FFF
    style A4 fill:#696969,stroke:#2F4F4F,color:#FFF
```

---

## 5. Sequence Diagram — The Revelation Transaction

```mermaid
sequenceDiagram
    participant P as Paradise Truth
    participant O as Orvonton Corps
    participant S as Word Symbols
    participant M as Mortal Mind
    participant C as Confusion Zone
    participant V as Conceptual Void

    P->>O: Authorize revelation
    O->>S: Translate into English
    S->>M: Present word symbols
    M->>M: Activate Meaning-Seeking (2)
    M->>C: Encounter Relational Perception (3)
    C->>C: Ideational Confusion (5) amplifies
    C->>V: Rooted in Conceptual Poverty (4)
    O-->>M: Symbolic Mediation (6) bridges gap
    Note over M,P: Revelatory Reception (7) — the downreach completes
    M->>M: Mind (1) integrates new meaning
```

---

## 6. State Diagram — Mortal Cognitive States

```mermaid
stateDiagram-v2
    [*] --> ConceptualPoverty: birth
    ConceptualPoverty --> IdeationalConfusion: exposure to terms
    IdeationalConfusion --> MeaningSeeking: curiosity arises
    MeaningSeeking --> RelationalPerception: patterns dimly sensed
    RelationalPerception --> IdeationalConfusion: complexity overwhelms
    MeaningSeeking --> SymbolicMediation: word-symbols studied
    SymbolicMediation --> RevelatoryReception: channel opens
    RevelatoryReception --> MindIntegration: truth grasped
    MindIntegration --> MeaningSeeking: deeper questions
    MindIntegration --> [*]: clarity achieved

    state ConceptualPoverty {
        [*] --> absent_frameworks
        absent_frameworks --> unknown_unknowns
    }
    state RevelatoryReception {
        [*] --> orvonton_translation
        orvonton_translation --> authorized_papers
    }
```

---

## 7. Pie Chart — Cognitive Load Distribution (Hypothetical Pre-Revelation Mortal)

```mermaid
pie title Cognitive Load Before Revelation
    "1 · Mind (substrate)" : 15
    "2 · Meaning-Seeking" : 20
    "3 · Relational Perception" : 10
    "4 · Conceptual Poverty" : 25
    "5 · Ideational Confusion" : 22
    "6 · Symbolic Mediation" : 5
    "7 · Revelatory Reception" : 3
```

---

## 8. Quadrant Chart — Aspect Positioning

```mermaid
quadrantChart
    title Aspects by Accessibility vs. Transformative Power
    x-axis Low Accessibility --> High Accessibility
    y-axis Low Transformative Power --> High Transformative Power
    quadrant-1 High Access + High Transform
    quadrant-2 Low Access + High Transform
    quadrant-3 Low Access + Low Transform
    quadrant-4 High Access + Low Transform
    Mind: [0.8, 0.3]
    Meaning-Seeking: [0.7, 0.5]
    Relational Perception: [0.3, 0.6]
    Conceptual Poverty: [0.1, 0.2]
    Ideational Confusion: [0.6, 0.15]
    Symbolic Mediation: [0.75, 0.7]
    Revelatory Reception: [0.15, 0.95]
```

---

## 9. Entity-Relationship Diagram — Ontology

```mermaid
erDiagram
    MIND ||--o{ MEANING_SEEKING : "activates"
    MIND ||--o{ RELATIONAL_PERCEPTION : "dimly senses"
    MEANING_SEEKING ||--|| SYMBOLIC_MEDIATION : "requires"
    RELATIONAL_PERCEPTION ||--o{ IDEATIONAL_CONFUSION : "generates"
    IDEATIONAL_CONFUSION }|--|| CONCEPTUAL_POVERTY : "rooted in"
    SYMBOLIC_MEDIATION ||--|| REVELATORY_RECEPTION : "opens channel for"
    REVELATORY_RECEPTION ||--|| MIND : "illuminates"
    REVELATORY_RECEPTION }o--|| CONCEPTUAL_POVERTY : "dissolves"

    MIND {
        string tier "Conscious"
        string source_phrase "IN THE MINDS of the mortals"
    }
    MEANING_SEEKING {
        string tier "Conscious"
        string source_phrase "meaning of God divinity deity"
    }
    RELATIONAL_PERCEPTION {
        string tier "Subconscious"
        string source_phrase "relationships of divine personalities"
    }
    CONCEPTUAL_POVERTY {
        string tier "Unconscious"
        string source_phrase "conceptual poverty"
    }
    IDEATIONAL_CONFUSION {
        string tier "Subconscious"
        string source_phrase "ideational confusion"
    }
    SYMBOLIC_MEDIATION {
        string tier "Conscious"
        string source_phrase "word symbols meanings attached"
    }
    REVELATORY_RECEPTION {
        string tier "Superconscious"
        string source_phrase "Orvonton corps truth revealers translate"
    }
```

---

## 10. Timeline — The Cognitive Journey

```mermaid
timeline
    title The Mortal Cognitive Journey Through Seven Aspects
    section Unconscious Origin
        Conceptual Poverty : The mortal begins in darkness : Frameworks for deity-understanding are absent : "Unknown unknowns"
    section Subconscious Stirring
        Ideational Confusion : Exposure to religious terms creates noise : Symbols float without anchoring : Category errors multiply
        Relational Perception : Patterns among divine names dimly sensed : Relationships suspected but not grasped : Intuition without vocabulary
    section Conscious Engagement
        Mind Activation : The mortal becomes aware of confusion : Awareness of awareness : The field is lit
        Meaning-Seeking : Active pursuit of definitions : What does God mean? Divinity? Deity? : Conceptual grasping begins
        Symbolic Mediation : Word-symbols studied as bridges : Meanings attached to terms : Language becomes the instrument
    section Superconscious Contact
        Revelatory Reception : The Orvonton corps reaches down : Truth translated into mortal language : The circuit completes
```

---

*All diagrams render natively on GitHub and in Obsidian.*
