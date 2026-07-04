---
type: FIBO Class
title: "controlled thing"
description: "something over which some party exercises some form of control with respect to some situation"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControlledThing
tags: [FND, Release]
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Undergoer.md", provenance: fibo}
  - {type: has-controlling-party, target: "/FND/OwnershipAndControl/Control/ControllingParty.md", provenance: fibo}
  - {type: is-controlled-thing-in, target: "/FND/OwnershipAndControl/Control/Control.md", provenance: fibo}
---

something over which some party exercises some form of control with respect to some situation

### Relationships
- is-a: [Undergoer](/CMNS/PartiesAndSituations/Undergoer.md)
- has-controlling-party: [ControllingParty](/FND/OwnershipAndControl/Control/ControllingParty.md)
- is-controlled-thing-in: [Control](/FND/OwnershipAndControl/Control/Control.md)
