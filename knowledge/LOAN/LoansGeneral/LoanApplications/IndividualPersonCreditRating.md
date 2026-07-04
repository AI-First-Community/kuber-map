---
type: FIBO Class
title: "individual person credit rating"
description: "credit rating that provides an opinion of the creditworthiness of a person"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/IndividualPersonCreditRating
tags: [LOAN, Provisional]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
detail: "Usually expressed as a credit score (e.g. FICO); a primary input to loan pricing and the approval decision."
detail_provenance: curated
examples:
  - "A FICO score of 720"
  - "A VantageScore"
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/CreditRatings/CreditRating.md", provenance: fibo}
---

credit rating that provides an opinion of the creditworthiness of a person

### Relationships
- is-a: [CreditRating](/FBC/DebtAndEquities/CreditRatings/CreditRating.md)
