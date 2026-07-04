---
type: FIBO Class
title: "cash settlement terms"
description: "contractual commitment to settle in cash"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/CashSettlementTerms
tags: [FBC, Release]
detail: "Note that the security price represents a price per share or per lot, whereas the settlement amount represents a total."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md", provenance: fibo}
  - {type: has-price, target: "/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md", provenance: fibo}
  - {type: has-settlement-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-settlement-method, target: "/FBC/FinancialInstruments/Settlement/DeliveryInCash.md", provenance: fibo}
---

contractual commitment to settle in cash

### Relationships
- is-a: [SettlementTerms](/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md)
- has-price: [SecurityPrice](/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
- has-settlement-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-settlement-method: [DeliveryInCash](/FBC/FinancialInstruments/Settlement/DeliveryInCash.md)
