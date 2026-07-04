---
type: FIBO Class
title: "party role"
description: "role played by an organization or individual that may be time bound"
resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
tags: [CMNS]
examples:
  - "Examples include organization member, employee, issuer, owner, partner in a partnership, shareholder, and so forth."
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/AgentRole.md", provenance: fibo}
  - {type: has-applicable-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
  - {type: is-played-by, target: "/CMNS/PartiesAndSituations/Party.md", provenance: fibo}
---

role played by an organization or individual that may be time bound

### Relationships
- is-a: [AgentRole](/CMNS/PartiesAndSituations/AgentRole.md)
- has-applicable-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
- is-played-by: [Party](/CMNS/PartiesAndSituations/Party.md)
