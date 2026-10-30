# Contributing

Field Shift is a public, evidence-driven project developed for the NASA International Space Apps Challenge 2026.

## Canonical language

English is the canonical language of the repository. Use English for documentation, issues, pull requests, commit messages, code comments, schemas, structured context, and presentation material.

## Working principles

Contributions should prioritize:

1. Human readability.
2. Evidence and provenance.
3. Traceability of decisions.
4. Reproducibility.
5. Simplicity before abstraction.
6. Explicit uncertainty and limitations.

Avoid speculative architecture. Add structure when a concrete requirement, dataset, decision, or implementation need justifies it.

## Documentation and context

`docs/` is primarily human-oriented explanatory documentation.

`context/` is the canonical operational context: structured, explicit knowledge intended to be understandable by humans and reliably consumable by software, analytical tooling, and AI agents.

These layers must complement each other. Do not maintain duplicate canonical facts in multiple places when a reference is sufficient.

## Data and evidence

When introducing a dataset, model assumption, or domain claim, document as appropriate:

- source and provider
- dataset or product identifier
- intended use
- relevant spatial and temporal scope
- known limitations
- provenance or retrieval method
- validation status

Do not present inferred or AI-generated information as evidence solely because an AI system produced it.

## AI-assisted contributions

AI-assisted work is allowed and expected where it improves productivity or analysis.

Human contributors remain responsible for validating factual claims, scientific assumptions, code behavior, data transformations, citations, provenance, and changes to accepted decision logic.

Field Shift follows a human-first, AI-optimized approach: AI should reduce reconstruction and repetitive work, not become a prerequisite for understanding the project.

## Learning governance

New patterns, hypotheses, or inferred relationships should enter the learning lifecycle as candidates. They must not silently modify active knowledge or decision rules.

The intended lifecycle is:

`candidate -> shadow -> validated -> promoted | rejected`

Promotion into active knowledge requires explicit validation.

## Security and privacy

Never commit:

- passwords
- API keys
- access tokens
- private keys
- local `.env` files
- personal information
- confidential information
- proprietary datasets without permission
- private NASA Earthdata credentials

Use environment variables and local credential mechanisms. Commit only safe examples such as `.env.example`.

## Commit style

Prefer small, conceptually coherent commits. Conventional-style prefixes are encouraged, for example:

- `docs:` documentation
- `feat:` product or framework capability
- `feat(context):` canonical context capability
- `feat(sources):` source registry changes
- `feat(learning):` learning lifecycle changes
- `chore:` repository maintenance or bootstrap
- `test:` tests and validation assets
