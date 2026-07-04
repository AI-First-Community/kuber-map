# Phase 0.5 Spike Results — FIBO Restriction Extraction

Date: 2026-07-04 · Scope: FND + LOAN (sparse checkout) · Verdict: **✅ De-risked — proceed to Phase 1**

## What we set out to prove
The audit flagged the #1 technical blocker: FIBO's real relationships (`secured-by`, `isCollateralizedBy`, …) are **`owl:Restriction` blank-node axioms on `rdfs:subClassOf`, not flat triples**. If our extractor couldn't walk them, the whole value prop (typed edges, cross-domain bridges, agent grounding) collapses.

## Result: it works, end to end
`etl/extract.py` (rdflib) → `out/intermediate.json` → `etl/to_okf.py` → `knowledge/` OKF bundle.

| Metric (FND + LOAN) | Value | Note |
|---|---|---|
| RDF files parsed | 79 | 16,685 triples merged |
| Classes extracted | 611 | |
| **with `skos:definition`** | **555 (90%)** | ⬆ curation budget **much smaller** than the audit feared |
| Total edges | 1,323 | |
| `is-a` (named subClassOf) | 659 | |
| **Typed edges (from restrictions)** | **664** | the hard part — **solved** |
| **Cross-domain edges** | **159** | LOAN→FND 92, LOAN→FBC 55, LOAN→BE 4, … |
| Maturity propagation | ✅ | per-ontology `hasMaturityLevel` → class tags (e.g. LOAN mortgages = *Provisional*) |

**Worked example** — `loan secured by real estate` [LOAN, Provisional] correctly yields both named `is-a` (→ CollateralizedLoan) and restriction-derived typed **cross-domain** edges (`isCollateralizedBy → RealProperty` [FND], `refersTo → SecurityAgreement` [FBC]).

## What this changes in the plan
1. **Blocker #1 (OWL restriction extraction) → resolved.** Readiness moves toward green for Phase 1.
2. **Definition coverage 90%**, not "many missing" — the curation bottleneck (audit's biggest cost concern) is smaller. Curation is now mostly *core-set selection + learner rewrites*, not *writing missing definitions*.
3. **Cross-domain edges already abundant *within* restrictions** — reconfirms the corrected thesis (§3.1): FIBO is *not* thin across domains at the axiom level; the gap is **lateral business bridges + surfacing**, which we can now *measure* per domain (this run: 159 FND/FBC/BE targets from LOAN).

## Known cleanups (not blockers)
- **Edge-label normalization:** labels mix spaced (`is performed by`) and camelCase (`isCollateralizedBy`) — the latter appears when the property's `rdfs:label` lives in a domain we didn't check out (FBC). Resolves as more domains load; add a normalization pass.
- **Leakage:** `FBC=3`, `UNSCOPED=12` classes appeared (imported stubs + non-fibo namespaces like Commons/LCC). Filter by "defined-here + fibo namespace" in the real ETL.
- **One self-referential axiom** (`assumes → LoanSecuredByRealEstate`) — inspect during ETL hardening; likely a modeling artifact, harmless.
- IRI→path mapping is currently flat `/<DOMAIN>/<id>.md`; formalize (with round-trip) before scaling.

## Artifacts produced
- `etl/extract.py` — restriction-aware extractor (walks `owl:onProperty` + `someValuesFrom`/`allValuesFrom`/`onClass`/`hasValue`)
- `etl/to_okf.py` — record → OKF markdown (frontmatter `relations:` + body links + per-domain `index.md`)
- `out/intermediate.json` — 611 class records
- `knowledge/` — generated OKF bundle (611 files)
- `.venv/` (rdflib 7.6.0), `fibo-source/` (sparse FND+LOAN, pinned to master — **pin to a Production tag next**)

## ETL hardening pass (done) — all spike cleanups closed
Added `etl/fibo_ns.py` (shared namespace/path/label helpers) + `etl/validate.py`; refactored extract/emit.

| Cleanup | Before | After |
|---|---|---|
| Edge labels | mixed (`is performed by`, `isCollateralizedBy`) | kebab-normalized (`is-performed-by`, `is-collateralized-by`) |
| Namespace leakage | 3 FBC + 12 Commons stubs emitted as junk nodes | classified (Commons→**CMNS**, LCC→**LCC**), 15 out-of-scope stubs dropped from bundle |
| Self-loops | present | **0** |
| **IRI→path collisions** | flat scheme silently overwrote (595/596) | **module-aware paths** mirror FIBO (`/LOAN/RealEstateLoans/Mortgages/…`), collision-free — e.g. FND's two `TransactionEvent` classes now resolve to distinct files |
| Definition coverage | 90% | **93%** (after dropping stubs) |
| FIBO source pin | `master` (floating) | pinned to **commit `ae12db3`** (`fibo-source.pin`) |

**Reality check on pinning:** the plan assumed a "FIBO Production tag" — but GitHub `edmcouncil/fibo` has only a `2018Q3` tag; modern releases roll on `master` and are published via OMG / spec.edmcouncil.org, not git tags. → We pin to a **commit SHA** for reproducibility (documented in `fibo-source.pin`).

Validation on the hardened bundle: 596 concepts, 1,278 frontmatter edges (924 resolved in-bundle, 354 pending cross-cluster links awaiting their domains), 0 self-loops, 219 orphan nodes (expected — roots + classes referenced only from not-yet-loaded domains).

## Recommended next step
Formalize the ETL (namespace filtering, edge-label normalization, IRI→path scheme, pin FIBO Production tag), then start the **Loan Origination MLV** (§10 Phase 1): hand-pick the ~40–60 `core:` concepts + lateral bridges, build the context-pack export, and run the grounded-vs-ungrounded agent eval.
