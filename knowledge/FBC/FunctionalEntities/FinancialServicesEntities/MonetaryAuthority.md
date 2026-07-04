---
type: FIBO Class
title: "monetary authority"
description: "regulatory agency that controls the monetary policy, regulation and supply of money in some country or group of countries"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/MonetaryAuthority
tags: [FBC, Release]
examples:
  - "a central bank, the executive branch of a government, a central bank for several nations, a currency board"
relations:
  - {type: is-a, target: "/CMNS/RegulatoryAgencies/RegulatoryAgency.md", provenance: fibo}
  - {type: regulates-supply-of, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
---

regulatory agency that controls the monetary policy, regulation and supply of money in some country or group of countries

### Relationships
- is-a: [RegulatoryAgency](/CMNS/RegulatoryAgencies/RegulatoryAgency.md)
- regulates-supply-of: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
