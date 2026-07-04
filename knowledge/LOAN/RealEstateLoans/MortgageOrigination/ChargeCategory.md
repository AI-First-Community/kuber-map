---
type: FIBO Class
title: "charge category"
description: "Examples include closing costs, interest, taxes, and other service-related fees."
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/ChargeCategory
tags: [LOAN, Provisional]
detail: "Use with LineItem, (has ChargeCategory instance), (hasNumericalValue for number of units) and (hasCost for the amount of money)"
relations:
  - {type: is-a, target: "/CMNS/Classifiers/Classifier.md", provenance: fibo}
---

Examples include closing costs, interest, taxes, and other service-related fees.

### Relationships
- is-a: [Classifier](/CMNS/Classifiers/Classifier.md)
