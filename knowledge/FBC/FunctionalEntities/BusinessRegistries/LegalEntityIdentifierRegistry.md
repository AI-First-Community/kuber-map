---
type: FIBO Class
title: "legal entity identifier registry"
description: "registry for registering and maintaining information about business entities for a particular jurisdiction"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LegalEntityIdentifierRegistry
tags: [FBC, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
examples:
  - "A GLEIF-accredited Local Operating Unit that issues LEIs."
examples_provenance: curated
synonyms:
  - "LEI registry"
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry.md", provenance: fibo}
  - {type: comprises, target: "/FBC/FunctionalEntities/BusinessRegistries/LegalEntityIdentifierRegistryEntry.md", provenance: fibo}
---

registry for registering and maintaining information about business entities for a particular jurisdiction

### Relationships
- is-a: [BusinessRegistry](/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry.md)
- comprises: [LegalEntityIdentifierRegistryEntry](/FBC/FunctionalEntities/BusinessRegistries/LegalEntityIdentifierRegistryEntry.md)
