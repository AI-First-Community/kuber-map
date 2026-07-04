---
type: FIBO Class
title: "business center code"
description: "code used to denote a metropolitan area where business is conducted"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCenters/BusinessCenterCode
tags: [FBC, Release]
detail: "The codes for business centers and municipalities defined herein are largely those identified either as FpML business centers or are locations where there is an exchange, as noted in the ISO 10962 MIC code standard."
relations:
  - {type: is-a, target: "/CMNS/Locations/GeographicRegionIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/CMNS/Locations/BusinessCenter.md", provenance: fibo}
---

code used to denote a metropolitan area where business is conducted

### Relationships
- is-a: [GeographicRegionIdentifier](/CMNS/Locations/GeographicRegionIdentifier.md)
- identifies: [BusinessCenter](/CMNS/Locations/BusinessCenter.md)
