---
type: FIBO Class
title: "loan offering"
description: "offering related to a loan product that may be a tailored to particular circumstances, aimed at a group of borrowers or individual borrower"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LoanProductOffering
tags: [LOAN, Provisional]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
detail: "A specific packaging of a loan product — its rate, term, and eligibility — marketed to a borrower segment or tailored to an individual applicant."
detail_provenance: curated
examples:
  - "A lender's advertised 6.5% 30-year fixed mortgage for first-time buyers."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Offering.md", provenance: fibo}
  - {type: applies-to, target: "/LOAN/LoansSpecific/LoanProducts/LoanProduct.md", provenance: fibo}
  - {type: has-member, target: "/LOAN/LoansSpecific/LoanProducts/LineItem.md", provenance: fibo}
---

offering related to a loan product that may be a tailored to particular circumstances, aimed at a group of borrowers or individual borrower

### Relationships
- is-a: [Offering](/FBC/ProductsAndServices/FinancialProductsAndServices/Offering.md)
- applies-to: [LoanProduct](/LOAN/LoansSpecific/LoanProducts/LoanProduct.md)
- has-member: [LineItem](/LOAN/LoansSpecific/LoanProducts/LineItem.md)
