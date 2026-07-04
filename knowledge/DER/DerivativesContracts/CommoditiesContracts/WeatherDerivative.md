---
type: FIBO Class
title: "weather derivative"
description: "derivative instrument whose primary underlying notional item is based on something related to the weather, for example, the average temperature in Chicago in January"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/WeatherDerivative
tags: [DER, Release]
detail: "In the CFI standard, weather is classified as an environmental resource. Such a derivative can be used to hedge risks related to the demand for heating fuel or electricity. The underlying 'asset' is not a negotiable commodity per se, but because the weather can impact the prices and other things related to other commodities, weather derivatives are treated as commodity derivatives for regulatory purposes."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md", provenance: fibo}
---

derivative instrument whose primary underlying notional item is based on something related to the weather, for example, the average temperature in Chicago in January

### Relationships
- is-a: [CommodityDerivative](/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative.md)
- is-a: [DerivativeInstrument](/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)
