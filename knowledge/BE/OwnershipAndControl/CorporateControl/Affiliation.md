---
type: FIBO Class
title: "affiliation"
description: "situation in which a controlled party is affiliated with a controlling party for some period of time"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/Affiliation
tags: [BE, Release]
relations:
  - {type: is-a, target: "/FND/OwnershipAndControl/Control/Control.md", provenance: fibo}
  - {type: has-actor, target: "/BE/OwnershipAndControl/CorporateControl/ControllingAffiliate.md", provenance: fibo}
  - {type: has-undergoer, target: "/BE/OwnershipAndControl/CorporateControl/ControlledAffiliate.md", provenance: fibo}
---

situation in which a controlled party is affiliated with a controlling party for some period of time

### Relationships
- is-a: [Control](/FND/OwnershipAndControl/Control/Control.md)
- has-actor: [ControllingAffiliate](/BE/OwnershipAndControl/CorporateControl/ControllingAffiliate.md)
- has-undergoer: [ControlledAffiliate](/BE/OwnershipAndControl/CorporateControl/ControlledAffiliate.md)
