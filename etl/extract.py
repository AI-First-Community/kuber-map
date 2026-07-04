#!/usr/bin/env python3
"""
FIBO extraction (Phase 0.5, hardened).

Pulls TYPED object-property relations out of FIBO's owl:Restriction blank-node axioms
(NOT flat triples), propagates per-ontology maturity to classes, classifies every class
and edge target into a cluster (FIBO domain / CMNS / LCC), and normalizes edge labels.

Usage:
    python etl/extract.py --fibo fibo-source --domains FND LOAN --out out/intermediate.json
"""
import argparse
import glob
import json
import os
import sys
from collections import Counter

from fibo_ns import cluster_of, local_name, normalize_edge_type
from rdflib import OWL, RDF, RDFS, BNode, Graph, Literal, URIRef
from rdflib.namespace import SKOS

FILLER_PREDS = [OWL.someValuesFrom, OWL.allValuesFrom, OWL.onClass, OWL.hasValue]
MATURITY_PRED = URIRef("https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel")


def load_domains(fibo_root, domains):
    """Parse every .rdf under the given domains. Returns (graph, class_source, files).
    class_source: class-URI -> {file, cluster, maturity} for classes DEFINED in a loaded file."""
    g = Graph()
    class_source = {}
    files = []
    for d in domains:
        files += glob.glob(os.path.join(fibo_root, d, "**", "*.rdf"), recursive=True)

    for f in files:
        try:
            fg = Graph().parse(f, format="xml")
        except Exception as e:
            print(f"  ! parse failed {f}: {e}", file=sys.stderr)
            continue
        g += fg
        maturity = None
        for ont in fg.subjects(RDF.type, OWL.Ontology):
            for lvl in fg.objects(ont, MATURITY_PRED):
                maturity = local_name(lvl)
        for c in set(fg.subjects(RDF.type, OWL.Class)):
            if isinstance(c, BNode):
                continue
            defined = (c, RDFS.label, None) in fg or (c, RDFS.subClassOf, None) in fg \
                      or (c, SKOS.definition, None) in fg
            if not defined:
                continue
            key = str(c)
            if key not in class_source or (maturity and not class_source[key].get("maturity")):
                class_source[key] = {"file": os.path.relpath(f), "cluster": cluster_of(key),
                                     "maturity": maturity}
    return g, class_source, files


def one(g, s, p):
    for o in g.objects(s, p):
        return o
    return None


def _lang_rank(lang):
    lang = (lang or "").lower()
    if lang == "en-us":
        return 0
    if lang == "en":
        return 1
    if lang.startswith("en"):
        return 2
    if lang == "":
        return 3
    return 4


def best_literal(g, s, p):
    """Deterministically pick ONE literal among possibly several for (s, p).

    FIBO ships multiple values for the same annotation (e.g. rdfs:label en-US 'program
    identifier' vs en-GB 'programme identifier', or two skos:definitions after ontology
    merge). rdflib yields them in unstable order, so `one()` produced non-reproducible
    bundles. Prefer en-US, then en, then other en-*, then untagged, then any; break ties
    on the string so the choice is fully deterministic."""
    objs = [o for o in g.objects(s, p) if isinstance(o, Literal)]
    if not objs:
        return None
    return min(objs, key=lambda o: (_lang_rank(getattr(o, "language", None)), str(o)))


def restriction_relation(g, restr):
    prop = one(g, restr, OWL.onProperty)
    if prop is None or not isinstance(prop, URIRef):
        return None
    for fp in FILLER_PREDS:
        filler = one(g, restr, fp)
        if isinstance(filler, URIRef):
            return prop, filler, local_name(fp)
    return None


def extract(g, class_source):
    prop_label = {}

    def edge_type(p):
        if p not in prop_label:
            lbl = best_literal(g, p, RDFS.label)
            prop_label[p] = normalize_edge_type(str(lbl) if lbl else local_name(p))
        return prop_label[p]

    records = []
    for c_uri in sorted(class_source):
        c = URIRef(c_uri)
        src = class_source[c_uri]
        label = best_literal(g, c, RDFS.label)
        definition = best_literal(g, c, SKOS.definition)
        seen = set()
        relations = []
        for sup in g.objects(c, RDFS.subClassOf):
            if isinstance(sup, URIRef):
                rel = ("is-a", str(sup))
                if rel in seen or str(sup) == c_uri:
                    continue
                seen.add(rel)
                relations.append({"type": "is-a", "edge": "subClassOf", "target": str(sup),
                                  "target_cluster": cluster_of(str(sup)), "provenance": "fibo"})
            elif isinstance(sup, BNode) and (sup, RDF.type, OWL.Restriction) in g:
                rr = restriction_relation(g, sup)
                if not rr:
                    continue
                prop, filler, quant = rr
                et = edge_type(prop)
                rel = (et, str(filler))
                if rel in seen or str(filler) == c_uri:   # drop dup + self-loop
                    continue
                seen.add(rel)
                relations.append({"type": et, "edge": local_name(prop), "quantifier": quant,
                                  "target": str(filler), "target_cluster": cluster_of(str(filler)),
                                  "provenance": "fibo"})
        # Stable, reproducible order: is-a first, then typed edges by (type, target).
        relations.sort(key=lambda r: (r["type"] != "is-a", r["type"], r["target"]))
        records.append({"iri": c_uri, "id": local_name(c),
                        "title": str(label) if label else local_name(c),
                        "description": str(definition) if definition else None,
                        "cluster": src["cluster"], "maturity": src["maturity"],
                        "source_file": src["file"], "relations": relations})
    return records


def summarize(records, files, requested):
    emit = [r for r in records if r["cluster"] in requested]
    n = len(emit)
    with_def = sum(1 for r in emit if r["description"])
    edges = [(r, e) for r in emit for e in r["relations"]]
    isa = [e for _, e in edges if e["type"] == "is-a"]
    typed = [e for _, e in edges if e["type"] != "is-a"]
    cross = [(r, e) for r, e in edges if e["target_cluster"] and e["target_cluster"] != r["cluster"]]
    pending = [e for _, e in edges if e["target_cluster"] and e["target_cluster"] not in requested]
    dropped = len(records) - n
    print("\n================ FIBO EXTRACTION — SUMMARY ================")
    print(f"RDF files parsed            : {len(files)}")
    print(f"Classes emitted (in {sorted(requested)}): {n}   (dropped {dropped} out-of-scope stubs)")
    print(f"  with skos:definition      : {with_def} ({100*with_def//max(n,1)}%)")
    print(f"Edges                       : {len(edges)}  (is-a {len(isa)}, typed {len(typed)})")
    print(f"  cross-cluster edges       : {len(cross)}")
    print(f"  -> targets not yet loaded : {len(pending)} (pending links, OKF-tolerated)")
    print("\nTop normalized typed edges:")
    for t, c in Counter(e['type'] for e in typed).most_common(12):
        print(f"   {c:4d}  {t}")
    print("\nCross-cluster directions:")
    for d, c in Counter(f"{r['cluster']} -> {e['target_cluster']}" for r, e in cross).most_common(12):
        print(f"   {c:4d}  {d}")
    print("==========================================================\n")
    return emit


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fibo", default="fibo-source")
    ap.add_argument("--domains", nargs="+", default=["FND", "LOAN"])
    ap.add_argument("--out", default="out/intermediate.json")
    args = ap.parse_args()
    requested = set(args.domains)

    print(f"Loading FIBO {args.domains} from {args.fibo} ...")
    g, class_source, files = load_domains(args.fibo, args.domains)
    print(f"  merged: {len(g):,} triples, {len(files)} files, {len(class_source):,} defined classes")

    records = extract(g, class_source)
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    json.dump(records, open(args.out, "w"), indent=2)
    print(f"Wrote {args.out} ({len(records)} records, all clusters)")

    summarize(records, files, requested)


if __name__ == "__main__":
    main()
