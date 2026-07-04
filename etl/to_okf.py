#!/usr/bin/env python3
"""
Map extracted FIBO records -> an OKF markdown bundle (PLAN.md §5).
Emits only classes whose cluster is in --clusters; cross-cluster edges to not-yet-loaded
domains remain as (OKF-tolerated) pending links.

Usage:
    python etl/to_okf.py --in out/intermediate.json --bundle knowledge --clusters FND LOAN
"""
import argparse
import glob
import json
import os

from fibo_ns import iri_to_path, local_name


def yaml_1line(s):
    return "" if s is None else s.replace('"', "'").replace("\n", " ").strip()


def load_core_iris(paths):
    """Collect the set of curated `core:` IRIs from curation JSON files.

    A curation file (e.g. curation/loan-origination.json) has a `core` list of entries,
    each carrying the real FIBO `iri` and a `core` flag. We stamp `core: true` on the
    matching concept file so the map's default view and context packs can select it.
    Files without a `core` list (e.g. bridges.json) are ignored."""
    core = set()
    for path in paths:
        try:
            data = json.load(open(path))
        except (OSError, json.JSONDecodeError):
            continue
        for entry in data.get("core", []):
            if entry.get("core") and entry.get("iri"):
                core.add(entry["iri"])
    return core


def emit(rec, is_core=False):
    tags = [rec["cluster"]] + ([rec["maturity"]] if rec["maturity"] else [])
    out = ["---", "type: FIBO Class", f'title: "{yaml_1line(rec["title"])}"']
    if rec["description"]:
        out.append(f'description: "{yaml_1line(rec["description"])}"')
    out += [f'resource: {rec["iri"]}', f'tags: [{", ".join(tags)}]']
    if is_core:
        out.append("core: true")
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
    ap.add_argument("--curation", nargs="+", default=["curation/loan-origination.json"],
                    help="curation JSON files whose `core:` entries stamp core: true")
    args = ap.parse_args()
    keep = set(args.clusters)
    curation_paths = [p for pat in args.curation for p in glob.glob(pat)] or args.curation
    core_iris = load_core_iris(curation_paths)

    records = [r for r in json.load(open(args.inp)) if r["cluster"] in keep]
    seen_paths = {}
    by_cluster = {}
    core_written = 0
    for r in records:
        cl = r["cluster"]
        is_core = r["iri"] in core_iris
        core_written += is_core
        rel = iri_to_path(r["iri"])            # single source of truth for placement
        path = os.path.join(args.bundle, rel.lstrip("/"))
        if path in seen_paths and seen_paths[path] != r["iri"]:
            print(f"  ! id collision: {path} ({seen_paths[path]} vs {r['iri']})")
        seen_paths[path] = r["iri"]
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w").write(emit(r, is_core=is_core))
        by_cluster.setdefault(cl, []).append(r)

    for cl, recs in by_cluster.items():
        with open(os.path.join(args.bundle, cl, "index.md"), "w") as fh:
            fh.write(f"# {cl}\n\n")
            for r in sorted(recs, key=lambda x: x["title"]):
                desc = (r["description"] or "").split(".")[0][:120]
                link = iri_to_path(r["iri"])[len(cl) + 2:]   # path relative to cluster dir
                mark = "core · " if r["iri"] in core_iris else ""
                fh.write(f'- {mark}[{r["title"]}]({link}) — {desc}\n')

    # Warn if a curated core IRI never matched an emitted class (moved/renamed → silent gap).
    emitted = set(seen_paths.values())
    missing = sorted(i for i in core_iris if i not in emitted)

    print(f"Wrote {sum(len(v) for v in by_cluster.values())} OKF files: "
          + ", ".join(f"{k}={len(v)}" for k, v in sorted(by_cluster.items())))
    print(f"Stamped core: true on {core_written}/{len(core_iris)} curated concepts.")
    if missing:
        print(f"  ! {len(missing)} core IRIs not emitted (out-of-scope cluster or moved):")
        for i in missing:
            print(f"    - {i}")


if __name__ == "__main__":
    main()
