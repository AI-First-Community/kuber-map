---
type: FIBO Class
title: "housing unit"
description: "house, an apartment, a mobile home or trailer, a group of rooms, or a single room occupied as separate living quarters, or if vacant, intended for occupancy as separate living quarters"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/HousingUnit
tags: [IND, Release]
detail: "Separate living quarters are those in which the occupants live separately from any other individuals in the building and which have direct access from outside the building or through a common hall. For vacant units, the criteria of separateness and direct access are applied to the intended occupants whenever possible."
relations:
  - {type: is-a, target: "/CMNS/Locations/PhysicalLocation.md", provenance: fibo}
  - {type: has-address, target: "/FND/Places/Addresses/PhysicalAddress.md", provenance: fibo}
---

house, an apartment, a mobile home or trailer, a group of rooms, or a single room occupied as separate living quarters, or if vacant, intended for occupancy as separate living quarters

### Relationships
- is-a: [PhysicalLocation](/CMNS/Locations/PhysicalLocation.md)
- has-address: [PhysicalAddress](/FND/Places/Addresses/PhysicalAddress.md)
