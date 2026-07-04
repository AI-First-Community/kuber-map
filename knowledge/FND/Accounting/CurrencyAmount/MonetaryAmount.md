---
type: FIBO Class
title: "monetary amount"
description: "measure that is an amount of money specified in monetary units"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
tags: [FND, Release]
core: true
detail: "A measured amount of money in a currency; the type used for principal, payments, income, and valuations throughout origination."
detail_provenance: curated
examples:
  - "$300,000.00 USD"
  - "€1,500.00"
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/ScalarQuantityValue.md", provenance: fibo}
  - {type: has-currency, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
---

measure that is an amount of money specified in monetary units

### Relationships
- is-a: [ScalarQuantityValue](/CMNS/QuantitiesAndUnits/ScalarQuantityValue.md)
- has-currency: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
