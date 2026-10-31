# Satellite and Supporting Data Sources — Multi-Attribute Evaluation

This document outlines the transparent evaluation of NASA Earth Observation datasets and Argentine ground-truth supporting sources for the Field Shift agricultural decision support engine.

## 1. Transparent Evaluation Framework

Rather than computing arbitrary pseudo-scientific numeric percentages, sources are qualified using concrete technical and operational attributes:

1. **Scientific Authority:** Recognized international space agency or national agricultural research institution.
2. **Spatial Scope & Resolution:** Macro-climate, regional grid, or field-scale applicability.
3. **Temporal Scope & Latency:** Historical baseline span and latency from observation to publication.
4. **Primary Decision Role:** Meteorological context, root-zone soil water estimation, crop history, or ground verification.
5. **Known Limitations:** Inherent scale constraints (e.g. coarse grid cannot resolve parcel boundaries, remote sensing classification uncertainty).

---

## 2. Multi-Attribute Evaluation Matrix

| Source Product | Providing Authority | Native Resolution | Temporal Frequency | Primary Role in Field Shift | Status for MVP | Known Limitations |
|---|---|---|---|---|---|---|
| **NASA POWER Daily AG** | NASA Langley ASDC / GMAO | 0.5° lat × 0.625° lon (MERRA-2 meteorology & PRECTOTCORR) / 1.0° (Solar) | Daily (1991–2025) | Historical climate normals, thermal & evaporative stress context | **CORE MVP** | Standard baseline acquisition uses MERRA-2 precipitation (~0.5° × 0.625°), NOT IMERG 0.1°. Regional grid spatial average, not a direct parcel rain gauge. (See `data/sources/power-parameter-lineage.yml`). |
| **NASA SMAP L4 (SPL4SMGP v8)** | NASA NSIDC / GSFC | 9 km global EASE-Grid 2.0 (native SPL4SMGP v8: 3-hourly, ~9 km) | Daily UTC (2015–2025) | Regional modeled surface & root-zone (0–100 cm) soil moisture context | **CORE CANDIDATE — RETRIEVAL/OBSERVATION BLOCKED** | Model-assimilated geophysical product (distinct from plant-available water). Available direct pathway: Earthdata / NSIDC archive (direct HDF5). Attempted project pathway: POWER high-resolution adapter query (2015–2025), which yielded 0 usable observations (all values -999.0 across 3,928 returned timestamps). Observation data is quarantined and blocked from decision models pending direct DAAC integration (E1 NOT_SATISFIED). |
| **INTA Mapa Nacional Cultivos** | INTA Argentina | 30 m (Sentinel-2 / Landsat classified raster) | Annual campaign (2018–2024) | Observed crop sequence history & baseline rotation verification | **CORE SUPPORTING** | Remote sensing classification uncertainty; 30 m pixel is a spectral class, not an on-farm management record or property boundary. |
| **INTA Agrometeorological Net** | INTA SIGA | Point station | Daily / Hourly | In-situ ground truth cross-validation for satellite temperature & precipitation | **VALIDATION REFERENCE** | Station density and distance to prototype anchor determine representativeness. |
| **INTA SisINTA** | INTA Argentina | Georeferenced field & lab soil profiles | Static / periodic sampling | Measured local soil profile physical properties (field capacity, wilting point, OC) | **PREFERRED LOCAL SOIL** | Discrete profile points; requires location, depth, and representativeness review before application to prototype field. |
| **ISRIC SoilGrids 250 m** | ISRIC World Soil Information | 250 m (Global ML spatial prediction) | Static modeled prediction (v2.0) | Secondary regional soil context and fallback when measured profiles are unavailable | **FALLBACK CONTEXT ONLY** | ISRIC explicitly advises against field/farm-level direct interpretation; carries explicit prediction intervals (q05, q50, q95). |
| **ECOSTRESS** | NASA JPL | 70 m | 1–5 days | Evapotranspiration (ET) and plant water stress | **MVP+ (Deferred)** | Orbital repeat cycle; post-MVP integration. |
| **HLS (Harmonized Landsat-Sentinel)** | NASA GSFC | 30 m | 2–3 days | Field-scale vegetation indices (NDVI/EVI) | **MVP+ (Deferred)** | Cloud cover susceptibility; reserved for field-scale phase. |
| **GPM IMERG** | NASA GSFC | 0.1° × 0.1° | 30 min / Daily | High-resolution precipitation supplement | **DEFERRED** | Optional high-resolution precipitation pathway in POWER and direct DAAC; not requested in baseline MVP. |
| **GRACE / GRACE-FO** | NASA / GFZ | ~300 km | Monthly | Deep aquifer and terrestrial water storage anomalies | **REGIONAL CONTEXT** | Extremely coarse; macro-hydrological basin context only. |

---

## 3. Soil Data Authority Principle

Field Shift establishes a strict hierarchy for soil evidence:

1. **Measured Ground Truth (INTA SisINTA):** Georeferenced, physically sampled and laboratory-analyzed soil profiles are the primary authority for soil water holding capacity and profile texture.
2. **Modeled Global Prediction (ISRIC SoilGrids):** Used exclusively as a contextual fallback when local surveyed profiles are absent. Global 250 m machine-learning outputs must carry their prediction intervals and never be presented as measured farm soil tests.
