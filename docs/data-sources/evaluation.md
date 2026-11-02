# Satellite and Supporting Data Sources — Multi-Attribute Evaluation

This document provides the current architectural evaluation of NASA Earth Observation datasets and Argentine supporting sources for the Field Shift agricultural decision-support system.

It separates three different questions:

```text
Is the source useful for the MVP?
Was evidence acquired in the frozen Extract snapshot?
What validation evidence already exists, and what scientific qualification is still missing?
```

These questions must not be collapsed into one status.

## 1. Transparent evaluation framework

Rather than computing arbitrary pseudo-scientific percentages, sources are qualified using concrete attributes:

1. **Scientific authority** — official provider/product provenance.
2. **Spatial support/resolution** — what geography the observation actually represents.
3. **Temporal support/coverage** — cadence, historical span, latency, and period semantics.
4. **Primary decision role** — why the source may matter to a crop-rotation decision.
5. **Acquisition state** — whether raw evidence is present in the frozen Extract snapshot.
6. **Existing validation evidence** — deterministic acquisition/integrity checks that can be reused.
7. **Remaining scientific validation** — semantics, quality, plausibility, consistency, representativeness, and agricultural fitness still to establish.
8. **Known limitations** — scale, representativeness, classification/model uncertainty, freshness, or other constraints.

## 2. Current MVP evaluation matrix

| Source / product | Intended Field Shift role | Acquisition state at cutoff 2026-11-01 | Validation state | Important limitations entering formal Validate |
|---|---|---|---|---|
| **NASA POWER Daily AG** | Long historical regional meteorological context | **ACQUIRED / FROZEN** | **Formal V1–V7 mapping pending; prior acquisition evidence reusable** | Product/variable spatial support must remain explicit. `PRECTOTCORR` is regional/reanalysis-scale evidence, not parcel rainfall. Meteorology and solar variables may have different native support. |
| **NASA SMAP L4 SPL4SMGP.008** | Regional modeled surface/root-zone soil-moisture context | **ACQUIRED via AppEEARS / FROZEN** | **E1 passed for `sm_surface` and `sm_rootzone`; `sm_rootzone_pctl` unusable; E2/V5–V7 pending** | Historical AppEEARS baseline is 2015-03-31→2025-12-31, 94,296 rows, no point/timestamp duplicates. Modeled soil moisture is not plant-available water. Native grid is regional, not parcel truth. Do not fabricate percentiles from fill-only `pctl`. |
| **REM San Luis** | Local station evidence for validation/context around prototype | **ACQUIRED / FROZEN** | **V1–V7 pending** | Station representativeness, gaps/continuity, physical anomalies, and provider-field semantics must be qualified. `pp` must not be canonically named precipitation until authoritative semantics/units are established. |
| **SMN 1991–2020 climatological normals** | Official climatological context and station-normal reference | **ACQUIRED** | **Role/table extraction qualification pending** | Normals describe climatology, not daily ground-truth observations. |
| **INTA Mapa Nacional de Cultivos** | Crop-classification/history context for candidate rotation understanding | **ACQUIRED / FROZEN** | **V1–V7 pending** | Classification uncertainty, class semantics, exact spatial support, campaign coverage, and distinction from farmer management records. |
| **SiSINTAR packaged soil profiles** | Preferred measured soil-profile context when representative | **ACQUIRED SNAPSHOT** | **V1–V7 pending** | Snapshot freshness relative to live service, depth/horizon semantics, variable units, spatial representativeness. Nearest profile != parcel soil truth. |
| **INTA SIGA material** | Supporting agrometeorological/local context candidate | **ACQUIRED CONTEXT MATERIAL** | **Exact resource semantics and incremental role pending** | Do not claim a complete local station series until the actual acquired resource is identified and qualified. Avoid redundancy with REM/other local evidence. |
| **ISRIC SoilGrids** | Modeled soil fallback when suitable local measured evidence is unavailable | **Not required in frozen MVP Extract** | **Not started** | Modeled prediction, not measured farm soil. Add only when a demonstrated local-soil evidence gap justifies it. |
| **ECOSTRESS** | ET / plant-water-stress candidate | **Deferred** | **Not started** | Adds complexity and revisit/coverage constraints; requires a concrete decision gap. |
| **HLS** | Higher-resolution vegetation/crop-condition candidate | **Deferred** | **Not started** | Cloud/processing burden; only add if field-scale vegetation context changes a decision. |
| **GPM IMERG** | Higher-resolution precipitation candidate | **Deferred** | **Not started** | Do not add merely because it exists; use only if POWER + local evidence leave a material precipitation decision gap. |
| **GRACE / GRACE-FO** | Macro-hydrological context candidate | **Deferred** | **Not started** | Very coarse scale; unlikely to support parcel/field rotation decisions directly. |

## 3. NASA MVP core

### POWER

POWER remains the climate-history core because it provides a long, consistent regional time series useful for historical context and downstream anomaly/thermal/water-demand indicators once variables are qualified.

Formal validation should first map existing acquisition evidence into V1–V7, then execute only missing checks: actual acquired dates, variables, units, missingness, duplicates, physical plausibility, native spatial semantics, freshness, and defensible local-comparison methods.

### SMAP

SMAP L4 remains the soil-moisture core because modeled root-zone moisture adds potential decision value that meteorology alone cannot provide.

The canonical historical AppEEARS baseline is task `be20a35b-82f5-41ff-b379-94cfd81b74cf`, covering `2015-03-31` through `2025-12-31` at three requested points. Acquisition/integrity evidence already establishes:

```text
request/product/point traceability          PASS
temporal row completeness                   PASS
point/timestamp duplicates                  0
sm_surface usable values                    94,296 / PASS
sm_rootzone usable values                   94,296 / PASS
sm_rootzone_pctl usable values              0 / NOT_SATISFIED
```

This evidence should be reused rather than re-created during formal validation.

The remaining question is not “did SMAP download?” but whether the qualified variables can be interpreted appropriately for Field Shift. Scientific work still includes seasonal/extreme behavior, quality semantics, any aggregation method, representative local-soil context, defensible cross-source comparison, and eventual agricultural fitness.

```text
ROOT_ZONE_SOIL_MOISTURE != PLANT_AVAILABLE_WATER
```

## 4. Local validation and soil hierarchy

### Local meteorological evidence

REM is the primary acquired local-station dataset currently available for direct validation/context around Villa Mercedes. SMN material provides official climatological context. SIGA is acquired supporting material whose exact incremental role still needs qualification.

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

The source architecture is sufficient to enter formal validation.

```text
V0  snapshot integrity                  PASS
V1  identity + structure + schema       NEXT / reuse prior evidence where sufficient
V2  spatial/temporal coverage
V3  missing/fill/nodata/duplicates
V4  units + physical plausibility
V5  quality flags + product semantics
V6  cross-source consistency
V7  agricultural fitness for MVP role
```

Formal validation is a reconciliation of evidence, not a requirement to re-run checks that already have sufficient frozen proof.

No source should be normalized into curated decision-ready data merely because it appears as `ACQUIRED` or has partial E1 checks in this document.
