---
type: FIBO Class
title: "exchange rate"
description: "rate at which one currency can be exchanged for another"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/ExchangeRate
tags: [FND, Release]
examples:
  - "The exchange rate between the U.S. dollar and British pound is distinct from the exchange rate between the U.S. dollar and the euro."
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Ratio.md", provenance: fibo}
  - {type: has-base-currency, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
  - {type: has-dealt-currency, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
---

rate at which one currency can be exchanged for another

### Relationships
- is-a: [Ratio](/CMNS/QuantitiesAndUnits/Ratio.md)
- has-base-currency: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
- has-dealt-currency: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
