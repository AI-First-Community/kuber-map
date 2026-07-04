---
type: FIBO Class
title: "mortgage"
description: "grant of financial interest in real property to a party that is not an owner of that real property and is recorded by a registration authority"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/Mortgage
tags: [LOAN, Release]
core: true
detail: "A mortgage prevents transfer of the ownership of the real property unless the financial interest is satisfied. Any loan can be collateralized by a mortgage, including, for example, a bail bond."
examples:
  - "A 30-year fixed-rate home loan"
  - "An FHA-insured mortgage"
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/SecurityAgreement.md", provenance: fibo}
  - {type: is-collateralized-by, target: "/FND/Places/RealProperty/RealProperty.md", provenance: fibo}
---

grant of financial interest in real property to a party that is not an owner of that real property and is recorded by a registration authority

### Relationships
- is-a: [SecurityAgreement](/FBC/DebtAndEquities/Debt/SecurityAgreement.md)
- is-collateralized-by: [RealProperty](/FND/Places/RealProperty/RealProperty.md)
