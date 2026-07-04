---
type: FIBO Class
title: "underwriting decision"
description: "classifier providing a loan approval recommendation determined either manually or by an automated underwriting system"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/UnderwritingDecision
tags: [LOAN, Provisional]
core: true
detail: "The outcome of assessing credit, capacity, and collateral — approve, approve with conditions, suspend, or deny."
detail_provenance: curated
examples:
  - "Approve"
  - "Approve with conditions"
  - "Suspend"
  - "Deny"
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/Classifiers/Classifier.md", provenance: fibo}
---

classifier providing a loan approval recommendation determined either manually or by an automated underwriting system

### Relationships
- is-a: [Classifier](/CMNS/Classifiers/Classifier.md)
