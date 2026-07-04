---
type: FIBO Class
title: "contractual transaction party"
description: "That which is party to a transaction which has contractual standing."
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/ContractualTransactionParty
tags: [FND, Informative]
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractParty.md", provenance: fibo}
  - {type: is-a, target: "/FND/TransactionsExt/REATransactions/TransactionParty.md", provenance: fibo}
  - {type: is-played-by, target: "/CMNS/Organizations/LegalPerson.md", provenance: fibo}
---

That which is party to a transaction which has contractual standing.

### Relationships
- is-a: [ContractParty](/FND/Agreements/Contracts/ContractParty.md)
- is-a: [TransactionParty](/FND/TransactionsExt/REATransactions/TransactionParty.md)
- is-played-by: [LegalPerson](/CMNS/Organizations/LegalPerson.md)
