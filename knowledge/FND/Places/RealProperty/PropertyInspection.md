---
type: FIBO Class
title: "property inspection"
description: "event that involves analyzing one or more aspects of a real property"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/PropertyInspection
tags: [FND, Release]
detail: "The concept of a property inspection is separate from conducting an overarching appraisal. Examples are termite inspections, construction inspections, evaluation for completion of some milestone, improvement, correction, etc."
relations:
  - {type: is-a, target: "/FND/Arrangements/Assessments/AssessmentEvent.md", provenance: fibo}
  - {type: evaluates, target: "/FND/Places/RealProperty/RealProperty.md", provenance: fibo}
  - {type: has-output, target: "/FND/Places/RealProperty/PropertyInspectionReport.md", provenance: fibo}
---

event that involves analyzing one or more aspects of a real property

### Relationships
- is-a: [AssessmentEvent](/FND/Arrangements/Assessments/AssessmentEvent.md)
- evaluates: [RealProperty](/FND/Places/RealProperty/RealProperty.md)
- has-output: [PropertyInspectionReport](/FND/Places/RealProperty/PropertyInspectionReport.md)
