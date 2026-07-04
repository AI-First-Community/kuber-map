---
type: FIBO Class
title: "business registration authority"
description: "registration authority that is responsible for maintaining a registry of business entities"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority
tags: [FBC, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
  - "Regulatory Reporting & Compliance (supervisory filing)"
detail: "A business registry may include any government-managed registry for registering a business, such as a state department of corporations in the US, as well as other registries such as a local operating unit (LOU) for registration of legal entity identifiers (LEIs). Any sanctioned registration authority as defined by the Registration Authorities List, published by GLEIF, is a business registration authority in this sense."
examples:
  - "A companies registry such as the UK Companies House."
examples_provenance: curated
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
