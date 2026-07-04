---
type: FIBO Class
title: "collateral valuation"
description: "assessment activity resulting in the valuation of real property as collateral"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/CollateralValuation
tags: [LOAN, Provisional]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
detail: "Typically an appraisal or automated valuation model (AVM); its result feeds the loan-to-value ratio and lien decisions."
detail_provenance: curated
examples:
  - "An appraisal or automated valuation model (AVM) of the pledged property."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Arrangements/Assessments/AssessmentActivity.md", provenance: fibo}
  - {type: evaluates, target: "/FBC/DebtAndEquities/Debt/Collateral.md", provenance: fibo}
  - {type: is-provided-by, target: "/FND/Arrangements/Assessments/Appraiser.md", provenance: fibo}
---

assessment activity resulting in the valuation of real property as collateral

### Relationships
- is-a: [AssessmentActivity](/FND/Arrangements/Assessments/AssessmentActivity.md)
- evaluates: [Collateral](/FBC/DebtAndEquities/Debt/Collateral.md)
- is-provided-by: [Appraiser](/FND/Arrangements/Assessments/Appraiser.md)
