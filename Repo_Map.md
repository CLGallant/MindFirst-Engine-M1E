# MindFirst Engine (M1E) — Repository Map

This document provides a high-level orientation to the structure of the M1E repository.  
It helps new contributors understand where each component of the specification lives.

---

## Repository Structure

### Root Directory

| File | Purpose |
|------|---------|
| `README.md` | Project overview and quick start guide |
| `LICENSE` | Dual MIT + MindFirst Ethical Provisions license |
| `Repo_Map.md` | This file – repository structure guide |
| `Next_Steps.md` | Planned development roadmap |
| `Cloud_Credits_Application.md` | Infrastructure planning document |

### Documentation Hub (`docs/`)

**Entry Point:** `docs/index.md` – Main documentation navigation hub

#### Core Documentation
- **`Public_Overview.md`** – Non-technical introduction to MindFirst

#### Manifestos (`docs/manifestos/`)
Philosophy and vision documents:
- `mind-first-manifesto.md` – Core MindFirst philosophy
- `expanded-manifesto.md` – Extended framework and applications

#### Phase 1: Foundations (`docs/phase1/`)
Conceptual foundations and rationale:
- `MindFirst_Phase_1_Foundations_and_Rationale.md`

#### Phase 2: Architecture Overview (`docs/phase2/`)
High-level technical architecture:
- `MindFirst_Phase_2_Whitepaper_Structure.md`

#### Phase 3: Technical Specification (`docs/phase3/`)
Complete technical specification including:
- Core architecture (OS-Profiler, OS-Interpreter, OS-Stabiliser)
- M1E API Layer and Response Generator
- Post-Identity Safety Mechanisms
- System Requirements & Constraints
- Cognitive-Signal Pipeline (end-to-end flow)
- Safeguarding Layer
- Challenges & Validation Roadmap
- Future Work
- Glossary of Core Terms

**Main File:** `Phase 3 — Technical Specification of the MindFirst Engine (M1E).md`

#### Phase 4: Governance and Safety (`docs/phase4/`)
Governance, ethics, and operational policies:
- **`Governance_and_Ethics_Policy.md`** – Unified governance and ethical framework
- `Phase 4 — Governancet.md` – Governance overview
- `Metadata_Pack.md` – Project metadata and standards

---

## Quick Access Paths

### For New Contributors
1. Start with `README.md`
2. Read `docs/Public_Overview.md` for conceptual understanding
3. Review `docs/phase4/Governance_and_Ethics_Policy.md` for contribution guidelines
4. Check `LICENSE` for legal and ethical constraints

### For Researchers
1. Begin with `docs/manifestos/` for philosophical foundation
2. Read `docs/phase1/` for theoretical rationale
3. Study `docs/phase3/` for complete technical specification
4. Reference `docs/phase4/Governance_and_Ethics_Policy.md` for ethical framework

### For Developers
1. Review `README.md` for project overview
2. Study `docs/phase3/` for technical architecture
3. Understand `docs/phase4/Governance_and_Ethics_Policy.md` for implementation constraints
4. Check `LICENSE` for compliance requirements
5. Read `Next_Steps.md` for development roadmap

---

## Key Concepts Directory

| Concept | Primary Location | Additional References |
|---------|------------------|----------------------|
| OS-Profiler | Phase 3 Technical Spec | Phase 2 Whitepaper |
| OS-Interpreter | Phase 3 Technical Spec | Phase 2 Whitepaper |
| OS-Stabiliser | Phase 3 Technical Spec | Phase 2 Whitepaper |
| M1E API Layer | Phase 3 Technical Spec | Phase 2 Whitepaper |
| Structural Neutrality | Governance and Ethics Policy | LICENSE, Phase 1 |
| Post-Identity Framework | Public Overview, Manifestos | Phase 1, Phase 3 |
| Safety Mechanisms | Phase 3 Technical Spec | Governance and Ethics Policy |
| Governance Rules | Phase 4 Governance and Ethics | LICENSE |
| Ethical Constraints | Phase 4 Governance and Ethics | LICENSE |

---

## Documentation Principles

### Structure
- **Phase-based organization** – Conceptual progression from foundations to implementation
- **Self-contained documents** – Each file can be read independently
- **Clear cross-references** – Links between related concepts
- **Navigation hub** – `docs/index.md` serves as central navigation point

### Content Guidelines
- **Transparency** – All architectural decisions documented
- **Accessibility** – Technical and non-technical versions available
- **Completeness** – Specification includes rationale and constraints
- **Maintainability** – Regular updates to reflect project evolution

---

## File Naming Conventions

- **Phase documents:** `Phase X — Title.md`
- **Descriptive names:** Use underscores for multi-word files
- **Consistent structure:** Maintain parallel organization across phases
- **Clear hierarchy:** Root → docs → phase → specific documents

---

## Recent Changes

**2025-12-12:** Repository simplification
- Consolidated license files into single comprehensive LICENSE
- Unified Governance_Charter.md and Ethical_Use_Policy.md into Governance_and_Ethics_Policy.md
- Moved manifesto files to `docs/manifestos/` directory
- Streamlined README.md to focus on overview and navigation
- Enhanced `docs/index.md` as comprehensive documentation hub

---

## Future Additions

As development proceeds, the repository will expand to include:
- Implementation code and prototypes
- Empirical validation results
- Integration examples and tutorials
- API documentation
- Testing frameworks
- Performance benchmarks

Stay tuned to `Next_Steps.md` for planned development milestones.

---

**For questions about repository organization, open an issue or contact the Project Steward.**
