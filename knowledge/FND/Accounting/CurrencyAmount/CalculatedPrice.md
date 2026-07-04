---
type: FIBO Class
title: "calculated price"
description: "monetary price determined by a formula"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/CalculatedPrice
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/MonetaryPrice.md", provenance: fibo}
  - {type: has-expression, target: "/CMNS/QuantitiesAndUnits/Expression.md", provenance: fibo}
  - {type: uses, target: "/FBC/FinancialInstruments/InstrumentPricing/PricingModel.md", provenance: fibo}
---

monetary price determined by a formula

### Relationships
- is-a: [MonetaryPrice](/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- has-expression: [Expression](/CMNS/QuantitiesAndUnits/Expression.md)
- uses: [PricingModel](/FBC/FinancialInstruments/InstrumentPricing/PricingModel.md)
