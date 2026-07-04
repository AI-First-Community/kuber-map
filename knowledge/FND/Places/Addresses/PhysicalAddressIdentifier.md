---
type: FIBO Class
title: "physical address identifier"
description: "unique identifier for a physical address"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddressIdentifier
tags: [FND, Release]
relations:
  - {type: is-a, target: "/CMNS/CodesAndCodeSets/CodeElement.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
  - {type: identifies, target: "/FND/Places/Addresses/PhysicalAddress.md", provenance: fibo}
  - {type: is-member-of, target: "/FND/Places/Addresses/PhysicalAddressingScheme.md", provenance: fibo}
---

unique identifier for a physical address

### Relationships
- is-a: [CodeElement](/CMNS/CodesAndCodeSets/CodeElement.md)
- is-a: [Identifier](/CMNS/Identifiers/Identifier.md)
- identifies: [PhysicalAddress](/FND/Places/Addresses/PhysicalAddress.md)
- is-member-of: [PhysicalAddressingScheme](/FND/Places/Addresses/PhysicalAddressingScheme.md)
