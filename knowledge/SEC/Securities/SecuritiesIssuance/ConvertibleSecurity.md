---
type: FIBO Class
title: "convertible security"
description: "security that can be converted into another security"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/ConvertibleSecurity
tags: [SEC, Release]
examples:
  - "Convertible securities may be convertible bonds or preferred stocks that pay regular interest and can be converted into shares of common stock (sometimes conditioned on the stock price appreciating to a predetermined level)."
  - "Warrants are equity convertible securities. They give the owner the option to buy newly issued shares at a determined exercise price and date."
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
  - {type: has-contractual-element, target: "/SEC/Securities/SecuritiesIssuance/ConversionTerms.md", provenance: fibo}
---

security that can be converted into another security

### Relationships
- is-a: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- has-contractual-element: [ConversionTerms](/SEC/Securities/SecuritiesIssuance/ConversionTerms.md)
