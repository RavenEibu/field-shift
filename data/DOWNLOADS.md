# Field Shift — Data Access and Downloads

This file centralizes the authoritative access points for the current Field Shift MVP data stack.

> Do not commit large downloaded datasets to Git. Keep raw files locally under `data/raw/` and preserve retrieval metadata in version-controlled manifests.

## 1. NASA POWER — climate and environmental time series

**Role:** core regional climate context.

- Data Access Viewer: https://power.larc.nasa.gov/data-access-viewer/
- Daily API documentation: https://power.larc.nasa.gov/docs/services/api/temporal/daily/
- Parameter dictionary: https://power.larc.nasa.gov/parameters/
- Hydrology / SMAP aliases: https://power.larc.nasa.gov/docs/methodology/data/sources_hydrology/

POWER is query-based rather than a single file download. Prefer a reproducible API request for the selected prototype coordinate and period.

Example request shape:

```text
https://power.larc.nasa.gov/api/temporal/daily/point
  ?parameters=<PARAMETERS>
  &community=AG
  &longitude=<LONGITUDE>
  &latitude=<LATITUDE>
  &start=<YYYYMMDD>
  &end=<YYYYMMDD>
  &format=CSV
  &time-standard=UTC
```

Candidate climate parameters include temperature, precipitation, relative humidity, wind, and solar radiation. SMAP L4 high-resolution aliases of interest include `SFMC`, `RZMC`, `SFMC_PRCNTL`, and `RZMC_PRCNTL`.

Do not download the full POWER archive for the MVP.

## 2. NASA SMAP L4 — surface and root-zone soil moisture

**Role:** core regional water-stress context.

Product: `SPL4SMGP`, Version 8.

- NSIDC product page: https://nsidc.org/data/spl4smgp/versions/8
- NASA Earthdata Search: https://search.earthdata.nasa.gov/search?q=SPL4SMGP
- DOI: https://doi.org/10.5067/T5RUATAQREF8

A free NASA Earthdata Login is required for direct raw-product access.

For the MVP, prefer a spatial/temporal subset rather than the complete 3-hourly global archive. POWER can also expose daily SMAP L4 aliases for a simpler first integration while NSIDC remains the product authority.

**Current quality note:** NSIDC reports that SMAP Standard and Near Real-Time data from 2026-05-14 through 2026-07-28 experienced a geolocation issue and L4 products for that interval are being reprocessed. Avoid treating that period as stable until the replacement is confirmed.

## 3. INTA — Mapa Nacional de Cultivos

**Role:** observed crop-history / crop-sequence baseline for Argentina.

These are 30 m GeoTIFF products. For a historical sequence, download the relevant summer/winter maps for each campaign and clip them locally to the prototype area.

### Campaign records

- 2024/2025: https://zenodo.org/records/17652712
- 2023/2024: https://zenodo.org/records/13984185
- 2022/2023: https://zenodo.org/records/10103323
- 2021/2022: https://zenodo.org/records/8284081
- 2020/2021: https://zenodo.org/records/8286318
- 2019/2020: https://zenodo.org/records/8286310
- 2018/2019: https://zenodo.org/records/8286326

### Direct latest GeoTIFF downloads

- Winter 2024: https://zenodo.org/records/17652712/files/MNC_inv24.tif?download=1
- Summer 2025: https://zenodo.org/records/17652712/files/MNC_ver25.tif?download=1

Also download the methodology/accuracy report from each campaign record. The crop class must remain tied to campaign, legend, product version, and documented classification accuracy.

## 4. INTA SisINTA / INTA GEO — measured soil profiles

**Role:** preferred local soil evidence.

- SisINTA information: https://www.argentina.gob.ar/noticias/sisinta-contiene-7000-perfiles-de-suelos-georreferenciados
- INTA GEO viewer: https://visor.inta.gob.ar/es#3.16/-33/-68.56

Do not bulk-download profiles blindly. First select a profile that is geographically and pedologically representative of the prototype area, then export its public field/laboratory data.

Required checks include location, sampling date, horizons/depths, methods, measured properties, landscape/soil unit, and representativeness.

## 5. INTA agrometeorological network — independent validation

**Role:** validate NASA regional climate signals against local in-situ observations where comparable.

- INTA agroclimatic portal: https://www.argentina.gob.ar/inta/informacion-agroclimatica
- SIGA: https://siga.inta.gob.ar/

INTA states that the network data are freely downloadable. Select the exact station only after the prototype area is fixed and record station identity, coordinates, elevation, period, variables, missingness, and measurement metadata.

## 6. FAO crop-water knowledge

**Role:** authoritative reference knowledge, not an observation dataset.

- FAO-56 — Crop Evapotranspiration: https://www.fao.org/4/x0490e/x0490e00.htm
- AquaCrop input requirements: https://www.fao.org/aquacrop/overview/input-requirements/

Use these sources to structure crop-water, rooting, growth-stage, evapotranspiration, soil-water, and management concepts. Do not treat generic FAO parameters as locally validated cultivar values without checking applicability.

## 7. SoilGrids — fallback only

**Role:** modeled soil context only when appropriate measured/local soil evidence is unavailable.

- SoilGrids documentation: https://docs.isric.org/globaldata/soilgrids/
- Access guidance: https://docs.isric.org/globaldata/soilgrids/SoilGrids_faqs_02.html
- WCS guidance: https://docs.isric.org/globaldata/soilgrids/wcs.html
- WebDAV index: https://files.isric.org/soilgrids/latest/data/

For the MVP, use WCS to request only the required spatial subset and properties. Do **not** download global SoilGrids maps: individual property/depth/quantile collections can be very large.

SoilGrids must remain labeled as modeled/predicted context, not as field measurement.

## Recommended download order

1. INTA crop maps for the campaigns needed to reconstruct crop history.
2. A selected local SisINTA soil profile after the prototype area is fixed.
3. NASA POWER through reproducible API requests — no bulk archive.
4. SMAP L4 through POWER aliases for the first prototype, then raw NSIDC/Earthdata subsets when raw-product validation is needed.
5. A nearby INTA/SIGA station for independent climate validation.
6. FAO reference material for crop-water modeling.
7. SoilGrids only if measured/local soil evidence remains incomplete.

Supporting NASA sources such as HLS, GPM IMERG, ECOSTRESS, and GRACE/GRACE-FO are intentionally not part of the first download set. See `context/source-fitness.md` for the rationale and current ratings.