---
type: FIBO Class
title: "home equity line of credit"
description: "line of credit granted to a homeowner secured by the equity value in a borrower's home or other property"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/HomeEquityLineOfCredit
tags: [LOAN, Release]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
detail: "Home equity loans allow the borrower to borrow against the difference between the fair market value of the property, as determined by an appraisal, and the amount of any outstanding debt on that property, which is typically a first mortgage. Common practice is to set the maximum amount that can be borrowed of up to 80 percent of the fair market value less any outstanding debt. Usually, the term of a HELOC can vary from 5 to up to 25 years, with an initial draw period during which the borrower can access the line of credit, followed by a repayment period during which monthly payments on principal and interest are due until the loan is paid in full. Note that there are restrictions in the US on the nature of the property that may be used as collateral for a HELOC - it must be classified as a 1-4 family dwelling. That determination is independent from the use of proceeds."
examples:
  - "A $50,000 revolving HELOC secured by a homeowner's equity."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/RevolvingLineOfCredit.md", provenance: fibo}
  - {type: is-a, target: "/LOAN/LoansSpecific/ConsumerLoans/SecuredConsumerLoan.md", provenance: fibo}
  - {type: is-a, target: "/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md", provenance: fibo}
---

line of credit granted to a homeowner secured by the equity value in a borrower's home or other property

### Relationships
- is-a: [RevolvingLineOfCredit](/FBC/DebtAndEquities/Debt/RevolvingLineOfCredit.md)
- is-a: [SecuredConsumerLoan](/LOAN/LoansSpecific/ConsumerLoans/SecuredConsumerLoan.md)
- is-a: [LoanSecuredByRealEstate](/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md)
