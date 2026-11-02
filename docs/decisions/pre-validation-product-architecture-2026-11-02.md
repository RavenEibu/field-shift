# Pre-Validation Product Architecture Baseline — 2026-11-02

## Decision

Before source validation and normalization begin, Field Shift freezes the product boundaries and data-consumption contracts that validation and transformation must satisfy.

This decision freezes **architecture and invariants**, not scientific conclusions or final physical schemas.

## Product boundary

`field-shift` is the standalone public solution.

It must run without:

- `ai-context`;
- `ai-framework-control`;
- `field-shift-context`;
- private seat repositories;
- chat/model memory;
- commercial software licenses.

Internal context repositories may help the team design, investigate, learn, and coordinate work, but they are not product runtime dependencies.

## Product responsibility map

```text
User / farmer / company
        │
        ├───────────────┐
        ▼               ▼
Visual exploration   Local assistant
                        │
                   CLIENT-CASE-001
                        │
                  ASSIST-TOOLS-001
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
Evidence services               Decision engine
          │                           │
          └─────────────┬─────────────┘
                        ▼
              Environmental context
                        │
            curated data / features
                        │
                 validated evidence
                        │
                      raw
```

The local assistant sits **above** the evidence and decision services. It is not a hidden bridge from raw NASA data directly to recommendations.

## Data lifecycle

The canonical lifecycle remains:

```text
raw
 -> staging
 -> validated
 -> curated
 -> features
 -> exports
```

Semantics:

- `raw`: immutable provider evidence;
- `staging`: reproducible temporary processing;
- `validated`: source-specific deterministic checks passed or limitations explicitly classified;
- `curated`: normalized analytical data under a serving contract;
- `features`: derived decision-relevant indicators with lineage;
- `exports`: regenerable consumer/demo outputs, never canonical evidence.

Validation and transformation are intentionally distinct:

```text
VALIDATE = what do we actually have and how trustworthy/fit is it?
TRANSFORM = how do we represent validated evidence for analysis and consumption?
```

## Serving baseline

Transform may target one or more existing serving contracts:

- `SERVE-TABULAR-001` → Parquet by default;
- `SERVE-VECTOR-001` → GeoParquet by default;
- `SERVE-RASTER-001` → GeoTIFF/COG when grid semantics must remain.

These are semantic contracts. Physical schemas may evolve during validation as long as the invariants remain satisfied.

## Open-source runtime baseline

Field Shift must be demonstrable end-to-end with open-source software.

Baseline candidates include:

```text
Python
DuckDB
Parquet / GeoParquet
GeoTIFF / COG
JupyterLab
QGIS
Apache Superset
Streamlit
```

PostgreSQL/PostGIS, MapLibre/Leaflet, vector search, or other infrastructure may be introduced only when validated product/data needs justify them.

No commercial runtime may be required for the reproducible baseline.

## Visualization boundary

Visualization tools consume prepared evidence; they do not own scientific meaning.

Scientific transformations, units, quality interpretation, decision rules, and derived indicators must remain versioned and testable outside dashboard configuration.

The same curated/features layer should be reusable by notebooks, BI/exploration, GIS, the demo UI, and the local assistant.

## Local assistant boundary

The optional local assistant uses:

- `CLIENT-CASE-001` for explicit current agricultural case state;
- `ASSIST-TOOLS-001` for bounded evidence/decision calls;
- a replaceable local language model for language understanding and explanation.

Framework-inspired principles intentionally retained in product form:

```text
MODEL_MEMORY != CLIENT_CASE
CHAT_HISTORY != CURRENT_CASE_STATE
EVIDENCE != DECISION
MODEL_CONFIDENCE != EVIDENCE
TYPED_TOOL != ARBITRARY_EXECUTION
```

Framework-specific machinery intentionally excluded from the public product runtime:

```text
SeatContext
WorkContext framework contracts
Director/program control
private-seat registry
framework evolution/adoption machinery
framework WAL/governance internals
```

## Location semantics

Field Shift is location-aware but must not create false parcel precision.

- coordinates identify a query target;
- hectares do not define geometry;
- field polygons are preferred when parcel relationships matter;
- coarse NASA cells remain coarse NASA evidence;
- station/profile distance and spatial relationship remain explicit;
- resampling or clipping does not create new information.

## Authority boundary

```text
User/human
  owns priorities, declared constraints, acceptance of assumptions, final action

Language model
  owns language understanding, case elicitation, bounded tool selection, explanation

Data layer
  owns validated/curated observations, provenance, quality, limitations

Indicator/decision engine
  owns deterministic calculations, rules, evaluated alternatives and trade-offs
```

## What is frozen before validation

- standalone public-product boundary;
- open-source-only reproducible runtime requirement;
- raw → staging → validated → curated → features → exports lifecycle;
- validation/transform separation;
- serving contracts by data shape;
- provenance/quality/scale preservation;
- visualization independence from scientific logic;
- Client Case state boundary;
- bounded assistant tool boundary;
- human/LLM/data/decision authority separation;
- no parcel-scale overclaiming;
- no arbitrary recommendation scores.

## What remains intentionally open until validation

- final source-specific validated schemas;
- exact curated physical tables/files;
- which source maps to which serving contract in every case;
- final quality-state reconciliation;
- source-specific missing/fill transformations;
- exact aggregation/resampling rules;
- scientific validity and decision role of each variable;
- derived indicator definitions that still require evidence/agronomic validation;
- final candidate rotations and active decision rules;
- whether PostGIS, Superset, semantic retrieval, or a larger UI stack is actually needed;
- exact local LLM/model size and verified 4 GB VRAM performance.

## Validation entry condition

Source validation may begin once shared work state and public maturity labels are reconciled with the frozen Extract snapshot.

Validation must answer source-specific questions without changing the architectural invariants above unless a material contradiction is discovered. Any such change requires an explicit architecture decision rather than silent drift.
