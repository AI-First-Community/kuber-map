---
type: FIBO Class
title: "commodity instrument"
description: "financial instrument representing an ownership interest in bulk goods, such as raw materials and primary agricultural products"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/CommodityInstrument
tags: [FBC, Release]
detail: "The value of the contract is derived from the market value of an underlying commodity or commodity index. Commodity derivatives can be physically or cash settled. Primary underliers include metals, agricultural goods and energy."
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md", provenance: fibo}
  - {type: has-commodity-value-as-of-execution-date, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-quantity-value, target: "/CMNS/QuantitiesAndUnits/ScalarQuantityValue.md", provenance: fibo}
  - {type: involves, target: "/FND/ProductsAndServices/ProductsAndServices/Commodity.md", provenance: fibo}
---

financial instrument representing an ownership interest in bulk goods, such as raw materials and primary agricultural products

### Relationships
- is-a: [FinancialInstrument](/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)
- has-commodity-value-as-of-execution-date: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-quantity-value: [ScalarQuantityValue](/CMNS/QuantitiesAndUnits/ScalarQuantityValue.md)
- involves: [Commodity](/FND/ProductsAndServices/ProductsAndServices/Commodity.md)
