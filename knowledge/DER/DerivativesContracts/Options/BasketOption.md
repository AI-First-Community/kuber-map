---
type: FIBO Class
title: "basket option"
description: "option whose underlying asset is a group, or basket, of commodities, securities, indices, or currencies"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/BasketOption
tags: [DER, Release]
detail: "As with other options, a basket option gives the holder the right, but not the obligation, to buy or sell the basket at a specific price, on or before a certain date. This exotic option has all the characteristics of a standard option, but with the basis of the strike price on the weighted value of its components. Currency baskets are the most popular type of basket option, and they will settle in the holder's home currency. Because it involves just one transaction, a basket option often costs less than multiple single options as it saves on commissions and fees."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/ExoticOption.md", provenance: fibo}
  - {type: has-contract-duration, target: "/CMNS/DatesAndTimes/ExplicitDuration.md", provenance: fibo}
  - {type: has-price-determination-method, target: "/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod.md", provenance: fibo}
---

option whose underlying asset is a group, or basket, of commodities, securities, indices, or currencies

### Relationships
- is-a: [ExoticOption](/DER/DerivativesContracts/Options/ExoticOption.md)
- has-contract-duration: [ExplicitDuration](/CMNS/DatesAndTimes/ExplicitDuration.md)
- has-price-determination-method: [PriceDeterminationMethod](/FBC/FinancialInstruments/InstrumentPricing/PriceDeterminationMethod.md)
