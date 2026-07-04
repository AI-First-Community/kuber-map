---
type: FIBO Class
title: "motor vehicle loan"
description: "collateralized, simple-interest loan that is repaid in monthly installments over a period of typically three to five years, for the purpose of purchasing a vehicle"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/MotorVehicleLoan
tags: [LOAN, Release]
relations:
  - {type: is-collateralized-by, target: "/FBC/DebtAndEquities/Debt/PhysicalCollateral.md", provenance: fibo}
  - {type: is-a, target: "/LOAN/LoansGeneral/Loans/CollateralizedLoan.md", provenance: fibo}
  - {type: is-a, target: "/LOAN/LoansSpecific/ConsumerLoans/SecuredConsumerLoan.md", provenance: fibo}
---

collateralized, simple-interest loan that is repaid in monthly installments over a period of typically three to five years, for the purpose of purchasing a vehicle

### Relationships
- is-collateralized-by: [PhysicalCollateral](/FBC/DebtAndEquities/Debt/PhysicalCollateral.md)
- is-a: [CollateralizedLoan](/LOAN/LoansGeneral/Loans/CollateralizedLoan.md)
- is-a: [SecuredConsumerLoan](/LOAN/LoansSpecific/ConsumerLoans/SecuredConsumerLoan.md)
