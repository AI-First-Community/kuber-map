---
type: FIBO Class
title: "highway contract address"
description: "delivery address whose delivery address line uses the abbreviation 'HC', followed by the route identifier, followed by 'BOX' followed by box number, in place of a street address"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/HighwayContractRouteAddress
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/Places/Addresses/PhysicalAddress.md", provenance: fibo}
  - {type: comprises, target: "/FND/Places/NorthAmerica/USPostalServiceAddresses/HighwayContractRoute.md", provenance: fibo}
  - {type: comprises, target: "/FND/Places/NorthAmerica/USPostalServiceAddresses/Mailbox.md", provenance: fibo}
---

delivery address whose delivery address line uses the abbreviation 'HC', followed by the route identifier, followed by 'BOX' followed by box number, in place of a street address

### Relationships
- is-a: [PhysicalAddress](/FND/Places/Addresses/PhysicalAddress.md)
- comprises: [HighwayContractRoute](/FND/Places/NorthAmerica/USPostalServiceAddresses/HighwayContractRoute.md)
- comprises: [Mailbox](/FND/Places/NorthAmerica/USPostalServiceAddresses/Mailbox.md)
