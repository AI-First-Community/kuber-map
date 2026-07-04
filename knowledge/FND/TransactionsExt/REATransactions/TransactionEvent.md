---
type: FIBO Class
title: "transaction event"
description: "The event component of a transaction"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionEvent
tags: [FND, Informative]
relations:
  - {type: has-end, target: "/FND/TransactionsExt/REATransactions/DischargingEvent.md", provenance: fibo}
  - {type: embodies, target: "/FND/TransactionsExt/REATransactions/EconomicCommitment.md", provenance: fibo}
  - {type: has-start, target: "/FND/TransactionsExt/REATransactions/TransactionUndertaking.md", provenance: fibo}
---

The event component of a transaction

### Relationships
- has-end: [DischargingEvent](/FND/TransactionsExt/REATransactions/DischargingEvent.md)
- embodies: [EconomicCommitment](/FND/TransactionsExt/REATransactions/EconomicCommitment.md)
- has-start: [TransactionUndertaking](/FND/TransactionsExt/REATransactions/TransactionUndertaking.md)
