---
type: FIBO Class
title: "rainbow option"
description: "exotic option linked to the performances of two or more underlying assets"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/RainbowOption
tags: [DER, Release]
detail: "Rainbbow options can speculate on the best performer in the group or minimum performances of all the underlying assets at one time. Each underlying may be called a color so the sum of all of these factors makes up a rainbow. These structures can be rather exotic and made for institutional clients when referring to financial assets. Rainbow options can be structured in many ways depending on how the performances of each underlying asset are considered. Some pay off based on the best or worst performance among the underlying assets. In other words, it looks at the top or bottom performance and pays off based on that single asset. These are sometimes called 'best of' or 'worst of' rainbow options. Rainbow options are usually calls or puts on the best or worst of n underlying assets. Like a basket option, which is written on a group of assets and pays out on a weighted-average gain on the basket as a whole, a rainbow option also considers a group of assets, but usually pays out on the level of one of them. A simple example is a call rainbow option written on FTSE 100, Nikkei and S&P 500 which will pay out the difference between the strike price and the level of the index that has risen by the largest amount of the three."
examples:
  - "A best of assets plus cash rainbow effectively has n + 1 payoff possibilities. If we consider a 2 asset 'best of plus cash', the payoff at expiry is a choice between Asset 1, Asset 2, or the predetermined cash amount. There is no strike price and the payoff is given as: Rainbow = max(S1, S2, Cash;T)"
  - "An asset maximum or minimum payout rainbow is similar to the best of n assets plus cash, with the exception that no cash payoff is possible and there is a strike price for this type of option. The payoff of a call and put are given as: Rainbow-Call = max[0, max(S1, S2) - X] Rainbow-Put = max[0, X - max(S1, S2)] Minimum of n Assets. The counterpart to a maximum of n assets, this rainbow pays out the value of the underperformer of the n assets. The payoff for minimum of 2 asset rainbow calls and puts are given as: Rainbow-Call = max[0, mainS1, S2) - X] Rainbow-Put = max[0, X - min(S1, S2)]"
  - "Better of n Assets This type of rainbow is similar to the best of n assets plus cash but with the exception that there is no possible cash payoff, and X is set to 0. With this in mind, a better of 2 assets rainbow is essentially a two-asset call option, with a payoff being: Rainbow = max[0, max(S1, S2)] Worse of n Assets Essentially the opposite to the better of n assets, with the payoff being on the asset with the lower value. We can give the payoff for this option on 2 assets as: Rainbow = max[0, min(S1, S2)]"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/ExoticOption.md", provenance: fibo}
---

exotic option linked to the performances of two or more underlying assets

### Relationships
- is-a: [ExoticOption](/DER/DerivativesContracts/Options/ExoticOption.md)
