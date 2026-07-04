---
type: FIBO Class
title: "LEI registered entity"
description: "a legal person that has registered for and is identified by a legal entity identifier"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LEIRegisteredEntity
tags: [BE, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
detail: "Note that the GLEIF data includes multiple LEIs for some entities due to corporate actions or other situations. The duplicates are typically archived after some period of time, but in order to reflect the reality in the data, the restriction is modeled as someValuesFrom rather than exactly 1 LEI for a given entity."
examples:
  - "A fund that has obtained a Legal Entity Identifier in order to trade derivatives."
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/Organizations/LegalPerson.md", provenance: fibo}
---

a legal person that has registered for and is identified by a legal entity identifier

### Relationships
- is-a: [LegalPerson](/CMNS/Organizations/LegalPerson.md)
