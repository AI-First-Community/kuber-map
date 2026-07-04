---
type: FIBO Class
title: "mountain range option"
description: "exotic option based on multiple underlying securities"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/MountainRangeOption
tags: [DER, Release]
detail: "The price of a mountain range option is based on multiple variables, the most important of which are the correlations between the individual securities in the basket. Some options have discrete payout levels, such as double the investment or triple the investment, if certain performance metrics are hit by the underlying securities while the option is in effect. Mountain range options cannot be priced with standard closed-form approaches. These exotic instruments instead require Monte Carlo simulation methods. Effects such as volatility skew, which is found in most options, can be even more pronounced within mountain range options. These options blend some of the key characteristics of basket-style or rainbow options—both of which have more than one underlying security or asset—and range options with multiyear time ranges. Prices are based on multiple variables - notably the correlations between the individual securities in the basket."
examples:
  - "Mountain range options are named after a series of mountains, each representing a different type of contract. Some of the most common include: (a) Altiplano options: Altiplano options provide investors with the features of both a traditional vanilla option along with a coupon payment, (b) Annapurna options: coupon rates are determined by the performance of the basket's worst-performing security when it drops under a specified range, (c) Everest options: Everest options place a long-term limit on an investor's option while offering a payout based on the lagging performers in the basket, (d) Atlas options: this type of option eliminates both the best - and worst - performing stocks in a basket of securities, and (e) Himalayan options: traders receive a payout based on the basket's best performing stock; payouts are provided on multiple dates."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/ExoticOption.md", provenance: fibo}
---

exotic option based on multiple underlying securities

### Relationships
- is-a: [ExoticOption](/DER/DerivativesContracts/Options/ExoticOption.md)
