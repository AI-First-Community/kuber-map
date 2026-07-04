#!/usr/bin/env bash
# Fetch the OMG Commons Ontology Library modules that FIBO imports, into commons-source/
# (gitignored). Commons is FIBO's shared upper ontology (Classifier, DatePeriod, Party, …);
# loading it lets the ~580 edges that point at Commons resolve to real nodes in the map.
#
# Commons isn't a public git repo we can pin, but each module IRI is content-negotiable:
# GET https://www.omg.org/spec/Commons/<Module>/  with Accept: application/rdf+xml returns
# that module's RDF/XML. We fetch exactly the modules FIBO's loaded domains reference.
set -euo pipefail

BASE="https://www.omg.org/spec/Commons"
DEST="commons-source"
MODULES=(
  AnnotationVocabulary BusinessAuthorizations Classifiers CodesAndCodeSets Collections
  ContextualDesignators ContextualIdentifiers DatesAndTimes Designators Documents
  Identifiers Locations Organizations PartiesAndSituations QuantitiesAndUnits
  RegistrationAuthorities RegulatoryAgencies RolesAndCompositions SitesAndFacilities
)

mkdir -p "$DEST"
ok=0
for m in "${MODULES[@]}"; do
  out="$DEST/$m.rdf"
  if curl -fsSL -H "Accept: application/rdf+xml" "$BASE/$m/" -o "$out" 2>/dev/null \
     && head -c 64 "$out" | grep -q "xml"; then
    ok=$((ok + 1))
  else
    echo "  ! failed to fetch $m" >&2
    rm -f "$out"
  fi
done
echo "Commons: fetched $ok/${#MODULES[@]} modules into $DEST/"
