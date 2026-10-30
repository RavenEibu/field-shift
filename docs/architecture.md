# Architecture

## Architectural objective

Field Shift separates observations, contextual knowledge, decision logic, and learning governance so that recommendations remain explainable and auditable.

```text
External Data Sources
        ↓
Ingestion and Validation
        ↓
Canonical Data Model
        ↓
Environmental Context
        +
Agricultural Knowledge
        +
Farmer Priorities
        ↓
Decision Engine
        ↓
Rotation Evaluation
        ↓
Evidence + Explanation + Uncertainty
        ↓
Observed Outcomes / New Evidence
        ↓
Governed Learning Lifecycle
```

## Two documentation layers

### Human layer

Primarily stored under `docs/`.

Its purpose is to explain:

- what the project does
- why the problem matters
- how the system works
- why major decisions were made
- what evidence exists
- what assumptions and limitations apply

A contributor should be able to understand the project without an AI assistant.

### Canonical operational context

Primarily stored under `context/`.

Its purpose is to hold explicit, structured, version-controlled knowledge that can be consumed consistently by:

- humans
- application code
- analytical tooling
- AI agents

Examples include:

- source definitions
- schemas
- terminology
- assumptions
- rules
- evidence relationships
- validation state

The context layer is not an AI-only layer. It is the shared operational representation of project knowledge.

## Knowledge flow

A useful pattern for decision traceability is:

```text
SOURCE
  ↓
VARIABLE
  ↓
INDICATOR
  ↓
AGRONOMIC INTERPRETATION
  ↓
DECISION RULE
  ↓
ROTATION EFFECT
  ↓
RECOMMENDATION
```

For example:

```text
SMAP
  ↓
soil_moisture
  ↓
persistent moisture deficit
  ↓
high water-stress context
  ↓
penalize water-demanding options
  ↓
rotation score changes
  ↓
explainable trade-off
```

The exact rule must be evidence-backed and validated before it is promoted into active decision logic.

## Spatial context

Field Shift may combine sources at different spatial resolutions, but it must preserve their effective information scale.

A coarse regional measurement and a high-resolution field observation can contribute to the same decision without pretending they have the same precision.

The architecture should therefore support evidence at multiple scales rather than force all observations into a falsely uniform grid.

## AI role

AI may assist with:

- structured context retrieval
- research synthesis
- data-quality analysis
- hypothesis generation
- explanation drafting
- candidate-learning detection
- repetitive transformation or documentation work

AI must not silently promote inferred facts or modify active decision rules without validation.

## Reusable framework role

Field Shift may reuse framework capabilities for context centralization, provenance, learning governance, and AI optimization.

Those capabilities are infrastructure. The public product remains centered on agricultural decision support.
