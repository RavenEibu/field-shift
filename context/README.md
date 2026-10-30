# Canonical Operational Context

`context/` is Field Shift's canonical operational knowledge layer.

It exists so that humans, application code, analytical tooling, and AI agents can work from the same explicit project context instead of reconstructing meaning from scattered documents.

## Human-first, machine-actionable

Context files should remain readable without specialized tooling while using structure where structure improves consistency and retrieval.

The goal is not to create an AI-only prompt repository. The goal is to maintain a shared operational representation of project knowledge.

## What belongs here

Examples include:

- data-source definitions
- domain terminology
- assumptions
- canonical entities and relationships
- evidence metadata
- decision rules
- validation state
- learning candidates and promotion history

Explanatory narratives, project rationale, and high-level architecture belong primarily in `docs/`.

## Canonical-source hierarchy

When sources disagree, prefer evidence in this order unless a documented reason justifies otherwise:

1. Authoritative provider documentation and dataset metadata.
2. Peer-reviewed or primary domain references.
3. Validated project-derived evidence.
4. Curated third-party discovery resources.
5. AI-generated synthesis or hypothesis.

AI-generated content is never authoritative solely because it is fluent or confident.

## Knowledge states

Structured knowledge should make its status explicit when relevant:

- `candidate` — identified but not yet validated for project use
- `validated` — checked against appropriate evidence
- `active` — approved for operational use
- `deprecated` — retained for traceability but no longer recommended
- `rejected` — evaluated and explicitly not accepted

## Provenance

Operational facts should preserve enough metadata to answer:

- Where did this come from?
- When was it checked?
- What version or product does it refer to?
- At what spatial and temporal scale is it valid?
- What transformation produced it?
- What limitations apply?
- Is it observation, interpretation, or inference?

## Repository relationship

`docs/` explains the project.

`context/` defines the operational knowledge the project uses.

Code should consume structured context where practical rather than hard-coding domain assumptions without provenance.
