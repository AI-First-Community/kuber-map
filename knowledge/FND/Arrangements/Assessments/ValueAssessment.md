---
type: FIBO Class
title: "value assessment"
description: "assessment event to estimate the value of something"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/ValueAssessment
tags: [FND, Release]
relations:
  - {type: applies-methodology, target: "/FND/Arrangements/Assessments/ValuationMethod.md", provenance: fibo}
  - {type: has-output, target: "/FND/Arrangements/Assessments/Appraisal.md", provenance: fibo}
  - {type: has-appraiser, target: "/CMNS/PartiesAndSituations/AgentRole.md", provenance: fibo}
  - {type: is-a, target: "/FND/Arrangements/Assessments/AssessmentEvent.md", provenance: fibo}
---

assessment event to estimate the value of something

### Relationships
- applies-methodology: [ValuationMethod](/FND/Arrangements/Assessments/ValuationMethod.md)
- has-output: [Appraisal](/FND/Arrangements/Assessments/Appraisal.md)
- has-appraiser: [AgentRole](/CMNS/PartiesAndSituations/AgentRole.md)
- is-a: [AssessmentEvent](/FND/Arrangements/Assessments/AssessmentEvent.md)
