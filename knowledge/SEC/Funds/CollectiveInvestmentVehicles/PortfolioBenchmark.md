---
type: FIBO Class
title: "portfolio benchmark"
description: "Security or other price against which the performance of the portfolio is evaluated."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/PortfolioBenchmark
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Measure.md", provenance: fibo}
  - {type: applies-to, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolio.md", provenance: fibo}
  - {type: defines-benchmark, target: "/IND/Indicators/Indicators/MarketRate.md", provenance: fibo}
---

Security or other price against which the performance of the portfolio is evaluated.

### Relationships
- is-a: [Measure](/CMNS/QuantitiesAndUnits/Measure.md)
- applies-to: [FundPortfolio](/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolio.md)
- defines-benchmark: [MarketRate](/IND/Indicators/Indicators/MarketRate.md)
