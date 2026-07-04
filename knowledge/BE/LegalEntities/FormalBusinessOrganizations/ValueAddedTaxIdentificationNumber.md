---
type: FIBO Class
title: "value-added tax identification number"
description: "tax identifier that identifies a taxable person (business) or non-taxable legal entity for a consumption tax that is assessed incrementally, levied on the price of a product or service at each stage of production, distribution, and sale to the end consumer"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/ValueAddedTaxIdentificationNumber
tags: [BE, Release]
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
