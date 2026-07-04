---
type: FIBO Class
title: "obligor"
description: "party that is bound legally or by agreement to repay a debt, make a payment, do something, or refrain from doing something"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Obligor
tags: [FND, Release]
synonyms:
  - "obligated party"
  - "obligator"
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/PartyRole.md", provenance: fibo}
  - {type: has-obligation, target: "/FND/Agreements/Agreements/Commitment.md", provenance: fibo}
---

party that is bound legally or by agreement to repay a debt, make a payment, do something, or refrain from doing something

### Relationships
- is-a: [PartyRole](/CMNS/PartiesAndSituations/PartyRole.md)
- has-obligation: [Commitment](/FND/Agreements/Agreements/Commitment.md)
