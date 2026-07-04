---
type: FIBO Class
title: "value assessment"
description: "assessment event to estimate the value of something"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/ValueAssessment
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/Arrangements/Assessments/AssessmentEvent.md", provenance: fibo}
  - {type: applies-methodology, target: "/FND/Arrangements/Assessments/ValuationMethod.md", provenance: fibo}
  - {type: has-appraiser, target: "/CMNS/PartiesAndSituations/AgentRole.md", provenance: fibo}
  - {type: has-output, target: "/FND/Arrangements/Assessments/Appraisal.md", provenance: fibo}
---

assessment event to estimate the value of something

### Relationships
- is-a: [AssessmentEvent](/FND/Arrangements/Assessments/AssessmentEvent.md)
- applies-methodology: [ValuationMethod](/FND/Arrangements/Assessments/ValuationMethod.md)
- has-appraiser: [AgentRole](/CMNS/PartiesAndSituations/AgentRole.md)
- has-output: [Appraisal](/FND/Arrangements/Assessments/Appraisal.md)
