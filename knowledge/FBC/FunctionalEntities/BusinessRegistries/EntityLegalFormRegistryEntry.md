---
type: FIBO Class
title: "entity legal form registry entry"
description: "entry in an entity legal form registry that conforms to ISO 20275"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/EntityLegalFormRegistryEntry
tags: [FBC, Release]
synonyms:
  - "ELF registry entry"
relations:
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegistryEntry.md", provenance: fibo}
  - {type: comprises, target: "/BE/LegalEntities/LEIEntities/EntityLegalFormIdentifier.md", provenance: fibo}
---

entry in an entity legal form registry that conforms to ISO 20275

### Relationships
- is-a: [RegistryEntry](/CMNS/RegistrationAuthorities/RegistryEntry.md)
- comprises: [EntityLegalFormIdentifier](/BE/LegalEntities/LEIEntities/EntityLegalFormIdentifier.md)
