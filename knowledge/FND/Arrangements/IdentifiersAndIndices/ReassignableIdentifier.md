---
type: FIBO Class
title: "reassignable identifier"
description: "identifier that uniquely identifies something for a given time period, and that may be reused to identify something else at a different point in time"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/ReassignableIdentifier
tags: [FND, Release]
detail: "If no assignment termination date is provided, the identifier is considered to be assigned and valid. If there is no initial assignment date, then the identifier is assumed to be assigned up until the termination date, if any."
examples:
  - "ticker symbol, vehicle license number, such as a vanity plate that can be reassigned and moved from one car to another"
relations:
  - {type: is-a, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
---

identifier that uniquely identifies something for a given time period, and that may be reused to identify something else at a different point in time

### Relationships
- is-a: [Identifier](/CMNS/Identifiers/Identifier.md)
