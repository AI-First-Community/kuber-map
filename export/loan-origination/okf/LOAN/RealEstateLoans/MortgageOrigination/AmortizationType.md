---
type: FIBO Class
title: "amortization type"
description: "classifier of amortization algorithms"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/AmortizationType
tags: [LOAN, Provisional]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
detail: "Determines how principal and interest are paid down over the term — fully amortizing loans retire the balance by maturity, while interest-only or balloon structures leave principal outstanding."
detail_provenance: curated
examples:
  - "Fully amortizing"
  - "Interest-only"
  - "Negative amortization"
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/Classifiers/Classifier.md", provenance: fibo}
---

classifier of amortization algorithms

### Relationships
- is-a: [Classifier](/CMNS/Classifiers/Classifier.md)
