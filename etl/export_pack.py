#!/usr/bin/env python3
"""
Export a use-case CONTEXT PACK — the product (PLAN.md §6).

Takes a use case's curated grounding closure (its `core:` concepts + the cross-domain
bridges it needs) and emits a portable pack an AI agent consumes as audit-ready grounding:

  export/<use-case>/
    pack.json     structured records for RAG / programmatic retrieval
    context.md    rendered grounding context for direct injection into an LLM prompt
    okf/          an OKF slice (the concept + bridge markdown, self-contained)
    README.md     what the pack is and how to cite from it

Every concept carries its FIBO `resource` IRI as the citation an agent cites, and every
edge/definition carries provenance (fibo | curated) so a regulator can trace each claim.

Grounded, not invented: concept data is read from out/intermediate.json (the extract) and
the curated overlays; the OKF slice is copied from the already-built knowledge/ bundle so
the pack and the map never drift.

Usage:
    python etl/export_pack.py --use-case loan-origination
"""
import argparse
import json
import os
import shutil

from fibo_ns import iri_to_path, local_name
from to_okf import load_definitions


def build_concepts(core_entries, recs, defs):
    """One grounding record per core concept, with resolved relation targets + provenance."""
    concepts = []
    for c in core_entries:
        iri = c["iri"]
        rec = recs.get(iri)
        if not rec:
            continue
        override = defs.get(iri)
        fibo_def = rec.get("description")
        if override and not (fibo_def or "").strip():
            definition, prov = override, "curated"
        else:
            definition, prov = fibo_def, ("fibo" if fibo_def else None)
        relations = [{"type": e["type"], "target": e["target"],
                      "target_title": (recs.get(e["target"]) or {}).get("title", local_name(e["target"])),
                      "provenance": e["provenance"]}
                     for e in rec["relations"]]
        concepts.append({
            "iri": iri, "title": rec["title"], "facet": c.get("facet"),
            "cluster": rec["cluster"], "maturity": rec.get("maturity"),
            "definition": definition, "definition_provenance": prov,
            "core": True, "citation": iri, "relations": relations,
        })
    concepts.sort(key=lambda x: (x["facet"] or "", x["title"]))
    return concepts


def build_bridges(bridge_entries, recs):
    out = []
    for b in bridge_entries:
        out.append({
            "id": b["id"], "edge": b["edge"], "kind": b["kind"],
            "source": b["source"], "source_title": (recs.get(b["source"]) or {}).get("title", local_name(b["source"])),
            "target": b["target"], "target_title": (recs.get(b["target"]) or {}).get("title", local_name(b["target"])),
            "provenance": "curated", "rationale": b["rationale"], "citation": b["citation"],
        })
    return out


def render_context_md(use_case, concepts, bridges):
    """A single grounding document for direct injection into an agent's prompt."""
    lines = [f"# Grounding context — {use_case}", "",
             "Curated FIBO concepts and cross-domain bridges that ground this agent. Cite the",
             "`resource` IRI on every claim. `provenance: fibo` = from FIBO; `provenance: curated`",
             "= authored by this project (grounded in FIBO's structure).", ""]
    by_facet = {}
    for c in concepts:
        by_facet.setdefault(c["facet"] or "Other", []).append(c)
    for facet in sorted(by_facet):
        lines.append(f"## {facet}")
        lines.append("")
        for c in by_facet[facet]:
            prov = f" _(definition: {c['definition_provenance']})_" if c["definition_provenance"] == "curated" else ""
            lines.append(f"### {c['title']}  [{c['cluster']}/{c['maturity'] or 'n/a'}]")
            lines.append(f"- **definition:** {c['definition'] or '(none in FIBO)'}{prov}")
            lines.append(f"- **cite:** {c['citation']}")
            fibo_rel = [r for r in c["relations"] if r["provenance"] == "fibo"]
            if fibo_rel:
                rel_str = "; ".join(f"{r['type']} → {r['target_title']}" for r in fibo_rel)
                lines.append(f"- **relations:** {rel_str}")
            lines.append("")
    if bridges:
        lines.append("## Cross-domain bridges (curated)")
        lines.append("")
        for b in bridges:
            lines.append(f"### {b['source_title']} → {b['target_title']}  _({b['kind']})_")
            lines.append(f"- **relation:** {b['source_title']} —[{b['edge']}]→ {b['target_title']} _(provenance: curated)_")
            lines.append(f"- **rationale:** {b['rationale']}")
            lines.append(f"- **cite:** {b['citation']}")
            lines.append("")
    return "\n".join(lines)


def copy_okf_slice(concepts, bundle, out_okf):
    """Copy the concept markdown from the built bundle into a self-contained OKF slice."""
    if os.path.isdir(out_okf):
        shutil.rmtree(out_okf)
    copied = 0
    for c in concepts:
        rel = iri_to_path(c["iri"]).lstrip("/")
        src = os.path.join(bundle, rel)
        if not os.path.exists(src):
            print(f"  ! OKF slice: {src} missing (build the bundle first)")
            continue
        dst = os.path.join(out_okf, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(src, dst)
        copied += 1
    bridges_src = os.path.join(bundle, "bridges")
    if os.path.isdir(bridges_src):
        shutil.copytree(bridges_src, os.path.join(out_okf, "bridges"))
    return copied


def write_index_md(use_case, concepts, bridges, out_okf):
    lines = [f"# {use_case} — OKF slice", "",
             f"{len(concepts)} grounding concepts + {len(bridges)} curated bridges.", ""]
    by_facet = {}
    for c in concepts:
        by_facet.setdefault(c["facet"] or "Other", []).append(c)
    for facet in sorted(by_facet):
        lines.append(f"## {facet}")
        for c in by_facet[facet]:
            lines.append(f"- [{c['title']}](.{iri_to_path(c['iri'])}) — {c['cluster']}")
        lines.append("")
    open(os.path.join(out_okf, "index.md"), "w").write("\n".join(lines))


def write_readme(use_case, out_dir, n_concepts, n_bridges):
    open(os.path.join(out_dir, "README.md"), "w").write("\n".join([
        f"# Context pack — {use_case}", "",
        "Audit-ready FIBO grounding for a financial AI agent.", "",
        "## Files",
        "- `pack.json` — structured concept + bridge records (RAG / programmatic retrieval).",
        "- `context.md` — the same content rendered for direct injection into an LLM prompt.",
        "- `okf/` — a self-contained OKF slice (concept + bridge markdown).", "",
        "## Retrieval endpoint (MCP)",
        "An agent can query this pack over the Model Context Protocol:",
        "",
        "```",
        "python etl/mcp_server.py --pack export/" + use_case + "/pack.json",
        "```",
        "",
        "Tools: `search_concepts(query, k)`, `get_concept(iri)`, `list_bridges()` — each result",
        "carries the FIBO `citation` IRI and `provenance`.", "",
        "## Citation model",
        f"{n_concepts} concepts, {n_bridges} curated bridges. Each concept's `citation` is its",
        "FIBO `resource` IRI — an agent cites it to justify a claim. `provenance` on every edge",
        "and definition is `fibo` (from FIBO) or `curated` (authored here, grounded in FIBO).", "",
        "Regenerate with `make pack` (after `make all`).", "",
    ]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", default="out/intermediate.json")
    ap.add_argument("--use-case", default="loan-origination")
    ap.add_argument("--core", default="curation/loan-origination.json")
    ap.add_argument("--bridges", default="curation/bridges.json")
    ap.add_argument("--defs", default="curation/definitions.json")
    ap.add_argument("--bundle", default="knowledge")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    out_dir = args.out or os.path.join("export", args.use_case)

    recs = {r["iri"]: r for r in json.load(open(args.inp))}
    core_doc = json.load(open(args.core))
    use_case = core_doc.get("use_case", args.use_case)
    core_entries = core_doc["core"]
    defs = load_definitions([args.defs])
    bridge_entries = json.load(open(args.bridges)).get("bridges", [])

    concepts = build_concepts(core_entries, recs, defs)
    bridges = build_bridges(bridge_entries, recs)

    os.makedirs(out_dir, exist_ok=True)
    curated_defs = sum(1 for c in concepts if c["definition_provenance"] == "curated")
    no_def = sum(1 for c in concepts if not c["definition"])
    pack = {
        "use_case": use_case,
        "generated_from": {"intermediate": args.inp, "core": args.core,
                           "bridges": args.bridges, "definitions": args.defs},
        "counts": {"concepts": len(concepts), "bridges": len(bridges),
                   "curated_definitions": curated_defs, "concepts_without_definition": no_def},
        "concepts": concepts, "bridges": bridges,
    }
    json.dump(pack, open(os.path.join(out_dir, "pack.json"), "w"), indent=2)
    open(os.path.join(out_dir, "context.md"), "w").write(render_context_md(use_case, concepts, bridges))
    out_okf = os.path.join(out_dir, "okf")
    copied = copy_okf_slice(concepts, args.bundle, out_okf)
    write_index_md(use_case, concepts, bridges, out_okf)
    write_readme(use_case, out_dir, len(concepts), len(bridges))

    print(f"Context pack -> {out_dir}/")
    print(f"  concepts     : {len(concepts)}  ({curated_defs} curated defs, {no_def} still undefined)")
    print(f"  bridges      : {len(bridges)} (curated)")
    print(f"  OKF slice    : {copied} concept files + bridges copied from {args.bundle}/")
    missing = len(core_entries) - len(concepts)
    if missing:
        print(f"  ! {missing} core entries did not resolve in {args.inp}")


if __name__ == "__main__":
    main()
