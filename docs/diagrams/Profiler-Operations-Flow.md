# MindFirst Engine - Profiler Operations Flow

[↩️ Back to Documentation Index](../index.md)

---

## OS Profiler Detailed Flow

The OS Profiler is the first active subsystem in M1E, responsible for extracting cognitive-structural signals from user communication without any demographic inference.

---

## High-Level Profiler Pipeline

```
┌───────────────────┐
│   User Input      │
│  (Raw Text/Speech)│
└─────────┬─────────┘
          │
          ▼
┌─────────────────────────────────────────────┐
│     PREPROCESSING & TOKENIZATION            │
│  • Normalize input format                   │
│  • Remove metadata (device, location, etc.) │
│  • Tokenize linguistic stream               │
└─────────┬───────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────┐
│      PARALLEL SIGNAL EXTRACTION             │
│                                              │
│  ┌────────────┐  ┌────────────┐            │
│  │ Recursion  │  │Compression │            │
│  │  Analysis  │  │   Index    │            │
│  └────────────┘  └────────────┘            │
│                                              │
│  ┌────────────┐  ┌────────────┐            │
│  │ Analytical │  │  Tangent   │            │
│  │   Tempo    │  │Probability │            │
│  └────────────┘  └────────────┘            │
│                                              │
│  ┌────────────┐  ┌────────────┐            │
│  │    Meta    │  │ Emotional  │            │
│  │ Monitoring │  │   Pacing   │            │
│  └────────────┘  └────────────┘            │
│                                              │
│  ┌────────────┐                             │
│  │  Conflict  │                             │
│  │  Handling  │                             │
│  └────────────┘                             │
└─────────┬───────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────┐
│       SIGNAL AGGREGATION & MAPPING          │
│  • Combine extracted signals                │
│  • Generate OS Map structure                │
│  • Apply normalization                      │
└─────────┬───────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────┐
│      POST-IDENTITY SAFETY CHECK             │
│  • Verify no demographic data present       │
│  • Block identity inference attempts        │
│  • Ensure cognitive-only signals            │
└─────────┬───────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────┐
│          OUTPUT: OS MAP                     │
│  {                                           │
│    recursion_depth: float,                  │
│    compression_factor: float,               │
│    tangent_probability: float,              │
│    meta_monitoring_density: float,          │
│    analytical_tempo: categorical,           │
│    conflict_style: categorical,             │
│    pacing_rhythm: vectorized_signature      │
│  }                                           │
└──────────────────────────────────────────────┘
```

---

## Detailed Signal Extraction Processes

### 1. Recursion Depth Analysis

```
Input Text
    │
    ▼
┌─────────────────────────┐
│ Parse Sentence Structure│
│ • Identify clauses      │
│ • Track nesting levels  │
│ • Count embedded logic  │
└───────┬─────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Measure Depth Patterns  │
│ • Max nesting depth     │
│ • Average depth         │
│ • Depth variance        │
└───────┬─────────────────┘
        │
        ▼
   recursion_depth: float
```

**Example Patterns**:
- **Low recursion** (1.2): "I like this. It works well. Simple design."
- **Medium recursion** (2.5): "I like this because it works well, which is important for my needs."
- **High recursion** (4.8): "I like this (because it works well for my needs (which are fairly specific (given my use case))), so I'll use it."

---

### 2. Compression/Expansion Index

```
Input Text
    │
    ▼
┌─────────────────────────┐
│ Measure Information     │
│ Density                 │
│ • Words per concept     │
│ • Elaboration patterns  │
│ • Redundancy analysis   │
└───────┬─────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Calculate Index         │
│ • Compression: < 1.0    │
│ • Neutral: ≈ 1.0        │
│ • Expansion: > 1.0      │
└───────┬─────────────────┘
        │
        ▼
 compression_factor: float
```

**Example Patterns**:
- **Compressed** (0.4): "Need fix. Bug #42. ASAP."
- **Neutral** (1.0): "There's a bug in issue #42 that needs fixing soon."
- **Expanded** (2.3): "I've noticed there seems to be a problem with the functionality described in issue #42, and I think it would be helpful if we could address it relatively soon."

---

### 3. Analytical Tempo Detection

```
Input Text
    │
    ▼
┌─────────────────────────┐
│ Analyze Pacing          │
│ • Sentence length dist. │
│ • Connective frequency  │
│ • Topic shift velocity  │
└───────┬─────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Categorize Tempo        │
│ • rapid: Fast shifts    │
│ • steady: Even pacing   │
│ • methodical: Deliberate│
│ • variable: Mixed       │
└───────┬─────────────────┘
        │
        ▼
analytical_tempo: categorical
```

---

### 4. Tangent Probability Measurement

```
Input Text (Multiple Messages)
    │
    ▼
┌─────────────────────────┐
│ Track Topic Coherence   │
│ • Main topic detection  │
│ • Branch point counting │
│ • Return-to-main freq.  │
└───────┬─────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Calculate Probability   │
│ • Branch frequency      │
│ • Branch depth          │
│ • Branch resolution     │
└───────┬─────────────────┘
        │
        ▼
tangent_probability: float (0.0 - 1.0)
```

**Interpretation**:
- **Low** (0.1-0.3): Stays focused on main topic
- **Medium** (0.4-0.6): Occasional related tangents
- **High** (0.7-1.0): Frequent exploration and branching

---

### 5. Meta-Monitoring Density

```
Input Text
    │
    ▼
┌─────────────────────────┐
│ Detect Meta-Markers     │
│ • "let me check..."     │
│ • "wait, that doesn't..." │
│ • "actually, I meant..."│
│ • Self-corrections      │
│ • Expectation tracking  │
└───────┬─────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Count & Normalize       │
│ • Markers per message   │
│ • Pattern over session  │
└───────┬─────────────────┘
        │
        ▼
meta_monitoring_density: float
```

---

### 6. Emotional Pacing Markers

```
Input Text
    │
    ▼
┌─────────────────────────┐
│ Extract Affective Timing│
│ • NOT emotional state   │
│ • Timing of affect      │
│ • Topic oscillation     │
│ • Stabilization attempts│
└───────┬─────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Pattern Recognition     │
│ • Pace of change        │
│ • Recovery time         │
│ • Consistency level     │
└───────┬─────────────────┘
        │
        ▼
emotional_pacing: vectorized
```

**Important**: This does NOT infer emotional states, only pacing patterns.

---

### 7. Conflict-Handling Patterns

```
Input Text (Clarification/Disagreement Contexts)
    │
    ▼
┌─────────────────────────┐
│ Identify Repair Strategy│
│ • Clarification requests│
│ • Concession patterns   │
│ • Redirection attempts  │
│ • Analytical challenges │
│ • Avoidance behaviors   │
└───────┬─────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Categorize Style        │
│ • collaborative         │
│ • analytical            │
│ • avoidant              │
│ • direct                │
└───────┬─────────────────┘
        │
        ▼
conflict_style: categorical
```

---

## Prohibited Operations (Safety Constraints)

```
┌─────────────────────────────────────────────┐
│         WHAT THE PROFILER MUST NOT DO       │
├─────────────────────────────────────────────┤
│ ❌ Infer gender from communication style    │
│ ❌ Infer race from linguistic patterns      │
│ ❌ Infer age from vocabulary choices        │
│ ❌ Infer nationality from any signals       │
│ ❌ Use demographic priors/stereotypes       │
│ ❌ Predict identity categories              │
│ ❌ Store long-term identity data            │
│ ❌ Interpret emotional pacing as emotion    │
└─────────────────────────────────────────────┘
```

These exclusions are **architectural constraints**, not optional guidelines.

---

## Error Handling & Drift Management

```
Continuous Monitoring
        │
        ▼
┌─────────────────────────┐
│ Detect Anomalies        │
│ • Sudden style shifts   │
│ • Intentional changes   │
│ • Context switches      │
│ • Testing behaviors     │
└───────┬─────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Decision Logic          │
│ Is it drift or intent?  │
└───┬─────────────────┬───┘
    │                 │
    │ Drift           │ Intent
    ▼                 ▼
┌─────────┐      ┌─────────┐
│Recali-  │      │  Adapt  │
│brate    │      │ Profile │
└─────────┘      └─────────┘
```

---

## Output Format

The Profiler produces a structured OS Map consumed by the Interpreter:

```json
{
  "recursion_depth": 2.7,
  "compression_factor": 1.2,
  "tangent_probability": 0.45,
  "meta_monitoring_density": 0.32,
  "analytical_tempo": "steady",
  "conflict_style": "collaborative",
  "pacing_rhythm": [0.8, 1.1, 0.9, 1.0],
  "session_context": {
    "message_count": 12,
    "stability_score": 0.87,
    "confidence": 0.92
  },
  "safety_validated": true,
  "timestamp": "2025-12-11T22:44:00Z"
}
```

---

## Integration with Other Subsystems

```
OS Profiler
     │
     ├──────────► OS Interpreter (consumes OS Map)
     │
     ├──────────► OS Stabiliser (monitors for drift)
     │
     └──────────► Audit Log (transparency/compliance)
```

---

## Performance Considerations

- **Latency**: < 50ms for signal extraction per message
- **Memory**: Minimal (session-scoped only, no long-term storage)
- **Accuracy**: Improves over first 3-5 interactions
- **Adaptation**: Real-time recalibration when patterns shift

---

[↩️ Back to Documentation Index](../index.md) | [🏗️ Architecture Diagram](./OS-Map-Architecture.md) | [📘 Technical Specification](../phase3/Phase%203%20—%20Technical%20Specification%20of%20the%20MindFirst%20Engine%20(M1E).md)
