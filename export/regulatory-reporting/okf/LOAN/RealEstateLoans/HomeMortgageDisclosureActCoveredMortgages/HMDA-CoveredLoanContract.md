---
type: FIBO Class
title: "HMDA covered loan contract"
description: "a closed-end mortgage loan or open-end line of credit that is not an excluded transaction for HMDA reporting under US section 1003.3(c) of the Revised Home Mortgage Disclosure Act of 2015"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-CoveredLoanContract
tags: [LOAN, Provisional]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
  - "Regulatory Reporting & Compliance (supervisory filing)"
detail: "A loan or application subject to Home Mortgage Disclosure Act reporting; the lender must record specified data points about it on its register."
detail_provenance: curated
examples:
  - "A closed-end home-purchase mortgage that must be reported under HMDA."
examples_provenance: curated
relations:
  - {type: is-a, target: "/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md", provenance: fibo}
  - {type: is-classified-by, target: "/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HowSubmitted.md", provenance: fibo}
---

a closed-end mortgage loan or open-end line of credit that is not an excluded transaction for HMDA reporting under US section 1003.3(c) of the Revised Home Mortgage Disclosure Act of 2015

### Relationships
- is-a: [LoanSecuredByRealEstate](/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md)
- is-classified-by: [HowSubmitted](/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HowSubmitted.md)
