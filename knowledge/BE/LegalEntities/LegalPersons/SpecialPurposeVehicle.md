---
type: FIBO Class
title: "special purpose vehicle"
description: "legal entity created to fulfill narrow, specific, and frequently temporary objectives"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/SpecialPurposeVehicle
tags: [BE, Release]
relations:
  - {type: is-a, target: "/CMNS/Organizations/LegalEntity.md", provenance: fibo}
  - {type: has-intended-liquidation-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
---

legal entity created to fulfill narrow, specific, and frequently temporary objectives

### Relationships
- is-a: [LegalEntity](/CMNS/Organizations/LegalEntity.md)
- has-intended-liquidation-date: [Date](/CMNS/DatesAndTimes/Date.md)
