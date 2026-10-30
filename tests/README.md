# Tests

This directory will contain automated tests and validation assets.

## Expected coverage

As implementation grows, tests should cover:

- source retrieval contracts
- schema validation
- data normalization
- units and missing-value handling
- spatial and temporal scope preservation
- indicator calculations
- decision-rule behavior
- inactive/shadow rule isolation
- recommendation traceability
- learning-lifecycle transitions
- reproducibility of known examples

## Scientific and functional validation

Passing software tests does not automatically validate an agronomic assumption.

Field Shift should distinguish:

- software correctness
- data-quality validation
- scientific or agronomic validation
- user-facing functional validation

All four may be necessary for recommendation-affecting behavior.
