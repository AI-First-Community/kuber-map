---
type: FIBO Class
title: "regional sovereignty"
description: "legal person that corresponds to an administrative division, administrative unit, administrative entity or country subdivision (or, sometimes, geopolitical division or subnational entity), that has the capacity to incur debt, issue contracts, and enter into relations with other similar entities"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/RegionalSovereignty
tags: [BE, Release]
examples:
  - "A country may be divided into provinces, which, in turn, are divided into counties, which, in turn, may be divided in whole or in part into municipalities; and so on."
relations:
  - {type: is-a, target: "/BE/GovernmentEntities/GovernmentEntities/Polity.md", provenance: fibo}
  - {type: has-shared-sovereignty-over, target: "/CMNS/Locations/GeopoliticalEntity.md", provenance: fibo}
  - {type: is-represented-by, target: "/BE/GovernmentEntities/GovernmentEntities/RegionalGovernment.md", provenance: fibo}
---

legal person that corresponds to an administrative division, administrative unit, administrative entity or country subdivision (or, sometimes, geopolitical division or subnational entity), that has the capacity to incur debt, issue contracts, and enter into relations with other similar entities

### Relationships
- is-a: [Polity](/BE/GovernmentEntities/GovernmentEntities/Polity.md)
- has-shared-sovereignty-over: [GeopoliticalEntity](/CMNS/Locations/GeopoliticalEntity.md)
- is-represented-by: [RegionalGovernment](/BE/GovernmentEntities/GovernmentEntities/RegionalGovernment.md)
