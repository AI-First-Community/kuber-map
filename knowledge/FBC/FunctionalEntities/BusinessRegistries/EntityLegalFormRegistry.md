---
type: FIBO Class
title: "entity legal form registry"
description: "registry for registering and maintaining information about the legal forms that are valid for business entities for a particular jurisdiction following the ISO 20275 standard"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/EntityLegalFormRegistry
tags: [FBC, Release]
synonyms:
  - "ELF registry"
relations:
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/Registry.md", provenance: fibo}
  - {type: comprises, target: "/FBC/FunctionalEntities/BusinessRegistries/EntityLegalFormRegistryEntry.md", provenance: fibo}
---

registry for registering and maintaining information about the legal forms that are valid for business entities for a particular jurisdiction following the ISO 20275 standard

### Relationships
- is-a: [Registry](/CMNS/RegistrationAuthorities/Registry.md)
- comprises: [EntityLegalFormRegistryEntry](/FBC/FunctionalEntities/BusinessRegistries/EntityLegalFormRegistryEntry.md)
