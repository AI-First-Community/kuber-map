---
type: FIBO Class
title: "mortgage"
description: "grant of financial interest in real property to a party that is not an owner of that real property and is recorded by a registration authority"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/Mortgage
tags: [LOAN, Release]
relations:
  - {type: is-collateralized-by, target: "/FND/Places/RealProperty/RealProperty.md", provenance: fibo}
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/SecurityAgreement.md", provenance: fibo}
---

grant of financial interest in real property to a party that is not an owner of that real property and is recorded by a registration authority

### Relationships
- is-collateralized-by: [RealProperty](/FND/Places/RealProperty/RealProperty.md)
- is-a: [SecurityAgreement](/FBC/DebtAndEquities/Debt/SecurityAgreement.md)
