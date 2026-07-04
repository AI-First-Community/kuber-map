---
type: FIBO Class
title: "price volatility"
description: "statistical measure of the rate of change in pricing for a given security or market index"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/PriceVolatility
tags: [IND, Release]
detail: "Volatility can be determined using the standard deviation or variance among prices for the security or market index over some period of time. For a specific security, volatility may measure the amount and frequency in rapid price fluctuation. It is computed as the annualized standard deviation of the percentage change in a security's daily price."
relations:
  - {type: is-a, target: "/IND/Indicators/Indicators/Volatility.md", provenance: fibo}
  - {type: has-argument, target: "/IND/Indicators/Indicators/PriceStructure.md", provenance: fibo}
---

statistical measure of the rate of change in pricing for a given security or market index

### Relationships
- is-a: [Volatility](/IND/Indicators/Indicators/Volatility.md)
- has-argument: [PriceStructure](/IND/Indicators/Indicators/PriceStructure.md)
