---
type: FIBO Class
title: "economic contract"
description: "A contract relating to and governing an economic transaction between two parties."
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicContract
tags: [FND, Informative]
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/Contract.md", provenance: fibo}
  - {type: embodies, target: "/FND/TransactionsExt/REATransactions/ContractualEconomicAgreement.md", provenance: fibo}
  - {type: has-contractual-element, target: "/FND/TransactionsExt/REATransactions/EconomicContractTermsSet.md", provenance: fibo}
---

A contract relating to and governing an economic transaction between two parties.

### Relationships
- is-a: [Contract](/FND/Agreements/Contracts/Contract.md)
- embodies: [ContractualEconomicAgreement](/FND/TransactionsExt/REATransactions/ContractualEconomicAgreement.md)
- has-contractual-element: [EconomicContractTermsSet](/FND/TransactionsExt/REATransactions/EconomicContractTermsSet.md)
