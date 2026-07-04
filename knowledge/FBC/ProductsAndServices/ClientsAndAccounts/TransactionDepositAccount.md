---
type: FIBO Class
title: "transaction deposit account"
description: "deposit account from which the depositor / account holder is permitted to make transfers or withdrawals by negotiable / transferable instruments, payment orders of withdrawal, telephone transfers, and so forth, and that may be accessible via an electronic device such as an automated teller machine (ATM), remote service unit (RSU), mobile device, and by debit card"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDepositAccount
tags: [FBC, Release]
detail: "Excluded from transaction accounts are savings deposits (both money market deposit accounts (MMDAs) and other savings deposits), even though such deposits permit some third-party transfers. However, an account that otherwise meets the definition of a savings deposit but that authorizes or permits the depositor to exceed the transfer limitations specified for that account shall be reported as a transaction account."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/ClientsAndAccounts/DepositAccount.md", provenance: fibo}
---

deposit account from which the depositor / account holder is permitted to make transfers or withdrawals by negotiable / transferable instruments, payment orders of withdrawal, telephone transfers, and so forth, and that may be accessible via an electronic device such as an automated teller machine (ATM), remote service unit (RSU), mobile device, and by debit card

### Relationships
- is-a: [DepositAccount](/FBC/ProductsAndServices/ClientsAndAccounts/DepositAccount.md)
