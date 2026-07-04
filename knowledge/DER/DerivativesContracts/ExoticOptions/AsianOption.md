---
type: FIBO Class
title: "Asian option"
description: "option whose exercise terms involve a payoff determined by the average underlying price (either the strike price or the settlement price) of the underlying asset over a predetermined period"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/AsianOption
tags: [DER, Release]
detail: "These options allow the buyer to purchase (or sell) the underlying asset at the average price instead of the spot price. There are various ways to interpret the word 'average,' and that needs to be specified in the options contract. Typically, the average price is a geometric or arithmetic average of the price of the underlying asset at discreet intervals, which are also specified in the options contract. Because of the averaging feature, Asian options reduce the volatility inherent in the option; therefore, Asian options are typically cheaper than European or American options. They are used by traders who are exposed to the underlying asset over some time, such as consumers and suppliers of commodities, etc."
examples:
  - "For an Asian call option using arithmetic averaging and a 30-day period for sampling the data: On Nov. 1, a trader purchased a 90-day arithmetic call option on stock XYZ with an exercise price of $22, where the averaging is based on the value of the stock after each 30-day period. The stock price after 30, 60, and 90 days was $21.00, $22.00, and $24.00. The arithmetic average (mean) is (21.00 + 22.00 + 24.00) / 3 = 22.33. The profit is the average minus the strike price 22.33 - 22 = 0.33 or $33.00 per 100 share contract. As with standard options, if the average price is below the strike price, the loss is limited to the premium paid for the call options."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/ExoticOption.md", provenance: fibo}
  - {type: has-asian-tail-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
  - {type: has-exercise-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: is-classified-by, target: "/DER/DerivativesContracts/ExoticOptions/AsianOptionClassifier.md", provenance: fibo}
  - {type: is-classified-by, target: "/DER/DerivativesContracts/ExoticOptions/AveragingStrategy.md", provenance: fibo}
  - {type: uses-currency-in-averaging, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
---

option whose exercise terms involve a payoff determined by the average underlying price (either the strike price or the settlement price) of the underlying asset over a predetermined period

### Relationships
- is-a: [ExoticOption](/DER/DerivativesContracts/Options/ExoticOption.md)
- has-asian-tail-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
- has-exercise-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- is-classified-by: [AsianOptionClassifier](/DER/DerivativesContracts/ExoticOptions/AsianOptionClassifier.md)
- is-classified-by: [AveragingStrategy](/DER/DerivativesContracts/ExoticOptions/AveragingStrategy.md)
- uses-currency-in-averaging: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
