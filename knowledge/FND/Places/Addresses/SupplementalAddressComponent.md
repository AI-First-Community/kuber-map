---
type: FIBO Class
title: "supplemental address component"
description: "address component that provides additional information that is important to ensuring proper delivery of communications"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SupplementalAddressComponent
tags: [FND, Release]
detail: "Supplemental components include post office box information, rural route and highway contract route information, private mailboxes, and so forth, that are not part of a conventional street address."
relations:
  - {type: is-a, target: "/FND/Places/Addresses/AddressComponent.md", provenance: fibo}
  - {type: comprises, target: "/FND/Places/Addresses/SupplementalAddressDesignator.md", provenance: fibo}
  - {type: comprises, target: "/FND/Places/Addresses/SupplementalAddressUnit.md", provenance: fibo}
---

address component that provides additional information that is important to ensuring proper delivery of communications

### Relationships
- is-a: [AddressComponent](/FND/Places/Addresses/AddressComponent.md)
- comprises: [SupplementalAddressDesignator](/FND/Places/Addresses/SupplementalAddressDesignator.md)
- comprises: [SupplementalAddressUnit](/FND/Places/Addresses/SupplementalAddressUnit.md)
