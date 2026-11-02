# Field Shift — Product Architecture

## 1. Architectural objective

Field Shift is a standalone, open-source agricultural decision-support product. It combines validated environmental evidence, local soil/crop context, farmer/company priorities, transparent indicators, and explicit decision rules to compare crop-rotation strategies under drought and climate variability.

The public product does **not** depend at runtime on the team's internal AI/context framework, private seats, or program-control repositories.

```text
INTERNAL DEVELOPMENT CONTEXT != PRODUCT RUNTIME
```

---

## 2. System overview

```text
┌──────────────────────────────────────────────────────────────┐
│ 1. ACQUISITION / RAW EVIDENCE              [EXTRACT FROZEN] │
│ POWER · SMAP · REM · SMN · MNC · SiSINTAR · SIGA · refs     │
│ immutable provider evidence + acquisition provenance         │
└──────────────────────────────┬───────────────────────────────┘
                               ▼
┌──────────────────────────────────────────────────────────────┐
│ 2. SOURCE VALIDATION                             [NEXT]      │
│ identity · schema · coverage · nodata · units · quality     │
│ plausibility · cross-source checks · agricultural fitness   │
└──────────────────────────────┬───────────────────────────────┘
                               ▼
┌──────────────────────────────────────────────────────────────┐
│ 3. CURATION / SERVING                         [NOT STARTED]  │
│ SERVE-TABULAR-001 · SERVE-VECTOR-001 · SERVE-RASTER-001    │
│ Parquet · GeoParquet · GeoTIFF/COG as justified             │
└──────────────────────────────┬───────────────────────────────┘
                               ▼
┌──────────────────────────────────────────────────────────────┐
│ 4. AGRICULTURAL FEATURES / INDICATORS            [PLANNED]  │
│ explicit transformations · assumptions · lineage            │
└──────────────────────────────┬───────────────────────────────┘
                               ▼
┌──────────────────────────────────────────────────────────────┐
│ 5. ROTATION DECISION ENGINE                       [PLANNED]  │
│ candidate eligibility · supporting factors · risks          │
│ trade-offs · evidence · unknowns · limitations              │
└──────────────────────────────┬───────────────────────────────┘
                               ▼
             ┌─────────────────┴─────────────────┐
             ▼                                   ▼
┌───────────────────────────┐       ┌──────────────────────────┐
│ 6A. VISUAL EXPLORATION    │       │ 6B. LOCAL ASSISTANT      │
│ replaceable FOSS consumer │       │ CLIENT-CASE-001          │
│                           │       │ ASSIST-TOOLS-001         │
└───────────────────────────┘       └──────────────────────────┘
             │                                   │
             └─────────────────┬─────────────────┘
                               ▼
                     Human operational decision
```

The assistant and visual surfaces consume the same prepared evidence/decision outputs. Neither owns scientific transformations or agronomic rules.

---

## 3. Data lifecycle and layer semantics

The canonical data lifecycle is defined in [`../data/ARCHITECTURE.md`](../data/ARCHITECTURE.md):

```text
raw
 -> staging
 -> validated
 -> curated
 -> features
 -> exports
```

### Raw

Original evidence exactly as acquired. Immutable after snapshot acquisition.

### Staging

Reproducible temporary processing. A staging artifact is not automatically validated or decision-ready.

### Validated

Evidence that has passed the applicable source-specific deterministic checks, or whose limitations have been explicitly classified. Validation establishes what the artifact/product actually means and whether it is fit for a defined role.

### Curated

Normalized analytical representations produced only from qualified validated inputs. Curated data must preserve provenance, native scale, units, quality, limitations, and transformation lineage.

### Features

Derived agricultural/environmental indicators. Every feature must retain input identities, method, parameters, assumptions, units, uncertainty/limitations, and decision role.

### Exports

Regenerable product/demo outputs. Exports are not canonical evidence.

Permanent distinction:

```text
VALIDATE != TRANSFORM
```

Validate asks what the source contains and how trustworthy/fit it is. Transform asks how qualified evidence should be represented for analysis and consumption.

---

## 4. Current source state before validation

The 2026-11-01 Extract cutoff is frozen and integrity-verified. Acquisition completeness must not be confused with scientific validation.

| Source | Acquisition state | Validation/decision state |
|---|---|---|
| NASA POWER | acquired | source-specific V1–V7 pending |
| NASA SMAP SPL4SMGP.008 via AppEEARS | acquired | structural/value/semantic/agricultural validation pending |
| REM San Luis | acquired historical responses | field semantics, continuity, missingness and plausibility pending |
| SMN | official climatological material acquired | intended as climatological context; exact use qualification pending |
| INTA Mapa Nacional de Cultivos | acquired baseline campaigns | classes, coverage, resolution and decision role pending |
| SiSINTAR | packaged snapshot acquired | variable semantics, depth/horizon, representativeness and freshness pending |
| INTA SIGA | acquired context | exact variables/use role pending validation |
| Agronomic references | acquired | authority/applicability must remain explicit |

An earlier SMAP retrieval through a POWER adapter produced only fill sentinels. That remains useful historical evidence about that retrieval path, but the current SMAP raw evidence for validation is the later AppEEARS acquisition.

---

## 5. Serving contracts

Validation should determine the appropriate downstream shape for each qualified source. Transform must satisfy one or more semantic serving contracts:

### `SERVE-TABULAR-001`

Long/tidy time-series or analytical records, normally Parquet.

### `SERVE-VECTOR-001`

Geometry-bearing observations/entities, normally GeoParquet.

### `SERVE-RASTER-001`

Native or explicitly derived raster grids, normally GeoTIFF/COG.

See [`contracts/serving-contracts.md`](contracts/serving-contracts.md).

A source is not required to satisfy every contract. Raster-to-point/zonal extraction creates a derived artifact with lineage; it does not erase the raster's native semantics.

---

## 6. Location-aware client case

A real user interaction is represented by [`CLIENT-CASE-001`](contracts/client-case.md), not by model memory.

A case may contain:

```text
actor / company
location representation
field area
field geometry when known
current crop / rotation history
irrigation/water constraints
soil information supplied by user
economic/operational constraints
goals / risk preferences
known facts
unknowns
assumptions
```

A point coordinate is a query target, not exact field geometry. Area in hectares does not define a parcel.

User declarations remain distinguishable from Field Shift observations and derived evidence.

---

## 7. Local conversational assistant

The optional local assistant is a product interaction layer, not the scientific engine.

```text
Natural language
     ↓
CLIENT-CASE-001
     ↓
material unknown detection
     ↓
ASSIST-TOOLS-001
     ↓
validated / curated evidence + deterministic decision functions
     ↓
explanation
```

Allowed responsibilities:

- understand Spanish/English user requests;
- structure/update the Client Case;
- ask targeted questions about material unknowns;
- choose among explicit product functions;
- explain returned evidence, risks, trade-offs, assumptions and limitations.

Forbidden responsibilities:

- invent observations;
- use raw provider files as decision-ready evidence;
- create active agronomic rules;
- silently override deterministic evaluations;
- treat model confidence as evidence.

See [`contracts/assistant-tools.md`](contracts/assistant-tools.md).

The exact local model/runtime is replaceable. A modest-hardware target (including approximately 4 GB VRAM with CPU fallback/hybrid inference) remains a design goal, not a validated performance claim.

---

## 8. Visualization and analytical consumption

Field Shift keeps scientific meaning independent from visualization technology.

Potential open-source consumers include:

- DuckDB / JupyterLab for analytical exploration;
- QGIS for geospatial inspection;
- Apache Superset for BI-style exploration if justified;
- Streamlit for a compact MVP product/demo surface;
- MapLibre/Leaflet later if web-map requirements justify them.

No visualization consumer may become the only location of scientific transformations or active decision logic.

```text
prepared evidence / features
        ├── notebook
        ├── BI/exploration
        ├── GIS
        ├── UI
        └── local assistant
```

---

## 9. Open-source runtime constraint

The reproducible baseline must run end-to-end without commercial licenses. Proprietary BI/GIS/database runtimes may not be required dependencies.

Candidate infrastructure is introduced only when a concrete validated requirement exists. In particular, PostgreSQL/PostGIS, vector retrieval, additional web services, or distributed data infrastructure are not baseline requirements today.

---

## 10. Authority and decision boundaries

```text
Human
  priorities + declared constraints + final operational decision

Local language model
  language understanding + requirements elicitation + bounded tool selection + explanation

Validated/curated data layer
  scientific observations + provenance + quality + limitations

Feature/indicator layer
  explicit deterministic derivations

Decision engine
  candidate evaluation + rules + risks + trade-offs + evidence chain
```

The expected recommendation chain is:

```text
Source
 -> Observation
 -> Derived Indicator
 -> Interpretation
 -> Decision Rule
 -> Rotation Effect
 -> Recommendation / Alternative
```

Skipping layers requires an explicit reason and must never be hidden behind AI output.

---

## 11. Frozen pre-validation invariants

The following are architectural constraints entering Validate:

```text
PUBLIC_PRODUCT_IS_STANDALONE
OPEN_SOURCE_RUNTIME_REQUIRED
RAW_BYTES_ARE_IMMUTABLE
READABLE != VALIDATED
VALIDATED != INTERPRETED
INTERPRETED != DECISION_RULE
VALIDATE != TRANSFORM
RESAMPLING != NEW_INFORMATION
DERIVED_DATA_MUST_RETAIN_LINEAGE
COARSE_REGIONAL_DATA != PARCEL_TRUTH
MODEL_MEMORY != CLIENT_CASE
MODEL_CONFIDENCE != EVIDENCE
SCIENTIFIC_LOGIC != VISUALIZATION_CONFIG
```

These may be changed only by an explicit architecture decision when validation uncovers a material contradiction.

---

## 12. Intentionally open until validation

The architecture does not pre-decide:

- final validated schema per source;
- final curated physical table/file layout;
- exact source-to-serving-contract mapping;
- quality-state vocabulary reconciliation;
- fill/missing conversion details per provider;
- aggregation/resampling methods;
- final indicators and thresholds;
- crop/rotation rules requiring agronomic validation;
- exact final visualization stack;
- whether a database server is needed;
- exact local LLM and quantization.

This prevents validation from becoming a ritual performed against conclusions already assumed by the architecture.
