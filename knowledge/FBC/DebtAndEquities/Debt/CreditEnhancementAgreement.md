---
type: FIBO Class
title: "credit enhancement agreement"
description: "collateral agreement that governs the exchange of collateral between parties to mitigate counterparty credit risk"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditEnhancementAgreement
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/CollateralAgreement.md", provenance: fibo}
  - {type: has-beneficiary, target: "/FBC/DebtAndEquities/Debt/CreditEnhancementBeneficiary.md", provenance: fibo}
  - {type: is-provided-by, target: "/FND/Agreements/Contracts/ContractPrincipal.md", provenance: fibo}
---

collateral agreement that governs the exchange of collateral between parties to mitigate counterparty credit risk

### Relationships
- is-a: [CollateralAgreement](/FND/Agreements/Contracts/CollateralAgreement.md)
- has-beneficiary: [CreditEnhancementBeneficiary](/FBC/DebtAndEquities/Debt/CreditEnhancementBeneficiary.md)
- is-provided-by: [ContractPrincipal](/FND/Agreements/Contracts/ContractPrincipal.md)
