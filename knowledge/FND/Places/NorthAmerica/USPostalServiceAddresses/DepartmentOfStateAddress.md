---
type: FIBO Class
title: "Department of State address"
description: "delivery address whose delivery address line uses 'UNIT' followed by the unit identifier, followed by 'BOX' followed by box number, in place of a street address, 'DPO' as the literal value for the city, and the appropriate armed forces subdivision code in place of a subdivision (state) code"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/DepartmentOfStateAddress
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/Places/Addresses/PhysicalAddress.md", provenance: fibo}
  - {type: comprises, target: "/FND/Places/NorthAmerica/USPostalServiceAddresses/DepartmentOfStateUnitComponent.md", provenance: fibo}
  - {type: comprises, target: "/FND/Places/NorthAmerica/USPostalServiceAddresses/Mailbox.md", provenance: fibo}
---

delivery address whose delivery address line uses 'UNIT' followed by the unit identifier, followed by 'BOX' followed by box number, in place of a street address, 'DPO' as the literal value for the city, and the appropriate armed forces subdivision code in place of a subdivision (state) code

### Relationships
- is-a: [PhysicalAddress](/FND/Places/Addresses/PhysicalAddress.md)
- comprises: [DepartmentOfStateUnitComponent](/FND/Places/NorthAmerica/USPostalServiceAddresses/DepartmentOfStateUnitComponent.md)
- comprises: [Mailbox](/FND/Places/NorthAmerica/USPostalServiceAddresses/Mailbox.md)
