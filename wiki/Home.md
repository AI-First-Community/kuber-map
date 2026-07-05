# Kuber Map for FIBO

**A curated, learner-first knowledge map of the Financial Industry Business Ontology (FIBO),
stored in Google's Open Knowledge Format (OKF), that doubles as audit-ready grounding context
for financial AI agents.**

<p align="center">
  <a href="https://ai-first-community.github.io/kuber-map/"><img src="images/demo-explore.gif" alt="Exploring a FIBO concept in Kuber Map — definition, provenance, FIBO citation, and connections" width="820"></a>
</p>

> **▶ Open the live app: <https://ai-first-community.github.io/kuber-map/>** — runs in the browser, installs as a PWA. See more demos in the [README](https://github.com/AI-First-Community/kuber-map#readme).

FIBO is a formal, exhaustive ontology built for modelers. Kuber Map reshapes it into three things
it isn't today:

1. **A teachable map** — a hand-picked "core" view with learner-friendly framing.
2. **A cross-domain bridge layer** — provenance-tagged links across FIBO's separately-governed
   domains, offered back to the EDM Council.
3. **Agent grounding** — per-use-case context packs that give financial AI agents accurate
   semantics with a FIBO provenance trail for audit.

**New here? Start with [Vision & Philosophy](Vision)** — the challenge FinTech faces adopting AI,
why grounding (not a bigger model) is the answer, and how this concept works.

## Two products in one repo

- **The map** (`index.html` landing + `app.html` graph): an interactive Cytoscape view of the
  curated ontology, with a use-case lens, forked from [Bodhi Map](https://github.com/AI-First-Community/Bodhi).
- **The context pack** (`export/`): a use case's grounding closure as `pack.json` (RAG),
  `context.md` (prompt injection), a self-contained OKF slice, and an MCP retrieval server an
  agent can call. Every concept carries its FIBO IRI as an audit citation.

## Status at a glance

| | |
|---|---|
| FIBO coverage | all **10 domains** + Commons — **3,104 concepts**, 6,676 typed relations, 68 sub-clusters |
| Curated use cases | **5** — loan origination, KYC, securities, regulatory reporting, derivatives (**284 core concepts**) |
| Cross-domain bridges | **19** validated, packaged as an EDM contribution proposal |
| Value proof | grounding lifts accuracy **+45.3pt** (263 questions, 5 use cases, gpt-4o-mini; held on gpt-4o), **97.0% auditable**, **0% grounded hallucination** |

See **[Use Cases](Use-Cases)**, **[Value Proof](Value-Proof)**, and **[Cross-Domain Bridges](Cross-Domain-Bridges)**.

## The golden rule

Every FIBO claim is grounded in the pinned FIBO source — never invented. Provenance is never
blurred: every relation and field is tagged `fibo` (from FIBO) or `curated` (authored here).
Start with **[Getting Started](Getting-Started)** to build it yourself.
