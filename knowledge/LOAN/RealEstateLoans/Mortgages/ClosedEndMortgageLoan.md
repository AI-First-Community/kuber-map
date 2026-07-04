---
type: FIBO Class
title: "closed-end mortgage loan"
description: "loan secured by real estate with no ability for the borrower to receive additional funds under the loan at a later date"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/ClosedEndMortgageLoan
tags: [LOAN, Release]
core: true
examples:
  - "A 30-year fixed-rate purchase mortgage with no further draws."
examples_provenance: curated
relations:
  - {type: is-a, target: "/LOAN/LoansGeneral/Loans/ClosedEndCredit.md", provenance: fibo}
  - {type: is-a, target: "/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md", provenance: fibo}
---

loan secured by real estate with no ability for the borrower to receive additional funds under the loan at a later date

### Relationships
- is-a: [ClosedEndCredit](/LOAN/LoansGeneral/Loans/ClosedEndCredit.md)
- is-a: [LoanSecuredByRealEstate](/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md)
