---
type: FIBO Class
title: "construction loan"
description: "loan covering construction and development costs, secured by a mortgage on the property financed"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/ConstructionLoans/ConstructionLoan
tags: [LOAN, Provisional]
relations:
  - {type: is-collateralized-by, target: "/FND/Places/RealProperty/RealProperty.md", provenance: fibo}
  - {type: is-a, target: "/LOAN/LoansGeneral/Loans/CollateralizedLoan.md", provenance: fibo}
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CreditFacility.md", provenance: fibo}
  - {type: has-milestone-provision, target: "/FND/Agreements/Contracts/ContractMilestone.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Contracts/MasterAgreement.md", provenance: fibo}
---

loan covering construction and development costs, secured by a mortgage on the property financed

### Relationships
- is-collateralized-by: [RealProperty](/FND/Places/RealProperty/RealProperty.md)
- is-a: [CollateralizedLoan](/LOAN/LoansGeneral/Loans/CollateralizedLoan.md)
- is-a: [CreditFacility](/FBC/DebtAndEquities/Debt/CreditFacility.md)
- has-milestone-provision: [ContractMilestone](/FND/Agreements/Contracts/ContractMilestone.md)
- is-a: [MasterAgreement](/FND/Agreements/Contracts/MasterAgreement.md)
