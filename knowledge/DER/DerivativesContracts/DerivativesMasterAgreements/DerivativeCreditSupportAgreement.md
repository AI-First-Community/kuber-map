---
type: FIBO Class
title: "derivative credit support agreement"
description: "addendum to the master agreement that governs the exchange of collateral between parties in derivatives transactions"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesMasterAgreements/DerivativeCreditSupportAgreement
tags: [DER, Release]
detail: "Note that in the case of a derivative credit support agreement, the beneficiary actually holds the collateral and has the right to ask for additional collateral if its value falls below the threshold agreed upon per the agreement."
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CreditEnhancementAgreement.md", provenance: fibo}
  - {type: is-subordinate-to, target: "/DER/DerivativesContracts/DerivativesMasterAgreements/DerivativeMasterAgreement.md", provenance: fibo}
---

addendum to the master agreement that governs the exchange of collateral between parties in derivatives transactions

### Relationships
- is-a: [CreditEnhancementAgreement](/FBC/DebtAndEquities/Debt/CreditEnhancementAgreement.md)
- is-subordinate-to: [DerivativeMasterAgreement](/DER/DerivativesContracts/DerivativesMasterAgreements/DerivativeMasterAgreement.md)
