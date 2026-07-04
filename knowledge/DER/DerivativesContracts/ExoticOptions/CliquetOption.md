---
type: FIBO Class
title: "cliquet option"
description: "exotic option that is a series of at-the-money (ATM) options, either puts or calls, where each successive option becomes active when the previous one expires"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/CliquetOption
tags: [DER, Release]
detail: "A cliquet is a cash-settled, exotic option that settles at predetermined dates and then resets its strike price based on the price of the underlying security at the time of settlement. Each new option within the cliquet enters into force when the previous option expires. The total premium and the exact reset dates are known at the time of transacting a cliquet. Investors can opt to receive their payout when each option expires or wait until the entire series plays out. A cliquet is a series of forward start options, all related to each other. Each forward start option represents the advance purchase of a put, or call, option with an at-the-money (ATM) strike price to be determined at a later date, typically when the option becomes active. A forward start option becomes active at a specified date in the future. The premium is paid in advance, while the time to expiration and the underlying security are established at the time the forward start option is purchased. If at the first settlement date the underlying security trades below the strike price of the option (for a call), then it expires worthless and resets to the price of the underlying security at the time of settlement. If at the end of the next settlement the underlying security trades above the new strike, the holder may elect to receive the difference between the market price of the underlying security and the strike price. Alternatively, the holder can let it ride to receive the sum of all payouts at maturity. The main advantage of initiating a cliquet is, if an investor expects volatility to rise, they can lock in their profits at predetermined levels and thus maximize their overall portfolio return."
synonyms:
  - "rachet option"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/ExoticOption.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/ExoticOptions/ForwardStartOption.md", provenance: fibo}
---

exotic option that is a series of at-the-money (ATM) options, either puts or calls, where each successive option becomes active when the previous one expires

### Relationships
- is-a: [ExoticOption](/DER/DerivativesContracts/Options/ExoticOption.md)
- comprises: [ForwardStartOption](/DER/DerivativesContracts/ExoticOptions/ForwardStartOption.md)
