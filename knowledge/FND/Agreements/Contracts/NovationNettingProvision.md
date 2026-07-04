---
type: FIBO Class
title: "novation netting provision"
description: "contractual element that specifies what should be done with respect to netting when a given contract is replaced with another"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/NovationNettingProvision
tags: [FND, Release]
detail: "Novation netting contemplates that for each value date and for each currency, the parties agree that all existing contracts will be canceled (discharged and extinguished) and simultaneously replaced by a new contract that aggregates and nets all of the payment obligations of the original contracts. Novation netting occurs immediately when a nettable transaction is entered into."
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/NettingProvision.md", provenance: fibo}
---

contractual element that specifies what should be done with respect to netting when a given contract is replaced with another

### Relationships
- is-a: [NettingProvision](/FND/Agreements/Contracts/NettingProvision.md)
