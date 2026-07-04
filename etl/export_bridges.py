#!/usr/bin/env python3
"""
Package the curated CROSS-DOMAIN BRIDGES as an EDM Council contribution-back.

Reads the validated bridge records (curation/*bridges.json — each already gated by
etl/bridges.py: both endpoints are real FIBO classes and FIBO does not already assert
the edge) and emits, into contrib/:

  edmc-bridge-contribution.md   human-readable proposal (methodology + per-use-case tables)
  fibo-bridges.ttl              RDF/Turtle: each bridge as a proposed triple in the
                                kmb: namespace + an owl:Axiom annotation carrying the
                                rationale, citation and provenance.

We do NOT assert FIBO/OMG object properties we haven't verified (Golden Rule 1 — never
invent). Proposed relations live in our own `kmb:` namespace and are clearly marked as
curated proposals; reviewers can map each edge to (or mint) the right FIBO property.

Usage:  python etl/export_bridges.py            # -> contrib/
"""
import glob
import json
import os
import re

F = "https://spec.edmcouncil.org/fibo/ontology/"
KMB = "https://ai-first-community.github.io/kuber-map/bridges/"

# curation file -> use-case label (for grouping in the proposal)
USE_CASE = {
    "bridges.json": "Loan origination & underwriting",
    "kyc-bridges.json": "KYC & beneficial ownership",
    "securities-bridges.json": "Securities instruments & issuance",
    "regulatory-reporting-bridges.json": "Regulatory reporting & compliance",
}


def camel(edge):
    parts = edge.split("-")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


def humanize_iri(iri):
    tail = iri.rstrip("/").split("/")[-1]
    tail = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", tail).replace("-", " ")
    return tail


def ttl_lit(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


def load_labels():
    labels = {}
    try:
        for r in json.load(open("out/intermediate.json")):
            labels[r["iri"]] = r["title"]
    except (OSError, json.JSONDecodeError):
        pass
    return labels


def load_bridges():
    out = []
    for path in sorted(glob.glob("curation/*bridges.json")):
        name = os.path.basename(path)
        uc = USE_CASE.get(name, name)
        data = json.load(open(path))
        for b in data.get("bridges", []):
            out.append({**b, "use_case": uc})
    return out


def label(labels, iri):
    return labels.get(iri) or humanize_iri(iri)


def emit_md(bridges, labels):
    edges = sorted({b["edge"] for b in bridges})
    lines = [
        "# Cross-domain bridges — FIBO contribution proposal",
        "",
        f"**{len(bridges)} curated cross-domain relations** that FIBO does not currently draw, "
        "surfaced while building learner-first, agent-grounding maps of FIBO for four financial "
        "use cases. Each is offered back to the EDM Council for consideration.",
        "",
        "*Author:* Sanjeev Azad <sanjeev.azad@gmail.com> · *License:* MIT · "
        "*Source project:* Kuber Map for FIBO.",
        "",
        "## How these were derived (and why they are safe to review)",
        "",
        "Every bridge passed an automated grounding gate (`etl/bridges.py`) before inclusion:",
        "",
        "1. **Both endpoints are real FIBO classes** — resolved against an extract of the pinned "
        "FIBO source (see `fibo-source.pin`); no invented IRIs.",
        "2. **FIBO does not already assert the edge** — the resolver rejects any relation FIBO "
        "already draws (source → target), so nothing here duplicates existing FIBO.",
        "3. **Each carries a rationale + an external citation** (regulation or standard), so a "
        "reviewer can trace the real-world basis of the proposed link.",
        "",
        "Proposed relations are expressed in a neutral `kmb:` namespace in the accompanying "
        "`fibo-bridges.ttl`; we deliberately do **not** assert unverified FIBO object properties. "
        "The intent is to identify the *gap*; mapping each edge to the right FIBO property (or "
        "minting one) is the reviewer's call.",
        "",
        "## Proposed relations (edges)",
        "",
        "| edge | proposed property |",
        "|---|---|",
    ]
    lines += [f"| {e} | `kmb:{camel(e)}` |" for e in edges]
    lines += [""]

    by_uc = {}
    for b in bridges:
        by_uc.setdefault(b["use_case"], []).append(b)
    for uc, items in by_uc.items():
        lines += [f"## {uc}  ({len(items)})", ""]
        for b in items:
            s, t = label(labels, b["source"]), label(labels, b["target"])
            lines += [
                f"### {s} —[{b['edge']}]→ {t}",
                f"- **kind:** {b['kind']}",
                f"- **source:** `{b['source']}`",
                f"- **target:** `{b['target']}`",
                f"- **rationale:** {b['rationale']}",
                f"- **citation:** {b['citation']}",
                "",
            ]
    return "\n".join(lines)


def emit_ttl(bridges, labels):
    edges = sorted({b["edge"] for b in bridges})
    L = [
        "@prefix owl: <http://www.w3.org/2002/07/owl#> .",
        "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .",
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
        "@prefix dct: <http://purl.org/dc/terms/> .",
        f"@prefix kmb: <{KMB}> .",
        "",
        "# Proposed cross-domain relations between FIBO classes (curated, grounded, gated).",
        "# Properties live in the kmb: namespace — these are PROPOSALS, not asserted FIBO axioms.",
        "",
    ]
    for e in edges:
        L += [f"kmb:{camel(e)} a owl:ObjectProperty ; rdfs:label {ttl_lit(e.replace('-', ' '))} ."]
    L += [""]
    for b in bridges:
        s, t, p = b["source"], b["target"], f"kmb:{camel(b['edge'])}"
        L += [
            f"<{s}> {p} <{t}> .",
            "[] a owl:Axiom ;",
            f"   owl:annotatedSource <{s}> ;",
            f"   owl:annotatedProperty {p} ;",
            f"   owl:annotatedTarget <{t}> ;",
            f"   rdfs:label {ttl_lit(b['id'])} ;",
            f"   kmb:kind {ttl_lit(b['kind'])} ;",
            f"   kmb:useCase {ttl_lit(b['use_case'])} ;",
            f"   rdfs:comment {ttl_lit(b['rationale'])} ;",
            f"   dct:source {ttl_lit(b['citation'])} .",
            "",
        ]
    return "\n".join(L)


def main():
    labels = load_labels()
    bridges = load_bridges()
    os.makedirs("contrib", exist_ok=True)
    open("contrib/edmc-bridge-contribution.md", "w").write(emit_md(bridges, labels))
    open("contrib/fibo-bridges.ttl", "w").write(emit_ttl(bridges, labels))
    by_uc = {}
    for b in bridges:
        by_uc[b["use_case"]] = by_uc.get(b["use_case"], 0) + 1
    print(f"Packaged {len(bridges)} bridges -> contrib/edmc-bridge-contribution.md + contrib/fibo-bridges.ttl")
    for uc, n in by_uc.items():
        print(f"  {n:2}  {uc}")


if __name__ == "__main__":
    main()
