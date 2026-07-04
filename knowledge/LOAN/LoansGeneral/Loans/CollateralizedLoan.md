---
type: FIBO Class
title: "collateralized loan"
description: "secured loan that is secured with cash or other acceptable collateral (real property, securities or other assets) provided by the borrower as specified in the collateral agreement"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/CollateralizedLoan
tags: [LOAN, Release]
core: true
detail: "A secured loan where specific assets (real property, securities, or cash) are pledged; the collateral reduces the lender's loss if the borrower defaults."
detail_provenance: curated
examples:
  - "A mortgage secured by real estate"
  - "A securities-backed line of credit"
examples_provenance: curated
relations:
  - {type: is-a, target: "/LOAN/LoansGeneral/Loans/SecuredLoan.md", provenance: fibo}
  - {type: is-collateralized-by, target: "/FBC/DebtAndEquities/Debt/Collateral.md", provenance: fibo}
  - {type: is-primary-contract-for, target: "/FND/Agreements/Contracts/CollateralAgreement.md", provenance: fibo}
---

secured loan that is secured with cash or other acceptable collateral (real property, securities or other assets) provided by the borrower as specified in the collateral agreement

### Relationships
- is-a: [SecuredLoan](/LOAN/LoansGeneral/Loans/SecuredLoan.md)
- is-collateralized-by: [Collateral](/FBC/DebtAndEquities/Debt/Collateral.md)
- is-primary-contract-for: [CollateralAgreement](/FND/Agreements/Contracts/CollateralAgreement.md)
