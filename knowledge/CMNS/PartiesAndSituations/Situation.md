---
type: FIBO Class
title: "situation"
description: "setting, state of being, or relationship that is relatively stable for some period of time"
resource: https://www.omg.org/spec/Commons/PartiesAndSituations/Situation
tags: [CMNS]
examples:
  - "Examples include ownership, control, possession, affiliation, beneficial ownership, employment, and other similar situations."
relations:
  - {type: has-object-role, target: "/CMNS/RolesAndCompositions/Role.md", provenance: fibo}
  - {type: has-subject-role, target: "/CMNS/RolesAndCompositions/Role.md", provenance: fibo}
  - {type: holds-during, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
---

setting, state of being, or relationship that is relatively stable for some period of time

### Relationships
- has-object-role: [Role](/CMNS/RolesAndCompositions/Role.md)
- has-subject-role: [Role](/CMNS/RolesAndCompositions/Role.md)
- holds-during: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
