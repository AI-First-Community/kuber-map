---
type: FIBO Class
title: "individual transaction"
description: "event that has a monetary impact and is documented in the records associated with an account"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/IndividualTransaction
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md", provenance: fibo}
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/Occurrence.md", provenance: fibo}
  - {type: applies-to-account, target: "/FBC/ProductsAndServices/ClientsAndAccounts/Account.md", provenance: fibo}
  - {type: exemplifies, target: "/FND/ProductsAndServices/ProductsAndServices/TransactionEvent.md", provenance: fibo}
  - {type: has-monetary-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-posting-date, target: "/FBC/ProductsAndServices/ClientsAndAccounts/PostingDate.md", provenance: fibo}
  - {type: has-transaction-date, target: "/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDate.md", provenance: fibo}
  - {type: involves-merchant, target: "/BE/FunctionalEntities/FunctionalEntities/Merchant.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/ProductsAndServices/ClientsAndAccounts/TransactionCategory.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/ProductsAndServices/ClientsAndAccounts/TransactionSubcategory.md", provenance: fibo}
  - {type: is-identified-by, target: "/FBC/ProductsAndServices/ClientsAndAccounts/TransactionIdentifier.md", provenance: fibo}
  - {type: is-registered-in, target: "/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord.md", provenance: fibo}
---

event that has a monetary impact and is documented in the records associated with an account

### Relationships
- is-a: [DatedCollectionConstituent](/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md)
- is-a: [Occurrence](/FND/DatesAndTimes/Occurrences/Occurrence.md)
- applies-to-account: [Account](/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)
- exemplifies: [TransactionEvent](/FND/ProductsAndServices/ProductsAndServices/TransactionEvent.md)
- has-monetary-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-posting-date: [PostingDate](/FBC/ProductsAndServices/ClientsAndAccounts/PostingDate.md)
- has-transaction-date: [TransactionDate](/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDate.md)
- involves-merchant: [Merchant](/BE/FunctionalEntities/FunctionalEntities/Merchant.md)
- is-classified-by: [TransactionCategory](/FBC/ProductsAndServices/ClientsAndAccounts/TransactionCategory.md)
- is-classified-by: [TransactionSubcategory](/FBC/ProductsAndServices/ClientsAndAccounts/TransactionSubcategory.md)
- is-identified-by: [TransactionIdentifier](/FBC/ProductsAndServices/ClientsAndAccounts/TransactionIdentifier.md)
- is-registered-in: [TransactionRecord](/FBC/ProductsAndServices/ClientsAndAccounts/TransactionRecord.md)
