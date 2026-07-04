---
type: FIBO Class
title: "transaction principal"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/TransactionPrincipal
tags: [FND, Informative]
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractPrincipal.md", provenance: fibo}
  - {type: is-a, target: "/FND/TransactionsExt/REATransactions/TransactionParty.md", provenance: fibo}
  - {type: transacts-with, target: "/FND/TransactionsExt/MarketTransactions/TransactionCounterparty.md", provenance: fibo}
---

FIBO class *transaction principal*.

### Relationships
- is-a: [ContractPrincipal](/FND/Agreements/Contracts/ContractPrincipal.md)
- is-a: [TransactionParty](/FND/TransactionsExt/REATransactions/TransactionParty.md)
- transacts-with: [TransactionCounterparty](/FND/TransactionsExt/MarketTransactions/TransactionCounterparty.md)
