---
type: FIBO Class
title: "relationship manager"
description: "responsible party who manages a client's account and oversees their relationship with the service provider"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/RelationshipManager
tags: [FBC, Release]
synonyms:
  - "account manager"
relations:
  - {type: is-a, target: "/CMNS/BusinessAuthorizations/ResponsibleParty.md", provenance: fibo}
  - {type: manages, target: "/FBC/ProductsAndServices/ClientsAndAccounts/Account.md", provenance: fibo}
---

responsible party who manages a client's account and oversees their relationship with the service provider

### Relationships
- is-a: [ResponsibleParty](/CMNS/BusinessAuthorizations/ResponsibleParty.md)
- manages: [Account](/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)
