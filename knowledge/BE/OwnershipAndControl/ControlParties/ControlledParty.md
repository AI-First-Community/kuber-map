---
type: FIBO Class
title: "controlled party"
description: "person or organization over which some party exercises some form of authority or influence with respect to some situation"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/ControlledParty
tags: [BE, Release]
core: true
relations:
  - {type: is-a, target: "/FND/OwnershipAndControl/Control/ControlledThing.md", provenance: fibo}
  - {type: is-played-by, target: "/CMNS/PartiesAndSituations/Party.md", provenance: fibo}
---

person or organization over which some party exercises some form of authority or influence with respect to some situation

### Relationships
- is-a: [ControlledThing](/FND/OwnershipAndControl/Control/ControlledThing.md)
- is-played-by: [Party](/CMNS/PartiesAndSituations/Party.md)
