---
type: FIBO Class
title: "ad hoc schedule entry"
description: "entry, including a date or date and time, among multiple non-regularly-recurring entries in a schedule"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/AdHocScheduleEntry
tags: [FND, Release]
detail: "Other ontologies can extend AdHocScheduleEntry as needed. In particular, the Occurrences ontology extends AdHocScheduleEntry to consist of occurrences (events) of a given OccurrenceKind. The meaning is that an ad hoc schedule entry comprises a date and an event which is scheduled to occur on that date. The Date of an AdHocScheduleEntry can be an ExplicitDate or any kind of CalculatedDate, such as:  * An OccurrenceBasedDate -- a Date that itself is defined by an Occurrence (see the Occurrences ontology) * A RelativeDate - a Date relative to another Date, such as T+3 * A SpecifiedDate - a Date that is defined by an arbitrary rule The cmns-dt;hasDate property may be used to reify a date, if it is important to do so for a given application, or if not and typically, the inherited cmns-dt;hasObservedDateTime property may be used together with a cmns-dt;CombinedDateTime value, as long as the resulting schedule is consistent in using one or the other."
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md", provenance: fibo}
  - {type: has-occurrence, target: "/FND/DatesAndTimes/Occurrences/Occurrence.md", provenance: fibo}
---

entry, including a date or date and time, among multiple non-regularly-recurring entries in a schedule

### Relationships
- is-a: [DatedCollectionConstituent](/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md)
- has-occurrence: [Occurrence](/FND/DatesAndTimes/Occurrences/Occurrence.md)
