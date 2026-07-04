---
type: FIBO Class
title: "listing"
description: "catalog entry for a securities offering managed by an exchange that provides the terms under which that security is made available on that exchange"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/Listing
tags: [SEC, Release]
core: true
examples:
  - "Apple Inc.'s listing on the Nasdaq Stock Market under ticker AAPL."
examples_provenance: curated
synonyms:
  - "market listing"
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesIdentification/SecurityRegistryEntry.md", provenance: fibo}
  - {type: has-currency, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
  - {type: has-last-trading-date-and-time, target: "/CMNS/DatesAndTimes/DateTime.md", provenance: fibo}
  - {type: has-registration-status, target: "/FBC/FunctionalEntities/BusinessRegistries/RegistrationStatus.md", provenance: fibo}
  - {type: has-restriction, target: "/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction.md", provenance: fibo}
  - {type: has-tick-size, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: lists, target: "/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md", provenance: fibo}
---

catalog entry for a securities offering managed by an exchange that provides the terms under which that security is made available on that exchange

### Relationships
- is-a: [SecurityRegistryEntry](/SEC/Securities/SecuritiesIdentification/SecurityRegistryEntry.md)
- has-currency: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
- has-last-trading-date-and-time: [DateTime](/CMNS/DatesAndTimes/DateTime.md)
- has-registration-status: [RegistrationStatus](/FBC/FunctionalEntities/BusinessRegistries/RegistrationStatus.md)
- has-restriction: [SecuritiesRestriction](/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction.md)
- has-tick-size: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- lists: [SecuritiesOffering](/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md)
