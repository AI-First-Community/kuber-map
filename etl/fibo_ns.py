"""Shared FIBO namespace helpers: cluster classification, IRI->path, label normalization."""
import re

FIBO_ONT = "https://spec.edmcouncil.org/fibo/ontology/"
COMMONS = "https://www.omg.org/spec/Commons/"
LCC = "https://www.omg.org/spec/LCC/"

FIBO_DOMAINS = {"FND", "BE", "FBC", "SEC", "DER", "IND", "LOAN", "BP", "CAE", "MD"}


def cluster_of(uri: str):
    """Map any class IRI to a cluster code, or None if external/not-mappable.

    FIBO domains -> the domain code (FND, LOAN, ...); Commons -> CMNS; LCC -> LCC.
    Everything else (skos, dct, w3 ...) -> None (dropped as a node; tolerated as a link target).
    """
    if not uri:
        return None
    if uri.startswith(FIBO_ONT):
        seg = uri[len(FIBO_ONT):].split("/", 1)[0]
        return seg if seg in FIBO_DOMAINS else None
    if uri.startswith(COMMONS):
        return "CMNS"
    if uri.startswith(LCC):
        return "LCC"
    return None


def local_name(uri) -> str:
    s = str(uri)
    for sep in ("#", "/"):
        if sep in s:
            s = s.rsplit(sep, 1)[-1]
    return s


def iri_to_path(uri: str) -> str | None:
    """Deterministic, collision-free bundle path for a class IRI, mirroring FIBO's
    module structure: /<CLUSTER>/<module>/<submodule>/<LocalName>.md.

    IRIs are globally unique, so replicating their path segments guarantees no collision
    (the flat /<CLUSTER>/<name>.md scheme collides, e.g. FND has two TransactionEvent classes).
    Returns None for unmappable IRIs so callers can mark broken links.
    """
    cl = cluster_of(uri)
    if not cl:
        return None
    if uri.startswith(FIBO_ONT):
        tail = uri[len(FIBO_ONT):].split("/")[1:]   # drop the domain segment (== cluster)
    elif uri.startswith(COMMONS):
        tail = uri[len(COMMONS):].split("/")
    elif uri.startswith(LCC):
        tail = uri[len(LCC):].split("/")
    else:
        return None
    tail = [t for t in tail if t]
    return "/" + "/".join([cl] + tail) + ".md"


_CAMEL = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")


def normalize_edge_type(raw: str) -> str:
    """Canonical kebab-case edge type from an rdfs:label ('is performed by') or a
    camelCase local name ('isCollateralizedBy') -> 'is-performed-by' / 'is-collateralized-by'."""
    if raw == "is-a":
        return raw
    s = _CAMEL.sub(" ", raw)            # split camelCase if it's a local name
    s = re.sub(r"[_/]", " ", s)
    s = re.sub(r"[^A-Za-z0-9]+", " ", s).strip().lower()
    return re.sub(r"\s+", "-", s)
