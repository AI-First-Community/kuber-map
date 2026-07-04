---
type: FIBO Class
title: "mortgage product"
description: "loan product, offered by a lender, that is realized as a mortgage — a loan secured by real property — with specific eligibility criteria, characteristics, and terms"
definition_provenance: curated
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/MortgageProduct
tags: [LOAN, Provisional]
core: true
examples:
  - "A jumbo 30-year fixed"
  - "A 7/1 ARM"
  - "An FHA 203(k) rehab loan"
examples_provenance: curated
relations:
  - {type: is-a, target: "/LOAN/LoansSpecific/LoanProducts/LoanProduct.md", provenance: fibo}
  - {type: is-exemplified-by, target: "/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md", provenance: fibo}
---

loan product, offered by a lender, that is realized as a mortgage — a loan secured by real property — with specific eligibility criteria, characteristics, and terms

### Relationships
- is-a: [LoanProduct](/LOAN/LoansSpecific/LoanProducts/LoanProduct.md)
- is-exemplified-by: [LoanSecuredByRealEstate](/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md)
