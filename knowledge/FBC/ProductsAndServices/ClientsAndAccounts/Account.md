---
type: FIBO Class
title: "account"
description: "container for records associated with a business arrangement for regular transactions and services"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/Account
tags: [FBC, Release]
detail: "In general, an account is associated with a contractual relationship between a buyer and seller under which payment may be made at a later time. General ledger accounts are an exception to this, however, and typically do not have account holders, including internal account holders. They may, on the other hand, have responsible parties."
relations:
  - {type: has-balance, target: "/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md", provenance: fibo}
  - {type: has-close-date, target: "/FBC/ProductsAndServices/ClientsAndAccounts/CloseDate.md", provenance: fibo}
  - {type: has-open-date, target: "/FBC/ProductsAndServices/ClientsAndAccounts/OpenDate.md", provenance: fibo}
  - {type: has-record, target: "/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord.md", provenance: fibo}
  - {type: is-held-by, target: "/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder.md", provenance: fibo}
  - {type: is-identified-by, target: "/FBC/ProductsAndServices/ClientsAndAccounts/AccountIdentifier.md", provenance: fibo}
  - {type: is-provided-by, target: "/FBC/ProductsAndServices/ClientsAndAccounts/AccountProvider.md", provenance: fibo}
---

container for records associated with a business arrangement for regular transactions and services

### Relationships
- has-balance: [Balance](/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md)
- has-close-date: [CloseDate](/FBC/ProductsAndServices/ClientsAndAccounts/CloseDate.md)
- has-open-date: [OpenDate](/FBC/ProductsAndServices/ClientsAndAccounts/OpenDate.md)
- has-record: [TransactionRecord](/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord.md)
- is-held-by: [AccountHolder](/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder.md)
- is-identified-by: [AccountIdentifier](/FBC/ProductsAndServices/ClientsAndAccounts/AccountIdentifier.md)
- is-provided-by: [AccountProvider](/FBC/ProductsAndServices/ClientsAndAccounts/AccountProvider.md)
