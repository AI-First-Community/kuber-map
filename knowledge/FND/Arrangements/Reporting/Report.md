---
type: FIBO Class
title: "report"
description: "document that provides a structured description of something, prepared on ad hoc, periodic, recurring, regular, or as required basis"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Report
tags: [FND, Release]
relations:
  - {type: is-submitted-to, target: "/CMNS/PartiesAndSituations/PartyRole.md", provenance: fibo}
  - {type: is-provided-by, target: "/FND/Arrangements/Reporting/ReportingParty.md", provenance: fibo}
  - {type: has-reporting-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
  - {type: has-report-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: is-reported-to, target: "/CMNS/PartiesAndSituations/PartyRole.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Documents/Document.md", provenance: fibo}
  - {type: has-report-date-time, target: "/CMNS/DatesAndTimes/DateTime.md", provenance: fibo}
  - {type: is-submitted-by, target: "/FND/Arrangements/Reporting/Submitter.md", provenance: fibo}
---

document that provides a structured description of something, prepared on ad hoc, periodic, recurring, regular, or as required basis

### Relationships
- is-submitted-to: [PartyRole](/CMNS/PartiesAndSituations/PartyRole.md)
- is-provided-by: [ReportingParty](/FND/Arrangements/Reporting/ReportingParty.md)
- has-reporting-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
- has-report-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- is-reported-to: [PartyRole](/CMNS/PartiesAndSituations/PartyRole.md)
- is-a: [Document](/CMNS/Documents/Document.md)
- has-report-date-time: [DateTime](/CMNS/DatesAndTimes/DateTime.md)
- is-submitted-by: [Submitter](/FND/Arrangements/Reporting/Submitter.md)
