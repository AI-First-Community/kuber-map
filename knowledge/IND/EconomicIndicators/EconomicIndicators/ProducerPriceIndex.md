---
type: FIBO Class
title: "producer price index"
description: "economic indicator representing measure of the rate of change over time in the prices of goods and services bought and sold by producers"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/ProducerPriceIndex
tags: [IND, Release]
detail: "Statistical agencies implement the Laspeyres index by putting it into price-relative (price change from the base period) and revenue-share (from the base period) format. In this form, the Laspeyres index can be written as the sum of base-period revenue shares of the items in the index times their corresponding price relatives. Statistical agency practice has introduced some approximations to the theoretical Laspeyres target due to a number of practical problems with producing the Laspeyres index exactly. For these and other pragmatic reasons, some agencies use alternatives depending on circumstances. See the IMF publication cited for a full explanation of the most commonly used approaches and trade-offs made for determining PPI. The standard methodology for a typical PPI is based on a Laspeyres price index with fixed quantities from an earlier base period. The construction of this index can be thought of in terms of selecting a basket of goods and services representative of base-period revenues, valuing this at base-period prices, and then repricing the same basket at current-period prices. The target PPI in this case is defined to be the ratio of these two revenues. Practicing statisticians use this methodology because it has at least three practical advantages. It is easily explained to the public, it can use often expensive and untimely weighting information from the date of the last (or an even earlier) survey or administrative source (rather than requiring sources of data for the current month), and it need not be revised if users accept the Laspeyres premise."
synonyms:
  - "PPI"
relations:
  - {type: is-a, target: "/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Expression.md", provenance: fibo}
  - {type: has-input, target: "/IND/EconomicIndicators/EconomicIndicators/FixedBasket.md", provenance: fibo}
---

economic indicator representing measure of the rate of change over time in the prices of goods and services bought and sold by producers

### Relationships
- is-a: [EconomicIndicator](/IND/EconomicIndicators/EconomicIndicators/EconomicIndicator.md)
- is-a: [Expression](/CMNS/QuantitiesAndUnits/Expression.md)
- has-input: [FixedBasket](/IND/EconomicIndicators/EconomicIndicators/FixedBasket.md)
