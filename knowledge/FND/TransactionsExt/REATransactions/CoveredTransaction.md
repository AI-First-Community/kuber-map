---
type: FIBO Class
title: "covered transaction"
description: "A transaction covered by some Master Agreement."
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/CoveredTransaction
tags: [FND, Informative]
relations:
  - {type: is-a, target: "/FND/TransactionsExt/REATransactions/ContractualTransaction.md", provenance: fibo}
  - {type: is-governed-by, target: "/FND/Agreements/Contracts/MasterAgreement.md", provenance: fibo}
---

A transaction covered by some Master Agreement.

### Relationships
- is-a: [ContractualTransaction](/FND/TransactionsExt/REATransactions/ContractualTransaction.md)
- is-governed-by: [MasterAgreement](/FND/Agreements/Contracts/MasterAgreement.md)
