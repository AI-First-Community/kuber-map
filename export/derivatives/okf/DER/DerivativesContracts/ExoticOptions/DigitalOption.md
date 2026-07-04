---
type: FIBO Class
title: "digital option"
description: "exotic option that has a pre-determined payout if the option is in-the-money and the payoff condition is satisfied"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/DigitalOption
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
detail: "There is an upfront fee called the premium for digital options, which is the maximum loss for the option. Unlike traditional options, digital options don't convert or exercise to the underlying asset's shares. Instead, they pay out a fixed reward if the asset's price is above or below the option's strike price."
examples:
  - "For example, let's say the ABC Index is trading at a level of 2,795 on June 2. An investor believes the ABC Index will trade above 2,800 before the end of the trading day, June 4th. The trader purchases 10 ABC Index options at a strike price of 2,800 options for $40 per contract. If the ABC Index closes above 2,800 at the end of the trading day on June 4, the investor is paid $100 per contract, which is a profit of $60 per contract or $600 (($100 - $40) x 10 contracts). However, if the ABC Index closes below 2,800 on June 4. The investor loses all of the premium amount or $400 ($40 x 10 contracts)."
synonyms:
  - "binary option"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/ExoticOptions/BarrierOption.md", provenance: fibo}
---

exotic option that has a pre-determined payout if the option is in-the-money and the payoff condition is satisfied

### Relationships
- is-a: [BarrierOption](/DER/DerivativesContracts/ExoticOptions/BarrierOption.md)
