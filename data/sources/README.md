# Source Registry

This directory contains canonical metadata for external data sources considered by Field Shift.

## Authority rule

Dataset versions, identifiers, access requirements, resolution, and limitations must be validated against authoritative provider documentation before they are treated as active project facts.

Third-party discovery resources may accelerate research but are not authoritative.

## Validation states

- `candidate`: promising source; metadata or project fit still requires validation
- `validated`: metadata checked against an authoritative provider
- `active`: validated and currently used by the implementation
- `deferred`: valid source intentionally outside the current MVP
- `deprecated`: retained for historical traceability but should not be used for new work

## Project priority

- `core`: preferred for the first complete decision loop
- `mvp_plus`: useful after the core loop works
- `supporting`: complementary evidence or cross-check
- `contextual`: broad context that should not drive field-scale decisions directly

## Spatial integrity

The registry distinguishes dataset storage/grid resolution from effective decision scale when necessary.

Resampling a coarse dataset onto a finer grid does not create finer information.

## Discovery resources

Space Data Atlas is useful for challenge-specific dataset discovery and starter code:

https://spacedata.swapniltamse.com/challenges/field-shift-adapting-farms/

It explicitly describes its datasets as suggestions rather than the official NASA resource list. Metadata from this or any other third-party source must be checked against the authoritative NASA provider before promotion.
