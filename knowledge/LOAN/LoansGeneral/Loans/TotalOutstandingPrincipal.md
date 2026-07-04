---
type: FIBO Class
title: "total outstanding principal"
description: "the principal balance of all loans secured by the property"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/TotalOutstandingPrincipal
tags: [LOAN, Release]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
detail: "The aggregate unpaid principal secured by the property across all loans; used with appraised value to compute the combined loan-to-value ratio."
detail_provenance: curated
examples:
  - "The combined unpaid principal of a first mortgage and a HELOC on the property."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/Principal.md", provenance: fibo}
---

the principal balance of all loans secured by the property

### Relationships
- is-a: [Principal](/FBC/DebtAndEquities/Debt/Principal.md)
