# Field Shift — Product Architecture

## 1. System Overview

Field Shift is structured as a modular, reproducible data pipeline and agronomic decision engine:

```text
┌──────────────────────────────────────────────────────────┐
│             1. DATA ACQUISITION LAYER [IMPLEMENTED]      │
│  NASA POWER Daily AG  │  NASA SMAP L4 Soil Moisture      │
│  INTA Ground Truth    │  INTA Crop Succession History    │
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

### Layer 1: Data Acquisition Layer `[IMPLEMENTED]`
- **Scope:** Automated ingestion of authoritative NASA Earth observations and local agricultural intelligence.
- **Current State:** Python-based point retrieval scripts for NASA POWER Daily AG and SMAP L4 daily adapter executed for the prototype anchor (`-33.6500, -65.3667`). Raw acquisitions are checksummed and archived in Git-ignored storage.

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
