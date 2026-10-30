# Data Source Fitness Rating

Field Shift rates data sources for **decision fitness**, not prestige.

A high rating means a source is authoritative, reproducible, transformable, and appropriate for the specific decision role assigned to it. It does **not** mean the source is exact at parcel scale or sufficient by itself to produce a crop-rotation recommendation.

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

where `A,V,D,S,T,O` are the six 0–5 dimension scores above. Scores are reported to one decimal when needed and must be mechanically reproducible from the dimensions.

## Interpretation

| Score | Classification | Field Shift use |
|---:|---|---|
| 85–100 | A — strong | Core or near-core source when its scale matches the decision role |
| 70–84 | B — useful with controls | Use with explicit limitations or as a supporting source |
| 55–69 | C — contextual/fallback | Do not make it decisive; preserve uncertainty and corroborate |
| <55 | D — weak for this use | Discovery, exploratory, or reject unless a narrow justified role exists |

## Hard gates

A numerical score cannot override these gates:

- A source whose spatial scale is incompatible with parcel-level claims cannot be used as parcel truth.
- A modeled/predicted value cannot be presented as a field measurement.
- A third-party curated source cannot override an authoritative product owner.
- A source with unresolved product/version identity cannot become canonical.
- A recommendation cannot exceed the strongest evidence layer supporting it.

## Current reviewed sources — 2026-10-30

| Source | Role | Score | Class | Decision use |
|---|---|---:|---|---|
| NASA SMAP L4 SPL4SMGP v8 | regional soil-moisture context | 94.5 | A | Core candidate for surface/root-zone water context; not parcel measurement |
| FAO-56 / AquaCrop knowledge | crop-water knowledge | 94.0 | A | Strong authoritative agronomic reference; not an observation dataset |
| INTA Mapa Nacional de Cultivos | observed crop history | 91.5 | A | Strong Argentina crop-history baseline at 30 m; classification uncertainty remains |
| NASA POWER / MERRA-2 meteorology | regional climate context | 90.5 | A | Core for historical climate context; not parcel weather truth |
| INTA SisINTA / soil profiles | local soil characterization | 90.5* | A* | Preferred soil evidence when an appropriate nearby/public profile exists |
| SoilGrids 250 m | modeled soil fallback | 71.0 | B + hard gate | Useful modeled context, but ISRIC explicitly advises against local/farm interpretation |

`*` The SisINTA rating is a **source-system rating**, not a rating for any specific profile. A selected profile must be separately checked for distance, date, sampling method, laboratory data, depth coverage, and representativeness before use.

SoilGrids illustrates why hard gates exist: its authority, uncertainty documentation, and transformability make it a useful global/regional model, but its provider explicitly discourages local/farm-level use. Therefore it remains **fallback/context only** even though the weighted score is class B.

## Source-selection rule

Prefer the smallest set that covers the decision chain:

```text
POWER climate context
+ SMAP L4 water context
+ INTA crop history
+ local soil evidence
+ authoritative crop/rotation knowledge
+ farmer priorities
```

Add ECOSTRESS, HLS, IMERG, GRACE/GRACE-FO, or other sources only when they materially improve a defined decision and their incremental value exceeds integration complexity.

## Important distinction

This source rating is a governance and source-selection aid. It is **not** a crop-rotation score. Numerical rotation scoring remains optional until its agronomic factors, formulas, weights, uncertainty treatment, and interpretation are independently justified.