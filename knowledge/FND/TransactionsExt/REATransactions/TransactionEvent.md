---
type: FIBO Class
title: "transaction event"
description: "The event component of a transaction"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/TransactionEvent
tags: [FND, Informative]
detail: "This describes an event. The event may be delivery of something or settlement of monies in payment for something delivered. A Transaction Event will have terms describing the commitment embodied in that side of that transaction."
relations:
  - {type: embodies, target: "/FND/TransactionsExt/REATransactions/EconomicCommitment.md", provenance: fibo}
  - {type: has-end, target: "/FND/TransactionsExt/REATransactions/DischargingEvent.md", provenance: fibo}
  - {type: has-start, target: "/FND/TransactionsExt/REATransactions/TransactionUndertaking.md", provenance: fibo}
---

The event component of a transaction

### Relationships
- embodies: [EconomicCommitment](/FND/TransactionsExt/REATransactions/EconomicCommitment.md)
- has-end: [DischargingEvent](/FND/TransactionsExt/REATransactions/DischargingEvent.md)
- has-start: [TransactionUndertaking](/FND/TransactionsExt/REATransactions/TransactionUndertaking.md)
