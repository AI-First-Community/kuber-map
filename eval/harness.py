#!/usr/bin/env python3
"""
Grounded-vs-ungrounded evaluation harness (PLAN.md §10, Phase 1 value proof).

Runs a loan-underwriting agent over a financial-semantics benchmark, WITH the curated
FIBO context pack (grounded) and WITHOUT it (ungrounded), and scores three things the
product claims to move:

  accuracy        keyword coverage of the gold answer (correct if >= THRESHOLD)
  hallucination   answer cites a FIBO-looking IRI that is NOT a real concept in the pack
  auditability    answer carries at least one VALID FIBO IRI citation (target: 100% grounded)

Scoring is deterministic (no LLM judge): accuracy is gold-keyword coverage; citations are
matched against the pack's real IRIs. The model itself is pluggable (see eval/adapters.py):
an offline oracle/stub for gate tests, or a live LLM run via a user command (EVAL_LLM_CMD).

Usage:
    python eval/harness.py --benchmark eval/benchmark.json --pack export/loan-origination/pack.json
    EVAL_LLM_CMD='my-model-cli' python eval/harness.py --adapter llm   # live value proof
"""
import argparse
import json
import re
import sys

sys.path.insert(0, "etl")
from retrieval import Pack, tokens  # noqa: E402

CORRECT_THRESHOLD = 0.6
IRI_RE = re.compile(r"https://spec\.edmcouncil\.org/fibo/ontology/[^\s,);\"']+")


def extract_citations(text):
    return [m.rstrip(".") for m in IRI_RE.findall(text or "")]


def keyword_coverage(answer, expected_keywords):
    """Fraction of gold keywords present in the answer (a keyword matches if all of its
    tokens appear). Deterministic proxy for factual accuracy."""
    if not expected_keywords:
        return 0.0
    toks = set(tokens(answer))
    hit = sum(1 for kw in expected_keywords if set(tokens(kw)) <= toks)
    return hit / len(expected_keywords)


def score_answer(answer, question, pack_iris):
    coverage = keyword_coverage(answer, question.get("expected_keywords", []))
    cites = extract_citations(answer)
    valid = [c for c in cites if c in pack_iris]
    invalid = [c for c in cites if c not in pack_iris]
    grounds = set(question.get("grounds", []))
    return {
        "id": question["id"],
        "coverage": coverage,
        "correct": coverage >= CORRECT_THRESHOLD,
        "auditable": len(valid) > 0,
        "hallucinated_citation": len(invalid) > 0,
        "cited_on_target": bool(grounds & set(valid)),
    }


def run(benchmark, adapter, pack):
    pack_iris = {c["iri"] for c in pack.concepts}
    rows = []
    for q in benchmark:
        answer = adapter(q)
        rows.append(score_answer(answer, q, pack_iris))
    return rows


def aggregate(rows):
    n = len(rows) or 1
    return {
        "n": len(rows),
        "accuracy": sum(r["correct"] for r in rows) / n,
        "mean_coverage": sum(r["coverage"] for r in rows) / n,
        "auditable": sum(r["auditable"] for r in rows) / n,
        "hallucination": sum(r["hallucinated_citation"] for r in rows) / n,
        "cited_on_target": sum(r["cited_on_target"] for r in rows) / n,
    }


def print_scorecard(grounded, ungrounded):
    g, u = aggregate(grounded), aggregate(ungrounded)
    pct = lambda x: f"{100 * x:5.1f}%"  # noqa: E731
    print("\n================ GROUNDED vs UNGROUNDED ================")
    print(f"{'metric':<20}{'ungrounded':>12}{'grounded':>12}{'delta':>10}")
    for key, label in [("accuracy", "accuracy"), ("auditable", "auditable (cite)"),
                       ("hallucination", "hallucination"), ("cited_on_target", "cite on-target")]:
        d = g[key] - u[key]
        print(f"{label:<20}{pct(u[key]):>12}{pct(g[key]):>12}{100 * d:>+9.1f}")
    lift = 100 * (g["accuracy"] - u["accuracy"])
    print("-------------------------------------------------------")
    print(f"accuracy lift: {lift:+.1f} pt   |   grounded auditability: {pct(g['auditable'])}")
    print(f"target: >= 15-20pt lift + 100% auditable  ->  "
          f"{'MET' if lift >= 15 and g['auditable'] >= 0.999 else 'not yet met'}")
    print(f"(n={g['n']} questions)")
    print("=======================================================\n")
    return {"grounded": g, "ungrounded": u, "accuracy_lift_pt": lift}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--benchmark", default="eval/benchmark.json")
    ap.add_argument("--pack", default="export/loan-origination/pack.json")
    ap.add_argument("--adapter", choices=["offline", "llm"], default="offline")
    ap.add_argument("--model", default="", help="model id, exported as EVAL_LLM_MODEL to the command")
    ap.add_argument("--out", default=None, help="write the scorecard JSON here")
    args = ap.parse_args()

    pack = Pack.load(args.pack)
    benchmark = json.load(open(args.benchmark))["questions"]

    import adapters
    grounded_fn, ungrounded_fn = adapters.build(args.adapter, pack, args.model)
    if grounded_fn is None:
        print(f"adapter '{args.adapter}' unavailable (missing key or SDK); nothing to run.")
        return 1

    grounded = run(benchmark, grounded_fn, pack)
    ungrounded = run(benchmark, ungrounded_fn, pack)
    card = print_scorecard(grounded, ungrounded)
    card["adapter"], card["model"] = args.adapter, args.model
    if args.adapter == "offline":
        print("NOTE: offline adapter = MECHANISM CHECK ONLY. The grounded oracle restates\n"
              "retrieved definitions and the ungrounded stub is a deliberate floor, so these\n"
              "numbers are NOT the product's value proof. Run --adapter llm (EVAL_LLM_CMD set)\n"
              "for real grounded-vs-ungrounded numbers.\n")
        card["note"] = "offline mechanism check — not the real value proof"
    if args.out:
        json.dump(card, open(args.out, "w"), indent=2)
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
