---
type: FIBO Class
title: "taxpayer identification number"
description: "identification number used by the Internal Revenue Service (IRS) in the administration of tax laws in the United States"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/TaxpayerIdentificationNumber
tags: [FBC, Release]
detail: "A TIN must be furnished on returns, statements, and other tax related documents. For example a number must be furnished: - When filing tax returns. - When claiming treaty benefits.  A TIN must be on a withholding certificate if the beneficial owner is claiming any of the following: - Tax treaty benefits (other than for income from marketable securities) - Exemption for effectively connected income - Exemption for certain annuities."
synonyms:
  - "TIN"
relations:
  - {type: is-a, target: "/FND/Parties/Parties/TaxIdentifier.md", provenance: fibo}
  - {type: is-applicable-in, target: "/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction.md", provenance: fibo}
  - {type: is-member-of, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/TaxpayerIdentificationNumberingScheme.md", provenance: fibo}
---

identification number used by the Internal Revenue Service (IRS) in the administration of tax laws in the United States

### Relationships
- is-a: [TaxIdentifier](/FND/Parties/Parties/TaxIdentifier.md)
- is-applicable-in: [UnitedStatesJurisdiction](/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction.md)
- is-member-of: [TaxpayerIdentificationNumberingScheme](/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/TaxpayerIdentificationNumberingScheme.md)
