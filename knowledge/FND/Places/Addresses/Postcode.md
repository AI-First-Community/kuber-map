---
type: FIBO Class
title: "postcode"
description: "sequence of characters used to assist in the sorting of mail"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Postcode
tags: [FND, Release]
relations:
  - {type: identifies, target: "/FND/Places/Addresses/PostCodeArea.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/CodesAndCodeSets/CodeElement.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Locations/GeographicRegionIdentifier.md", provenance: fibo}
---

sequence of characters used to assist in the sorting of mail

### Relationships
- identifies: [PostCodeArea](/FND/Places/Addresses/PostCodeArea.md)
- is-a: [CodeElement](/CMNS/CodesAndCodeSets/CodeElement.md)
- is-a: [GeographicRegionIdentifier](/CMNS/Locations/GeographicRegionIdentifier.md)
