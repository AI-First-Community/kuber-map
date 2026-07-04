#!/usr/bin/env python3
"""
Model adapters for the eval harness. An adapter is a callable: question -> answer text.

Two families:
  offline    deterministic, no network/command. `grounded` retrieves from the pack and answers
             with definitions + valid citations (the mechanism's upper bound); `ungrounded` is
             a no-grounding stub. Use for gate tests and demonstrating the harness.
  llm        a live model, invoked provider-agnostically via a user command (EVAL_LLM_CMD):
             the harness pipes a prompt on stdin and reads the answer on stdout, so any model
             CLI works and no vendor SDK is a dependency. `grounded` injects pack-retrieved
             concepts and asks the model to cite FIBO IRIs; `ungrounded` asks the bare question.
             This produces the REAL value-proof numbers.

`build(name, pack, model)` returns (grounded_fn, ungrounded_fn), or (None, None) if that
adapter can't run in this environment.
"""
import os
import subprocess

RETRIEVE_K = 4

SYSTEM = ("You are a financial loan-underwriting assistant. Answer concisely. When the "
          "provided FIBO grounding context is relevant, cite the exact resource IRI(s) you "
          "relied on. Do not invent IRIs.")

# Grounded runs only: force an explicit, verbatim citation line so every answer is auditable.
GROUNDED_INSTRUCTION = (
    "Base your answer on the FIBO grounding context above. Then, on a final separate line, write "
    "exactly 'Sources:' followed by the `cite:` IRI(s) from the context that support your answer, "
    "copied verbatim and space-separated. Always include the Sources line, and cite only IRIs that "
    "appear in the context above.")


def _grounding_block(pack, question):
    hits = pack.search(question, k=RETRIEVE_K)
    return "\n".join(f"- {h['title']}: {h['definition']}\n  cite: {h['citation']}" for h in hits), hits


# ---- offline ------------------------------------------------------------------------------

def _offline_grounded(pack):
    def answer(q):
        _, hits = _grounding_block(pack, q["question"])
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


# ---- llm (live, provider-agnostic via EVAL_LLM_CMD) ---------------------------------------

def _run_cmd(cmd, model, prompt):
    """Pipe `prompt` to the user's model command on stdin; return its stdout answer.
    EVAL_LLM_MODEL is exported so the command can select the model if it wants."""
    env = dict(os.environ, EVAL_LLM_MODEL=model or "")
    r = subprocess.run(cmd, shell=True, input=prompt, capture_output=True, text=True, env=env)
    return r.stdout.strip()


def _llm_grounded(pack, model, cmd):
    def answer(q):
        block, _ = _grounding_block(pack, q["question"])
        prompt = (f"{SYSTEM}\n\nFIBO grounding context:\n{block}\n\nQuestion: {q['question']}"
                  f"\n\n{GROUNDED_INSTRUCTION}")
        return _run_cmd(cmd, model, prompt)
    return answer


def _llm_ungrounded(model, cmd):
    def answer(q):
        return _run_cmd(cmd, model, f"{SYSTEM}\n\nQuestion: {q['question']}")
    return answer


def build(name, pack, model):
    if name == "offline":
        return _offline_grounded(pack), _offline_ungrounded(pack)
    if name == "llm":
        cmd = os.environ.get("EVAL_LLM_CMD")
        if not cmd:
            return None, None
        return _llm_grounded(pack, model, cmd), _llm_ungrounded(model, cmd)
    return None, None
