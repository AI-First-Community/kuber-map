#!/usr/bin/env python3
"""
Author curated CROSS-DOMAIN BRIDGES — lateral relations FIBO does not draw natively, needed to
make a use case coherent. These are the project's contribution-back candidates for EDM Council,
so each is GROUNDED and GATED:

  * both endpoints must resolve to real FIBO classes in out/intermediate.json (no invented IRIs);
  * FIBO must NOT already assert an equivalent edge (source --*--> target) — we never duplicate
    FIBO or mislabel provenance;
  * every bridge carries a rationale + citation for review.

The resolver exits non-zero if any bridge fails these gates. Emits knowledge/bridges/*.md (OKF,
provenance: curated) + curation/bridges.json.

Usage:
    python etl/bridges.py --in out/intermediate.json
"""
import argparse
import json
import os

from fibo_ns import iri_to_path

# ---- Bridge spec: Loan Origination & Underwriting -----------------------------------------
# (source_id, source_cluster), edge, (target_id, target_cluster), rationale, citation, kind
BRIDGES = [
    {
        "id": "hmda-covered-loan-reported-in-hmda-report",
        "source": ("HMDA-CoveredLoanContract", "LOAN"),
        "edge": "reported-in",
        "target": ("HMDA-Report", "LOAN"),
        "kind": "intra-domain gap",
        "rationale": "HMDA requires every covered loan/application to be recorded on the "
                     "institution's Loan/Application Register that constitutes the HMDA report. "
                     "FIBO models both HMDA-CoveredLoanContract and HMDA-Report but does not "
                     "connect the reported loan to the report that reports it.",
        "citation": "12 CFR 1003.4 (Regulation C — compilation of reportable data)",
    },
    {
        "id": "hmda-report-filed-by-financial-institution",
        "source": ("HMDA-Report", "LOAN"),
        "edge": "filed-by",
        "target": ("FinancialInstitution", "FBC"),
        "kind": "cross-domain (LOAN->FBC)",
        "rationale": "A HMDA report is filed by a covered financial institution. FIBO links "
                     "HMDA-Report to the RegulatoryAgency it is submitted-to, but not to the "
                     "filing institution — leaving the filer unresolved.",
        "citation": "12 CFR 1003.2 (covered institution); 12 CFR 1003.5 (reporting)",
    },
    {
        "id": "financial-institution-identified-by-lei",
        "source": ("FinancialInstitution", "FBC"),
        "edge": "identified-by",
        "target": ("LegalEntityIdentifier", "BE"),
        "kind": "cross-domain (FBC->BE)",
        "rationale": "For KYC / entity resolution a financial institution is identified by its "
                     "Legal Entity Identifier. FIBO defines LegalEntityIdentifier in BE but does "
                     "not connect FinancialInstitution to it.",
        "citation": "ISO 17442 (LEI); FIBO BE LegalEntityIdentifier",
    },
    {
        "id": "lender-played-by-financial-institution",
        "source": ("Lender", "FBC"),
        "edge": "played-by",
        "target": ("FinancialInstitution", "FBC"),
        "kind": "role->entity gap (FBC)",
        "rationale": "Lender is modeled as a party role (is-a ContractParty/Creditor); "
                     "FinancialInstitution is the legal-entity type that plays it. FIBO leaves "
                     "the role-to-entity link implicit, blocking resolution of 'the lender' to a "
                     "regulated institution.",
        "citation": "FIBO FBC party-role vs entity modeling",
    },
]


def resolve(idx, id_cluster):
    hits = idx.get(id_cluster, [])
    return hits[0] if hits else None


def fibo_has_edge(src_rec, target_iri):
    """True if FIBO already asserts any edge from src to target (so a bridge would be redundant)."""
    return any(e["target"] == target_iri for e in src_rec["relations"])


def emit_md(b, src, tgt):
    tpath = iri_to_path(tgt["iri"])
    return "\n".join([
        "---",
        "type: Cross-Domain Relation",
        f'title: "{src["title"]} -> {tgt["title"]}"',
        f'description: "{b["rationale"].split(".")[0]}."',
        f'tags: [bridge, {src["cluster"]}, {tgt["cluster"]}]',
        "relations:",
        f'  - {{type: {b["edge"]}, target: "{tpath}", provenance: curated}}',
        f'source_class: "{iri_to_path(src["iri"])}"',
        f'kind: "{b["kind"]}"',
        f'citation: "{b["citation"]}"',
        f'rationale: "{b["rationale"]}"',
        "---",
        "",
        f'**{src["title"]}** --[{b["edge"]}]--> **{tgt["title"]}**  _(curated bridge — {b["kind"]})_',
        "",
        b["rationale"],
        "",
        f'*Citation:* {b["citation"]}',
        "",
    ])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", default="out/intermediate.json")
    ap.add_argument("--bundle", default="knowledge")
    ap.add_argument("--out", default="curation/bridges.json")
    ap.add_argument("--spec", default=None,
                    help="bridge spec JSON (list of {id, source:[id,cl], edge, target:[id,cl], "
                         "kind, rationale, citation}); default = built-in loan-origination bridges")
    args = ap.parse_args()

    if args.spec:
        raw = json.load(open(args.spec))
        raw = raw.get("bridges", raw) if isinstance(raw, dict) else raw
        bridges = [{**b, "source": tuple(b["source"]), "target": tuple(b["target"])} for b in raw]
    else:
        bridges = BRIDGES

    recs = json.load(open(args.inp))
    idx = {}
    for r in recs:
        idx.setdefault((r["id"], r["cluster"]), []).append(r)

    ok, errors = [], []
    for b in bridges:
        src = resolve(idx, b["source"])
        tgt = resolve(idx, b["target"])
        if not src:
            errors.append((b["id"], f"source {b['source']} not found"))
            continue
        if not tgt:
            errors.append((b["id"], f"target {b['target']} not found"))
            continue
        if fibo_has_edge(src, tgt["iri"]):
            errors.append((b["id"], "FIBO already links these — bridge would duplicate (provenance risk)"))
            continue
        ok.append((b, src, tgt))

    print("=== CROSS-DOMAIN BRIDGE NOMINATION — Loan Origination ===")
    for b, src, tgt in ok:
        print(f'\n  [{b["kind"]}]')
        print(f'  {src["cluster"]} {src["title"]}  --[{b["edge"]}]-->  {tgt["cluster"]} {tgt["title"]}')
        print(f'    rationale: {b["rationale"][:110]}...')
        print(f'    citation : {b["citation"]}')

    if errors:
        print("\n❌ REJECTED bridges (fix before contributing):")
        for bid, why in errors:
            print(f"   {bid}: {why}")

    bdir = os.path.join(args.bundle, "bridges")
    os.makedirs(bdir, exist_ok=True)
    for b, src, tgt in ok:
        open(os.path.join(bdir, f'{b["id"]}.md'), "w").write(emit_md(b, src, tgt))
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    json.dump({"bridges": [{"id": b["id"], "edge": b["edge"], "kind": b["kind"],
                            "source": src["iri"], "target": tgt["iri"],
                            "rationale": b["rationale"], "citation": b["citation"]}
                           for b, src, tgt in ok]}, open(args.out, "w"), indent=2)
    print(f"\nAccepted {len(ok)} bridges -> {bdir}/ + {args.out}")
    return 1 if errors else 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
