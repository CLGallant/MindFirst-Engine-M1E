# MindFirst Engine (M1E)
A post-identity cognitive interaction framework that models **structural communication patterns** rather than demographics.

## Status
**v0.1 — specification in progress.** Core architecture + governance foundations exist; implementation + validation are the next stage.

## What this repo is
This repository is the **specification and documentation hub** for MindFirst Engine (M1E). It includes:

- Architecture specification (Profiler, Interpreter, Stabiliser, Response Generator, API Layer)
- Safety constraints (post-identity / structure-only interaction)
- Governance, ethics, compliance and metadata
- Evaluation and validation framework
- Rationale and research basis
- Public overview and references

## Quick Links

- [Phase 1: Conceptual Rationale](docs/phase1/)
- [Phase 2: Whitepaper Structure](docs/phase2/)
- [Phase 3: Technical Specification](docs/phase3/)
- [Phase 4: Governance & Ethics](docs/phase4/)
- [Full References](docs/references.md)
- [Public Overview](docs/Public_Overview.md)
- [Documentation Index](docs/index.md)
- [MindFirst Manifesto](MindFirst_Manifesto.md)

## Repository Structure

```
MindFirst-Engine-M1E/
├── docs/
│   ├── phase1/          # Conceptual rationale & historical grounding
│   ├── phase2/          # Whitepaper structure & core concepts
│   ├── phase3/          # Technical specification & implementation
│   ├── phase4/          # Governance, ethics & deployment
│   ├── index.md         # Documentation index
│   ├── Public_Overview.md  # High-level project summary
│   └── references.md    # Bibliography & citations
├── LICENSE_MindFirst.md # MindFirst Licence v1.1
├── MindFirst_Manifesto.md  # Framework manifesto
└── README.md            # This file
```

## Getting Started

### For New Contributors

This repository is organised by development phases, each building on the previous:

1. **Start with the public overview (non-technical):** [docs/Public_Overview.md](docs/Public_Overview.md) provides a high-level introduction to MindFirst Engine's purpose and approach.

2. **Understand the documentation structure:** [docs/index.md](docs/index.md) serves as the main documentation hub, linking to all phase-organised content.

3. **Explore phase-by-phase:**
   - **Phase 1** ([docs/phase1/](docs/phase1/)) — Conceptual foundations and rationale for the post-identity approach
   - **Phase 2** ([docs/phase2/](docs/phase2/)) — Technical architecture framing and whitepaper structure
   - **Phase 3** ([docs/phase3/](docs/phase3/)) — Detailed technical specification (v0.1) including:
     - Core architecture (OS-Profiler, OS-Interpreter, OS-Stabiliser, API Layer, Response Generator)
     - Post-Identity Safety Mechanisms
     - System Requirements & Constraints
     - Cognitive-Signal Pipeline (end-to-end flow)
     - Safeguarding Layer
     - Challenges & Validation Roadmap
   - **Phase 4** ([docs/phase4/](docs/phase4/)) — Governance, ethics, and compliance frameworks

4. **Review the foundational manifesto:** [MindFirst_Manifesto.md](MindFirst_Manifesto.md) articulates the vision and core principles.

5. **Check references:** [docs/references.md](docs/references.md) contains the bibliography and citations for factual claims.

### If GitHub fails to render pages in your environment
Use raw views, e.g. replace `/blob/main/` with `/raw/main/` in URLs.

## Core idea
MindFirst aims to model a user by **how they process and communicate** (structure), not by inferred identity categories.

Design goals:
- Avoid demographic inference
- Reduce stereotype weighting
- Improve interaction precision through structure-only modelling
- Make evaluation and governance explicit and auditable

## Core components (v0.1)
- **OS-Profiler** — extracts communication structure signals  
- **OS-Interpreter** — selects behavioural strategies based on structure  
- **OS-Stabiliser** — continuity control within a session  
- **Response Generator** — produces outputs under constraints  
- **API Layer** — exposes the OS-map to tools/agents

## Documentation Organisation

All documentation is written to be readable independently, while maintaining cross-references for deeper exploration.

| Phase | Path | Purpose |
|------:|------|---------|
| 1 | `docs/phase1/` | Foundations and rationale |
| 2 | `docs/phase2/` | Architecture framing and whitepaper structure |
| 3 | `docs/phase3/` | Technical specification (v0.1) |
| 4 | `docs/phase4/` | Governance, licence, ethics policy, metadata |

## Governance and ethics
Located in `docs/phase4/`:
- Governance Charter
- Ethical Use Policy
- Metadata Pack

These documents define permitted use, constraints, and maintenance requirements.

## Licence
This project is licensed under the **MindFirst Licence (v1.1)**.  
See `LICENSE_MindFirst.md` for terms.

## Contributing
Contributions are welcome (research, engineering, evaluation, governance).  
Start with the [Getting Started](#getting-started) section and open an issue or PR with a clear scope and references where claims are made.

## Contact
Use GitHub issues for discussion and change proposals.