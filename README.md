# Field Shift

**Adapting Farms with NASA Data**

Field Shift is an evidence-driven agricultural decision-support project developed for the **NASA International Space Apps Challenge 2026**.

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

Field Shift will maintain two complementary layers:

- **Human-oriented documentation** for explaining the problem, architecture, decisions, methodology, evidence, and limitations.
- **Canonical operational context** for structured, explicit, machine-actionable knowledge that can be consumed consistently by humans, software, analytical tools, and AI agents.

These layers should complement each other rather than duplicate or contradict one another.

## Learning model

The project may use a controlled learning lifecycle to identify new evidence and candidate knowledge. AI-generated or automatically detected patterns are not treated as truth by default.

Candidate learnings should remain in shadow evaluation until they have sufficient evidence and human validation to be promoted into active knowledge or decision logic.

## Project status

Field Shift is currently in the **discovery and architecture phase**.

Initial priorities are:

1. Validate candidate NASA data sources.
2. Define the canonical environmental data model.
3. Identify appropriate soil and crop knowledge sources.
4. Define how crop rotations will be represented.
5. Establish an evidence-based decision model.
6. Define the initial MVP scope.

## Security and data policy

Never commit:

- API keys
- passwords
- access tokens
- local `.env` files
- personal or confidential information
- proprietary datasets without explicit permission
- private Earthdata credentials

Credentials must be handled outside version control.

## Language

English is the canonical language of the repository, including documentation, issues, pull requests, commit messages, code comments, schemas, and structured context.

## License

This project is licensed under the MIT License. See `LICENSE`.
