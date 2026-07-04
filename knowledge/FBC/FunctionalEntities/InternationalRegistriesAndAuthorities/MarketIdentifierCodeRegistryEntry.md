---
type: FIBO Class
title: "market identifier code registry entry"
description: "entry in a market identifier code registry that conforms to ISO 10383"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/MarketIdentifierCodeRegistryEntry
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegistryEntry.md", provenance: fibo}
  - {type: comprises, target: "/FBC/FunctionalEntities/Markets/MarketIdentifier.md", provenance: fibo}
  - {type: has-market-identifier-code-status, target: "/FBC/FunctionalEntities/Markets/MarketIdentifierCodeStatus.md", provenance: fibo}
  - {type: is-included-in, target: "/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/MarketIdentifierCodeRegistry.md", provenance: fibo}
---

entry in a market identifier code registry that conforms to ISO 10383

### Relationships
- is-a: [RegistryEntry](/CMNS/RegistrationAuthorities/RegistryEntry.md)
- comprises: [MarketIdentifier](/FBC/FunctionalEntities/Markets/MarketIdentifier.md)
- has-market-identifier-code-status: [MarketIdentifierCodeStatus](/FBC/FunctionalEntities/Markets/MarketIdentifierCodeStatus.md)
- is-included-in: [MarketIdentifierCodeRegistry](/FBC/FunctionalEntities/InternationalRegistriesAndAuthorities/MarketIdentifierCodeRegistry.md)
