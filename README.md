# Field Shift

> **Data-driven crop rotation decisions under climate variability using NASA Earth Observations and local agricultural intelligence.**

Field Shift is an open-source agronomic decision support system designed for the NASA Space Apps Challenge. It assists farmers, agronomists, and land managers in evaluating resilient crop rotation sequences that mitigate drought risks and sustain long-term soil productivity.

---

## 1. Project Implementation Maturity

Field Shift maintains transparent labeling of implementation status across each functional subsystem:

| Subsystem | Maturity Status | Implementation Scope & Evidence |
|---|---|---|
| **Data Acquisition Layer** | `[IMPLEMENTED]` | Automated NASA POWER daily point acquisition (1991–2025) and SMAP L4 daily adapter retrieval executed against prototype anchor. |
| **Standardization & Schemas** | `[PROTOTYPED]` | JSON schemas for acquisition receipts and canonical observations defined (`data/schemas/`); baseline data validation in progress. |
| **Agro-Climatic Indicators** | `[PLANNED]` | Specification of evaporative demand, thermal stress, and root-zone soil moisture deficit metrics documented in methodology. |
| **Rotation Decision Model** | `[PLANNED]` | Multi-objective trade-off framework comparing economic margin vs climate resilience across rotation sequences. |
| **Interactive Demo & UX** | `[CONCEPTUAL]` | Exploratory Jupyter walkthrough notebooks and interactive decision prototype architecture planned for challenge showcase. |

---

## 2. The Agricultural Decision Problem

Under escalating climate variability, extreme heat events, and recurring droughts, conventional crop sequences often deplete soil water reserves, increase financial risk, and degrade soil biology.

```text
Agricultural Problem
    ↓
Farmer Decision: "Which crop rotation strategy minimizes climate risk while sustaining farm viability?"
    ↓
NASA Earth Observations (POWER Climate Baseline + SMAP Root-Zone Soil Moisture)
    ↓
Local Context (INTA Soil Series & Crop History)
    ↓
Scientific Methodology & Multi-Objective Trade-Off Evaluation
    ↓
Actionable Decision Recommendations & Interactive Demonstration
```

---

## 3. NASA Earth Observation Core

Field Shift builds its environmental baseline on authoritative NASA Earth science data:

1. **NASA POWER (Prediction of Worldwide Energy Resources):**
   - **Daily Agroclimatology (AG):** Provides 35 years (1991–2025) of continuous meteorological history on a 0.5° lat × 0.625° lon grid: solar radiation (`ALLSKY_SFC_SW_DWN`), air temperature extremes (`T2M_MAX`, `T2M_MIN`), relative humidity (`RH2M`), and precipitation (`PRECTOTCORR`).
   - **Decision Role:** Computes historical climate normals, thermal stress duration, and atmospheric evaporative demand.
2. **NASA SMAP (Soil Moisture Active Passive):**
   - **Level-4 Global Geophysical Data (SPL4SMGP Version 8, DOI: 10.5067/T5RUATAQREF8):** Model-assimilated root-zone soil moisture (`RZMC`, 0–100 cm depth) and surface soil moisture (`SFMC`, 0–5 cm depth) on a 9 km global grid.
   - **Decision Role:** Quantifies root-zone plant-available water at critical crop development stages and fallow recovery periods.
3. **Local Argentine Ground Truth (INTA):**
   - **INTA Agrometeorological Network:** In-situ ground truth cross-validation for satellite precipitation and temperature.
   - **INTA Mapa Nacional de Cultivos:** Historical 30 m classified crop succession patterns.
   - **INTA SisINTA:** Measured soil profile physical properties (field capacity, wilting point, organic carbon) from georeferenced field and laboratory surveys.
   - **ISRIC SoilGrids:** Contextual modeled fallback (250 m) when measured local profiles are unavailable.

---

## 4. Prototype Anchor: Villa Mercedes, San Luis

To ground the methodology in real-world agriculture, Field Shift anchors its MVP on the **EEA INTA San Luis Experimental Field** (Villa Mercedes, San Luis, Argentina: `-33.6500, -65.3667`, EPSG:4326). This semi-arid, climate-sensitive agricultural zone exhibits pronounced rainfall variability and water-limited crop yields, making it an ideal proving ground for rotation resilience modeling.

---

## 5. Validated Runtime Compatibility Envelope

Field Shift execution is validated against a defined workstation compatibility envelope:

- **Hardware Architecture:** Linux x86_64
- **Operating System:** CachyOS / compatible modern Linux userspace (glibc 2.38+)
- **Storage / Mount Baseline:** Canonical portable mount at `/mnt/field-shift`
- **Python Tooling:** Managed via `uv` with strictly frozen dependencies (`uv.lock`)
- **Python Version:** 3.13
- **Geospatial System Libraries:** GDAL 3.13+, PROJ 9.9+, GEOS 3.15+

### Installation & Verification
```bash
# Clone the repository
git clone https://github.com/RavenEibu/field-shift.git
cd field-shift

# Synchronize reproducible virtual environment
uv sync --frozen

# Verify environment and system bindings
uv run python scripts/verify_environment.py
```

---

## 6. Repository Structure

```text
field-shift/
├── data/
│   ├── manifests/         # Authoritative acquisition receipts & data manifests
│   ├── schemas/           # JSON schemas for observations & acquisitions
│   └── sources/           # Formal specifications of NASA and INTA data sources
├── docs/
│   ├── architecture.md    # Pipeline architecture, engine dataflow, and maturity tags
│   ├── contracts/         # Data contracts and decision evaluation schemas
│   ├── data-sources/      # Transparent source evaluation matrix and reviews
│   └── methodology/       # Agronomic assumptions and operational model
├── notebooks/             # Reproducible scientific walkthrough notebooks
├── presentation/          # NASA presentation decks and visual demo assets
├── scripts/               # Environment verification and reproducibility tools
└── src/                   # Decision engine, indicators, and model logic
```

---

## 7. License & Open Source Governance

Field Shift is open-source software licensed under the [MIT License](LICENSE). See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).
