---
type: FIBO Class
title: "commodity swap"
description: "commodity derivative that includes, without limitation, any swap for which the primary underlying notional item is a physical commodity, or the price, or behavior of the price, or the level of a commodity index, or other aspect related to a physical commodity"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommoditySwap
tags: [DER, Release]
detail: "Commodities that can be swapped include: energy. metal, agriculture, environmental, freight, polypropylene products, fertilizer, paper, single and multiple commodity indexes and baskets, and multi-commodity assets where each leg references a different commodity. Commodity swaps typically involve the exchange of a floating commodity price for a set price over an agreed-upon period."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative.md", provenance: fibo}
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/ReturnSwap.md", provenance: fibo}
  - {type: has-return-leg, target: "/DER/DerivativesContracts/CommoditiesContracts/CommodityReturnLeg.md", provenance: fibo}
---

commodity derivative that includes, without limitation, any swap for which the primary underlying notional item is a physical commodity, or the price, or behavior of the price, or the level of a commodity index, or other aspect related to a physical commodity

### Relationships
- is-a: [CommodityDerivative](/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative.md)
- is-a: [ReturnSwap](/DER/DerivativesContracts/Swaps/ReturnSwap.md)
- has-return-leg: [CommodityReturnLeg](/DER/DerivativesContracts/CommoditiesContracts/CommodityReturnLeg.md)
