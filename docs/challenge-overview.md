# Challenge Overview

## Field Shift: Adapting Farms with NASA Data

Field Shift is developed for the **2026 NASA International Space Apps Challenge**.

Official challenge page: https://www.spaceappschallenge.org/2026/challenges/field-shift-adapting-farms-with-nasa-data/

The official challenge asks teams to create a decision-support tool that combines NASA Earth observations with local soil information, crop characteristics, and farmer priorities so farmers can explore crop-rotation strategies that strengthen soil health and adapt to changing environmental conditions.

## Problem framing

Farmers make rotation decisions under interacting pressures such as changing rainfall, water shortages, temperature variability, extreme weather, and declining soil health.

Earth-observation data can characterize environmental conditions, but observations alone do not answer the farmer's decision:

> Given the conditions of my field or region, which crop-rotation strategies should I consider, and why?

Field Shift focuses on the layer between observation and decision.

## Four input families

### 1. NASA Earth observation data

Candidate signals include:

- precipitation
- temperature
- soil moisture
- evapotranspiration and plant water use
- vegetation condition
- regional water-storage trends

### 2. Local soil context

Candidate characteristics include:

- texture
- water-holding capacity
- organic matter
- pH
- drainage characteristics
- other locally available agronomic attributes

### 3. Crop knowledge

Candidate characteristics include:

- water requirements
- drought tolerance
- growing period
- rooting characteristics
- nutrient interactions
- rotation compatibility
- soil-health effects

### 4. Farmer priorities

Different farmers may optimize for different outcomes, including:

- water conservation
- soil health
- productivity
- resilience
- diversification
- lower climate risk

The recommendation model must preserve these priorities instead of assuming a single universal optimum.

## Expected decision support

Field Shift should not stop at an environmental dashboard.

The target output is a comparison of plausible rotation strategies with understandable evidence, benefits, risks, trade-offs, uncertainty, and limitations.

A useful result should answer:

- what environmental evidence is relevant
- how the evidence affects the evaluation
- why one rotation scores differently from another
- what assumptions were used
- what the system does not know

## Research accelerator

Space Data Atlas provides a useful third-party mapping between the challenge and candidate NASA datasets, including starter code:

https://spacedata.swapniltamse.com/challenges/field-shift-adapting-farms/

It is **not an official NASA resource list**. Field Shift may use it to accelerate discovery, but authoritative NASA product documentation remains the canonical source for dataset metadata and limitations.
