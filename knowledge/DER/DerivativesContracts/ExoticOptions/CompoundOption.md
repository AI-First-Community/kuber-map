---
type: FIBO Class
title: "compound option"
description: "exotic option for which the underlying asset is another option"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/CompoundOption
tags: [DER, Release]
detail: "Therefore, there are two strike prices and two exercise dates. They are available for any combination of calls and puts. For example, a put where the underlying is a call option or a call where the underlying is a put option. The underlying is the second option, while the initial option is called the overlying. If the compound option is exercised, there are two premiums."
examples:
  - "For example, assume an investor wants to buy a put to sell 100 shares of stock at $50. The stock is currently trading at $55. The investor could buy a Call-Put, which allows them to buy a call now, for say $1 per share ($100), which will allow them to buy a put with a $50 strike in the future. They pay the $1 per share now, but only need to pay the fee for the second option if they exercise the first resulting in them receiving the second option."
synonyms:
  - "split-fee options"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/ExoticOption.md", provenance: fibo}
  - {type: comprises, target: "/FBC/FinancialInstruments/FinancialInstruments/Option.md", provenance: fibo}
---

exotic option for which the underlying asset is another option

### Relationships
- is-a: [ExoticOption](/DER/DerivativesContracts/Options/ExoticOption.md)
- comprises: [Option](/FBC/FinancialInstruments/FinancialInstruments/Option.md)
