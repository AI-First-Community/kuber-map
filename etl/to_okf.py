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


def load_definitions(paths):
    """Collect learner-friendly definition overrides: iri -> definition text.

    Only for CORE concepts that FIBO ships with no skos:definition (see curation/
    definitions.json). Each is grounded in the class's FIBO superclass/axioms, and applied
    with `definition_provenance: curated` so ours is never confused with FIBO's own text."""
    defs = {}
    for path in paths:
        try:
            data = json.load(open(path))
        except (OSError, json.JSONDecodeError):
            continue
        for entry in data.get("definitions", []):
            if entry.get("iri") and entry.get("definition"):
                defs[entry["iri"]] = entry["definition"]
    return defs


def load_examples(paths):
    """Curated real-world examples per concept: iri -> [example, ...]. Illustrative instances
    (general domain knowledge), applied when FIBO supplies none; marked provenance curated."""
    out = {}
    for path in paths:
        try:
            data = json.load(open(path))
        except (OSError, json.JSONDecodeError):
            continue
        for e in data.get("examples", []):
            if e.get("iri") and e.get("examples"):
                out[e["iri"]] = e["examples"]
    return out


def emit(rec, is_core=False, curated_def=False, curated_examples=False):
    tags = [rec["cluster"]] + ([rec["maturity"]] if rec["maturity"] else [])
    out = ["---", "type: FIBO Class", f'title: "{yaml_1line(rec["title"])}"']
    if rec["description"]:
        out.append(f'description: "{yaml_1line(rec["description"])}"')
        if curated_def:
            out.append("definition_provenance: curated")
    out += [f'resource: {rec["iri"]}', f'tags: [{", ".join(tags)}]']
    if is_core:
        out.append("core: true")
    # Richer FIBO annotations for the detail card: explanatory/usage notes, examples, synonyms.
    if rec.get("explanatory"):
        out.append(f'detail: "{yaml_1line(" ".join(rec["explanatory"]))}"')
    for key in ("examples", "synonyms"):
        vals = rec.get(key) or []
        if vals:
            out.append(f"{key}:")
            out += [f'  - "{yaml_1line(v)}"' for v in vals]
            if key == "examples" and curated_examples:
                out.append("examples_provenance: curated")
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
    ap.add_argument("--curation", nargs="+",
                    default=["curation/loan-origination.json", "curation/definitions.json",
                             "curation/examples.json"],
                    help="curation JSON: `core:` stamps core; `definitions:`/`examples:` overlay content")
    args = ap.parse_args()
    keep = set(args.clusters)
    curation_paths = [p for pat in args.curation for p in glob.glob(pat)] or args.curation
    core_iris = load_core_iris(curation_paths)
    definitions = load_definitions(curation_paths)
    examples = load_examples(curation_paths)

    records = [r for r in json.load(open(args.inp)) if r["cluster"] in keep]
    seen_paths = {}
    by_cluster = {}
    core_written = 0
    curated_defs = 0
    refused = []      # overrides we declined because FIBO already has a real definition
    for r in records:
        cl = r["cluster"]
        is_core = r["iri"] in core_iris
        core_written += is_core
        curated_def = False
        override = definitions.get(r["iri"])
        if override:
            if (r["description"] or "").strip():
                refused.append(r["iri"])           # never replace real FIBO text (Rule 3)
            else:
                r = {**r, "description": override}  # local copy; also flows to the index
                curated_def = True
                curated_defs += 1
        # Curated examples fill in where FIBO supplies none (provenance kept distinct).
        curated_examples = False
        ex_override = examples.get(r["iri"])
        if ex_override and not (r.get("examples") or []):
            r = {**r, "examples": ex_override}
            curated_examples = True
        rel = iri_to_path(r["iri"])            # single source of truth for placement
        path = os.path.join(args.bundle, rel.lstrip("/"))
        if path in seen_paths and seen_paths[path] != r["iri"]:
            print(f"  ! id collision: {path} ({seen_paths[path]} vs {r['iri']})")
        seen_paths[path] = r["iri"]
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w").write(emit(r, is_core=is_core, curated_def=curated_def,
                                   curated_examples=curated_examples))
        by_cluster.setdefault(cl, []).append(r)

    for cl, recs in by_cluster.items():
        with open(os.path.join(args.bundle, cl, "index.md"), "w") as fh:
            fh.write(f"# {cl}\n\n")
            for r in sorted(recs, key=lambda x: x["title"]):
                desc = (r["description"] or "").split(".")[0][:120]
                link = iri_to_path(r["iri"])[len(cl) + 2:]   # path relative to cluster dir
                mark = "core · " if r["iri"] in core_iris else ""
                fh.write(f'- {mark}[{r["title"]}]({link}) — {desc}\n')

    # Warn if a curated IRI never matched an emitted class (moved/renamed → silent gap).
    emitted = set(seen_paths.values())
    missing = sorted(i for i in core_iris if i not in emitted)
    defs_missing = sorted(i for i in definitions if i not in emitted)

    print(f"Wrote {sum(len(v) for v in by_cluster.values())} OKF files: "
          + ", ".join(f"{k}={len(v)}" for k, v in sorted(by_cluster.items())))
    print(f"Stamped core: true on {core_written}/{len(core_iris)} curated concepts.")
    print(f"Applied {curated_defs}/{len(definitions)} curated definition overrides.")
    if refused:
        print(f"  ! {len(refused)} overrides REFUSED (FIBO already has a definition — kept FIBO's):")
        for i in refused:
            print(f"    - {i}")
    if missing:
        print(f"  ! {len(missing)} core IRIs not emitted (out-of-scope cluster or moved):")
        for i in missing:
            print(f"    - {i}")
    if defs_missing:
        print(f"  ! {len(defs_missing)} definition-override IRIs not emitted (moved/renamed?):")
        for i in defs_missing:
            print(f"    - {i}")


if __name__ == "__main__":
    main()
