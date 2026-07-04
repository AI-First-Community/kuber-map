---
type: FIBO Class
title: "market transaction"
description: "Any transaction which defines a supply of some negotiable item in return for some Consideration. The Market Transaction has a Principal and a Counterparty, i.e. it is not symmetrical."
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/MarketTransaction
tags: [FND, Informative]
relations:
  - {type: has-counterparty, target: "/FND/TransactionsExt/MarketTransactions/TransactionCounterparty.md", provenance: fibo}
  - {type: consideration, target: "/FND/TransactionsExt/REATransactions/EconomicResource.md", provenance: fibo}
  - {type: payment-terms, target: "/FND/TransactionsExt/MarketTransactions/MarketTransactionPaymentTerms.md", provenance: fibo}
  - {type: is-a, target: "/FND/TransactionsExt/REATransactions/EconomicTransaction.md", provenance: fibo}
  - {type: has-principal-party, target: "/FND/TransactionsExt/MarketTransactions/TransactionPrincipal.md", provenance: fibo}
---

Any transaction which defines a supply of some negotiable item in return for some Consideration. The Market Transaction has a Principal and a Counterparty, i.e. it is not symmetrical.

### Relationships
- has-counterparty: [TransactionCounterparty](/FND/TransactionsExt/MarketTransactions/TransactionCounterparty.md)
- consideration: [EconomicResource](/FND/TransactionsExt/REATransactions/EconomicResource.md)
- payment-terms: [MarketTransactionPaymentTerms](/FND/TransactionsExt/MarketTransactions/MarketTransactionPaymentTerms.md)
- is-a: [EconomicTransaction](/FND/TransactionsExt/REATransactions/EconomicTransaction.md)
- has-principal-party: [TransactionPrincipal](/FND/TransactionsExt/MarketTransactions/TransactionPrincipal.md)
