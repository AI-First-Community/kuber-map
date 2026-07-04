---
type: FIBO Class
title: "ledger entry"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/LedgerEntry
tags: [FND, Informative]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegistryEntry.md", provenance: fibo}
  - {type: has-monetary-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-posting-date, target: "/FBC/ProductsAndServices/ClientsAndAccounts/PostingDate.md", provenance: fibo}
  - {type: has-transaction-date, target: "/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDate.md", provenance: fibo}
  - {type: is-registered-in, target: "/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccount.md", provenance: fibo}
---

FIBO class *ledger entry*.

### Relationships
- is-a: [DatedCollectionConstituent](/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md)
- is-a: [RegistryEntry](/CMNS/RegistrationAuthorities/RegistryEntry.md)
- has-monetary-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-posting-date: [PostingDate](/FBC/ProductsAndServices/ClientsAndAccounts/PostingDate.md)
- has-transaction-date: [TransactionDate](/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDate.md)
- is-registered-in: [LedgerAccount](/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccount.md)
