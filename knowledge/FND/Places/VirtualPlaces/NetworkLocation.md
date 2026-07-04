---
type: FIBO Class
title: "network location"
description: "a virtual location that may be identified by a network address (an identifier for a node or interface)"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/VirtualPlaces/NetworkLocation
tags: [FND, Release]
relations:
  - {type: is-a, target: "/CMNS/Locations/VirtualLocation.md", provenance: fibo}
  - {type: is-identified-by, target: "/FND/Places/Addresses/Address.md", provenance: fibo}
---

a virtual location that may be identified by a network address (an identifier for a node or interface)

### Relationships
- is-a: [VirtualLocation](/CMNS/Locations/VirtualLocation.md)
- is-identified-by: [Address](/FND/Places/Addresses/Address.md)
