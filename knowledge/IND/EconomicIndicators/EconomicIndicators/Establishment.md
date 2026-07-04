---
type: FIBO Class
title: "establishment"
description: "an enterprise (or part of an enterprise) that operates from a single physical location"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Establishment
tags: [IND, Release]
detail: "The physical location of a certain economic activity - for example, a factory, mine, store, or office. An individual establishment is generally classified by having one NAICS code associated with it for statistical purposes, whereas an enterprise may be classified by multiple NAICS codes. The statistical structure is defined based on the operating structure and the accounting data produced by that entity. A given location may only need to publish revenues, whereas an operating unit (establishment) has employment statistics, etc. An establishment is defined as a producing unit at a single geographical location at which or from which economic activity is conducted and for which, at a minimum, employment data are available. In the case of a home-based business, the actual physical location would be specified as two distinct institutional units - as a household from a personal living and consumer perspective and as an establishment / operating unit due to the statistics required of the business."
relations:
  - {type: is-a, target: "/IND/EconomicIndicators/EconomicIndicators/InstitutionalUnit.md", provenance: fibo}
  - {type: has-address, target: "/FND/Places/Addresses/PhysicalAddress.md", provenance: fibo}
  - {type: is-constituent-of, target: "/IND/EconomicIndicators/EconomicIndicators/Enterprise.md", provenance: fibo}
---

an enterprise (or part of an enterprise) that operates from a single physical location

### Relationships
- is-a: [InstitutionalUnit](/IND/EconomicIndicators/EconomicIndicators/InstitutionalUnit.md)
- has-address: [PhysicalAddress](/FND/Places/Addresses/PhysicalAddress.md)
- is-constituent-of: [Enterprise](/IND/EconomicIndicators/EconomicIndicators/Enterprise.md)
