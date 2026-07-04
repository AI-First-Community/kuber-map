---
type: FIBO Class
title: "dated collection constituent"
description: "element of a collection that is associated with a date and time"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent
tags: [FND, Release]
detail: "Note that the use of several options for the representation of a date and time stamp enables extensions for milliseconds, nanoseconds using an xsd:string that has the format of an xsd:dateTime datatype but extends the level of granularity consistently. An example of where this is required is to represent prices that change multiple times in a given day. The use of custom datatypes is outside the OWL 2 RL profile and so users should consider commenting out the restriction on hasObservedDateTime altogether or change the data range to rdfs:Literal in applications that are constrained to OWL 2 RL."
relations:
  - {type: is-a, target: "/CMNS/Collections/Constituent.md", provenance: fibo}
  - {type: has-observed-date-and-time, target: "/CMNS/DatesAndTimes/CombinedDateTime.md", provenance: fibo}
---

element of a collection that is associated with a date and time

### Relationships
- is-a: [Constituent](/CMNS/Collections/Constituent.md)
- has-observed-date-and-time: [CombinedDateTime](/CMNS/DatesAndTimes/CombinedDateTime.md)
