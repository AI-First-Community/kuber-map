#!/usr/bin/env python3
"""
Map extracted FIBO records -> an OKF markdown bundle (PLAN.md §5).
Emits only classes whose cluster is in --clusters; cross-cluster edges to not-yet-loaded
domains remain as (OKF-tolerated) pending links.

Usage:
    python etl/to_okf.py --in out/intermediate.json --bundle knowledge --clusters FND LOAN
"""
import argparse
import json
import os

from fibo_ns import iri_to_path, local_name


def yaml_1line(s):
    return "" if s is None else s.replace('"', "'").replace("\n", " ").strip()


def emit(rec):
    tags = [rec["cluster"]] + ([rec["maturity"]] if rec["maturity"] else [])
    out = ["---", "type: FIBO Class", f'title: "{yaml_1line(rec["title"])}"']
    if rec["description"]:
        out.append(f'description: "{yaml_1line(rec["description"])}"')
    out += [f'resource: {rec["iri"]}', f'tags: [{", ".join(tags)}]']
    rels = [e for e in rec["relations"] if iri_to_path(e["target"])]
    if rels:
        out.append("relations:")
        for e in rels:
            out.append(f'  - {{type: {e["type"]}, target: "{iri_to_path(e["target"])}", '
                       f'provenance: {e["provenance"]}}}')
    out += ["---", "", rec["description"] or f'FIBO class *{rec["title"]}*.', ""]
    if rels:
        out.append("### Relationships")
        for e in rels:
            out.append(f'- {e["type"]}: [{local_name(e["target"])}]({iri_to_path(e["target"])})')
        out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", default="out/intermediate.json")
    ap.add_argument("--bundle", default="knowledge")
    ap.add_argument("--clusters", nargs="+", default=["FND", "LOAN"])
    args = ap.parse_args()
    keep = set(args.clusters)

    records = [r for r in json.load(open(args.inp)) if r["cluster"] in keep]
    seen_paths = {}
    by_cluster = {}
    for r in records:
        cl = r["cluster"]
        rel = iri_to_path(r["iri"])            # single source of truth for placement
        path = os.path.join(args.bundle, rel.lstrip("/"))
        if path in seen_paths and seen_paths[path] != r["iri"]:
            print(f"  ! id collision: {path} ({seen_paths[path]} vs {r['iri']})")
        seen_paths[path] = r["iri"]
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w").write(emit(r))
        by_cluster.setdefault(cl, []).append(r)

    for cl, recs in by_cluster.items():
        with open(os.path.join(args.bundle, cl, "index.md"), "w") as fh:
            fh.write(f"# {cl}\n\n")
            for r in sorted(recs, key=lambda x: x["title"]):
                desc = (r["description"] or "").split(".")[0][:120]
                link = iri_to_path(r["iri"])[len(cl) + 2:]   # path relative to cluster dir
                fh.write(f'- [{r["title"]}]({link}) — {desc}\n')

    print(f"Wrote {sum(len(v) for v in by_cluster.values())} OKF files: "
          + ", ".join(f"{k}={len(v)}" for k, v in sorted(by_cluster.items())))


if __name__ == "__main__":
    main()
