# Vision and Philosophy: Why Kuber Map

> The knowledge base and taxonomy for applying AI and agentic AI in finance, the right way.

This document is the "why". For how it is built, see [Architecture](Architecture.md); for what it
proves, see [`SPIKE_RESULTS.md`](../SPIKE_RESULTS.md).

## The challenge: every FinTech wants AI, few can trust it in production

Walk into any bank, insurer, asset manager, or FinTech today and you will find the same picture:
dozens of AI pilots, real enthusiasm, and very little in production where it matters. The models
are impressive in the demo and unusable in the audit. The gap between "we tried GenAI" and "we
deployed it into a regulated workflow" is where most financial AI strategies quietly stall.

The reason is not a lack of talent or budget. It is that a large language model is **fluent but not
grounded**. It has read the internet, so it can talk about a mortgage, a beneficial owner, or a
credit default swap convincingly. But it *knows* finance only approximately, as a statistical echo
of text it has seen. In consumer chat, approximately right is good enough. In finance,
approximately right is wrong. A model that defines "beneficial owner" loosely, or blurs
"de facto control" and "de jure control", or invents a regulation, has not made a typo. It has
created a compliance and reputational liability.

That surfaces as three failures that block production:

1. **Hallucination.** The model fabricates facts, definitions, and even official-looking
   citations. Ask an ungrounded model a precise question and it will confidently cite a regulation
   or an identifier that does not exist. In our own measurements, an ungrounded model fabricated a
   FIBO-looking identifier in the majority of answers.
2. **Inconsistency.** The same concept gets a slightly different meaning each time, so two agents,
   or the same agent twice, disagree about what a "customer" or a "controlling party" is. There is
   no shared source of truth, so there is no reproducibility.
3. **No auditability.** Even when the answer is correct, the model cannot show *why*. It cannot
   point to the authoritative definition it relied on. In a regulated industry, an answer you
   cannot trace is an answer you cannot use.

## Why the usual AI strategy does not fix it

Most AI strategies respond to this by reaching for more of the engine: a bigger model, a better
prompt, another agent framework, a larger vector database of documents. Those help at the margin,
but they optimise the engine while ignoring the map. They assume the problem is capability. The
problem is **shared, precise, auditable meaning.**

Two assumptions quietly break here:

- **"A better model will know this."** It will not. We ran the same experiment on a small model and
  a much stronger one. The stronger model's *ungrounded* accuracy barely moved. The missing
  knowledge is not general intelligence; it is the specific structure of financial concepts and the
  exact identifiers that make an answer traceable. Scale of training does not supply that. Grounding
  does.
- **"We have the data."** Firms have data lakes, warehouses, and documents. But data is not
  knowledge. A row in a table does not say what a "loan-to-value ratio" *means*, which regulation
  governs it, or how it relates to collateral, borrower, and disclosure. Agents reason on meaning
  and relationships, not on rows. The semantic layer, the part that says what things are and how
  they connect, is the piece that is usually missing.

The right way to adopt AI in finance is **foundation first, then agents.** Give the AI the language
of the business, made precise and traceable, and the agents built on top become accurate,
consistent, and auditable almost as a side effect. Skip the foundation, and every agent you build
inherits the same three failures.

## The missing foundation already exists, but no one can use it

The industry does not need a new ontology of finance. It already agreed on one. The **Financial
Industry Business Ontology (FIBO)**, stewarded by the EDM Council and the Object Management Group,
is a formal, standards-grade definition of financial concepts and how they relate: instruments,
entities, parties, contracts, regulations, and more. It is the closest thing finance has to a
shared source of truth for meaning, and it is open (MIT licensed).

And yet almost no team uses FIBO directly, for good reasons:

- It is **built for ontologists, not for teams or agents.** It is exhaustive and dense, with
  thousands of classes and relationships expressed in OWL/RDF. There is no learner's path into it,
  no "start here".
- Its meaning is **hard to extract.** The interesting relationships hide inside `owl:Restriction`
  blank-node axioms, not in simple statements. You cannot just read it.
- It is **governed in separate domains** that real work has to cross. A mortgage-backed security is
  backed by mortgage loans, but securities and loans live in different, separately maintained parts
  of the ontology, and the edge between them is often not drawn.
- It is **not packaged for an AI agent.** There is no ready grounding context, no per-task slice, no
  provenance trail an agent can cite.

So the standard exists, but it sits on a shelf. The knowledge is there; the usability is not.

## The idea: make the standard usable, teachable, and agent-ready

Kuber Map does not compete with FIBO. It makes FIBO **usable**, in two directions at once:

- **For people**, as a curated, learner-first *map*: a hand-picked "core" view with plain-language
  framing, worked examples, and the relationships drawn out, so a human can actually learn the
  domain instead of drowning in it.
- **For AI agents**, as **audit-ready grounding context**: per-use-case packs an agent retrieves
  and reasons on, where every concept carries its FIBO identifier as a citation, and every fact is
  tagged with its origin.

The name says the intent. Kubera is the treasurer of the gods, the keeper of wealth. Kuber Map is
meant to be the treasury of financial knowledge: not more data, but organised, navigable, trusted
meaning. The map metaphor is borrowed in spirit from the Bodhi Map approach, that knowledge is best
understood as a landscape you can navigate, not a document you scroll.

### How it works, in three layers

The layers are ordered by value, and that ordering drives every decision in the project.

1. **Agent grounding (the product).** Each real financial task, originating a loan, resolving a
   beneficial owner, filing a regulatory report, trading a derivative, becomes a *use case*: a
   curated slice of the ontology with the concepts, examples, and cross-domain links that task
   actually needs, exported as a context pack an agent grounds on. Every concept carries its FIBO
   identifier, so every agent claim is traceable to the standard.

2. **Cross-domain bridges (the moat).** Where FIBO models two concepts in separate domains but does
   not connect them, and a real task needs that connection, Kuber Map curates the missing edge, with
   a rationale and a regulatory or standards citation, validated so it never duplicates or
   contradicts FIBO. These bridges are the hard, high-value part, and they are contributed back to
   the EDM Council so the whole community benefits.

3. **The map (the surface).** The interactive map is where the curation is done, demonstrated, and
   taught. It is the human-facing window onto the same grounded knowledge the agents use.

Throughout, **provenance is never blurred.** Every relationship and every field is marked as coming
from FIBO or as curated here. An auditor can always separate the standard from our additions. This
is not decoration; it is the whole point. Trust comes from traceability.

## The value: measured, not asserted

The claim that grounding matters is easy to make and easy to doubt. So we measured it. We ran the
same agent over the same questions, once **with** the curated FIBO grounding pack and once
**without**, and scored accuracy, auditability, and hallucination deterministically.

Across **209 questions in four independent financial domains, on two different models**, grounding:

- **lifted accuracy by roughly 45 points** (from the mid-40s to the low-90s),
- **took auditability from 0% to over 95%** (nearly every grounded answer cites a real, checkable
  FIBO identifier), and
- **eliminated grounded hallucination entirely (to 0%)**, from as high as 90% without grounding.

Crucially, the lift held on a much stronger model too, which is the proof that the value is in the
grounding, not the model. (Full numbers in [`SPIKE_RESULTS.md`](../SPIKE_RESULTS.md).)

Translated into business terms, grounding is what turns an AI pilot into something a regulated
institution can actually deploy:

- **Accuracy** you can rely on, because the agent reasons on agreed definitions, not guesses.
- **Consistency** across teams and agents, because they share one source of truth.
- **Auditability** by construction, because every answer carries its citation, so compliance and
  risk are built in rather than bolted on.
- **Compounding leverage**, because the semantic layer is reused across every use case. The second
  agent is cheaper and safer to build than the first, and the tenth cheaper than the second.

## What this means for an AI strategy

The lesson for any financial institution's AI strategy is simple, and it is the reason this project
exists: **do not start with the model. Start with the meaning.** The differentiator in financial AI
is not who has the biggest model, everyone rents the same ones. It is who has grounded those models
in a shared, precise, auditable understanding of their business.

Kuber Map is a working demonstration of that thesis, built on the open industry standard, proven
with numbers, and given back to the community. It shows that the path from AI experiment to AI in
production runs through grounding, and that the foundation for grounding in finance already exists.
It just needed to be made usable.

## Why open, why community

This is MIT-licensed and public on purpose. It is built on an open standard (FIBO), it contributes
its cross-domain bridges back to the standard's stewards, and it asks nothing to run: no vendor
lock-in, no paid tier, no dependency you cannot replace. A shared semantic foundation for financial
AI should belong to the community that depends on it. That is the point of a treasury: it is held in
common, and everyone is richer for it.
