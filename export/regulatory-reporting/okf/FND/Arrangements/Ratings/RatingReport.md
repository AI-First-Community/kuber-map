---
type: FIBO Class
title: "rating report"
description: "report describing a set of ratings"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingReport
tags: [FND, Release]
core: true
use_cases:
  - "Regulatory Reporting & Compliance (supervisory filing)"
examples:
  - "A credit rating agency's report assigning an issuer an 'AA' rating."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Arrangements/Assessments/AssessmentReport.md", provenance: fibo}
  - {type: reports-on, target: "/FND/Arrangements/Ratings/Rating.md", provenance: fibo}
---

report describing a set of ratings

### Relationships
- is-a: [AssessmentReport](/FND/Arrangements/Assessments/AssessmentReport.md)
- reports-on: [Rating](/FND/Arrangements/Ratings/Rating.md)
