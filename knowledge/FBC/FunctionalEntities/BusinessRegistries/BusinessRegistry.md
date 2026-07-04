---
type: FIBO Class
title: "business registry"
description: "registry for registering and maintaining information about business entities"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/Registry.md", provenance: fibo}
  - {type: comprises, target: "/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistryEntry.md", provenance: fibo}
  - {type: is-managed-by, target: "/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority.md", provenance: fibo}
---

registry for registering and maintaining information about business entities

### Relationships
- is-a: [Registry](/CMNS/RegistrationAuthorities/Registry.md)
- comprises: [BusinessRegistryEntry](/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistryEntry.md)
- is-managed-by: [BusinessRegistrationAuthority](/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority.md)
