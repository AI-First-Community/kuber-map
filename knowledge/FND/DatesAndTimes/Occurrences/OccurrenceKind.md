---
type: FIBO Class
title: "occurrence kind"
description: "classifier that specifies the general nature of an occurrence (event)"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceKind
tags: [FND, Release]
detail: "As types (or categories) of events, OccurenceKinds do not happen; OccurenceKinds describe Occurrences which happen and exemplify an OccurenceKind. As occurrences are things that actually happen, they have an actual date where as OccurenceKinds do not have an actual date. In order for other ontologies to accept FinancialDates without committing to the particular notions of 'Occurrence' and 'OccurrenceKind' that is modeled here, all aspects of Occurrences are captured in this ontolog"
examples:
  - "loan origination"
  - "trade settlement"
relations:
  - {type: is-a, target: "/CMNS/Classifiers/Classifier.md", provenance: fibo}
  - {type: classifies, target: "/FND/DatesAndTimes/Occurrences/Occurrence.md", provenance: fibo}
---

classifier that specifies the general nature of an occurrence (event)

### Relationships
- is-a: [Classifier](/CMNS/Classifiers/Classifier.md)
- classifies: [Occurrence](/FND/DatesAndTimes/Occurrences/Occurrence.md)
