---
type: FIBO Class
title: "mortgage loan purpose"
description: "the purpose for which mortgage loan proceeds will be used, such as real property purchase, dwelling construction, or loan refinancing"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/MortgageLoanPurpose
tags: [LOAN, Provisional]
core: true
examples:
  - "Purchase"
  - "Rate-and-term refinance"
  - "Construction"
  - "Cash-out"
examples_provenance: curated
relations:
  - {type: is-a, target: "/LOAN/LoansSpecific/LoanProducts/LoanPurpose.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Classifiers/Classifier.md", provenance: fibo}
---

the purpose for which mortgage loan proceeds will be used, such as real property purchase, dwelling construction, or loan refinancing

### Relationships
- is-a: [LoanPurpose](/LOAN/LoansSpecific/LoanProducts/LoanPurpose.md)
- is-a: [Classifier](/CMNS/Classifiers/Classifier.md)
