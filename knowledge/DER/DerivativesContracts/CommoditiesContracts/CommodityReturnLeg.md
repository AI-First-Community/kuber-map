---
type: FIBO Class
title: "commodity return leg"
description: "leg of a commodity return swap in which the return is based on a physical commodity, or the price, or behavior of the price, or any other aspect related to a physical commodity"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityReturnLeg
tags: [DER, Release]
detail: "The cash flows from a commodity may be negative as you have a cost from holding the commodity but there are no interim cash flows, so it equates to a negative interest rate. So a commodity swap is like a TRS in that it is based on the return on the increase in value."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/ReturnLeg.md", provenance: fibo}
  - {type: has-underlier, target: "/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivativeUnderlier.md", provenance: fibo}
---

leg of a commodity return swap in which the return is based on a physical commodity, or the price, or behavior of the price, or any other aspect related to a physical commodity

### Relationships
- is-a: [ReturnLeg](/DER/DerivativesContracts/Swaps/ReturnLeg.md)
- has-underlier: [CommodityDerivativeUnderlier](/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivativeUnderlier.md)
