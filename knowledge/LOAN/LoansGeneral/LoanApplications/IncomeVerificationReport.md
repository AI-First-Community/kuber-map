---
type: FIBO Class
title: "income verification report"
description: "report providing the methodology and supporting documentation used to verify the borrower's income"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/IncomeVerificationReport
tags: [LOAN, Provisional]
core: true
detail: "Documents such as pay stubs, W-2s, tax returns, or a verification of employment that support claimed income and help satisfy ability-to-repay rules."
detail_provenance: curated
examples:
  - "A verification of employment (VOE) with pay stubs and W-2s."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Arrangements/Assessments/AssessmentReport.md", provenance: fibo}
---

report providing the methodology and supporting documentation used to verify the borrower's income

### Relationships
- is-a: [AssessmentReport](/FND/Arrangements/Assessments/AssessmentReport.md)
