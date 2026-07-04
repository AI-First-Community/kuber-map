---
type: FIBO Class
title: "request"
description: "event in which some party asks another party for something at some point in time"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Request
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/Occurrence.md", provenance: fibo}
  - {type: exemplifies, target: "/FND/Arrangements/Reporting/RequestActivity.md", provenance: fibo}
  - {type: has-request-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: has-request-date-time, target: "/CMNS/DatesAndTimes/DateTime.md", provenance: fibo}
  - {type: is-requested-by, target: "/FND/Arrangements/Reporting/Requester.md", provenance: fibo}
  - {type: is-requested-of, target: "/CMNS/PartiesAndSituations/PartyRole.md", provenance: fibo}
---

event in which some party asks another party for something at some point in time

### Relationships
- is-a: [Occurrence](/FND/DatesAndTimes/Occurrences/Occurrence.md)
- exemplifies: [RequestActivity](/FND/Arrangements/Reporting/RequestActivity.md)
- has-request-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- has-request-date-time: [DateTime](/CMNS/DatesAndTimes/DateTime.md)
- is-requested-by: [Requester](/FND/Arrangements/Reporting/Requester.md)
- is-requested-of: [PartyRole](/CMNS/PartiesAndSituations/PartyRole.md)
