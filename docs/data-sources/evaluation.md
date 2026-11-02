# Satellite and Supporting Data Sources — Multi-Attribute Evaluation

This document provides the current architectural evaluation of NASA Earth Observation datasets and Argentine supporting sources for the Field Shift agricultural decision-support system.

It separates three different questions:

```text
Is the source useful for the MVP?
Was evidence acquired in the frozen Extract snapshot?
Has that evidence been scientifically validated for its intended role?
```

These questions must not be collapsed into one status.

## 1. Transparent evaluation framework

Rather than computing arbitrary pseudo-scientific percentages, sources are qualified using concrete attributes:

1. **Scientific authority** — official provider/product provenance.
2. **Spatial support/resolution** — what geography the observation actually represents.
3. **Temporal support/coverage** — cadence, historical span, latency, and period semantics.
4. **Primary decision role** — why the source may matter to a crop-rotation decision.
5. **Acquisition state** — whether raw evidence is present in the frozen Extract snapshot.
6. **Validation state** — whether identity, schema, coverage, missing/fill, units, quality, plausibility, consistency, and agricultural fitness have been qualified.
7. **Known limitations** — scale, representativeness, classification/model uncertainty, freshness, or other constraints.

## 2. Current MVP evaluation matrix

| Source / product | Intended Field Shift role | Acquisition state at cutoff 2026-11-01 | Validation state | Important limitations entering V1 |
|---|---|---|---|---|
| **NASA POWER Daily AG** | Long historical regional meteorological context | **ACQUIRED / FROZEN** | **V1–V7 pending** | Product/variable spatial support must remain explicit. `PRECTOTCORR` is regional/reanalysis-scale evidence, not parcel rainfall. Meteorology and solar variables may have different effective native support. |
| **NASA SMAP L4 SPL4SMGP.008** | Regional modeled surface/root-zone soil-moisture context | **ACQUIRED via AppEEARS / FROZEN** | **V1–V7 pending** | AppEEARS structure/value/fill semantics still require validation. Modeled soil moisture is not plant-available water. Native grid is regional, not parcel truth. Earlier POWER-adapter all-fill response is historical retrieval-path evidence only. |
| **REM San Luis** | Local station evidence for validation/context around prototype | **ACQUIRED / FROZEN** | **V1–V7 pending** | Station representativeness, gaps/continuity, physical anomalies, and provider-field semantics must be qualified. `pp` must not be canonically named precipitation until authoritative semantics/units are established. |
| **SMN 1991–2020 climatological normals** | Official climatological context and station-normal reference | **ACQUIRED** | **Role/extract qualification pending** | Normals describe climatology, not daily ground-truth observations. |
| **INTA Mapa Nacional de Cultivos** | Crop-classification/history context for candidate rotation understanding | **ACQUIRED / FROZEN** | **V1–V7 pending** | Classification uncertainty, class semantics, exact spatial support, campaign coverage, and distinction from farmer management records. |
| **SiSINTAR packaged soil profiles** | Preferred measured soil-profile context when representative | **ACQUIRED SNAPSHOT** | **V1–V7 pending** | Snapshot freshness relative to live service, depth/horizon semantics, variable units, spatial representativeness. Nearest profile != parcel soil truth. |
| **INTA SIGA material** | Supporting agrometeorological/local context candidate | **ACQUIRED / FROZEN** | **Exact semantics and role pending** | Exact acquired variables, periods, station/source semantics, and redundancy with REM/other evidence must be evaluated before active use. |
| **ISRIC SoilGrids** | Modeled soil fallback when suitable local measured evidence is unavailable | **Not required in frozen MVP Extract** | **Not started** | Modeled prediction, not measured farm soil. Add only when a demonstrated local-soil evidence gap justifies it. |
| **ECOSTRESS** | ET / plant-water-stress candidate | **Deferred** | **Not started** | Adds complexity and revisit/coverage constraints; requires a concrete decision gap. |
| **HLS** | Higher-resolution vegetation/crop-condition candidate | **Deferred** | **Not started** | Cloud/processing burden; only add if field-scale vegetation context changes a decision. |
| **GPM IMERG** | Higher-resolution precipitation candidate | **Deferred** | **Not started** | Do not add merely because it exists; use only if POWER + local evidence leave a material precipitation decision gap. |
| **GRACE / GRACE-FO** | Macro-hydrological context candidate | **Deferred** | **Not started** | Very coarse scale; unlikely to support parcel/field rotation decisions directly. |

## 3. NASA MVP core

### POWER

POWER remains the climate-history core because it provides a long, consistent regional time series useful for historical context and downstream anomaly/thermal/water-demand indicators once variables are validated.

Validation must still establish actual acquired dates, variables, units, missingness, duplicates, physical plausibility, native spatial semantics, and appropriate local-comparison methods.

### SMAP

SMAP L4 remains the soil-moisture core candidate because modeled root-zone moisture may add decision value that meteorology alone cannot provide.

The relevant frozen raw evidence is now the AppEEARS acquisition for `SPL4SMGP.008`, not the earlier failed POWER-adapter path.

The intended role remains **regional soil-moisture context**. Validation must determine whether the requested variables are structurally/value usable, what fill/nodata semantics apply, and how the extracted point representation relates to the native grid.

## 4. Local validation and soil hierarchy

### Local meteorological evidence

REM is the primary acquired local-station dataset currently available for direct source validation around Villa Mercedes. SMN material provides official climatological context. SIGA is an acquired supporting source whose exact incremental role still needs qualification.

Do not use one source to “validate” another unless units, variable meaning, time support, spatial relation, and observation type are actually comparable.

### Soil evidence hierarchy

Field Shift prefers measured/profile-based soil evidence when a suitable representative profile exists, while preserving the distinction between profile location and target field.

```text
representative measured profile
        ↓ preferred when justified
modeled regional fallback
        ↓ only when needed
explicit unknown
```

A modeled grid should not be introduced automatically to hide missing local soil evidence.

## 5. Source-selection discipline

The MVP should remain small:

```text
POWER + SMAP + local climate validation + soil evidence + crop context + crop knowledge
```

Additional NASA products are promoted only if validation or decision-engine design identifies a material evidence gap that they can address at an appropriate scale.

```text
DATASET_EXISTS != DATASET_ADDS_DECISION_VALUE
MORE_SOURCES != BETTER_DECISION_SUPPORT
```

## 6. Validation handoff

The current source-evaluation architecture is sufficient to enter validation.

Validation sequence:

```text
V0  snapshot integrity                  PASS
V1  identity + structure + schema       NEXT
V2  spatial/temporal coverage
V3  missing/fill/nodata/duplicates
V4  units + physical plausibility
V5  quality flags + product semantics
V6  cross-source consistency
V7  agricultural fitness for MVP role
```

No source should be normalized into curated decision-ready data merely because it appears as `ACQUIRED` in this document.
