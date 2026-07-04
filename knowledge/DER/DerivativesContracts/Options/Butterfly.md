---
type: FIBO Class
title: "butterfly"
description: "strategy that combines bull and bear spreads with a fixed risk and capped profit"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Butterfly
tags: [DER, Release]
detail: "These spreads are intended as a market-neutral strategy and pay off the most if the underlying asset does not move prior to option expiration. They involve either four calls, four puts, or a combination of puts and calls with three strike prices. Butterfly spreads pay off the most if the underlying asset price doesn't change before the option expires. The upper and lower strike prices are equal distance from the middle, or at-the-money, strike price."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/OptionTradingStrategy.md", provenance: fibo}
  - {type: comprises, target: "/FBC/FinancialInstruments/FinancialInstruments/Option.md", provenance: fibo}
  - {type: has-exercise-price, target: "/DER/DerivativesContracts/Options/StrikePrice.md", provenance: fibo}
---

strategy that combines bull and bear spreads with a fixed risk and capped profit

### Relationships
- is-a: [OptionTradingStrategy](/DER/DerivativesContracts/Options/OptionTradingStrategy.md)
- comprises: [Option](/FBC/FinancialInstruments/FinancialInstruments/Option.md)
- has-exercise-price: [StrikePrice](/DER/DerivativesContracts/Options/StrikePrice.md)
