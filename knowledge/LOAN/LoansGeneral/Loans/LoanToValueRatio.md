---
type: FIBO Class
title: "loan-to-value ratio"
description: "ratio, expressed as a percentage, between the principal amount of the loan and the appraised value of the asset securing the financing"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/LoanToValueRatio
tags: [LOAN, Release]
relations:
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md", provenance: fibo}
  - {type: applies-to, target: "/FND/OwnershipAndControl/Ownership/Asset.md", provenance: fibo}
  - {type: has-argument, target: "/FBC/DebtAndEquities/Debt/Principal.md", provenance: fibo}
  - {type: has-argument, target: "/FND/Arrangements/Assessments/AppraisedValue.md", provenance: fibo}
  - {type: refers-to, target: "/FND/Arrangements/Assessments/Appraisal.md", provenance: fibo}
---

ratio, expressed as a percentage, between the principal amount of the loan and the appraised value of the asset securing the financing

### Relationships
- is-a: [PercentageMonetaryAmount](/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)
- applies-to: [Asset](/FND/OwnershipAndControl/Ownership/Asset.md)
- has-argument: [Principal](/FBC/DebtAndEquities/Debt/Principal.md)
- has-argument: [AppraisedValue](/FND/Arrangements/Assessments/AppraisedValue.md)
- refers-to: [Appraisal](/FND/Arrangements/Assessments/Appraisal.md)
