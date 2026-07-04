#!/usr/bin/env python3
"""
Model adapters for the eval harness. An adapter is a callable: question -> answer text.

Two families:
  offline    deterministic, no network/key. `grounded` retrieves from the pack and answers
             with definitions + valid citations (the mechanism's upper bound); `ungrounded`
             is a no-grounding stub. Use for gate tests and demonstrating the harness.
  anthropic  a live Claude agent (needs ANTHROPIC_API_KEY + the anthropic SDK). `grounded`
             injects pack-retrieved concepts and asks it to cite FIBO IRIs; `ungrounded`
             asks the bare question. This produces the REAL value-proof numbers.

`build(name, pack, model)` returns (grounded_fn, ungrounded_fn), or (None, None) if that
adapter can't run in this environment.
"""
import os

RETRIEVE_K = 4

SYSTEM = ("You are a financial loan-underwriting assistant. Answer concisely. When the "
          "provided FIBO grounding context is relevant, cite the exact `resource` IRI(s) "
          "you relied on. Do not invent IRIs.")


def _grounding_block(pack, question):
    hits = pack.search(question, k=RETRIEVE_K)
    lines = []
    for h in hits:
        lines.append(f"- {h['title']}: {h['definition']}\n  cite: {h['citation']}")
    return "\n".join(lines), hits


# ---- offline ------------------------------------------------------------------------------

def _offline_grounded(pack):
    def answer(q):
        block, hits = _grounding_block(pack, q["question"])
        # An ideally-grounded agent restates the retrieved definitions and cites their IRIs.
        defs = " ".join(h["definition"] or "" for h in hits)
        cites = " ".join(h["citation"] for h in hits)
        return f"{defs}\nSources: {cites}"
    return answer


def _offline_ungrounded(_pack):
    def answer(_q):
        # No grounding, no citation — the floor the grounded run is measured against.
        return "Based on general knowledge, but without a specific authoritative source."
    return answer


# ---- anthropic (live) ---------------------------------------------------------------------

def _anthropic_client():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return None
    try:
        import anthropic
    except ImportError:
        return None
    return anthropic.Anthropic()


def _ask_claude(client, model, system, prompt):
    msg = client.messages.create(model=model, max_tokens=1024, system=system,
                                 messages=[{"role": "user", "content": prompt}])
    return "".join(b.text for b in msg.content if getattr(b, "type", None) == "text")


def _anthropic_grounded(pack, model, client):
    def answer(q):
        block, _ = _grounding_block(pack, q["question"])
        prompt = f"FIBO grounding context:\n{block}\n\nQuestion: {q['question']}"
        return _ask_claude(client, model, SYSTEM, prompt)
    return answer


def _anthropic_ungrounded(model, client):
    def answer(q):
        return _ask_claude(client, model, SYSTEM, f"Question: {q['question']}")
    return answer


def build(name, pack, model):
    if name == "offline":
        return _offline_grounded(pack), _offline_ungrounded(pack)
    if name == "anthropic":
        client = _anthropic_client()
        if client is None:
            return None, None
        return _anthropic_grounded(pack, model, client), _anthropic_ungrounded(model, client)
    return None, None
