---
type: FIBO Class
title: "barrier option"
description: "option whose final exercise depends upon the path taken by the price of an underlying instrument, i.e., whose payoff depends on whether or not the underlying asset has reached or exceeded a predetermined price"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/BarrierOption
tags: [DER, Release]
detail: "A barrier option can be a knock-out, meaning it expires worthless if the underlying exceeds a certain price, limiting profits for the holder and limiting losses for the writer. It can also be a knock-in, meaning it has no value until the underlying reaches a certain price. Barrier options can be puts or calls. Barrier options typically have cheaper premiums than traditional vanilla options, primarily because the barrier increases the chances of the option expiring worthless. A trader may choose the cheaper (relative to a comparable vanilla) barrier option if they feel it is quite likely the underlying will hit the barrier. Barrier features include any terms related to exercising the option ahead of the expiry date."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/ExoticOption.md", provenance: fibo}
  - {type: has-monitoring-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
---

option whose final exercise depends upon the path taken by the price of an underlying instrument, i.e., whose payoff depends on whether or not the underlying asset has reached or exceeded a predetermined price

### Relationships
- is-a: [ExoticOption](/DER/DerivativesContracts/Options/ExoticOption.md)
- has-monitoring-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
