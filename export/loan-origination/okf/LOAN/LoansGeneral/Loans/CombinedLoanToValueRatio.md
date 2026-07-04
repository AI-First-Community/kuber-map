---
type: FIBO Class
title: "combined loan-to-value ratio"
description: "ratio of the total amount of debt that is secured by the asset(s) and the appraised value of the asset(s) securing the financing"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/CombinedLoanToValueRatio
tags: [LOAN, Release]
core: true
relations:
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md", provenance: fibo}
  - {type: applies-to, target: "/FND/OwnershipAndControl/Ownership/Asset.md", provenance: fibo}
  - {type: has-argument, target: "/FND/Arrangements/Assessments/AppraisedValue.md", provenance: fibo}
  - {type: has-argument, target: "/LOAN/LoansGeneral/Loans/TotalOutstandingPrincipal.md", provenance: fibo}
  - {type: refers-to, target: "/FND/Arrangements/Assessments/Appraisal.md", provenance: fibo}
---

ratio of the total amount of debt that is secured by the asset(s) and the appraised value of the asset(s) securing the financing

### Relationships
- is-a: [PercentageMonetaryAmount](/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)
- applies-to: [Asset](/FND/OwnershipAndControl/Ownership/Asset.md)
- has-argument: [AppraisedValue](/FND/Arrangements/Assessments/AppraisedValue.md)
- has-argument: [TotalOutstandingPrincipal](/LOAN/LoansGeneral/Loans/TotalOutstandingPrincipal.md)
- refers-to: [Appraisal](/FND/Arrangements/Assessments/Appraisal.md)
