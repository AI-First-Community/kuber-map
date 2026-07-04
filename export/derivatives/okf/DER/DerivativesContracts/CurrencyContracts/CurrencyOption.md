---
type: FIBO Class
title: "currency option"
description: "option giving the buyer (holder) the right, but not the obligation, to buy or sell currency at a specified exchange rate during a specified period of time"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyOption
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
detail: "For this right, a premium is paid to the broker, which will vary depending on the number of contracts purchased. Currency options are one of the best ways for corporations or individuals to hedge against adverse movements in exchange rates. Investors can hedge against foreign currency risk by purchasing a currency option put or call. For example, assume that an investor believes that the USD/EUR rate is going to increase from 0.80 to 0.90 (meaning that it will become more expensive for a European investor to buy U.S dollars). In this case, the investor would want to buy a call option on USD/EUR so that he or she could stand to gain from an increase in the exchange rate (or the USD rise)."
examples:
  - "An option to buy EUR against USD at 1.10."
examples_provenance: curated
synonyms:
  - "FX option"
  - "foreign exchange option"
  - "forex option"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative.md", provenance: fibo}
  - {type: is-a, target: "/DER/DerivativesContracts/Options/VanillaOption.md", provenance: fibo}
  - {type: has-strike-rate, target: "/FND/Accounting/CurrencyAmount/ExchangeRate.md", provenance: fibo}
---

option giving the buyer (holder) the right, but not the obligation, to buy or sell currency at a specified exchange rate during a specified period of time

### Relationships
- is-a: [CurrencyDerivative](/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative.md)
- is-a: [VanillaOption](/DER/DerivativesContracts/Options/VanillaOption.md)
- has-strike-rate: [ExchangeRate](/FND/Accounting/CurrencyAmount/ExchangeRate.md)
