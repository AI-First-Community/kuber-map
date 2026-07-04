---
type: FIBO Class
title: "account-specific service agreement"
description: "service-agreement that is account-specific, applicable in cases where a client might hold multiple accounts with differing terms and conditions"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountSpecificServiceAgreement
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/ProductsAndServices/ProductsAndServices/ServiceAgreement.md", provenance: fibo}
  - {type: applies-to, target: "/FBC/ProductsAndServices/ClientsAndAccounts/Account.md", provenance: fibo}
  - {type: has-contract-party, target: "/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder.md", provenance: fibo}
  - {type: has-contract-party, target: "/FBC/ProductsAndServices/ClientsAndAccounts/AccountProvider.md", provenance: fibo}
---

service-agreement that is account-specific, applicable in cases where a client might hold multiple accounts with differing terms and conditions

### Relationships
- is-a: [ServiceAgreement](/FND/ProductsAndServices/ProductsAndServices/ServiceAgreement.md)
- applies-to: [Account](/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)
- has-contract-party: [AccountHolder](/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder.md)
- has-contract-party: [AccountProvider](/FBC/ProductsAndServices/ClientsAndAccounts/AccountProvider.md)
