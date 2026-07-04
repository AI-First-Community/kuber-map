---
type: FIBO Class
title: "construction loan"
description: "loan covering construction and development costs, secured by a mortgage on the property financed"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/ConstructionLoans/ConstructionLoan
tags: [LOAN, Provisional]
detail: "A construction loan credit facility tranche (sub-facility) is a portion of a construction loan that is released in stages, or tranches, to fund specific phases of a construction project. Each tranche (committed sub-facility) is released once the borrower reaches a certain milestone, such as pouring concrete or completing the foundation. The borrower typically only pays interest on the amount that has been released at any given time. The Project Management Institute (PMI) breaks down most construction projects into five phases, which are initiation, planning, execution, monitoring and control, and closeout. Construction loans also typically include milestones at which a portion of the total facility is advanced to the borrower given proof of completion or meeting other requirements with respect to the work."
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CreditFacility.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Contracts/MasterAgreement.md", provenance: fibo}
  - {type: is-a, target: "/LOAN/LoansGeneral/Loans/CollateralizedLoan.md", provenance: fibo}
  - {type: has-milestone-provision, target: "/FND/Agreements/Contracts/ContractMilestone.md", provenance: fibo}
  - {type: is-collateralized-by, target: "/FND/Places/RealProperty/RealProperty.md", provenance: fibo}
---

loan covering construction and development costs, secured by a mortgage on the property financed

### Relationships
- is-a: [CreditFacility](/FBC/DebtAndEquities/Debt/CreditFacility.md)
- is-a: [MasterAgreement](/FND/Agreements/Contracts/MasterAgreement.md)
- is-a: [CollateralizedLoan](/LOAN/LoansGeneral/Loans/CollateralizedLoan.md)
- has-milestone-provision: [ContractMilestone](/FND/Agreements/Contracts/ContractMilestone.md)
- is-collateralized-by: [RealProperty](/FND/Places/RealProperty/RealProperty.md)
