---
type: FIBO Class
title: "street address"
description: "index to a location that consists of a primary address number, predirectional, street name, suffix, postdirectional, and an optional secondary unit"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/StreetAddress
tags: [FND, Release]
relations:
  - {type: has-predirectional-symbol, target: "/FND/Places/Addresses/PredirectionalSymbol.md", provenance: fibo}
  - {type: has-secondary-unit, target: "/FND/Places/Addresses/SecondaryUnit.md", provenance: fibo}
  - {type: has-postdirectional-symbol, target: "/FND/Places/Addresses/PostdirectionalSymbol.md", provenance: fibo}
  - {type: has-primary-address-number, target: "/FND/Places/Addresses/PrimaryAddressNumber.md", provenance: fibo}
  - {type: has-street-name, target: "/FND/Places/Addresses/StreetName.md", provenance: fibo}
  - {type: has-street-suffix, target: "/FND/Places/Addresses/StreetSuffix.md", provenance: fibo}
  - {type: is-a, target: "/FND/Places/Addresses/AddressComponent.md", provenance: fibo}
---

index to a location that consists of a primary address number, predirectional, street name, suffix, postdirectional, and an optional secondary unit

### Relationships
- has-predirectional-symbol: [PredirectionalSymbol](/FND/Places/Addresses/PredirectionalSymbol.md)
- has-secondary-unit: [SecondaryUnit](/FND/Places/Addresses/SecondaryUnit.md)
- has-postdirectional-symbol: [PostdirectionalSymbol](/FND/Places/Addresses/PostdirectionalSymbol.md)
- has-primary-address-number: [PrimaryAddressNumber](/FND/Places/Addresses/PrimaryAddressNumber.md)
- has-street-name: [StreetName](/FND/Places/Addresses/StreetName.md)
- has-street-suffix: [StreetSuffix](/FND/Places/Addresses/StreetSuffix.md)
- is-a: [AddressComponent](/FND/Places/Addresses/AddressComponent.md)
