---
type: FIBO Class
title: "polity"
description: "legal person that is a supranational entity, crown, state, or subordinate civil authority, such as a province, prefecture, county, municipality, city, or district representing the people of that entity"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/Polity
tags: [BE, Release]
relations:
  - {type: is-a, target: "/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Organizations/LegalPerson.md", provenance: fibo}
  - {type: has-sovereignty-over, target: "/CMNS/Locations/GeopoliticalEntity.md", provenance: fibo}
  - {type: is-represented-by, target: "/BE/GovernmentEntities/GovernmentEntities/Government.md", provenance: fibo}
---

legal person that is a supranational entity, crown, state, or subordinate civil authority, such as a province, prefecture, county, municipality, city, or district representing the people of that entity

### Relationships
- is-a: [GovernmentBody](/BE/GovernmentEntities/GovernmentEntities/GovernmentBody.md)
- is-a: [LegalPerson](/CMNS/Organizations/LegalPerson.md)
- has-sovereignty-over: [GeopoliticalEntity](/CMNS/Locations/GeopoliticalEntity.md)
- is-represented-by: [Government](/BE/GovernmentEntities/GovernmentEntities/Government.md)
