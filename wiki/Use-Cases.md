# Use Cases

Kuber Map curates FIBO into **learner-first, agent-grounding use cases**. Each is a hand-picked
"core" concept set drawn from across FIBO's domains, with worked examples on every card, a set of
validated cross-domain bridges, and an exported context pack an AI agent can ground on.

## The five use cases

| Use case | Core | Spans | Bridges | Pack |
|---|---|---|---|---|
| **Loan origination & underwriting** | 71 | LOAN, FBC, FND, BE | 4 | `export/loan-origination/` |
| **KYC & beneficial ownership** | 58 | CMNS, BE, FND, FBC | 4 | `export/kyc/` |
| **Securities instruments & issuance** | 59 | SEC, FBC | 3 | `export/securities/` |
| **Regulatory reporting & compliance** | 52 | CMNS, FBC, FND, BE, BP, LOAN, CAE, SEC (8 clusters) | 4 | `export/regulatory-reporting/` |
| **Derivatives contracts & trading** | 60 | DER, FBC, FND | 4 | `export/derivatives/` |

**284 core concepts, 19 cross-domain bridges** in total. On the map these are the default view;
the **use-case lens** (top bar) focuses one, and each detail card shows which use case(s) a concept
belongs to.

## How a use case is built (spec-driven, grounded)

A use case is a spec under `curation/usecases/` — no code change to add one:

1. **Facet spec** (`<uc>.json`) — a list of `[local-id, cluster]` entries grouped into facets.
   `etl/nominate_core.py` resolves every id against the FIBO extract and **rejects any that isn't
   a real class** (the anti-hallucination gate).
2. **Bridges** (`<uc>-bridges.json`) — cross-domain relations FIBO doesn't draw natively.
   `etl/bridges.py` verifies both endpoints exist **and** that FIBO doesn't already assert the
   edge, and requires a rationale + citation for each.
3. **Overlays** (`<uc>-examples.json`, `-definitions.json`) — worked examples and gap-filling
   definitions, applied only where FIBO supplies none, marked `provenance: curated`.
4. **Pack** — `etl/export_pack.py` emits the grounding closure as `pack.json` + `context.md` +
   an OKF slice.

Regenerate everything with `make curate && make pack` (see [Getting Started](Getting-Started)).

## Why use cases, not just the whole ontology

Dumping all 3,104 FIBO concepts at a learner or an agent is noise. A use case is the **minimal
coherent slice** for a real task (originate a loan, resolve a beneficial owner, file a regulatory
report), with the cross-domain links that make it usable — and it's exactly what the
[value-proof eval](Value-Proof) measures.
