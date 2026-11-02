# Field Shift

> **Evidence-driven crop rotation decision support under drought, water stress, and climate variability using NASA Earth observations and local agricultural context.**

Field Shift is an open-source prototype for the NASA International Space Apps Challenge 2026. It helps farmers, agronomists, companies, and land managers understand environmental conditions, compare crop-rotation alternatives, and see the evidence, assumptions, risks, trade-offs, uncertainty, and limitations behind each evaluation.

Field Shift is not an opaque AI recommender. The agricultural decision problem is the product; AI is an optional interaction layer over explicit evidence and deterministic decision logic.

---

## 1. Product question

> Given the environmental and agricultural conditions of a field or region, which crop rotation strategies should be considered, and why?

Conceptual flow:

```text
NASA Earth Observation Data
+ Local Soil Data
+ Crop Knowledge
+ Farmer / Company Priorities
        ↓
Environmental Context
        ↓
Decision Engine
        ↓
Rotation Alternatives
        ↓
Evidence + Risks + Trade-offs + Explanation
```

---

## 2. Current implementation maturity

The repository distinguishes acquisition, validation, transformation, and decision readiness. **Acquired does not mean scientifically validated or decision-ready.**

| Subsystem | Current state | Scope |
|---|---|---|
| **Data acquisition** | `[EXTRACT FROZEN / VERIFIED]` | A multi-source raw snapshot was frozen at the 2026-11-01 cutoff and integrity-verified. POWER, SMAP AppEEARS outputs, INTA crop-map data, SiSINTA snapshot data, SIGA material, REM San Luis station responses, SMN climatological material, and agronomic references have been acquired. Source-specific scientific validation is pending. |
| **Source validation** | `[NEXT]` | V0 snapshot integrity is complete. V1–V7 source/product identity, schema, coverage, missing/fill values, units, quality semantics, cross-source consistency, and agricultural fitness remain to be executed. |
| **Serving/data contracts** | `[DEFINED]` | Tabular/time-series, vector geospatial, and raster serving contracts constrain Transform while preserving provenance, native scale, quality, and limitations. |
| **Transformation / curated data** | `[NOT STARTED]` | No source should be normalized into decision-ready curated data until its validation requirements and semantics are established. |
| **Agro-climatic indicators** | `[PLANNED]` | Indicator definitions require validated environmental/soil evidence and explicit assumptions before activation. |
| **Rotation decision engine** | `[PLANNED]` | Transparent qualitative/explicit-rule evaluation is preferred over unjustified scoring. |
| **Visual exploration** | `[ARCHITECTURE DEFINED]` | Replaceable open-source consumers will use curated/features data; visualization tools do not own scientific logic. |
| **Local conversational assistant** | `[CONTRACTS DEFINED / NOT IMPLEMENTED]` | `CLIENT-CASE-001` and `ASSIST-TOOLS-001` define a lightweight local assistant that elicits needs, queries governed evidence/functions, and explains results without becoming the decision engine. |

---

## 3. NASA Earth observation core

### NASA POWER

POWER is the baseline source for long historical regional meteorological context. The acquired material includes daily variables such as temperature, precipitation, humidity, wind, pressure, and solar-radiation context.

Important scientific boundary: POWER variables retain their product-specific spatial support. A regional/reanalysis grid value must not be represented as an exact parcel measurement.

**State:** acquired; validation pending.

### NASA SMAP

The MVP uses SMAP L4 `SPL4SMGP.008` as a candidate source for regional modeled surface and root-zone soil-moisture context. The frozen Extract snapshot includes AppEEARS task outputs for three prototype/reference points and the requested surface/root-zone variables.

An earlier POWER-adapter attempt returned only fill sentinels; that historical failure is not evidence that SMAP observations are absent. The AppEEARS acquisition is now the relevant raw evidence and still requires structural, value, fill/nodata, product-semantic, and agricultural-fitness validation.

**State:** acquired; validation pending.

---

## 4. Local and agricultural evidence

The frozen Extract snapshot also includes local/context sources selected for complementary roles:

- **REM San Luis:** local station evidence for Villa Mercedes, Villa Reynolds, and AgroZAL. Coverage/missingness and field semantics such as `pp` still require authoritative validation; suspect physical values must be flagged rather than silently cleaned.
- **SMN:** official climatological-normal material for regional climate context. Normals are not daily ground-truth observations.
- **INTA Mapa Nacional de Cultivos:** crop-history/classification campaigns acquired for later spatial and rotation-context evaluation.
- **SiSINTAR:** measured-soil snapshot material acquired with an explicit freshness limitation relative to any live service; nearest profile does not equal parcel soil truth.
- **INTA SIGA and agronomic references:** acquired context to be qualified for exact decision role during validation.

Source selection and acquisition do not automatically imply suitability for the decision engine.

---

## 5. Prototype geography

The first reproducible prototype is anchored in the **Villa Mercedes / General Pedernera, San Luis, Argentina** agricultural context, using `-33.6500, -65.3667` (`EPSG:4326`) as the initial regional query anchor.

A coordinate is a query target, not a field boundary. When a real client/company case is used, the product should accept a field polygon when available and otherwise state the limits of point/regional representation.

---

## 6. Data architecture

```text
raw
 -> staging
 -> validated
 -> curated
 -> features
 -> exports
```

Core invariants:

```text
RAW_BYTES_ARE_IMMUTABLE
READABLE != VALIDATED
VALIDATED != INTERPRETED
INTERPRETED != DECISION_RULE
RESAMPLING != NEW_INFORMATION
DERIVED_DATA_MUST_RETAIN_LINEAGE
```

Preferred serving forms after validation:

- Parquet for tabular/time-series data;
- GeoParquet for vector/geospatial data;
- GeoTIFF/COG when raster-grid semantics remain decision-relevant.

See [`data/ARCHITECTURE.md`](data/ARCHITECTURE.md) and [`docs/contracts/serving-contracts.md`](docs/contracts/serving-contracts.md).

---

## 7. Product interaction architecture

Field Shift supports two complementary product surfaces over the same governed evidence:

```text
                 curated / features / decisions
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
      visual exploration       local assistant
                                      │
                               CLIENT-CASE-001
                                      │
                               ASSIST-TOOLS-001
```

The assistant may understand Spanish/English requests, structure a client case, detect material unknowns, invoke explicit Field Shift functions, and explain evidence-backed results. It must not invent observations, create active agronomic rules, or convert language-model confidence into scientific evidence.

The public product is standalone and has no runtime dependency on internal AI/context-framework repositories.

See:

- [`docs/contracts/client-case.md`](docs/contracts/client-case.md)
- [`docs/contracts/assistant-tools.md`](docs/contracts/assistant-tools.md)
- [`docs/decisions/local-decision-support-assistant-2026-11-02.md`](docs/decisions/local-decision-support-assistant-2026-11-02.md)
- [`docs/decisions/pre-validation-product-architecture-2026-11-02.md`](docs/decisions/pre-validation-product-architecture-2026-11-02.md)

---

## 8. Open-source-only runtime baseline

The reproducible Field Shift baseline must run end-to-end without commercial software licenses.

Current/open candidates include Python, DuckDB, Parquet/GeoParquet, GeoTIFF/COG, JupyterLab, QGIS, Apache Superset, and Streamlit. PostgreSQL/PostGIS, MapLibre/Leaflet, semantic retrieval, or other infrastructure should be added only when validated needs justify them.

Scientific logic must remain outside visualization-only configuration.

---

## 9. Repository structure

```text
field-shift/
├── data/                  # lifecycle, manifests, schemas and source specifications
├── docs/
│   ├── architecture.md    # public product architecture
│   ├── contracts/         # serving, client-case and decision contracts
│   ├── data-sources/      # source evaluation and provenance
│   ├── decisions/         # public architecture/source decisions
│   └── methodology/       # scientific/agronomic methodology
├── learning/              # governed product learning lifecycle
├── notebooks/             # reproducible exploration
├── presentation/          # challenge/demo material
├── scripts/               # reproducibility and validation tooling
├── src/                   # product implementation
└── tests/                 # schema, logic and scientific-integrity tests
```

Internal collaborative context and private personal learning repositories are deliberately not part of the public runtime.

---

## 10. Reproducibility and license

Field Shift is open-source software licensed under the [MIT License](LICENSE). The baseline is designed for a Linux x86_64 environment using Python tooling and open geospatial libraries; exact validated compatibility claims remain limited to environments actually tested by the team.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).
