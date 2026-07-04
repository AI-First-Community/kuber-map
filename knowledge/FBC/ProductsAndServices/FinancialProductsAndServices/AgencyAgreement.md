---
type: FIBO Class
title: "agency agreement"
description: "agreement that designates a party as a registered agent to represent and act on behalf of another party in some, typically legal, financial, or medical capacity"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/AgencyAgreement
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/WrittenContract.md", provenance: fibo}
  - {type: has-contract-party, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent.md", provenance: fibo}
---

agreement that designates a party as a registered agent to represent and act on behalf of another party in some, typically legal, financial, or medical capacity

### Relationships
- is-a: [WrittenContract](/FND/Agreements/Contracts/WrittenContract.md)
- has-contract-party: [RegisteredAgent](/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent.md)
