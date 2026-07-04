---
type: FIBO Class
title: "appraisal"
description: "written estimate of the market value of something as of some point in time, typically provided by a qualified appraiser"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Appraisal
tags: [FND, Release]
core: true
relations:
  - {type: is-a, target: "/FND/Arrangements/Assessments/AssessmentReport.md", provenance: fibo}
  - {type: estimates-value-at, target: "/FND/Arrangements/Assessments/AppraisedValue.md", provenance: fibo}
  - {type: evaluates, target: "/FND/OwnershipAndControl/Ownership/Asset.md", provenance: fibo}
  - {type: is-generated-by, target: "/FND/Arrangements/Assessments/Appraiser.md", provenance: fibo}
---

written estimate of the market value of something as of some point in time, typically provided by a qualified appraiser

### Relationships
- is-a: [AssessmentReport](/FND/Arrangements/Assessments/AssessmentReport.md)
- estimates-value-at: [AppraisedValue](/FND/Arrangements/Assessments/AppraisedValue.md)
- evaluates: [Asset](/FND/OwnershipAndControl/Ownership/Asset.md)
- is-generated-by: [Appraiser](/FND/Arrangements/Assessments/Appraiser.md)
