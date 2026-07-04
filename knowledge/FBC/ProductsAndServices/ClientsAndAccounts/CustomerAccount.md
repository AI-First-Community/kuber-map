---
type: FIBO Class
title: "customer account"
description: "account that represents an identified, named collection of balances and cumulative totals used to summarize customer transaction-related activity over a designated period of time"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/ClientsAndAccounts/Account.md", provenance: fibo}
  - {type: is-defined-in, target: "/FND/ProductsAndServices/ProductsAndServices/ServiceAgreement.md", provenance: fibo}
  - {type: is-held-by, target: "/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccountHolder.md", provenance: fibo}
  - {type: is-identified-by, target: "/FBC/ProductsAndServices/ClientsAndAccounts/AccountIdentifier.md", provenance: fibo}
---

account that represents an identified, named collection of balances and cumulative totals used to summarize customer transaction-related activity over a designated period of time

### Relationships
- is-a: [Account](/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)
- is-defined-in: [ServiceAgreement](/FND/ProductsAndServices/ProductsAndServices/ServiceAgreement.md)
- is-held-by: [CustomerAccountHolder](/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccountHolder.md)
- is-identified-by: [AccountIdentifier](/FBC/ProductsAndServices/ClientsAndAccounts/AccountIdentifier.md)
