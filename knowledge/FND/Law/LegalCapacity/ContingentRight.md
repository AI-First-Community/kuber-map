---
type: FIBO Class
title: "contingent right"
description: "right that depends on a future event or the performance of an action"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContingentRight
tags: [FND, Release]
detail: "Contingent means that the interest, claim, or right is conditional, realized only when and if something occurs."
relations:
  - {type: is-a, target: "/FND/Law/LegalCapacity/Right.md", provenance: fibo}
  - {type: implies, target: "/FND/Law/LegalCapacity/ContingentObligation.md", provenance: fibo}
  - {type: is-conferred-on, target: "/CMNS/PartiesAndSituations/Party.md", provenance: fibo}
---

right that depends on a future event or the performance of an action

### Relationships
- is-a: [Right](/FND/Law/LegalCapacity/Right.md)
- implies: [ContingentObligation](/FND/Law/LegalCapacity/ContingentObligation.md)
- is-conferred-on: [Party](/CMNS/PartiesAndSituations/Party.md)
