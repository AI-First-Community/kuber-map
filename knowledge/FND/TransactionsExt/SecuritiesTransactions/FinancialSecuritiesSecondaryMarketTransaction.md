---
type: FIBO Class
title: "financial securities secondary market transaction"
description: "A Transaction in which some negotiable security is provided in exchange for some Consideration."
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/FinancialSecuritiesSecondaryMarketTransaction
tags: [FND, Informative]
relations:
  - {type: subject, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
  - {type: has-principal-party, target: "/FND/TransactionsExt/SecuritiesTransactions/SecuritiesTransactionPrincipal.md", provenance: fibo}
  - {type: is-a, target: "/FND/TransactionsExt/REATransactions/ContractualTransaction.md", provenance: fibo}
  - {type: is-a, target: "/FND/TransactionsExt/MarketTransactions/MarketTransaction.md", provenance: fibo}
  - {type: has-counterparty, target: "/FND/TransactionsExt/SecuritiesTransactions/SecuritiesTransactionCounterparty.md", provenance: fibo}
  - {type: embodies, target: "/FND/TransactionsExt/SecuritiesTransactions/SecuritiesTransactionContract.md", provenance: fibo}
---

A Transaction in which some negotiable security is provided in exchange for some Consideration.

### Relationships
- subject: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- has-principal-party: [SecuritiesTransactionPrincipal](/FND/TransactionsExt/SecuritiesTransactions/SecuritiesTransactionPrincipal.md)
- is-a: [ContractualTransaction](/FND/TransactionsExt/REATransactions/ContractualTransaction.md)
- is-a: [MarketTransaction](/FND/TransactionsExt/MarketTransactions/MarketTransaction.md)
- has-counterparty: [SecuritiesTransactionCounterparty](/FND/TransactionsExt/SecuritiesTransactions/SecuritiesTransactionCounterparty.md)
- embodies: [SecuritiesTransactionContract](/FND/TransactionsExt/SecuritiesTransactions/SecuritiesTransactionContract.md)
