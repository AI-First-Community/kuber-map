# Show HN + Reddit — launch posts

> These communities reward technical substance and honesty over polish. Tone is plainer and more
> candid than the LinkedIn/X copy. Lead with what it is, show the method, and state the limits.

---

## Show HN

**Title:**
Show HN: Kuber Map – audit-ready FIBO grounding for financial AI agents

**URL:** https://ai-first-community.github.io/kuber-map/

**Text:**
Hi HN. Kuber Map is an open, curated map of FIBO (the Financial Industry Business Ontology, an EDM
Council standard) that doubles as grounding context for financial AI agents.

The problem I kept hitting: LLMs are fluent but not grounded on financial concepts. Ask about a
mortgage, a beneficial owner, or a regulatory report and you get confident, plausible, and subtly
wrong — which is fine for a demo and a liability for anything audited.

FIBO already defines these concepts precisely, but it's a formal OWL ontology built for modelers —
exhaustive and hard to use directly. Kuber Map reshapes it into three things it isn't out of the
box: a curated, learner-first "core" view; a cross-domain bridge layer; and per-use-case context
packs an agent can retrieve and cite.

I wanted to know whether grounding actually helps or just feels rigorous, so I measured it. Same
model, same questions, with the FIBO context pack vs. without, scored deterministically (string/IRI
checks — no LLM judging itself):

- Accuracy: 47.5% → 92.8% (+45.3pt)
- Answers citing a real FIBO IRI: 0% → 97%
- Hallucinated citations: 55% → 0%

Across 263 questions over 5 use cases (loan origination, KYC, securities, regulatory reporting,
derivatives) on gpt-4o-mini, then corroborated on gpt-4o (the same three of those benchmarks, 157
questions). The lift held on the stronger model — grounding, not scale, is doing the work.

How it's built:
- Deterministic ETL: FIBO OWL/RDF → an intermediate JSON → Open Knowledge Format bundle. Relations
  come from walking owl:Restriction blank nodes; the build reproduces byte-for-byte from a pinned
  FIBO commit.
- Every concept keeps its FIBO IRI as a citation; every edge/definition is tagged `fibo`
  (extracted) or `curated` (added by a human, with a rationale). That split is enforced in CI.
- Output: `pack.json` (RAG records), `context.md` (prompt injection), a self-contained OKF slice,
  and a stdlib MCP retrieval server.
- The map is a Cytoscape graph (desktop) + a separate mobile PWA, both over one generated data
  file. No backend; it's a static site on GitHub Pages.

Honest limits: the curated core is 284 concepts across 5 use cases (the full extract is ~3,100);
the benchmark is mine and modest in size; the cross-domain bridges are a proposal, not yet blessed
by the EDM Council; and it's static — no live FIBO sync yet.

MIT-licensed. Contributions (especially new use cases — they're spec-driven JSON, no code) are very
welcome.

Code: https://github.com/AI-First-Community/kuber-map
Happy to answer anything about the extraction, the eval, or the provenance model.

---

## Reddit — r/fintech

**Title:** I built an open, audit-ready FIBO knowledge map to ground financial AI agents (MIT, measured +45pt accuracy)

**Body:**
FinTech teams keep telling me the same thing: the AI pilot demos great and then can't go near a
regulated decision because you can't explain where an answer came from.

Kuber Map is my attempt at the missing piece — grounding. It's a curated map of FIBO (the industry's
standard ontology) packaged as context an agent can cite. Every answer traces back to a real FIBO
IRI, and "standard vs. our curation" provenance is never blurred, so it's auditable.

I measured grounded vs. ungrounded on the same model/questions: accuracy 47.5% → 92.8%, auditable
answers 0% → 97%, hallucinated citations 55% → 0% (263 questions, 5 use cases on gpt-4o-mini,
deterministic scoring; corroborated on gpt-4o). The lift held on the stronger model, so it's
grounding doing the work, not scale.

It's free and open — runs in the browser, installs as an app, MIT-licensed. Live app and repo:
- https://ai-first-community.github.io/kuber-map/
- https://github.com/AI-First-Community/kuber-map

Would genuinely value feedback from people doing KYC, lending, or reg-reporting AI. What use case
should it cover next?

---

## Reddit — r/MachineLearning

**Title:** [P] Kuber Map: grounding financial LLM agents in FIBO — +45pt accuracy, 0% hallucinated citations, measured

**Body:**
Sharing a project on domain grounding. Thesis: for finance, a shared formal ontology (FIBO) as
retrieval context beats reaching for a bigger model.

Setup: curated per-use-case slices of FIBO exported as context packs (RAG records + prompt-injection
doc + an MCP retrieval server). Concepts carry their IRI; provenance (extracted vs. curated) is
tracked and CI-enforced.

Eval: grounded vs. ungrounded, same model and questions, deterministic scoring (no LLM-as-judge).
263 questions across 5 use cases on gpt-4o-mini (corroborated on gpt-4o, 157 questions in 3 domains):
- accuracy 47.5% → 92.8% (+45.3pt)
- answers citing a valid IRI 0% → 97%
- hallucinated citations 55% → 0%

The gap didn't close on the stronger model, which is the interesting part — the win is from
grounding, not capability.

Build is a deterministic OWL→OKF pipeline (relations from owl:Restriction blank nodes,
byte-reproducible from a pinned commit). MIT, no backend. Code + harness:
https://github.com/AI-First-Community/kuber-map

Critiques of the benchmark design welcome — it's intentionally simple and I'd like to harden it.
