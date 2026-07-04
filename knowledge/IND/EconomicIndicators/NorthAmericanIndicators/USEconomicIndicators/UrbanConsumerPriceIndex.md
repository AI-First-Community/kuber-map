---
type: FIBO Class
title: "urban consumer price index"
description: "an economic indicator representing a measure of the average change over time in the prices paid by urban consumers for a market basket of consumer goods and services"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/UrbanConsumerPriceIndex
tags: [IND, Release]
synonyms:
  - "CPI-U"
relations:
  - {type: is-a, target: "/IND/EconomicIndicators/EconomicIndicators/ConsumerPriceIndex.md", provenance: fibo}
  - {type: applies-to, target: "/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/UrbanConsumersUniverse.md", provenance: fibo}
  - {type: has-argument, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Basket.md", provenance: fibo}
  - {type: has-argument, target: "/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/UrbanConsumersUniverse.md", provenance: fibo}
  - {type: has-publisher, target: "/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/AmericanStatisticsPublisher.md", provenance: fibo}
  - {type: is-published-by, target: "/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/BureauOfLaborStatistics.md", provenance: fibo}
---

an economic indicator representing a measure of the average change over time in the prices paid by urban consumers for a market basket of consumer goods and services

### Relationships
- is-a: [ConsumerPriceIndex](/IND/EconomicIndicators/EconomicIndicators/ConsumerPriceIndex.md)
- applies-to: [UrbanConsumersUniverse](/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/UrbanConsumersUniverse.md)
- has-argument: [Basket](/FBC/ProductsAndServices/FinancialProductsAndServices/Basket.md)
- has-argument: [UrbanConsumersUniverse](/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/UrbanConsumersUniverse.md)
- has-publisher: [AmericanStatisticsPublisher](/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/AmericanStatisticsPublisher.md)
- is-published-by: [BureauOfLaborStatistics](/IND/EconomicIndicators/NorthAmericanIndicators/USEconomicIndicators/BureauOfLaborStatistics.md)
