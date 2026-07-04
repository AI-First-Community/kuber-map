---
type: FIBO Class
title: "occurrence"
description: "happening of an OccurrenceKind, i.e., an event"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Occurrence
tags: [FND, Release]
detail: "Each occurrence has a date time stamp, which identifies when the event occurred, and, optionally, a location (possibly virtual), that identifies where the occurrence happened. In order for other ontologies to accept FinancialDates without committing to the particular notions of 'Occurrence' and 'OccurrenceKind' that is modeled here, all aspects of Occurrences are captured in this ontology."
synonyms:
  - "event"
relations:
  - {type: exemplifies, target: "/FND/DatesAndTimes/Occurrences/OccurrenceKind.md", provenance: fibo}
  - {type: has-location, target: "/CMNS/Locations/Location.md", provenance: fibo}
  - {type: is-classified-by, target: "/FND/DatesAndTimes/Occurrences/OccurrenceKind.md", provenance: fibo}
---

happening of an OccurrenceKind, i.e., an event

### Relationships
- exemplifies: [OccurrenceKind](/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)
- has-location: [Location](/CMNS/Locations/Location.md)
- is-classified-by: [OccurrenceKind](/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)
