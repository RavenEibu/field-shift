# Data Source Fitness Rating

Field Shift rates data sources for **decision fitness**, not prestige.

A high rating means a source is authoritative, reproducible, transformable, and appropriate for the specific decision role assigned to it. It does **not** mean the source is exact at parcel scale, non-redundant, or sufficient by itself to produce a crop-rotation recommendation.

## Rating dimensions

Each dimension is scored from 0 to 5.

| Dimension | Weight | Question |
|---|---:|---|
| Authority and provenance | 20% | Is the source authoritative, versioned, citable, and traceable? |
| Scientific validation and uncertainty | 20% | Are validation methods, uncertainty, quality flags, or known errors documented? |
| Decision relevance | 20% | Does the source materially inform Field Shift's crop-rotation decision? |
| Spatial and temporal fitness | 15% | Is its native scale appropriate for the role assigned to it? |
| Transformability and access | 15% | Can it be retrieved, subset, transformed, and reproduced reliably? |
| Operational stability | 10% | Are access paths, versions, and update behavior sufficiently stable for the MVP? |

Overall score:

```text
score_100 = 20*A/5 + 20*V/5 + 20*D/5 + 15*S/5 + 15*T/5 + 10*O/5
```

where `A,V,D,S,T,O` are the six 0–5 dimension scores above. Scores must be mechanically reproducible from the dimensions.

## Interpretation

| Score | Classification | General interpretation |
|---:|---|---|
| 85–100 | A — strong | Strong source for its declared role |
| 70–84 | B — useful with controls | Useful with explicit limitations or supporting role |
| 55–69 | C — contextual/fallback | Do not make it decisive; preserve uncertainty and corroborate |
| <55 | D — weak for current use | Discovery/exploratory or reject unless narrowly justified |

## Hard gates

A numerical score cannot override these gates:

- A source whose spatial scale is incompatible with parcel-level claims cannot be used as parcel truth.
- A modeled/predicted value cannot be presented as a field measurement.
- A third-party curated source cannot override an authoritative product owner.
- A source with unresolved product/version identity cannot become canonical.
- A recommendation cannot exceed the strongest evidence layer supporting it.

## Incremental-value gate

A high-quality source is not automatically an MVP dependency.

After fitness, Field Shift separately asks:

```text
What decision gap does this source close?
Does another selected source already cover that role?
Will it materially improve uncertainty, scale, validation, or explainability?
Is that benefit worth the integration and QA cost?
```

This prevents dataset accumulation from becoming a substitute for a clear agricultural decision model.

## Current reviewed sources — 2026-10-30

| Source | Primary role | Fitness | Class | MVP disposition |
|---|---|---:|---|---|
| NASA SMAP L4 SPL4SMGP v8 | regional surface/root-zone soil moisture | 94.5 | A | **Core** |
| FAO-56 / AquaCrop | crop-water knowledge | 94.0 | A | **Core knowledge** |
| INTA Mapa Nacional de Cultivos | observed crop-history context | 91.5 | A | **Core candidate** |
| NASA POWER / MERRA-2 | regional climate context | 90.5 | A | **Core** |
| INTA SisINTA | measured soil-profile source system | 90.5* | A* | **Preferred local soil** |
| INTA agrometeorological network | local in-situ validation | 89.5* | A* | **Validation reference** |
| NASA HLS v2.0 | 30 m surface-reflectance / vegetation response | 87.5 | A | Deferred: use only for unresolved field-scale vegetation questions |
| NASA GPM IMERG Final v07/V07B | precipitation-specific context | 87.0 | A | Deferred: use when POWER precipitation is insufficient or needs cross-checking |
| NASA ECOSTRESS ECO_L3T_JET v2 | ~70 m evapotranspiration / stress | 83.5 | B | MVP+: valuable after core loop works |
| NASA GRACE/GRACE-FO JPL mascons | broad water-storage anomaly | 74.0 | B | Context only |
| ISRIC SoilGrids 250 m | modeled soil fallback | 71.0 | B + hard gate | Fallback/context only |

`*` Source-system rating only. A concrete station or soil profile requires its own identity, representativeness, method, completeness, and quality review.

## Why high scores can still be deferred

### HLS

HLS is scientifically strong and has field-relevant 30 m resolution, but the INTA crop map already covers the MVP's initial crop-history requirement with a locally curated classification product. HLS should be added only if Field Shift needs vegetation-response indicators or spatial patterns that the crop map cannot answer.

### IMERG

IMERG is a strong precipitation product and the Final Run is appropriate for research. POWER already supplies precipitation in the initial climate context, so IMERG should enter only if precipitation-specific temporal detail, cross-validation, or event analysis changes the decision.

### GRACE

GRACE is authoritative for broad total-water-storage anomalies, but its underlying independent mascons are far too coarse to distinguish field rotation choices. A 0.5-degree distributed grid must not be interpreted as independent 0.5-degree information.

### SoilGrids

SoilGrids illustrates why hard gates exist: its authority, uncertainty documentation, and transformability make it a useful global/regional model, but ISRIC explicitly discourages local/farm-level interpretation. Therefore it remains fallback/context only even though the weighted score falls in class B.

## Source-selection rule

The preferred MVP evidence stack is:

```text
POWER climate context
+ SMAP L4 water context
+ INTA crop history
+ measured/local soil evidence
+ FAO/INTA crop knowledge
+ farmer priorities
+ local in-situ climate validation where available
```

Additional sources enter only after a concrete evidence gap is documented.

## Important distinction

```text
SOURCE FITNESS SCORE
!= INCREMENTAL MVP VALUE
!= TRANSFORMATION CONFIDENCE
!= RECOMMENDATION CONFIDENCE
```

This source rating is a governance and source-selection aid. It is **not** a crop-rotation score. Numerical rotation scoring remains optional until its agronomic factors, formulas, weights, uncertainty treatment, and interpretation are independently justified.
