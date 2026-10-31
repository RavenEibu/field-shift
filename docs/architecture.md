# Field Shift — Product Architecture

## 1. System Overview

Field Shift is structured as a modular, reproducible data pipeline and agronomic decision engine:

```text
┌──────────────────────────────────────────────────────────┐
│             1. DATA ACQUISITION LAYER [PARTIAL]          │
│  NASA POWER Daily AG [IMPLEMENTED]                       │
│  NASA SMAP L4 Soil Moisture [TRANSPORT RETRIEVED/NO OBS] │
│  INTA Ground Truth & Soil Series [PLANNED]               │
│  INTA Crop Succession History [PLANNED]                  │
└────────────────────────────┬─────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────┐
│          2. STANDARDIZATION & VALIDATION [PROTOTYPED]    │
│  - Spatial & temporal harmonization (UTC, EPSG:4326)     │
│  - Strict schema validation (canonical-observation)      │
│  - Evidence Claim Gate verification                      │
└────────────────────────────┬─────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────┐
│         3. AGRO-CLIMATIC INDICATOR ENGINE [PLANNED]      │
│  - Root-zone water availability index                    │
│  - Critical growth window drought risk                   │
│  - Thermal extreme frequency (heat/frost stress)         │
│  - Fallow recharge efficiency                            │
└────────────────────────────┬─────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────┐
│        4. ROTATION DECISION & TRADE-OFF MODEL [PLANNED]  │
│  - Multi-sequence comparative evaluation                 │
│  - Trade-off matrix: Economic Yield vs Climate Resilience │
│  - Transparent explanation & agronomic rationale         │
└────────────────────────────┬─────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────┐
│             5. PRESENTATION & DEMO UX [CONCEPTUAL]       │
│  - Interactive rotation explorer (Streamlit / Notebook)  │
│  - Field profile inspection                              │
│  - Exportable decision reports for farmers               │
└──────────────────────────────────────────────────────────┘
```

---

## 2. Layer-by-Layer Subsystem Specifications & Maturity

### Layer 1: Data Acquisition Layer `[PARTIALLY IMPLEMENTED]`
- **Scope:** Automated ingestion of authoritative NASA Earth observations and local agricultural intelligence.
- **Granular Implementation State by Source:**
  - **NASA POWER Daily AG (`[IMPLEMENTED]`):** Automated point retrieval scripts executed for prototype anchor (`-33.6500, -65.3667`) covering 1991–2025. Standard meteorology (MERRA-2 0.5°×0.625°) and solar radiation (1.0°×1.0°) acquired and checksummed.
  - **NASA SMAP L4 Soil Moisture (`[TRANSPORT IMPLEMENTED / NO USABLE OBS]`):** SPL4SMGP v8 metadata verified; initial transport via POWER-wrapped adapter retrieved but returned sentinel fill values (-999.0) resulting in 0 usable observations. Observation data is not validated or used in models pending direct Earthdata L4 integration.
  - **INTA Ground Truth, SisINTA Soil Series & Agromet (`[PLANNED]`):** Field measurement and soil profile integrations designed and planned; no automated live pipeline implemented yet.
  - **INTA Mapa Nacional de Cultivos (`[PLANNED]`):** Crop sequence classification mapping planned for future rotation modeling.

### Layer 2: Standardization & Schema Validation `[PROTOTYPED]`
- **Scope:** Normalization of heterogeneous formats (JSON, GeoTIFF, HDF5) into canonical data models with explicit CRS (EPSG:4326) and UTC timestamps.
- **Current State:** JSON schemas for `acquisition-record` and `canonical-observation` defined under `data/schemas/`. Validation against Evidence Claim Gates underway.

### Layer 3: Agro-Climatic Indicator Engine `[PLANNED]`
- **Scope:** Computation of agronomic indicators quantifying moisture stress, crop water requirements (FAO-56), and historical climatic anomalies.
- **Current State:** Mathematical formulations and indicator definitions drafted in methodology specifications; computation engine implementation scheduled.

### Layer 4: Rotation Decision & Trade-Off Model `[PLANNED]`
- **Scope:** Multi-objective evaluation of crop sequences under simulated climate stress, balancing short-term economic gross margins against multi-year soil moisture preservation.
- **Current State:** Decision contract schema and rotation templates drafted under `docs/contracts/decisions/`.

### Layer 5: Presentation & Demonstration UX `[CONCEPTUAL]`
- **Scope:** Interactive user interface for farmers and challenge judges to explore rotation scenarios, inspect soil parameters, and evaluate trade-offs.
- **Current State:** Conceptual architecture and walkthrough notebooks planned for demonstration phase.

---

## 3. Decoupled Product Canon

The public codebase is strictly self-contained and reproducible. All schemas under `data/schemas/` govern incoming observations. Internal research context, collaborative agent work contexts, and personal notes are strictly decoupled from public releases.
