---
type: FIBO Class
title: "de facto controlling interest party"
description: "party that exercises some control over an entity other than via explicit, legal means"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/DeFactoControllingInterestParty
tags: [BE, Release]
relations:
  - {type: is-a, target: "/FND/OwnershipAndControl/Control/ControllingParty.md", provenance: fibo}
  - {type: is-controlling-party-in, target: "/FND/OwnershipAndControl/Control/DeFactoControl.md", provenance: fibo}
  - {type: nominates, target: "/BE/OwnershipAndControl/Executives/BoardMember.md", provenance: fibo}
---

party that exercises some control over an entity other than via explicit, legal means

### Relationships
- is-a: [ControllingParty](/FND/OwnershipAndControl/Control/ControllingParty.md)
- is-controlling-party-in: [DeFactoControl](/FND/OwnershipAndControl/Control/DeFactoControl.md)
- nominates: [BoardMember](/BE/OwnershipAndControl/Executives/BoardMember.md)
