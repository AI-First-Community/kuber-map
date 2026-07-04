---
type: FIBO Class
title: "business registry entry"
description: "entry in a business registry"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistryEntry
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegistryEntry.md", provenance: fibo}
  - {type: comprises, target: "/BE/LegalEntities/CorporateBodies/RegistrationIdentifier.md", provenance: fibo}
  - {type: has-registration-date, target: "/CMNS/DatesAndTimes/CombinedDateTime.md", provenance: fibo}
  - {type: has-registration-status, target: "/FBC/FunctionalEntities/BusinessRegistries/RegistrationStatus.md", provenance: fibo}
---

entry in a business registry

### Relationships
- is-a: [RegistryEntry](/CMNS/RegistrationAuthorities/RegistryEntry.md)
- comprises: [RegistrationIdentifier](/BE/LegalEntities/CorporateBodies/RegistrationIdentifier.md)
- has-registration-date: [CombinedDateTime](/CMNS/DatesAndTimes/CombinedDateTime.md)
- has-registration-status: [RegistrationStatus](/FBC/FunctionalEntities/BusinessRegistries/RegistrationStatus.md)
