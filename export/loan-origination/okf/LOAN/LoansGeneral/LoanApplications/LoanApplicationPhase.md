---
type: FIBO Class
title: "loan application phase"
description: "distinct phase in the lifecycle of a loan application, such as pre-qualification, application intake, underwriting, or decisioning"
definition_provenance: curated
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/LoanApplicationPhase
tags: [LOAN, Provisional]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
detail: "Tracks where an application sits in the workflow — for example pre-qualification, intake, underwriting, or decisioning — often driving permissions and turn-time targets."
detail_provenance: curated
examples:
  - "Pre-qualification"
  - "Application intake"
  - "Underwriting"
  - "Decisioning"
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/LifecycleStage.md", provenance: fibo}
---

distinct phase in the lifecycle of a loan application, such as pre-qualification, application intake, underwriting, or decisioning

### Relationships
- is-a: [LifecycleStage](/FND/Arrangements/Lifecycles/LifecycleStage.md)
