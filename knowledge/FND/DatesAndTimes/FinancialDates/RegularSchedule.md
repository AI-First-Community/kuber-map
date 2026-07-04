---
type: FIBO Class
title: "regular schedule"
description: "schedule whose time intervals recur regularly"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/FinancialDates/RegularSchedule
tags: [FND, Release]
detail: "A RegularSchedule is a Schedule defined as a set of Dates that start on a recurrence start date and repeat after each recurrence interval. The size of this set is defined by a count.  The 'initial ScheduleStub' associated with a RegularSchedule identifies any special treatment applied before the recurrence start date. Similarly, a 'final ScheduleStub' identifies any special handling at the end of the recurrences. For example, a mortgage loan that is due each calendar month may have an initial payment due before the first calendar month, or a final payment due after the last monthly payment. A parametric schedule is a regular schedule for one of the events that occur in a periodic schedule of interest accruals, interest payments, and (for floating rate swapstreams), changes to the interest rate. Parametric schedules may be specified individually but more commonly, calculation events are scheduled, with other dates specified as offsets. In a regular schedule, related dates may be independently parametrically scheduled. Other ontologies can extend RegularSchedule as needed.  In particular, the Occurrences ontology extends RegularSchedule to 'comprise' an 'OccurrenceKind'. The intended meaning is that a regular schedule comprises a number of scheduled dates and an event which is scheduled to occur on each of those dates, in other words an Occurrence of the OccurrenceKind should happen on each Date defined by the RegularSchedule. The recurrence start date can be an ExplicitDate or any kind of CalculatedDate. Hence, the starting date could be relative to another Date (e.g. T+3) or triggered by the Occurrence of an OccurrenceKind, etc.  The recurrence start date can also be relative to the starting Date of the overall DatePeriod of the Schedule."
examples:
  - "A 30 year mortgage is payable monthly on the 10th of the month, starting July 2015. The mortgage is issued on June 15, 2015 so the first payment is for the period June 15-June 30, and the last payment is for June 1-14 2045.  The payment schedule is a RegularSchedule with these properties:  * comprises: regular payment OccurrenceKind (with payment details) (see the 'comprises' property of the Occurrences ontology) * hasInitialStub: June 15-30, 2015 for initial payment * hasFinalStub: June 1-14, 2045 for final payment * hasCount: 358 * hasOverallPeriod starting Date: June 15, 2015 with a duration of 30 years * hasRecurrenceInterval: specifies 10th day of each calendar month * hasRecurrenceStartDate: July 1, 2015"
  - "A corporate bond pays interest for 10 years starting on the first day of 2015. Interest payments are due 15 days after the expiration of each 6 month period: on July 15 and January 16.  The payment schedule is a RegularSchedule, with these properties:  * comprises: identifies the interest payment details * overall DatePeriod starting date is '2015-01-01', ending date is '2025-01-15', and duration is 'P10Y15D' * hasCount is 20 (2 payments per year for 10 years) * hasRecurrenceInterval is 'P6M' * hasRecurrenceStartDate is '2015-01-15'"
  - "An ISDA FpML schedule has a specified date (via a convention), and a date roll rule which is specified for the whole schedule and applies to each of the dates returned by the parametric specification of the schedule. It has: (1) a schedule beginning and end; (2) a set of regular repeating periods: the scheduled event takes place once per period; (3) optionally one or two stubs (one start and one end), which may be longer than the repeating period, or shorter. The precise parameters used are: Start of the overall Schedule period: Effective Date End of the overall Schedule period: Termination Date Start of first regular period: not specified (assume Effective Date) Length of each regular period: Frequency (a duration) There are generally three ways in which the regular periods of a parametric schedule may be expressed: first plus last first plus period length last plus period length event date plus period length. In FpML, Roll events (the date that something rolls over from the value used in one period to the value used in the next) is defined in a Roll Convention, which may be a day of the month, a day of the week, or some published set of dates, typically the ISDA quarterly dates for these events. This is therefore the date within the regular period (before adjustments) when the event occurs. This is in addition to a date for the start or end of such a period. In general this applies to the Calculation Schedule (i.e. the event is the calculation event) with other dates specified relative to this, however in principle the other related events (payment and reset or refix) are specified relative to this."
synonyms:
  - "parametric schedule"
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/Schedule.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Collections/StructuredCollection.md", provenance: fibo}
  - {type: comprises, target: "/FND/DatesAndTimes/Occurrences/OccurrenceKind.md", provenance: fibo}
  - {type: has-anchor-date, target: "/FND/DatesAndTimes/FinancialDates/AnchorDate.md", provenance: fibo}
  - {type: has-business-day-convention, target: "/FND/DatesAndTimes/BusinessDates/BusinessDayConvention.md", provenance: fibo}
  - {type: has-final-stub, target: "/FND/DatesAndTimes/FinancialDates/ScheduleStub.md", provenance: fibo}
  - {type: has-initial-stub, target: "/FND/DatesAndTimes/FinancialDates/ScheduleStub.md", provenance: fibo}
  - {type: has-occurrence, target: "/FND/DatesAndTimes/Occurrences/Occurrence.md", provenance: fibo}
  - {type: has-recurrence-interval, target: "/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md", provenance: fibo}
---

schedule whose time intervals recur regularly

### Relationships
- is-a: [Schedule](/FND/DatesAndTimes/FinancialDates/Schedule.md)
- is-a: [StructuredCollection](/CMNS/Collections/StructuredCollection.md)
- comprises: [OccurrenceKind](/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)
- has-anchor-date: [AnchorDate](/FND/DatesAndTimes/FinancialDates/AnchorDate.md)
- has-business-day-convention: [BusinessDayConvention](/FND/DatesAndTimes/BusinessDates/BusinessDayConvention.md)
- has-final-stub: [ScheduleStub](/FND/DatesAndTimes/FinancialDates/ScheduleStub.md)
- has-initial-stub: [ScheduleStub](/FND/DatesAndTimes/FinancialDates/ScheduleStub.md)
- has-occurrence: [Occurrence](/FND/DatesAndTimes/Occurrences/Occurrence.md)
- has-recurrence-interval: [RecurrenceInterval](/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
