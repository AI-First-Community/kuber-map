---
type: FIBO Class
title: "cardholder"
description: "account holder to whom a payment card is issued"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/Cardholder
tags: [LOAN, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccountHolder.md", provenance: fibo}
  - {type: holds, target: "/LOAN/LoansSpecific/CardAccounts/CardAccount.md", provenance: fibo}
---

account holder to whom a payment card is issued

### Relationships
- is-a: [CustomerAccountHolder](/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccountHolder.md)
- holds: [CardAccount](/LOAN/LoansSpecific/CardAccounts/CardAccount.md)
