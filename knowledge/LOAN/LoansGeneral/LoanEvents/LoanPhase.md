---
type: FIBO Class
title: "loan phase"
description: "distinct phase in the lifecycle of a loan, such as origination, disbursement, repayment, or closure"
definition_provenance: curated
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/LoanPhase
tags: [LOAN, Provisional]
core: true
detail: "The stage of a loan across its whole life (origination, disbursement, repayment, payoff), distinct from the application workflow."
detail_provenance: curated
examples:
  - "Origination"
  - "Disbursement"
  - "Repayment"
  - "Payoff / closure"
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/LifecycleStage.md", provenance: fibo}
---

distinct phase in the lifecycle of a loan, such as origination, disbursement, repayment, or closure

### Relationships
- is-a: [LifecycleStage](/FND/Arrangements/Lifecycles/LifecycleStage.md)
