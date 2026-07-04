---
type: FIBO Class
title: "assessment event"
description: "event involving the evaluation or estimation of the nature, quality, or ability of someone or something"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AssessmentEvent
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/Occurrence.md", provenance: fibo}
  - {type: exemplifies, target: "/FND/Arrangements/Assessments/AssessmentActivity.md", provenance: fibo}
  - {type: has-output, target: "/FND/Arrangements/Assessments/AssessmentReport.md", provenance: fibo}
  - {type: has-output, target: "/FND/Arrangements/Assessments/Opinion.md", provenance: fibo}
  - {type: is-provided-by, target: "/CMNS/PartiesAndSituations/AgentRole.md", provenance: fibo}
---

event involving the evaluation or estimation of the nature, quality, or ability of someone or something

### Relationships
- is-a: [Occurrence](/FND/DatesAndTimes/Occurrences/Occurrence.md)
- exemplifies: [AssessmentActivity](/FND/Arrangements/Assessments/AssessmentActivity.md)
- has-output: [AssessmentReport](/FND/Arrangements/Assessments/AssessmentReport.md)
- has-output: [Opinion](/FND/Arrangements/Assessments/Opinion.md)
- is-provided-by: [AgentRole](/CMNS/PartiesAndSituations/AgentRole.md)
