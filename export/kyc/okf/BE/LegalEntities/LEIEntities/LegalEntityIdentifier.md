---
type: FIBO Class
title: "legal entity identifier"
description: "an organization identifier that uniquely identifies a legal person as defined in ISO 17442"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifier
tags: [BE, Release]
relations:
  - {type: is-a, target: "/CMNS/Organizations/OrganizationIdentifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegisteredIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/CMNS/Organizations/LegalPerson.md", provenance: fibo}
  - {type: is-defined-in, target: "/BE/LegalEntities/LEIEntities/LegalEntityIdentifierScheme.md", provenance: fibo}
---

an organization identifier that uniquely identifies a legal person as defined in ISO 17442

### Relationships
- is-a: [OrganizationIdentifier](/CMNS/Organizations/OrganizationIdentifier.md)
- is-a: [RegisteredIdentifier](/CMNS/RegistrationAuthorities/RegisteredIdentifier.md)
- identifies: [LegalPerson](/CMNS/Organizations/LegalPerson.md)
- is-defined-in: [LegalEntityIdentifierScheme](/BE/LegalEntities/LEIEntities/LegalEntityIdentifierScheme.md)
