---
type: FIBO Class
title: "collateralized loan"
description: "secured loan that is secured with cash or other acceptable collateral (real property, securities or other assets) provided by the borrower as specified in the collateral agreement"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/CollateralizedLoan
tags: [LOAN, Release]
relations:
  - {type: is-collateralized-by, target: "/FBC/DebtAndEquities/Debt/Collateral.md", provenance: fibo}
  - {type: is-primary-contract-for, target: "/FND/Agreements/Contracts/CollateralAgreement.md", provenance: fibo}
  - {type: is-a, target: "/LOAN/LoansGeneral/Loans/SecuredLoan.md", provenance: fibo}
---

secured loan that is secured with cash or other acceptable collateral (real property, securities or other assets) provided by the borrower as specified in the collateral agreement

### Relationships
- is-collateralized-by: [Collateral](/FBC/DebtAndEquities/Debt/Collateral.md)
- is-primary-contract-for: [CollateralAgreement](/FND/Agreements/Contracts/CollateralAgreement.md)
- is-a: [SecuredLoan](/LOAN/LoansGeneral/Loans/SecuredLoan.md)
