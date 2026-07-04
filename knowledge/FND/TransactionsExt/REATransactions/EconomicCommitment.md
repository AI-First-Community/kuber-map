---
type: FIBO Class
title: "economic commitment"
description: "Some Commitment which forms part of the subject of some Transaction, being an undertaking by one or other of the parties to the transaction, extended to the other party to that same transaction."
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicCommitment
tags: [FND, Informative]
relations:
  - {type: is-a, target: "/FND/Agreements/Agreements/Commitment.md", provenance: fibo}
  - {type: made-by, target: "/FND/TransactionsExt/REATransactions/TransactionParty.md", provenance: fibo}
  - {type: is-conferred-by, target: "/FND/TransactionsExt/REATransactions/EconomicAgreement.md", provenance: fibo}
---

Some Commitment which forms part of the subject of some Transaction, being an undertaking by one or other of the parties to the transaction, extended to the other party to that same transaction.

### Relationships
- is-a: [Commitment](/FND/Agreements/Agreements/Commitment.md)
- made-by: [TransactionParty](/FND/TransactionsExt/REATransactions/TransactionParty.md)
- is-conferred-by: [EconomicAgreement](/FND/TransactionsExt/REATransactions/EconomicAgreement.md)
