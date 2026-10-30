# Field Shift

**Adapting Farms with NASA Data**

Field Shift is an evidence-driven agricultural decision-support project developed for the **NASA International Space Apps Challenge 2026**.

Official challenge: https://www.spaceappschallenge.org/2026/challenges/field-shift-adapting-farms-with-nasa-data/

The project explores how NASA Earth observation data, local soil information, crop characteristics, and farmer priorities can be combined to evaluate and compare crop rotation strategies under changing water and climate conditions.

## Problem

Farmers make crop-rotation decisions under uncertainty related to drought, soil conditions, water availability, and climate variability. Environmental observations are valuable, but they do not directly answer the decision a farmer must make.

Field Shift aims to bridge that gap by turning heterogeneous environmental and agricultural evidence into understandable, traceable, and actionable decision support.

## Goal

Field Shift is intended to help users answer questions such as:

- What environmental conditions characterize a field or region?
- How has water availability changed over time?
- Which crop-rotation strategies are better aligned with current conditions?
- What are the benefits, risks, and trade-offs of each alternative?
- What evidence supports each recommendation?

## Initial data sources under evaluation

The project is currently evaluating NASA Earth observation products including:

- NASA POWER
- SMAP
- ECOSTRESS
- Harmonized Landsat Sentinel-2 (HLS)
- GPM IMERG
- GRACE / GRACE-FO

Validated source metadata and project priority are maintained under [`context/sources/`](context/sources/).

Additional soil and crop datasets will be evaluated separately and must preserve source provenance and licensing constraints.

## Conceptual architecture

```text
NASA Earth Observation Data
            +
     Local Soil Data
            +
      Crop Knowledge
            +
    Farmer Priorities
            ↓
    Environmental Context
            ↓
     Decision Engine
            ↓
   Rotation Alternatives
            ↓
 Evidence + Risks + Trade-offs
            ↓
     New Evidence / Outcomes
            ↓
 Governed Learning Lifecycle
```

## Design principles

### Human-first

The project must remain understandable without requiring an AI system. Documentation, decisions, assumptions, data sources, and limitations should be accessible to humans first.

### Evidence-driven

Recommendations should be traceable to their underlying data, assumptions, and decision rules.

### AI-optimized where useful

Structured context should allow software and AI agents to work with project knowledge without repeatedly reconstructing it from scattered documentation. AI optimization must not reduce human readability.

### Traceable learning

New observations or inferred relationships must not automatically become accepted knowledge. Potential learnings should move through an explicit lifecycle:

```text
Observation
    ↓
Learning Candidate
    ↓
Shadow Evaluation
    ↓
Validation
    ↓
Promotion or Rejection
```

### Human-governed

Changes affecting decision logic or accepted knowledge require validation before becoming active.

### Reproducible

Data processing and decision logic should be reproducible whenever technically possible.

### Open by design

This repository is intended for public collaboration and public data. Secrets, credentials, personal information, proprietary datasets, and confidential material must never be committed.

## Documentation model

Field Shift maintains two complementary layers:

- **Human-oriented documentation** under [`docs/`](docs/) for the problem, architecture, methodology, decisions, evidence, and limitations.
- **Canonical operational context** under [`context/`](context/) for structured, explicit, machine-actionable knowledge shared by humans, software, analytical tools, and AI agents.

These layers should complement each other rather than duplicate or contradict one another.

## Repository map

| Path | Purpose |
| --- | --- |
| [`docs/`](docs/) | Human-oriented challenge, scope, architecture, principles, and roadmap |
| [`context/`](context/) | Canonical operational knowledge, source registry, assumptions, glossary, and decision contracts |
| [`learning/`](learning/) | Governed candidate → shadow → validation → promotion/rejection lifecycle |
| [`data/`](data/) | Data handling, provenance, and reproducibility policy |
| [`src/`](src/) | Application and data-processing implementation |
| [`notebooks/`](notebooks/) | Reproducible exploration and analytical experiments |
| [`tests/`](tests/) | Software, data, decision, and learning validation |
| [`presentation/`](presentation/) | NASA Space Apps presentation assets and challenge-first storytelling |

## Decision model

Field Shift keeps the reasoning chain explicit:

```text
Source
  ↓
Observation
  ↓
Derived Indicator
  ↓
Agronomic Interpretation
  ↓
Validated Decision Rule
  ↓
Rotation Effect
  ↓
Comparative Evaluation
```

AI may help retrieve context, analyze evidence, generate candidates, or draft explanations, but it must not silently invent reasons or promote new decision logic.

## Learning model

The project uses a controlled learning lifecycle to identify new evidence and candidate knowledge. AI-generated or automatically detected patterns are not treated as truth by default.

Candidate learnings remain outside active behavior until they have sufficient evidence, evaluation, and explicit validation to be promoted into operational context or decision logic.

## Project status

Field Shift is currently in the **discovery, data-validation, and architecture phase**.

The repository foundation, initial NASA source registry, canonical context model, decision contract, and governed learning model are established.

Next priorities are:

1. Run reproducible NASA POWER and SMAP examples for a real test location.
2. Define the canonical observation schema and data-quality checks.
3. Select the MVP geography.
4. Identify appropriate soil and crop knowledge sources.
5. Define the first candidate rotations and evidence-backed decision rules.
6. Build one complete end-to-end decision loop before expanding the data stack.

See [`docs/roadmap.md`](docs/roadmap.md) for the phased plan.

## Security and data policy

Never commit:

- API keys
- passwords
- access tokens
- local `.env` files
- personal or confidential information
- proprietary datasets without explicit permission
- private Earthdata credentials

Credentials must be handled outside version control. See [`SECURITY.md`](SECURITY.md).

## Language

English is the canonical language of the repository, including documentation, issues, pull requests, commit messages, code comments, schemas, structured context, and NASA-facing presentation material.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE).
