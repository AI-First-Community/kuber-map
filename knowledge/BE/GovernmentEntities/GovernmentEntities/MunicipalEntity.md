---
type: FIBO Class
title: "municipal entity"
description: "polity that typically represents a city, township, or other administrative subdivision having corporate status and powers of self-government or jurisdiction"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/MunicipalEntity
tags: [BE, Release]
relations:
  - {type: is-a, target: "/BE/GovernmentEntities/GovernmentEntities/Polity.md", provenance: fibo}
  - {type: has-sovereignty-over, target: "/CMNS/Locations/Municipality.md", provenance: fibo}
  - {type: is-represented-by, target: "/BE/GovernmentEntities/GovernmentEntities/MunicipalGovernment.md", provenance: fibo}
---

polity that typically represents a city, township, or other administrative subdivision having corporate status and powers of self-government or jurisdiction

### Relationships
- is-a: [Polity](/BE/GovernmentEntities/GovernmentEntities/Polity.md)
- has-sovereignty-over: [Municipality](/CMNS/Locations/Municipality.md)
- is-represented-by: [MunicipalGovernment](/BE/GovernmentEntities/GovernmentEntities/MunicipalGovernment.md)
