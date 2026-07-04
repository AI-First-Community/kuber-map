---
type: FIBO Class
title: "reverse mortgage loan"
description: "loan secured by real estate that pays money to the borrower against a set principal limit based on the value of existing equity in the underlying collateral"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/ReverseMortgageLoan
tags: [LOAN, Release]
core: true
relations:
  - {type: is-a, target: "/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md", provenance: fibo}
  - {type: has-credit-limit, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

loan secured by real estate that pays money to the borrower against a set principal limit based on the value of existing equity in the underlying collateral

### Relationships
- is-a: [LoanSecuredByRealEstate](/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md)
- has-credit-limit: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
