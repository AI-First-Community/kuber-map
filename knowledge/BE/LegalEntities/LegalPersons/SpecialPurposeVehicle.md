---
type: FIBO Class
title: "special purpose vehicle"
description: "legal entity created to fulfill narrow, specific, and frequently temporary objectives"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/SpecialPurposeVehicle
tags: [BE, Release]
detail: "A special purpose vehicle (SPV), also known as a special purpose entity (SPE), refers to a legal entity, typically a limited company or partnership, created to isolate a parent company from financial risk, including bankruptcy."
synonyms:
  - "SPE"
  - "SPV"
  - "special purpose entity"
relations:
  - {type: is-a, target: "/CMNS/Organizations/LegalEntity.md", provenance: fibo}
  - {type: has-intended-liquidation-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
---

legal entity created to fulfill narrow, specific, and frequently temporary objectives

### Relationships
- is-a: [LegalEntity](/CMNS/Organizations/LegalEntity.md)
- has-intended-liquidation-date: [Date](/CMNS/DatesAndTimes/Date.md)
