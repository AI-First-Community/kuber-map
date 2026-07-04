#!/usr/bin/env python3
"""
Keyword retrieval over a context pack (PLAN.md §6) — the logic an agent's grounding
endpoint runs. Pure standard library (no vector DB, no extra deps): for the curated
70-concept scale, weighted token overlap is fast, deterministic, and explainable — and
every hit carries the FIBO `citation` IRI + provenance so answers stay auditable.

Used by etl/mcp_server.py (the MCP tool) and the grounded eval runner.
"""
import json
import re

_STOP = {"a", "an", "the", "of", "to", "in", "on", "for", "and", "or", "is", "are",
         "by", "with", "that", "this", "as", "at", "be", "it", "its", "from", "which",
         "some", "any", "may", "can", "was", "were", "has", "have", "not"}


def tokens(text):
    return [t for t in re.split(r"[^a-z0-9]+", (text or "").lower()) if t and t not in _STOP]


class Pack:
    """A loaded context pack with keyword search + citation lookup."""

    def __init__(self, data):
        self.use_case = data.get("use_case")
        self.concepts = data.get("concepts", [])
        self.bridges = data.get("bridges", [])
        self._by_iri = {c["iri"]: c for c in self.concepts}
        # Precompute a weighted token bag per concept: title terms count more than definition.
        self._bags = []
        for c in self.concepts:
            bag = {}
            for tok in tokens(c["title"]):
                bag[tok] = bag.get(tok, 0) + 3
            for tok in tokens(c.get("facet")):
                bag[tok] = bag.get(tok, 0) + 2
            for tok in tokens(c.get("definition")):
                bag[tok] = bag.get(tok, 0) + 1
            self._bags.append(bag)

    @classmethod
    def load(cls, path):
        return cls(json.load(open(path)))

    def search(self, query, k=5):
        """Top-k concepts by weighted token overlap. Deterministic: ties break on title.
        Returns lightweight hits (title, definition, provenance, citation, score)."""
        q = set(tokens(query))
        scored = []
        for c, bag in zip(self.concepts, self._bags, strict=True):
            score = sum(w for tok, w in bag.items() if tok in q)
            if score > 0:
                scored.append((score, c))
        scored.sort(key=lambda sc: (-sc[0], sc[1]["title"]))
        return [self._hit(c, score) for score, c in scored[:k]]

    def get(self, iri):
        """Full concept record for an IRI (the citation target), or None."""
        return self._by_iri.get(iri)

    @staticmethod
    def _hit(c, score):
        return {"iri": c["iri"], "title": c["title"], "cluster": c["cluster"],
                "definition": c.get("definition"),
                "definition_provenance": c.get("definition_provenance"),
                "citation": c["citation"], "score": score}
