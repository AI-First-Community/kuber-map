# Kuber Map — spike & milestone results

## Phase 1 MLV — value proof: grounded vs ungrounded eval

Date: 2026-07-04 · Model: `gpt-4o-mini` · n = 53 loan-underwriting questions · Verdict: **✅ Grounding works — the thesis holds.**

The Phase-1 question ("is this just fancy tech?") now has a real, first-party financial-semantics
number. A loan-underwriting agent answered the same 53 questions **with** the curated FIBO context
pack injected vs **without** it. Scoring is deterministic (gold-keyword coverage for accuracy;
citations matched against the pack's real IRIs), no LLM judge.

| Metric | Ungrounded | Grounded | Δ |
|---|---|---|---|
| **Accuracy** (correct ≥ 60% keyword coverage) | 45.3% | **84.9%** | **+39.6 pt** |
| Mean keyword coverage | 50.8% | 87.9% | +37.1 |
| **Auditable** (answer carries a valid FIBO IRI citation) | 0% | **98.1%** | +98.1 |
| Cite on-target (cites the grounding concept) | 0% | 88.7% | +88.7 |
| Hallucinated citation (cites an IRI not in the pack) | 5.7% | **0.0%** | −5.7 |

**Headline (our own number, not borrowed): a +39.6-point accuracy lift**, past the ≥15–20pt target,
with auditability at **98.1%** (52 of 53 grounded answers cite a real FIBO IRI) and **zero** grounded
citation hallucinations.

**Reading the numbers honestly:**
- The lift is real and large: grounding more than halves the error rate (54.7% → 15.1% wrong).
- **Auditability is 98.1%** after tightening the grounded prompt to require a verbatim
  "Sources: <IRI>" line (`eval/adapters.py` `GROUNDED_INSTRUCTION`). A first run without that
  instruction scored 88.7%; the remaining gap is one stray non-citing answer, not a data gap.
- **Grounded hallucination 0%** — the model now copies the provided IRIs verbatim instead of
  mangling them. Ungrounded's 5.7% is the opposite failure: with no context it invents IRIs, which,
  being fake, never count as valid citations, so ungrounded auditability stays 0%.
- Single run, one model (`gpt-4o-mini`), deterministic keyword scoring — directional, not a
  benchmark. Re-run across models/seeds before quoting it as a headline stat.

**Reproduce:** `EVAL_LLM_CMD='python eval/openai_cli.py --model gpt-4o-mini' python eval/harness.py --adapter llm`
(benchmark `eval/benchmark.json`, harness `eval/harness.py`, 53 questions grounded in the pack).

### Corroboration — second use case (KYC / beneficial ownership)

Date: 2026-07-04 · Model: `gpt-4o-mini` · n = 50 KYC questions · Verdict: **✅ The lift generalizes — it is not a loan-domain artifact.**

The same experiment on an independent use case (50 questions on entity resolution, beneficial
ownership, control, and identifiers, grounded in `export/kyc/pack.json`), with a domain-neutral
system prompt. If grounding only helped because the loan questions were tuned to the loan pack, a
different domain would wash the lift out. It did not — the lift is **larger**.

| Metric | Ungrounded | Grounded | Δ |
|---|---|---|---|
| **Accuracy** (correct ≥ 60% keyword coverage) | 44.0% | **92.0%** | **+48.0 pt** |
| **Auditable** (answer carries a valid FIBO IRI citation) | 0% | **92.0%** | +92.0 |
| Cite on-target (cites the grounding concept) | 0% | 84.0% | +84.0 |
| **Hallucinated citation** (cites an IRI not in the pack) | **90.0%** | **0.0%** | −90.0 |

**Reading the numbers honestly:**
- **+48-point accuracy lift** — even larger than loan's +39.6, on FIBO-specific control/ownership
  concepts (de facto vs de jure control, entity controlling party, ownership control situation)
  where an ungrounded model answers loosely.
- **Ungrounded hallucinated a FIBO-looking IRI 90% of the time** here (vs 5.7% on loan) — with no
  context and questions that beg for a citation, the bare model confidently fabricates IRIs. Grounded
  hallucination is **0%**. This is the audit-safety case in one number.
- Grounded auditability is **92%** (46 of 50 cite a real pack IRI); the 4 misses are retrieval gaps
  where the top-k context did not surface the exact grounding concept, not fabrications.
- Same caveats as above: single run, one model, deterministic keyword scoring — directional.

**Reproduce:** `EVAL_LLM_CMD='./.venv/bin/python eval/openai_cli.py' ./.venv/bin/python eval/harness.py --benchmark eval/kyc-benchmark.json --pack export/kyc/pack.json --adapter llm --model gpt-4o-mini`

### Corroboration — third use case (Securities instruments & issuance)

Date: 2026-07-04 · Model: `gpt-4o-mini` · n = 54 securities questions · Verdict: **✅ Target fully met — +53.7 pt lift, 100% auditable.**

Third independent use case (54 questions on bonds, equity, funds, securitization, issuance and
identification, grounded in `export/securities/pack.json`), same method and domain-neutral prompt.

| Metric | Ungrounded | Grounded | Δ |
|---|---|---|---|
| **Accuracy** (correct ≥ 60% keyword coverage) | 40.7% | **94.4%** | **+53.7 pt** |
| **Auditable** (answer carries a valid FIBO IRI citation) | 0% | **100.0%** | +100.0 |
| Cite on-target (cites the grounding concept) | 0% | 94.4% | +94.4 |
| **Hallucinated citation** (cites an IRI not in the pack) | **85.2%** | **0.0%** | −85.2 |

This run **fully meets the bar** (≥15–20 pt lift **and** 100% auditability): every grounded answer
cited a real pack IRI, none fabricated. The accuracy lift is the largest of the three.

**Reproduce:** `EVAL_LLM_CMD='./.venv/bin/python eval/openai_cli.py' ./.venv/bin/python eval/harness.py --benchmark eval/securities-benchmark.json --pack export/securities/pack.json --adapter llm --model gpt-4o-mini`

### Corroboration — fourth use case (Regulatory reporting & compliance)

Date: 2026-07-04 · Model: `gpt-4o-mini` · n = 52 reg-reporting questions · Verdict: **✅ Holds on the most cross-domain use case (8 clusters).**

Fourth independent use case (52 questions on regulators, regulations, reports, disclosure
requirements, reporting mechanisms and filings, grounded in `export/regulatory-reporting/pack.json`).

| Metric | Ungrounded | Grounded | Δ |
|---|---|---|---|
| **Accuracy** (correct ≥ 60% keyword coverage) | 59.6% | **96.2%** | **+36.5 pt** |
| **Auditable** (answer carries a valid FIBO IRI citation) | 0% | **94.2%** | +94.2 |
| Cite on-target (cites the grounding concept) | 0% | 90.4% | +90.4 |
| **Hallucinated citation** (cites an IRI not in the pack) | **69.2%** | **0.0%** | −69.2 |

Ungrounded accuracy is the highest of the four (59.6%) — many reg concepts (*regulation*, *report*,
*credit rating agency*) are generic enough that a bare model half-knows them — yet grounding still
adds **+36.5 pt** and, decisively, takes auditability 0% → 94% and kills the 69% ungrounded IRI
hallucination. Even where the base model is strongest, grounding is what makes the answer *citable*.

### Value proof — five use cases, one conclusion (gpt-4o-mini)

| Use case | n | Accuracy (ungrounded → grounded) | Lift | Auditability | Ungrounded hallucination |
|---|---|---|---|---|---|
| Loan origination | 53 | 45.3% → 84.9% | **+39.6 pt** | 98.1% | 5.7% → 0% |
| KYC / beneficial ownership | 50 | 44.0% → 92.0% | **+48.0 pt** | 92.0% | 90.0% → 0% |
| Securities instruments & issuance | 54 | 40.7% → 94.4% | **+53.7 pt** | 100.0% | 85.2% → 0% |
| Regulatory reporting & compliance | 52 | 59.6% → 96.2% | **+36.5 pt** | 94.2% | 69.2% → 0% |
| Derivatives contracts & trading | 54 | 48.1% → 96.3% | **+48.1 pt** | 100.0% | 72.2% → 0% |
| **Aggregate** | **263** | **47.5% → 92.8%** | **+45.3 pt** | **97.0%** | 55.1% → 0% |

Across **263 questions in five independent financial domains**, grounding in the curated FIBO context
pack lifts accuracy **+36.5 to +53.7 points** (+45.3 aggregate), takes auditability from **0% to
92–100%** (97.0% aggregate), and drives grounded IRI hallucination to **0%** every time (from 5.7–90%
ungrounded). The effect is not a loan-domain artifact; it is the product thesis.

### Corroboration — stronger model (gpt-4o)

Date: 2026-07-04 · Model: `gpt-4o` · same three benchmarks (157 questions) · Verdict: **✅ The lift is model-robust — a stronger model does not close the gap.**

The obvious objection to any RAG result is "a better base model would just know this." It does not:
on gpt-4o, grounding still lifts accuracy **+40 to +48 pt** per domain and eliminates hallucination.

| Use case | n | Accuracy (ungrounded → grounded) | Lift | Auditability | Ungrounded hallucination |
|---|---|---|---|---|---|
| Loan origination | 53 | 35.8% → 83.0% | **+47.2 pt** | 94.3% | 17.0% → 0% |
| KYC / beneficial ownership | 50 | 52.0% → 92.0% | **+40.0 pt** | 92.0% | 42.0% → 0% |
| Securities instruments & issuance | 54 | 46.3% → 94.4% | **+48.1 pt** | 100.0% | 48.1% → 0% |
| **Aggregate** | **157** | **44.6% → 89.8%** | **+45.2 pt** | **95.5%** | **35.7% → 0%** |

gpt-4o's ungrounded accuracy is barely higher than gpt-4o-mini's (44.6% vs 43.3%) — the missing
knowledge is FIBO-specific structure and exact IRIs, which scale of parametric training does not
supply. gpt-4o hallucinates fewer fake IRIs unprompted than the mini (35.7% vs ~60% aggregate) but
still fabricates them a third of the time with no grounding; grounded, it is **0%** on both models.

**Two models, three domains, one conclusion:** the value is in the grounding, not the model. Grounding
lifts accuracy **~+45–47 pt aggregate**, takes auditability to **95–97%**, and eliminates grounded IRI
hallucination — on both gpt-4o-mini and gpt-4o. **Next (optional):** surface on the landing; add more
use cases.

**Reproduce:** `EVAL_LLM_CMD='./.venv/bin/python eval/openai_cli.py' ./.venv/bin/python eval/harness.py --benchmark eval/kyc-benchmark.json --pack export/kyc/pack.json --adapter llm --model gpt-4o`

---

## Phase 0.5 Spike Results — FIBO Restriction Extraction

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
