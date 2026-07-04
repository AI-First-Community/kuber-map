---
type: FIBO Class
title: "transaction record"
description: "record of transactions associated with an account"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord
tags: [FBC, Release]
detail: "The date a particular transaction record is closed typically corresponds to (and may precede) the date the account is closed, though in the case of certain accounts, such as a credit card account, if a customer is issued a new account or card number due to loss, fraud, or for some other reason, it is possible that multiple transaction records would be associated with the account. In that case, the close date might correspond to the date that a hold was placed on the original account."
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Documents/Record.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/Registry.md", provenance: fibo}
  - {type: applies-to-account, target: "/FBC/ProductsAndServices/ClientsAndAccounts/Account.md", provenance: fibo}
  - {type: comprises, target: "/FBC/ProductsAndServices/ClientsAndAccounts/IndividualTransaction.md", provenance: fibo}
  - {type: has-close-date, target: "/FBC/ProductsAndServices/ClientsAndAccounts/CloseDate.md", provenance: fibo}
  - {type: has-open-date, target: "/FBC/ProductsAndServices/ClientsAndAccounts/OpenDate.md", provenance: fibo}
  - {type: is-identified-by, target: "/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecordIdentifier.md", provenance: fibo}
  - {type: is-managed-by, target: "/FBC/ProductsAndServices/ClientsAndAccounts/AccountProvider.md", provenance: fibo}
---

record of transactions associated with an account

### Relationships
- is-a: [DatedStructuredCollection](/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
- is-a: [Record](/CMNS/Documents/Record.md)
- is-a: [Registry](/CMNS/RegistrationAuthorities/Registry.md)
- applies-to-account: [Account](/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)
- comprises: [IndividualTransaction](/FBC/ProductsAndServices/ClientsAndAccounts/IndividualTransaction.md)
- has-close-date: [CloseDate](/FBC/ProductsAndServices/ClientsAndAccounts/CloseDate.md)
- has-open-date: [OpenDate](/FBC/ProductsAndServices/ClientsAndAccounts/OpenDate.md)
- is-identified-by: [TransactionRecordIdentifier](/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecordIdentifier.md)
- is-managed-by: [AccountProvider](/FBC/ProductsAndServices/ClientsAndAccounts/AccountProvider.md)
