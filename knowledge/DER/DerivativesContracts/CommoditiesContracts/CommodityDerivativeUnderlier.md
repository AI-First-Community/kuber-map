---
type: FIBO Class
title: "commodity derivative underlier"
description: "underlier of a commodity derivative, including, but not limited to, the negotiable commodity itself"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivativeUnderlier
tags: [DER, Release]
detail: "The underlying of a commodity swap may include a physical commodity, or the price, or behavior of the price, or any other aspect of a physical commodity."
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/Underlier.md", provenance: fibo}
  - {type: has-as-of-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: has-commodity-value-as-of-date, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-quantity-value, target: "/CMNS/QuantitiesAndUnits/ScalarQuantityValue.md", provenance: fibo}
  - {type: involves, target: "/FND/ProductsAndServices/ProductsAndServices/Commodity.md", provenance: fibo}
---

underlier of a commodity derivative, including, but not limited to, the negotiable commodity itself

### Relationships
- is-a: [Underlier](/FBC/FinancialInstruments/FinancialInstruments/Underlier.md)
- has-as-of-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- has-commodity-value-as-of-date: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-quantity-value: [ScalarQuantityValue](/CMNS/QuantitiesAndUnits/ScalarQuantityValue.md)
- involves: [Commodity](/FND/ProductsAndServices/ProductsAndServices/Commodity.md)
