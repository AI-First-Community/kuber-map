---
type: FIBO Class
title: "value-added tax identification number"
description: "tax identifier that identifies a taxable person (business) or non-taxable legal entity for a consumption tax that is assessed incrementally, levied on the price of a product or service at each stage of production, distribution, and sale to the end consumer"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/ValueAddedTaxIdentificationNumber
tags: [BE, Release]
detail: "If the ultimate consumer is a business that collects and pays to the government VAT on its products or services, it can reclaim the tax paid. Not all localities require VAT to be charged, and exports are often exempt. VAT is usually implemented as a destination-based tax, where the tax rate is based on the location of the consumer and applied to the sales price."
synonyms:
  - "VAT identification number"
  - "VAT registration number"
  - "VATIN"
relations:
  - {type: is-a, target: "/FND/Parties/Parties/TaxIdentifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Organizations/OrganizationIdentifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegisteredIdentifier.md", provenance: fibo}
---

tax identifier that identifies a taxable person (business) or non-taxable legal entity for a consumption tax that is assessed incrementally, levied on the price of a product or service at each stage of production, distribution, and sale to the end consumer

### Relationships
- is-a: [TaxIdentifier](/FND/Parties/Parties/TaxIdentifier.md)
- is-a: [OrganizationIdentifier](/CMNS/Organizations/OrganizationIdentifier.md)
- is-a: [RegisteredIdentifier](/CMNS/RegistrationAuthorities/RegisteredIdentifier.md)
