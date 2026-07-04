---
type: FIBO Class
title: "majority controlling party"
description: "controlling party that possesses, either directly or indirectly, the power to direct or cause the direction of the management and policies of a legal person, whether through the ownership of a majority of voting securities, by contract, or otherwise"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/MajorityControllingParty
tags: [BE, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
examples:
  - "A shareholder holding 55% of the voting rights."
examples_provenance: curated
relations:
  - {type: is-a, target: "/BE/OwnershipAndControl/ControlParties/EntityControllingParty.md", provenance: fibo}
---

controlling party that possesses, either directly or indirectly, the power to direct or cause the direction of the management and policies of a legal person, whether through the ownership of a majority of voting securities, by contract, or otherwise

### Relationships
- is-a: [EntityControllingParty](/BE/OwnershipAndControl/ControlParties/EntityControllingParty.md)
