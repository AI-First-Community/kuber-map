---
type: FIBO Class
title: "board composition control"
description: "situation in which a voting shareholder, entity owner, or some other party in the case of a not-for-profit organization, appoints and/or nominates someone to the board of directors of an organization for some period of time"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardCompositionControl
tags: [BE, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
examples:
  - "Control through the right to appoint a majority of the board of directors."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/OwnershipAndControl/Control/Control.md", provenance: fibo}
  - {type: involves-controlled-thing, target: "/BE/OwnershipAndControl/Executives/BoardMember.md", provenance: fibo}
---

situation in which a voting shareholder, entity owner, or some other party in the case of a not-for-profit organization, appoints and/or nominates someone to the board of directors of an organization for some period of time

### Relationships
- is-a: [Control](/FND/OwnershipAndControl/Control/Control.md)
- involves-controlled-thing: [BoardMember](/BE/OwnershipAndControl/Executives/BoardMember.md)
