---
type: FIBO Class
title: "business register identifier"
description: "identifier that uniquely identifies a business register, such as a register identified by the Global Legal Entity Identifier Foundation (GLEIF) registration authorities list"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegisterIdentifier
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
  - {type: identifies, target: "/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry.md", provenance: fibo}
  - {type: is-registered-by, target: "/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority.md", provenance: fibo}
---

identifier that uniquely identifies a business register, such as a register identified by the Global Legal Entity Identifier Foundation (GLEIF) registration authorities list

### Relationships
- is-a: [Identifier](/CMNS/Identifiers/Identifier.md)
- identifies: [BusinessRegistry](/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry.md)
- is-registered-by: [BusinessRegistrationAuthority](/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority.md)
