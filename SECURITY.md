# Security Policy

Field Shift is a public repository. Public does not mean that secrets or private data belong in version control.

## Never commit sensitive material

Do not commit passwords, tokens, API keys, private keys, local credential files, personal information, confidential information, proprietary datasets without permission, or private NASA Earthdata credentials.

If a secret is accidentally committed, treat it as compromised and rotate or revoke it immediately. Removing it from the latest commit is not sufficient because Git history may retain it.

## Environment configuration

Use environment variables or supported local credential stores. Only safe variable names and non-sensitive examples belong in `.env.example`.

## Public data policy

Datasets included or referenced by this repository must have clear provenance and usage rights appropriate for a public project. When in doubt, link to the authoritative source and provide retrieval instructions rather than committing a copy.

## Reporting

Do not publish credentials, personal data, or exploitable security details in a public issue. Use GitHub's private security reporting mechanism when available, or contact the repository maintainers privately through their GitHub profile.
