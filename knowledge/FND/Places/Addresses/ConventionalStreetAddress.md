---
type: FIBO Class
title: "conventional street address"
description: "physical address that identifies a location on a street to which communications may be delivered"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
tags: [FND, Release]
detail: "Other unconventional addresses may include rural and highway route addresses, general delivery addresses, post office box addresses, private mail center addresses, and so forth."
relations:
  - {type: is-a, target: "/FND/Places/Addresses/PhysicalAddress.md", provenance: fibo}
  - {type: has-street-address, target: "/FND/Places/Addresses/StreetAddress.md", provenance: fibo}
---

physical address that identifies a location on a street to which communications may be delivered

### Relationships
- is-a: [PhysicalAddress](/FND/Places/Addresses/PhysicalAddress.md)
- has-street-address: [StreetAddress](/FND/Places/Addresses/StreetAddress.md)
