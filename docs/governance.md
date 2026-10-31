# Context Governance

## Purpose

This document defines how operational knowledge enters, changes, and leaves the Field Shift context layer.

## No silent promotion

A newly observed pattern, AI-generated hypothesis, or derived relationship must not silently become active domain knowledge or decision logic.

Changes that affect recommendations should be explicit, reviewable, and attributable.

## Source precedence

For dataset metadata, authoritative provider documentation takes precedence over third-party summaries.

For agronomic claims, prefer primary or well-established domain references and local expert validation where applicable.

Third-party resources may accelerate discovery but should be labeled as such.

## Required distinction

The system should distinguish among:

- `observation`: measured or estimated source data
- `derived_indicator`: transformation of observations
- `interpretation`: domain meaning assigned to an indicator
- `hypothesis`: unvalidated proposed relationship
- `decision_rule`: approved logic that affects evaluation
- `recommendation`: output produced by applying evidence and rules

## Human validation

Human review is required before candidate knowledge can become active when it:

- changes a decision rule
- changes accepted agronomic interpretation
- changes recommendation weighting
- overrides or contradicts an authoritative source
- materially changes user-facing risk or suitability conclusions

## AI responsibilities

AI systems may:

- retrieve context
- compare evidence
- identify inconsistencies
- summarize research
- propose structured candidates
- draft explanations
- detect possible patterns

AI systems must not treat their own output as independent evidence.

## Conflict handling

When two sources conflict:

1. preserve both claims and provenance
2. identify the conflict explicitly
3. compare authority, version, date, scope, and methodology
4. avoid forced reconciliation when evidence is insufficient
5. record the resolution or unresolved state

## Change history

Git history is part of project provenance. Prefer small, coherent commits so knowledge changes remain auditable.
