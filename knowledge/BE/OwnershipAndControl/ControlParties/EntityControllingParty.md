---
type: FIBO Class
title: "entity controlling party"
description: "party that has the authority to control some legal entity"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/EntityControllingParty
tags: [BE, Release]
core: true
relations:
  - {type: is-a, target: "/FND/OwnershipAndControl/Control/ControllingParty.md", provenance: fibo}
  - {type: is-controlling-party-of, target: "/CMNS/Organizations/LegalEntity.md", provenance: fibo}
---

party that has the authority to control some legal entity

### Relationships
- is-a: [ControllingParty](/FND/OwnershipAndControl/Control/ControllingParty.md)
- is-controlling-party-of: [LegalEntity](/CMNS/Organizations/LegalEntity.md)
