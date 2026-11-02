# Open-Source Runtime Stack Decision — 2026-11-02

## Decision

Field Shift must be installable, runnable, inspectable, and demonstrable end-to-end without requiring commercial software licenses or proprietary runtime services.

The scientific and analytical core must remain independent from the visualization technology. Validation rules, transformations, indicators, provenance, and decision logic belong in version-controlled code, schemas, and reproducible datasets rather than existing only inside dashboards.

## Baseline direction

The MVP should evolve from validated data shape and workload rather than from a preselected dashboard product.

Preferred open analytical formats and tools are:

- Python for validation, transformation, indicators, and decision logic;
- Parquet for tabular and time-series analytical data;
- GeoParquet for vector geospatial analytical data;
- GeoTIFF/COG when raster semantics must be preserved;
- DuckDB for local analytical SQL and file-based serving;
- JupyterLab for exploration and scientific analysis;
- QGIS and GeoPandas for spatial inspection and analysis;
- Apache Superset as a candidate reusable BI-style analyst surface;
- Streamlit as a candidate rapid interactive MVP/product surface;
- MapLibre GL JS or Leaflet if web-native mapping becomes necessary.

PostgreSQL/PostGIS is deferred until a validated requirement exists for centralized serving, multiple consumers, application/API access, or repeated indexed spatial queries.

## Not baseline dependencies

Field Shift must not require Power BI, Tableau, ArcGIS, Oracle Database, Microsoft SQL Server, proprietary mapping SDKs, or cloud-only commercial BI/analytics services in order to reproduce, validate, demonstrate, or operate the project.

This does not prohibit a contributor from using proprietary software personally when available; it prohibits making that software a required part of the reproducible project path.

## Architecture invariant

```text
raw evidence
  -> validated data
  -> curated analytical data
  -> derived features / indicators
  -> serving layer
  -> replaceable visualization / decision interface
```

Visualization requirements may constrain what the data pipeline must preserve, but visualization software must not define the scientific meaning of Field Shift data.

## Complexity gate

Candidate technologies are not automatic implementation commitments. A new service or platform is introduced only when a validated project requirement justifies its operational and architectural complexity.
