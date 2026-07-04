---
type: FIBO Class
title: "undertaking event"
description: "Something which occurs at a point in time, at which a party makes some commitment to some other party."
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/UndertakingEvent
tags: [FND, Informative]
relations:
  - {type: is-a, target: "/FND/TransactionsExt/REATransactions/TransactionBusinessEvent.md", provenance: fibo}
  - {type: triggers, target: "/FND/TransactionsExt/REATransactions/LedgerEntry.md", provenance: fibo}
  - {type: is-a, target: "/FND/TransactionsExt/REATransactions/Undertaking.md", provenance: fibo}
---

Something which occurs at a point in time, at which a party makes some commitment to some other party.

### Relationships
- is-a: [TransactionBusinessEvent](/FND/TransactionsExt/REATransactions/TransactionBusinessEvent.md)
- triggers: [LedgerEntry](/FND/TransactionsExt/REATransactions/LedgerEntry.md)
- is-a: [Undertaking](/FND/TransactionsExt/REATransactions/Undertaking.md)
