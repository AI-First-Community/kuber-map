---
type: FIBO Class
title: "chartered legal person"
description: "a legal person created by a royal charter or decree"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/CharteredLegalPerson
tags: [BE, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
detail: "In a monarchy or principality, the monarch typically vests the power to create such bodies, in an entity called (for example) the Privy Council."
examples:
  - "Anything with 'Royal Institute' in the name. Also universities are generally set up by royal charter in a monarchy or principality, (often pre-dating any Privy Council i.e. directly be the monarch in the case of older universities). The Bank of England and the British Broadcasting Council (BBC) are also incorporated through Royal Charter."
relations:
  - {type: is-a, target: "/CMNS/Organizations/LegalEntity.md", provenance: fibo}
---

a legal person created by a royal charter or decree

### Relationships
- is-a: [LegalEntity](/CMNS/Organizations/LegalEntity.md)
