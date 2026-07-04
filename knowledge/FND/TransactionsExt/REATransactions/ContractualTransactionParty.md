---
type: FIBO Class
title: "contractual transaction party"
description: "That which is party to a transaction which has contractual standing."
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/ContractualTransactionParty
tags: [FND, Informative]
detail: "In REA, transactions may include those which are not between legal entities,such as for example internal transactions within a business and between business units. This term Contractual Transaction Party forms the basis for all party definitions for transactions which have some formal contractual basis as being between discrete legal entities (legal persons or other contractually capable entities e.g. non incorporated entities). This is the basis for all derivatives transactions, securities market transactions and so on."
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
