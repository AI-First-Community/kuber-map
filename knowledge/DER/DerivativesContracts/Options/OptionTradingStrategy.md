---
type: FIBO Class
title: "option trading strategy"
description: "trading tactic involving more than one option type, strike price, or expiration date on the same underlying asset"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionTradingStrategy
tags: [DER, Release]
detail: "Note that some trading strategies may be considered financial instruments in their own right, but most strategies are not. The critical differentiators include whether the strategy itself can be traded, whether it has a financial instrument identifier independently from the identifier(s) of the embedded instrument(s), such as a FIGI or ISIN, and so forth. Option trading strategies refer to buying calls or put options or selling calls or put options or both together for the purpose of limiting losses and/or optimizing profits. Basically, these strategies utilize one or more combinations for the best outcome possible based on defined parameters. Simple combinations include option spread trades such as vertical spreads, calendar (or horizontal) spreads, and diagonal spreads. More involved combinations include trades such as condor or butterfly spreads which are actually combinations of two vertical spreads."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/TradingStrategy.md", provenance: fibo}
  - {type: comprises, target: "/FBC/FinancialInstruments/FinancialInstruments/Option.md", provenance: fibo}
---

trading tactic involving more than one option type, strike price, or expiration date on the same underlying asset

### Relationships
- is-a: [TradingStrategy](/FBC/ProductsAndServices/FinancialProductsAndServices/TradingStrategy.md)
- comprises: [Option](/FBC/FinancialInstruments/FinancialInstruments/Option.md)
