---
type: FIBO Class
title: "breach of covenant"
description: "classifier of events representing breaking a promise specified in a contract to do or not to do something, without a legitimate excuse"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/BreachOfCovenant
tags: [FND, Release]
detail: "In the case of a breach of a covenant or warranty, the contract remains binding and damages only are recoverable for the breach, whereas a breach of contract typically invalidates the entire contract."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEvent.md", provenance: fibo}
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/OccurrenceKind.md", provenance: fibo}
  - {type: applies-to, target: "/FND/Agreements/Contracts/Contract.md", provenance: fibo}
  - {type: refers-to, target: "/FND/Agreements/Contracts/ContractualCommitment.md", provenance: fibo}
---

classifier of events representing breaking a promise specified in a contract to do or not to do something, without a legitimate excuse

### Relationships
- is-a: [ContractLifecycleEvent](/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEvent.md)
- is-a: [OccurrenceKind](/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)
- applies-to: [Contract](/FND/Agreements/Contracts/Contract.md)
- refers-to: [ContractualCommitment](/FND/Agreements/Contracts/ContractualCommitment.md)
