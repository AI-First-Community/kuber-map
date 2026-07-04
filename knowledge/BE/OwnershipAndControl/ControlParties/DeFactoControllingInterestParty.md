---
type: FIBO Class
title: "de facto controlling interest party"
description: "party that exercises some control over an entity other than via explicit, legal means"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/DeFactoControllingInterestParty
tags: [BE, Release]
core: true
detail: "A control owner (i.e., control person, per SEC regulations) may have some means or right that allows them to exercise control over board composition, other than through proxy assignment or vote. Not all control persons have this facility, as it is not inherent to having a significant (for example, 20 percent or more) ownership stake."
examples:
  - "a silent partner, i.e. where someone has made a large investment, which is bilateral (not part of the constitutional framework of the company)"
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
