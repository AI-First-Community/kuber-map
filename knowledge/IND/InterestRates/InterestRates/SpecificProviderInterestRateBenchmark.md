---
type: FIBO Class
title: "specific-provider interest rate benchmark"
description: "interest rate benchmark that is made available by a specific market data provider for reference purposes"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/SpecificProviderInterestRateBenchmark
tags: [IND, Release]
detail: "Benchmarks, such as those published by Bloomberg, Thomson-Reuters, and others, are usually quoted as of a specific date and time of day."
relations:
  - {type: is-a, target: "/IND/InterestRates/InterestRates/InterestRateBenchmark.md", provenance: fibo}
  - {type: is-provided-by, target: "/BE/FunctionalEntities/Publishers/MarketDataProvider.md", provenance: fibo}
---

interest rate benchmark that is made available by a specific market data provider for reference purposes

### Relationships
- is-a: [InterestRateBenchmark](/IND/InterestRates/InterestRates/InterestRateBenchmark.md)
- is-provided-by: [MarketDataProvider](/BE/FunctionalEntities/Publishers/MarketDataProvider.md)
