---
type: FIBO Class
title: "institutional unit"
description: "party that is capable, in its own right, of owning assets, incurring liabilities, and engaging in economic activities and in transactions with other parties"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/InstitutionalUnit
tags: [IND, Release]
detail: "There is a hierarchical relationship between institutional units and establishments. An institutional unit contains one or more entire establishment(s); an establishment belongs to one and only one institutional unit. There are two main types of units in the real world that may qualify as institutional units, namely persons or groups of persons in the form of households, and legal or social entities."
relations:
  - {type: is-a, target: "/BE/FunctionalEntities/FunctionalEntities/FunctionalEntity.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/PartiesAndSituations/PartyRole.md", provenance: fibo}
---

party that is capable, in its own right, of owning assets, incurring liabilities, and engaging in economic activities and in transactions with other parties

### Relationships
- is-a: [FunctionalEntity](/BE/FunctionalEntities/FunctionalEntities/FunctionalEntity.md)
- is-a: [PartyRole](/CMNS/PartiesAndSituations/PartyRole.md)
