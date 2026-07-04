---
type: FIBO Class
title: "loan application status"
description: "classifier indicating the state of a loan application at a particular point in its lifecycle, such as submitted, under review, approved, declined, or withdrawn"
definition_provenance: curated
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/LoanApplicationStatus
tags: [LOAN, Provisional]
core: true
examples:
  - "Submitted"
  - "Under review"
  - "Approved"
  - "Declined"
  - "Withdrawn"
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/LifecycleStatus.md", provenance: fibo}
---

classifier indicating the state of a loan application at a particular point in its lifecycle, such as submitted, under review, approved, declined, or withdrawn

### Relationships
- is-a: [LifecycleStatus](/FND/Arrangements/Lifecycles/LifecycleStatus.md)
