---
type: FIBO Class
title: "de jure control"
description: "control that exists as a matter of law, i.e., legitimate, legal control of something"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/DeJureControl
tags: [FND, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
examples:
  - "Control by legal right, e.g. holding more than 50% of the voting shares."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Law/LegalCapacity/LegalConstruct.md", provenance: fibo}
  - {type: is-a, target: "/FND/OwnershipAndControl/Control/Control.md", provenance: fibo}
---

control that exists as a matter of law, i.e., legitimate, legal control of something

### Relationships
- is-a: [LegalConstruct](/FND/Law/LegalCapacity/LegalConstruct.md)
- is-a: [Control](/FND/OwnershipAndControl/Control/Control.md)
