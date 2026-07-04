---
type: FIBO Class
title: "lookback option"
description: "exotic option that minimizes the uncertainties related to the timing of market entry, providing the holder the advantage of knowing history when determining when to exercise their option"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/LookbackOption
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
detail: "As a type of exotic option, the lookback allows the user to 'look back,' or review, the prices of an underlying asset over the lifespan of the option after it has been purchased. The holder may then exercise the option based on the most beneficial price of the underlying asset. The holder can take advantage of the widest differential between the strike price and the price of the underlying asset. Lookback options do not trade on major exchanges. Instead, they are unlisted and trade over-the-counter (OTC). This type of option reduces uncertainties associated with the timing of market entry and reduces the chances the option will expire worthlessly. Lookback options are expensive to execute, so these advantages come at a cost. Lookback options are cash settled options, which means the holder receives a cash settlement at execution based on the most advantageous differential between high and low prices during the purchase period. Sellers of lookback options would price the option at or near the widest expected distance of price differential based on past volatility and demand for the options. The cost to purchase this option would be taken up front. The settlement will equate to the profits they could have made from buying or selling the underlying asset. If the settlement was greater than the initial cost of the option, then the option buyer would have profit at settlement, otherwise loss."
examples:
  - "An option whose payoff uses the most favourable price over its life."
examples_provenance: curated
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/ExoticOption.md", provenance: fibo}
  - {type: has-contractual-element, target: "/DER/DerivativesContracts/ExoticOptions/LookbackStrikeTerms.md", provenance: fibo}
---

exotic option that minimizes the uncertainties related to the timing of market entry, providing the holder the advantage of knowing history when determining when to exercise their option

### Relationships
- is-a: [ExoticOption](/DER/DerivativesContracts/Options/ExoticOption.md)
- has-contractual-element: [LookbackStrikeTerms](/DER/DerivativesContracts/ExoticOptions/LookbackStrikeTerms.md)
