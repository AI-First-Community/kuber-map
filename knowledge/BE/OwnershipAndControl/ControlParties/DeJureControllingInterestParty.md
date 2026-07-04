---
type: FIBO Class
title: "de jure controlling interest party"
description: "party that has the legal authority to exercise control"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty
tags: [BE, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
examples:
  - "A shareholder with a legal majority of the voting rights."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/OwnershipAndControl/Control/ControllingParty.md", provenance: fibo}
  - {type: is-controlling-party-in, target: "/FND/OwnershipAndControl/Control/DeJureControl.md", provenance: fibo}
---

party that has the legal authority to exercise control

### Relationships
- is-a: [ControllingParty](/FND/OwnershipAndControl/Control/ControllingParty.md)
- is-controlling-party-in: [DeJureControl](/FND/OwnershipAndControl/Control/DeJureControl.md)
