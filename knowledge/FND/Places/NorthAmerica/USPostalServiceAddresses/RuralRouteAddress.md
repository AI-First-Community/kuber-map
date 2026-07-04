---
type: FIBO Class
title: "rural route address"
description: "delivery address whose delivery address line uses the abbreviation 'RR', followed by the route identifier, followed by 'BOX' followed by box number, in place of a street address"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/RuralRouteAddress
tags: [FND, Release]
relations:
  - {type: comprises, target: "/FND/Places/NorthAmerica/USPostalServiceAddresses/RuralRoute.md", provenance: fibo}
  - {type: comprises, target: "/FND/Places/NorthAmerica/USPostalServiceAddresses/Mailbox.md", provenance: fibo}
  - {type: is-a, target: "/FND/Places/Addresses/PhysicalAddress.md", provenance: fibo}
---

delivery address whose delivery address line uses the abbreviation 'RR', followed by the route identifier, followed by 'BOX' followed by box number, in place of a street address

### Relationships
- comprises: [RuralRoute](/FND/Places/NorthAmerica/USPostalServiceAddresses/RuralRoute.md)
- comprises: [Mailbox](/FND/Places/NorthAmerica/USPostalServiceAddresses/Mailbox.md)
- is-a: [PhysicalAddress](/FND/Places/Addresses/PhysicalAddress.md)
