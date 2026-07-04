---
type: FIBO Class
title: "strip strategy"
description: "option trading strategy that involves a sequential set of options with periodic reset dates, such that each period between resets behaves like an individual option"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/StripStrategy
tags: [DER, Release]
detail: "Typically, a strip is a strategy that involves being long in one call position and two put options, all with the same strike price on a single underlying stock. The investor who adopts this strategy believes that the underlying price of the stock will plummet in the near-term future. All three of the options will have the same expiration date and the same strike price. If the investor is correct and the price drastically decreases, the puts will pay out substantially. If the investor is wrong and the price of the underlying asset increases, the call option will mitigate the loss. The period between resets may be called a Caplet or Floorlet."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/OptionTradingStrategy.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/Options/CallOption.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/Options/PutOption.md", provenance: fibo}
  - {type: has-schedule, target: "/FND/DatesAndTimes/FinancialDates/Schedule.md", provenance: fibo}
---

option trading strategy that involves a sequential set of options with periodic reset dates, such that each period between resets behaves like an individual option

### Relationships
- is-a: [OptionTradingStrategy](/DER/DerivativesContracts/Options/OptionTradingStrategy.md)
- comprises: [CallOption](/DER/DerivativesContracts/Options/CallOption.md)
- comprises: [PutOption](/DER/DerivativesContracts/Options/PutOption.md)
- has-schedule: [Schedule](/FND/DatesAndTimes/FinancialDates/Schedule.md)
