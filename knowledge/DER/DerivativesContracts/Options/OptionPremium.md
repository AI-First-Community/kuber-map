---
type: FIBO Class
title: "option premium"
description: "current market price of an option contract"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionPremium
tags: [DER, Release]
detail: "The option premium is the income received by the seller (writer) of an option contract to another party. In-the-money option premiums are composed of two factors: intrinsic and extrinsic value. Out-of-the-money options' premiums consist solely of extrinsic value. For stock options, the premium is quoted as a dollar amount per share, and most contracts represent the commitment of 100 shares."
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/MarketPrice.md", provenance: fibo}
  - {type: has-expression, target: "/DER/DerivativesContracts/Options/OptionPremiumFormula.md", provenance: fibo}
  - {type: has-monetary-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-quantity-value, target: "/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md", provenance: fibo}
---

current market price of an option contract

### Relationships
- is-a: [MarketPrice](/FBC/FinancialInstruments/InstrumentPricing/MarketPrice.md)
- has-expression: [OptionPremiumFormula](/DER/DerivativesContracts/Options/OptionPremiumFormula.md)
- has-monetary-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-quantity-value: [PercentageMonetaryAmount](/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)
