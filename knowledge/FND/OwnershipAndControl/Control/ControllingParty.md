---
type: FIBO Class
title: "controlling party"
description: "actor that exercises some form of control in the context of some situation"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControllingParty
tags: [FND, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Actor.md", provenance: fibo}
  - {type: is-controlling-party-in, target: "/FND/OwnershipAndControl/Control/Control.md", provenance: fibo}
  - {type: is-party-controlling, target: "/FND/OwnershipAndControl/Control/ControlledThing.md", provenance: fibo}
---

actor that exercises some form of control in the context of some situation

### Relationships
- is-a: [Actor](/CMNS/PartiesAndSituations/Actor.md)
- is-controlling-party-in: [Control](/FND/OwnershipAndControl/Control/Control.md)
- is-party-controlling: [ControlledThing](/FND/OwnershipAndControl/Control/ControlledThing.md)
