---
type: FIBO Class
title: "legal entity identifier scheme"
description: "a scheme that specifies the elements of an unambiguous legal entity identifier (LEI) scheme to identify the legal entities relevant to any financial transaction"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifierScheme
tags: [BE, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
examples:
  - "The Global LEI System, operated under GLEIF."
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/Organizations/OrganizationIdentificationScheme.md", provenance: fibo}
  - {type: defines, target: "/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md", provenance: fibo}
---

a scheme that specifies the elements of an unambiguous legal entity identifier (LEI) scheme to identify the legal entities relevant to any financial transaction

### Relationships
- is-a: [OrganizationIdentificationScheme](/CMNS/Organizations/OrganizationIdentificationScheme.md)
- defines: [LegalEntityIdentifier](/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md)
