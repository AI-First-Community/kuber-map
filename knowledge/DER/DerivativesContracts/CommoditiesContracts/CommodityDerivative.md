---
type: FIBO Class
title: "commodity derivative"
description: "derivative instrument whose primary underlying item is a physical commodity, or the price, or related index, or any other aspect related to a physical commodity"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative
tags: [DER, Release]
detail: "The price of any commodity used as the basis for a commodity derivative may vary according to supply and demand as of the execution date of the contract and at various other times during the lifetime of the contract depending on contract terms. Valuation of a commodity derivative may depend on the spot price for the underlying commodity, futures price, supply and demand, convenience yield, cost of money and/or interest rates, volatility, which models were used to predict future pricing, and so forth."
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/CommodityInstrument.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md", provenance: fibo}
  - {type: has-underlier, target: "/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivativeUnderlier.md", provenance: fibo}
---

derivative instrument whose primary underlying item is a physical commodity, or the price, or related index, or any other aspect related to a physical commodity

### Relationships
- is-a: [CommodityInstrument](/FBC/FinancialInstruments/FinancialInstruments/CommodityInstrument.md)
- is-a: [DerivativeInstrument](/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)
- has-underlier: [CommodityDerivativeUnderlier](/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivativeUnderlier.md)
