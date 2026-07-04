---
type: FIBO Class
title: "contractual economic agreement"
description: "An economic agreement forming part of a transaction, which has contractual standing as evidenced by a contract between the two parties to the Agreement."
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/ContractualEconomicAgreement
tags: [FND, Informative]
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/Contract.md", provenance: fibo}
  - {type: is-a, target: "/FND/TransactionsExt/REATransactions/EconomicAgreement.md", provenance: fibo}
  - {type: confers, target: "/FND/Agreements/Contracts/ContractualCommitment.md", provenance: fibo}
  - {type: has-contract-party, target: "/FND/TransactionsExt/REATransactions/ContractualTransactionParty.md", provenance: fibo}
---

An economic agreement forming part of a transaction, which has contractual standing as evidenced by a contract between the two parties to the Agreement.

### Relationships
- is-a: [Contract](/FND/Agreements/Contracts/Contract.md)
- is-a: [EconomicAgreement](/FND/TransactionsExt/REATransactions/EconomicAgreement.md)
- confers: [ContractualCommitment](/FND/Agreements/Contracts/ContractualCommitment.md)
- has-contract-party: [ContractualTransactionParty](/FND/TransactionsExt/REATransactions/ContractualTransactionParty.md)
