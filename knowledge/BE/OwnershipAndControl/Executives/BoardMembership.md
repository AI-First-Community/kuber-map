---
type: FIBO Class
title: "board membership"
description: "situation relating an individual member of the board of directors to the organization"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardMembership
tags: [BE, Release]
relations:
  - {type: is-a, target: "/FND/OwnershipAndControl/Control/Control.md", provenance: fibo}
  - {type: has-party-in-control, target: "/BE/OwnershipAndControl/Executives/BoardMember.md", provenance: fibo}
  - {type: involves-controlled-thing, target: "/BE/OwnershipAndControl/ControlParties/ControlledParty.md", provenance: fibo}
---

situation relating an individual member of the board of directors to the organization

### Relationships
- is-a: [Control](/FND/OwnershipAndControl/Control/Control.md)
- has-party-in-control: [BoardMember](/BE/OwnershipAndControl/Executives/BoardMember.md)
- involves-controlled-thing: [ControlledParty](/BE/OwnershipAndControl/ControlParties/ControlledParty.md)
