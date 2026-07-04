---
type: FIBO Class
title: "commodity future"
description: "futures contract to buy or sell a predetermined amount of a commodity at a specific price on a specific date in the future"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityFuture
tags: [DER, Release]
detail: "A commodity future is an agreement to purchase or sell a commodity for delivery in the future: (1) at a price that is determined at initiation of the contract; (2) that obligates each party to the contract to fulfill the contract at the specified price; (3) that is used to assume or shift price risk; and (4) that may be satisfied by delivery or offset."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/Future.md", provenance: fibo}
---

futures contract to buy or sell a predetermined amount of a commodity at a specific price on a specific date in the future

### Relationships
- is-a: [CommodityDerivative](/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative.md)
- is-a: [Future](/FBC/FinancialInstruments/FinancialInstruments/Future.md)
