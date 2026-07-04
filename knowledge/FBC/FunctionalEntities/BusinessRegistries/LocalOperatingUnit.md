---
type: FIBO Class
title: "local operating unit"
description: "registrar that is authorized by the Global LEI Foundation to issue legal entity identifiers"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LocalOperatingUnit
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/Registrar.md", provenance: fibo}
  - {type: issues, target: "/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md", provenance: fibo}
  - {type: registers, target: "/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md", provenance: fibo}
---

registrar that is authorized by the Global LEI Foundation to issue legal entity identifiers

### Relationships
- is-a: [Registrar](/CMNS/RegistrationAuthorities/Registrar.md)
- issues: [LegalEntityIdentifier](/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md)
- registers: [LegalEntityIdentifier](/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md)
