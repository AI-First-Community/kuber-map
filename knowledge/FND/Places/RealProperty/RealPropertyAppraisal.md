---
type: FIBO Class
title: "real property appraisal"
description: "value assessment that estimates the amount of money some real property is worth"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealPropertyAppraisal
tags: [FND, Release]
relations:
  - {type: evaluates, target: "/FND/Places/RealProperty/RealProperty.md", provenance: fibo}
  - {type: has-input, target: "/FND/Places/RealProperty/PropertyInspectionReport.md", provenance: fibo}
  - {type: is-a, target: "/FND/Arrangements/Assessments/Appraisal.md", provenance: fibo}
  - {type: is-provided-by, target: "/FND/Arrangements/Assessments/Appraiser.md", provenance: fibo}
---

value assessment that estimates the amount of money some real property is worth

### Relationships
- evaluates: [RealProperty](/FND/Places/RealProperty/RealProperty.md)
- has-input: [PropertyInspectionReport](/FND/Places/RealProperty/PropertyInspectionReport.md)
- is-a: [Appraisal](/FND/Arrangements/Assessments/Appraisal.md)
- is-provided-by: [Appraiser](/FND/Arrangements/Assessments/Appraiser.md)
