---
type: FIBO Class
title: "account statement"
description: "periodic summary of account activity for a given period of time"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountStatement
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/Documents/LegalDocument.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Documents/Record.md", provenance: fibo}
  - {type: applies-to-account, target: "/FBC/ProductsAndServices/ClientsAndAccounts/Account.md", provenance: fibo}
  - {type: has-ending-balance, target: "/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md", provenance: fibo}
  - {type: has-reporting-period, target: "/CMNS/DatesAndTimes/ExplicitDatePeriod.md", provenance: fibo}
  - {type: has-starting-balance, target: "/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md", provenance: fibo}
  - {type: records-transaction, target: "/FBC/ProductsAndServices/ClientsAndAccounts/IndividualTransaction.md", provenance: fibo}
---

periodic summary of account activity for a given period of time

### Relationships
- is-a: [LegalDocument](/CMNS/Documents/LegalDocument.md)
- is-a: [Record](/CMNS/Documents/Record.md)
- applies-to-account: [Account](/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)
- has-ending-balance: [Balance](/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md)
- has-reporting-period: [ExplicitDatePeriod](/CMNS/DatesAndTimes/ExplicitDatePeriod.md)
- has-starting-balance: [Balance](/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md)
- records-transaction: [IndividualTransaction](/FBC/ProductsAndServices/ClientsAndAccounts/IndividualTransaction.md)
