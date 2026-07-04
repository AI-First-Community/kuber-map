---
type: FIBO Class
title: "client identifier"
description: "sequence of characters uniquely identifying a client within the context of some organization"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/ClientIdentifier
tags: [FND, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
examples:
  - "A reference code identifying a client in an adviser's records."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Parties/Parties/PartyRoleIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/FND/ProductsAndServices/ProductsAndServices/Client.md", provenance: fibo}
---

sequence of characters uniquely identifying a client within the context of some organization

### Relationships
- is-a: [PartyRoleIdentifier](/FND/Parties/Parties/PartyRoleIdentifier.md)
- identifies: [Client](/FND/ProductsAndServices/ProductsAndServices/Client.md)
