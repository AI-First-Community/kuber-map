---
type: FIBO Class
title: "appraisal"
description: "written estimate of the market value of something as of some point in time, typically provided by a qualified appraiser"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Appraisal
tags: [FND, Release]
relations:
  - {type: estimates-value-at, target: "/FND/Arrangements/Assessments/AppraisedValue.md", provenance: fibo}
  - {type: is-a, target: "/FND/Arrangements/Assessments/AssessmentReport.md", provenance: fibo}
  - {type: is-generated-by, target: "/FND/Arrangements/Assessments/Appraiser.md", provenance: fibo}
  - {type: evaluates, target: "/FND/OwnershipAndControl/Ownership/Asset.md", provenance: fibo}
---

written estimate of the market value of something as of some point in time, typically provided by a qualified appraiser

### Relationships
- estimates-value-at: [AppraisedValue](/FND/Arrangements/Assessments/AppraisedValue.md)
- is-a: [AssessmentReport](/FND/Arrangements/Assessments/AssessmentReport.md)
- is-generated-by: [Appraiser](/FND/Arrangements/Assessments/Appraiser.md)
- evaluates: [Asset](/FND/OwnershipAndControl/Ownership/Asset.md)
