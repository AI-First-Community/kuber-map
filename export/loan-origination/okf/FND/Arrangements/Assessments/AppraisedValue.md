---
type: FIBO Class
title: "appraised value"
description: "estimated value of some asset as of a given point in time"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AppraisedValue
tags: [FND, Release]
core: true
detail: "Serves as the denominator of the loan-to-value ratio and the basis for how much a lender will advance against the property."
detail_provenance: curated
examples:
  - "$450,000 — the appraiser's estimate of a property's market value."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Arrangements/Assessments/MarketValue.md", provenance: fibo}
---

estimated value of some asset as of a given point in time

### Relationships
- is-a: [MarketValue](/FND/Arrangements/Assessments/MarketValue.md)
