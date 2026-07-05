# Security Policy

Kuber Map is a static web app (`*.html` + `js/`), a Python ETL pipeline, and a curated
knowledge bundle. There is no server, no user accounts, and no secrets in the repository. Still,
we take reports seriously — a supply-chain issue in a dependency, a script-injection bug in the
map UI, or an accidentally committed credential all matter.

## Reporting a vulnerability

**Please do not open a public issue for a security problem.** Instead, use either:

- **GitHub private reporting** — the repo's **Security → Report a vulnerability** tab (preferred;
  keeps the report private and tracked), or
- **Email** — [sanjeev.azad@gmail.com](mailto:sanjeev.azad@gmail.com) with `KUBER-MAP SECURITY` in
  the subject.

Include what you found, where (file / URL / dependency), and how to reproduce it. A minimal proof
of concept helps a lot.

## What to expect

- **Acknowledgement** within a few days.
- An assessment and, for confirmed issues, a fix on `main` as soon as practical.
- Credit in the release notes if you'd like it (optional).

Because this is a volunteer-run community project, timelines are best-effort — thank you for your
patience and for disclosing responsibly.

## Scope

**In scope**
- Cross-site scripting or injection in the map UI (`app.html`, `m.html`, `js/`).
- Vulnerable or compromised dependencies (Python or the vendored front-end libraries).
- Secrets, tokens, or private data accidentally committed to the repository.
- CI / GitHub Actions workflow issues that could allow untrusted code execution.

**Out of scope (use a normal issue instead)**
- **FIBO fidelity** — a wrong definition, IRI, or relationship is a correctness bug, not a
  security issue. File a [FIBO fidelity issue](https://github.com/AI-First-Community/kuber-map/issues/new/choose)
  and cite the source.
- Findings that require a compromised maintainer machine or physical access.
- Missing security headers on the GitHub Pages host (outside our control).

## Supported versions

This project ships from `main` (the live app is built from it). Fixes land on `main`; there are no
separate maintained release branches.
