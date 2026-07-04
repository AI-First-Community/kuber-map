# Cross-Domain Bridges

FIBO is organized into separately-governed domains (LOAN, SEC, DER, …). Real financial tasks cross
those boundaries — a mortgage-backed security is backed by mortgage *loans*; a reporting party is
identified by its *LEI*. FIBO often models both endpoints but doesn't draw the edge between them.

Kuber Map curates those missing edges as **bridges**. They are the project's contribution-back
candidate for the EDM Council, and each is grounded and gated.

## How a bridge is validated

`etl/bridges.py` rejects a bridge unless:

1. **Both endpoints resolve to real FIBO classes** in the extract — no invented IRIs.
2. **FIBO does not already assert the edge** (source → target) — nothing here duplicates FIBO.
3. It carries a **rationale + an external citation** (a regulation or standard).

Bridges are stored as OKF with `provenance: curated`, so they're never confused with FIBO's own
relations. There are **19** across the five use cases.

## Examples

| Bridge | Kind | Citation |
|---|---|---|
| HMDA-covered-loan **reported-in** HMDA-report | LOAN intra-domain | 12 CFR 1003.4 (Reg C) |
| legal-entity **identified-by** LEI | CMNS → BE | ISO 17442; FATF Rec. 24 |
| beneficial-owner **beneficial-owner-of** legal-entity | BE → CMNS | FATF Recs 24 & 25; US CDD rule |
| MBS **backed-by** mortgage | SEC → LOAN | SEC Regulation AB, 17 CFR 229.1100 |
| issuer **identified-by** LEI | FBC → BE | ISO 17442; MiFID II / SEC |
| reporting-party **identified-by** LEI | FND → BE | ISO 17442; MiFID II; CFTC |
| regulatory-report **submitted-to** regulatory-agency | CMNS | supervisory reporting practice |
| credit-default-swap **references** bond | DER → SEC | ISDA Credit Derivatives Definitions |
| swap **cleared-through** clearing-house | DER → FBC | Dodd-Frank Title VII; EU EMIR |

(Full list of 19 in [contrib/edmc-bridge-contribution.md](https://github.com/AI-First-Community/Bodhi-Map-For-FinTech/blob/main/contrib/edmc-bridge-contribution.md).)

## The contribution package

`make contrib` (`etl/export_bridges.py`) packages all 19 bridges into `contrib/`:

- **`edmc-bridge-contribution.md`** — the proposal: methodology + per-use-case tables with IRIs,
  rationale, and citations.
- **`fibo-bridges.ttl`** — RDF/Turtle where each bridge is a proposed triple in a neutral `kmb:`
  namespace plus an `owl:Axiom` annotation carrying its rationale, citation, and provenance.

We deliberately do **not** assert unverified FIBO/OMG object properties (Golden Rule 1: never
invent). The artifact identifies the *gap* and cites its basis; mapping each edge to the right FIBO
property — or minting one — is the reviewer's call.
