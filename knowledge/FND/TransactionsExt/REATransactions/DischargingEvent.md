---
type: FIBO Class
title: "discharging event"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/DischargingEvent
tags: [FND, Informative]
relations:
  - {type: is-a, target: "/FND/TransactionsExt/REATransactions/TransactionBusinessEvent.md", provenance: fibo}
  - {type: terminates, target: "/FND/TransactionsExt/REATransactions/EconomicCommitment.md", provenance: fibo}
  - {type: triggers, target: "/FND/TransactionsExt/REATransactions/LedgerEntry.md", provenance: fibo}
---

FIBO class *discharging event*.

### Relationships
- is-a: [TransactionBusinessEvent](/FND/TransactionsExt/REATransactions/TransactionBusinessEvent.md)
- terminates: [EconomicCommitment](/FND/TransactionsExt/REATransactions/EconomicCommitment.md)
- triggers: [LedgerEntry](/FND/TransactionsExt/REATransactions/LedgerEntry.md)
