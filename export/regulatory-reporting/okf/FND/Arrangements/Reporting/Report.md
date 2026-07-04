---
type: FIBO Class
title: "report"
description: "document that provides a structured description of something, prepared on ad hoc, periodic, recurring, regular, or as required basis"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Report
tags: [FND, Release]
core: true
use_cases:
  - "Regulatory Reporting & Compliance (supervisory filing)"
detail: "Reports may refer to specific periods, events, occurrences, or subjects, and may be communicated or presented in oral, electronic, or written form."
examples:
  - "An annual report filed by a company with its regulator."
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/Documents/Document.md", provenance: fibo}
  - {type: has-report-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: has-report-date-time, target: "/CMNS/DatesAndTimes/DateTime.md", provenance: fibo}
  - {type: has-reporting-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
  - {type: is-provided-by, target: "/FND/Arrangements/Reporting/ReportingParty.md", provenance: fibo}
  - {type: is-reported-to, target: "/CMNS/PartiesAndSituations/PartyRole.md", provenance: fibo}
  - {type: is-submitted-by, target: "/FND/Arrangements/Reporting/Submitter.md", provenance: fibo}
  - {type: is-submitted-to, target: "/CMNS/PartiesAndSituations/PartyRole.md", provenance: fibo}
---

document that provides a structured description of something, prepared on ad hoc, periodic, recurring, regular, or as required basis

### Relationships
- is-a: [Document](/CMNS/Documents/Document.md)
- has-report-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- has-report-date-time: [DateTime](/CMNS/DatesAndTimes/DateTime.md)
- has-reporting-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
- is-provided-by: [ReportingParty](/FND/Arrangements/Reporting/ReportingParty.md)
- is-reported-to: [PartyRole](/CMNS/PartiesAndSituations/PartyRole.md)
- is-submitted-by: [Submitter](/FND/Arrangements/Reporting/Submitter.md)
- is-submitted-to: [PartyRole](/CMNS/PartiesAndSituations/PartyRole.md)
