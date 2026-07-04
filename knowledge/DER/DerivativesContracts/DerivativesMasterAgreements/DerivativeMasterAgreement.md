---
type: FIBO Class
title: "derivative master agreement"
description: "master agreement covering derivatives transactions to be carried out between the parties to this contract"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesMasterAgreements/DerivativeMasterAgreement
tags: [DER, Release]
detail: "The ISDA Master Agreement (Multicurrency-Cross Border version published in 1992) enables trading counterparties to include foreign exchange transactions under a global cross-product close-out netting master agreement. Because there are significant differences in market practices between the derivatives markets and the international foreign exchange spot and forward markets, parties to the ISDA frequently incorporate the ISDA FX and Currency Options Definitions and further tailor the ISDA Schedule to reflect standard market practice for the foreign exchange products."
examples:
  - "Related to conditions precedent that may apply: 'Each obligation of each party under Section 2(a)(i) is subject to (1) the condition precedent that no Event of Default or Potential Event of Default with respect to the other party has occurred and is continuing, (2) the condition precedent that no Early Termination Date in respect of the relevant Transaction has occurred or been effectively designated and (3) each other applicable condition precedent specified in this Agreement. ' In the above, the Obligations defined under Section 2(a)(i) of the Master Agrement is the obligation to make each payment or delivery defined in a Confirmation for a transaction carried out under this Master Agreement."
  - "Sample preamble to one of these: 'EXAMPLE BANK, a Michigan banking corporation and SAMPLECOMPANY US, INC. a Delaware corporation have entered and/or anticipate entering into one or more transactions (each a 'Transaction') that are or will be governed by this Master Agreement, which includes the schedule (the 'Schedule'), and the documents and other confirming evidence (each a 'Confirmation') exchanged between the parties confirming those Transactions. '"
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CreditAgreement.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Contracts/MasterAgreement.md", provenance: fibo}
---

master agreement covering derivatives transactions to be carried out between the parties to this contract

### Relationships
- is-a: [CreditAgreement](/FBC/DebtAndEquities/Debt/CreditAgreement.md)
- is-a: [MasterAgreement](/FND/Agreements/Contracts/MasterAgreement.md)
