---
type: FIBO Class
title: "customer identifier"
description: "sequence of characters uniquely identifying a customer within the context of some organization"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/CustomerIdentifier
tags: [FND, Release]
core: true
relations:
  - {type: is-a, target: "/FND/Parties/Parties/PartyRoleIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/FND/ProductsAndServices/ProductsAndServices/Customer.md", provenance: fibo}
---

sequence of characters uniquely identifying a customer within the context of some organization

### Relationships
- is-a: [PartyRoleIdentifier](/FND/Parties/Parties/PartyRoleIdentifier.md)
- identifies: [Customer](/FND/ProductsAndServices/ProductsAndServices/Customer.md)
