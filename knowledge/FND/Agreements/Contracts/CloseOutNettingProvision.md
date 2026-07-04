---
type: FIBO Class
title: "close-out netting provision"
description: "netting provision that may be triggered when a counterparty defaults, leading to the termination of all outstanding transactions between the parties"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/CloseOutNettingProvision
tags: [FND, Release]
detail: "In the case of close-out netting, the financial positions of the defaulting party are assessed to determine their worth, and total amounts owed are offset, resulting in a single net payment obligation."
synonyms:
  - "close out netting provision"
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/NettingProvision.md", provenance: fibo}
---

netting provision that may be triggered when a counterparty defaults, leading to the termination of all outstanding transactions between the parties

### Relationships
- is-a: [NettingProvision](/FND/Agreements/Contracts/NettingProvision.md)
