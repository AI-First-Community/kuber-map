---
type: FIBO Class
title: "motor vehicle loan"
description: "collateralized, simple-interest loan that is repaid in monthly installments over a period of typically three to five years, for the purpose of purchasing a vehicle"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/MotorVehicleLoan
tags: [LOAN, Release]
detail: "Many lenders will only approve auto loans for vehicles (i.e., cars, trucks) that are a certain age (typically 5 years or less) due to depreciation of the value of the vehicle. Because an auto loan is a 'secured' type of loan, the vehicle that is being financed is used as collateral (i.e. if the borrower fails to repay the loan, the vehicle may be seized by the lender)."
synonyms:
  - "auto loan"
relations:
  - {type: is-a, target: "/LOAN/LoansGeneral/Loans/CollateralizedLoan.md", provenance: fibo}
  - {type: is-a, target: "/LOAN/LoansSpecific/ConsumerLoans/SecuredConsumerLoan.md", provenance: fibo}
  - {type: is-collateralized-by, target: "/FBC/DebtAndEquities/Debt/PhysicalCollateral.md", provenance: fibo}
---

collateralized, simple-interest loan that is repaid in monthly installments over a period of typically three to five years, for the purpose of purchasing a vehicle

### Relationships
- is-a: [CollateralizedLoan](/LOAN/LoansGeneral/Loans/CollateralizedLoan.md)
- is-a: [SecuredConsumerLoan](/LOAN/LoansSpecific/ConsumerLoans/SecuredConsumerLoan.md)
- is-collateralized-by: [PhysicalCollateral](/FBC/DebtAndEquities/Debt/PhysicalCollateral.md)
