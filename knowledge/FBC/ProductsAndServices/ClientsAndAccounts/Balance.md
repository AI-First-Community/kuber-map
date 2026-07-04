---
type: FIBO Class
title: "balance"
description: "amount of money available or owed"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Balance
tags: [FBC, Release]
detail: "The balance is the net amount after factoring in all debits and credits, including service charges and fees."
relations:
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

amount of money available or owed

### Relationships
- is-a: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
