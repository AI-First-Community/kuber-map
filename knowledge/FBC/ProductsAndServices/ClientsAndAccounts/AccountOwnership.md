---
type: FIBO Class
title: "account ownership"
description: "holding of an account"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountOwnership
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Holding.md", provenance: fibo}
  - {type: has-owned-asset, target: "/FBC/ProductsAndServices/ClientsAndAccounts/AccountAsAnAsset.md", provenance: fibo}
  - {type: has-owning-party, target: "/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder.md", provenance: fibo}
---

holding of an account

### Relationships
- is-a: [Holding](/FBC/ProductsAndServices/FinancialProductsAndServices/Holding.md)
- has-owned-asset: [AccountAsAnAsset](/FBC/ProductsAndServices/ClientsAndAccounts/AccountAsAnAsset.md)
- has-owning-party: [AccountHolder](/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder.md)
