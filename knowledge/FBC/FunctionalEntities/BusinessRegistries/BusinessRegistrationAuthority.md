---
type: FIBO Class
title: "business registration authority"
description: "registration authority that is responsible for maintaining a registry of business entities"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/Registrar.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegistrationAuthority.md", provenance: fibo}
  - {type: manages, target: "/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry.md", provenance: fibo}
  - {type: registers, target: "/BE/LegalEntities/CorporateBodies/RegistrationIdentifier.md", provenance: fibo}
---

registration authority that is responsible for maintaining a registry of business entities

### Relationships
- is-a: [Registrar](/CMNS/RegistrationAuthorities/Registrar.md)
- is-a: [RegistrationAuthority](/CMNS/RegistrationAuthorities/RegistrationAuthority.md)
- manages: [BusinessRegistry](/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry.md)
- registers: [RegistrationIdentifier](/BE/LegalEntities/CorporateBodies/RegistrationIdentifier.md)
