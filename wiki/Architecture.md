# Architecture

Two toolchains, one bundle in the middle. FIBO's OWL/RDF is turned into a clean OKF knowledge
bundle, which then feeds three consumers: the interactive map (for people), the context packs (for
AI agents), and the bridge contribution (for the EDM Council).

## System overview

```mermaid
flowchart TB
  subgraph SRC["Sources (pinned, MIT)"]
    FIBO["FIBO OWL/RDF<br/>10 domains"]
    CMNS["OMG Commons<br/>upper ontology"]
  end

  subgraph PY["Python ETL"]
    EX["extract.py<br/>walks owl:Restriction axioms"]
    IM[("intermediate.json")]
    TO["to_okf.py<br/>applies curation overlays"]
  end

  subgraph CUR["Curation (hand-authored, grounded)"]
    NC["nominate_core.py<br/>use-case core sets"]
    BR["bridges.py<br/>cross-domain bridges"]
    OV["examples / definitions / notes"]
  end

  BUNDLE[("knowledge/ OKF bundle<br/>3,104 concepts, 19 bridges")]

  subgraph OUT["Consumers"]
    JS["scripts/okf.js"] --> DATA[("js/data.js")] --> MAP{{"Interactive map<br/>(people)"}}
    EP["export_pack.py"] --> PACK[("export/ context packs")] --> AGENT(("AI agent"))
    EB["export_bridges.py"] --> CONTRIB[("contrib/<br/>EDM proposal")]
  end

  FIBO --> EX
  CMNS --> EX
  EX --> IM --> TO --> BUNDLE
  NC --> TO
  OV --> TO
  BR --> BUNDLE
  BUNDLE --> JS
  BUNDLE --> EP
  BUNDLE --> EB
```

Everything left of the bundle is **generated**; only the `curation/` overlays and
`knowledge/bridges/` are hand-authored. Extraction is deterministic, so the bundle reproduces
byte-for-byte.

## 1. Extract (`etl/extract.py`)

FIBO ships as OWL/RDF where the interesting relationships hide inside `owl:Restriction` blank-node
axioms on `rdfs:subClassOf`, not as flat triples. `extract.py` walks those into a flat
`out/intermediate.json`. `fibo_ns.py` classifies every IRI into a cluster (FIBO domain / `CMNS` /
`LCC`) and maps it to a stable path.

## 2. Build the OKF bundle (`etl/to_okf.py`)

One markdown file per concept, with YAML frontmatter:

```yaml
type: FIBO Class
title: "bond"
description: "tradable debt instrument representing a loan..."   # from FIBO skos:definition
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond   # the audit citation
tags: [SEC, Release]
core: true
use_cases: ["Securities Instruments & Issuance (capital markets)"]
relations:
  - {type: is-a, target: "/FBC/.../DebtInstrument", provenance: fibo}
  - {type: backed-by, target: "/LOAN/.../Mortgage", provenance: curated}   # a bridge
```

## 3. Curation and use cases

A use case is spec-driven. Dropping a spec under `curation/usecases/` adds one, no code change:

```mermaid
flowchart LR
  SPEC["usecases/&lt;uc&gt;.json<br/>facet spec"] --> NC["nominate_core.py<br/>resolve + gate"]
  NC -->|"every id must be a<br/>real FIBO class"| CORE[("curation/&lt;uc&gt;.json<br/>core set")]

  BSPEC["usecases/&lt;uc&gt;-bridges.json"] --> BR["bridges.py"]
  BR -->|"endpoints real AND<br/>FIBO doesn't already draw it"| BFILES[("knowledge/bridges/")]

  EXJSON["&lt;uc&gt;-examples.json<br/>&lt;uc&gt;-definitions.json"] --> TO2["to_okf.py"]
  CORE --> TO2
  TO2 --> BUNDLE2[("knowledge/ bundle")]
  BFILES --> BUNDLE2
  BUNDLE2 --> PACK2["export_pack.py<br/>-&gt; export/&lt;uc&gt;/"]
```

Five use cases are curated this way (loan origination, KYC, securities, regulatory reporting,
derivatives): **284 core concepts, 19 validated cross-domain bridges**. The `nominate_core` and
`bridges` steps are **anti-hallucination gates**: they exit non-zero if any id or bridge endpoint
isn't a real FIBO class, so a use case can never reference a concept that doesn't exist.

## 4. The map (`scripts/okf.js` + `okf.config.js` + `js/`)

`okf.config.js` holds everything that isn't a concept: the domains (split into module sub-clusters),
maturity levels, relation styling (curated bridges drawn distinctly), and the interactive flows.
`scripts/okf.js build` emits `js/data.js`. `js/graph.js` (forked from Bodhi) renders it with
Cytoscape + fcose; the CSS is byte-identical to Bodhi. The default view lays out only the visible
core, so load stays fast even on the full 3,104-node ontology, and a use-case lens focuses one use
case at a time.

## 5. Agent grounding at runtime

This is the product: an agent answers a financial question grounded in the pack, and every answer
carries a checkable FIBO citation.

```mermaid
sequenceDiagram
  participant U as User / task
  participant A as AI agent
  participant R as Retrieval (pack.json)
  participant M as LLM
  U->>A: financial question
  A->>R: search the use-case context pack
  R-->>A: top concepts + FIBO IRIs + provenance
  A->>M: question + grounding context
  M-->>A: answer + "Sources: <FIBO IRIs>"
  A-->>U: grounded, citable answer
  Note over R,M: every concept carries its FIBO IRI,<br/>so the answer is traceable to the standard
```

`etl/export_pack.py` emits each use case's grounding closure as `pack.json` (RAG records),
`context.md` (prompt injection), and an OKF slice. `etl/retrieval.py` + `etl/mcp_server.py` expose
it as an MCP retrieval endpoint.

## 6. The eval (`eval/`) — grounded vs ungrounded

The value proof runs the same agent twice and scores the difference deterministically (no LLM
judge):

```mermaid
flowchart LR
  Q["benchmark question<br/>(grounded in a real pack IRI)"]
  Q --> G["grounded run<br/>(pack injected)"]
  Q --> N["ungrounded run<br/>(bare question)"]
  G --> S["deterministic scorer"]
  N --> S
  S --> R["accuracy · auditability · hallucination"]
```

Result across **209 questions in four domains, on gpt-4o-mini (corroborated on gpt-4o)**: a
**+44.5-point aggregate accuracy lift, 96.2% auditable, 0% grounded hallucination**. See
**[Value Proof](Value-Proof)**.

## Provenance model

Provenance is never blurred. Every relation and every overlaid field is tagged `fibo` (from FIBO)
or `curated` (authored here). Overlays only fill gaps; they never overwrite real FIBO text. This is
what makes an answer auditable and what keeps the EDM Council contribution honest.

The fuller repo-side version is in
[docs/Architecture.md](https://github.com/AI-First-Community/Bodhi-Map-For-FinTech/blob/main/docs/Architecture.md).
