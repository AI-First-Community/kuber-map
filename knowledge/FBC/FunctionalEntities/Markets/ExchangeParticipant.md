---
type: FIBO Class
title: "exchange participant"
description: "registered agent who, in accordance with the rules of an exchange, may trade on or through the exchange and whose name is entered in a list, register or roll kept by the exchange as an agent who may trade on or through the exchange"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/ExchangeParticipant
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Organizations/OrganizationMember.md", provenance: fibo}
  - {type: is-registered-by, target: "/FBC/FunctionalEntities/Markets/Exchange.md", provenance: fibo}
---

registered agent who, in accordance with the rules of an exchange, may trade on or through the exchange and whose name is entered in a list, register or roll kept by the exchange as an agent who may trade on or through the exchange

### Relationships
- is-a: [RegisteredAgent](/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent.md)
- is-a: [OrganizationMember](/CMNS/Organizations/OrganizationMember.md)
- is-registered-by: [Exchange](/FBC/FunctionalEntities/Markets/Exchange.md)
