---
type: FIBO Class
title: "customer account holder"
description: "party that owns a customer account"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccountHolder
tags: [FBC, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder.md", provenance: fibo}
  - {type: holds, target: "/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md", provenance: fibo}
---

party that owns a customer account

### Relationships
- is-a: [AccountHolder](/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder.md)
- holds: [CustomerAccount](/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md)
