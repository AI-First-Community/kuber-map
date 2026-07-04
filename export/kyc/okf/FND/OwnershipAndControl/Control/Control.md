---
type: FIBO Class
title: "control"
description: "situation in which some party has the power to direct or strongly influence the direction of the management and policies related to something"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/Control
tags: [FND, Release]
detail: "Control may be direct (explicit) or indirect (implicit), derived through ownership of voting shares, beneficial ownership, other ownership relations, through provisions of a contract, or otherwise."
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Situation.md", provenance: fibo}
  - {type: has-party-in-control, target: "/FND/OwnershipAndControl/Control/ControllingParty.md", provenance: fibo}
  - {type: involves-controlled-thing, target: "/FND/OwnershipAndControl/Control/ControlledThing.md", provenance: fibo}
---

situation in which some party has the power to direct or strongly influence the direction of the management and policies related to something

### Relationships
- is-a: [Situation](/CMNS/PartiesAndSituations/Situation.md)
- has-party-in-control: [ControllingParty](/FND/OwnershipAndControl/Control/ControllingParty.md)
- involves-controlled-thing: [ControlledThing](/FND/OwnershipAndControl/Control/ControlledThing.md)
