---
type: FIBO Class
title: "credit spread"
description: "yield spread that reflects the additional net yield an investor can earn from a security with more credit risk relative to one with less credit risk"
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/CreditSpread
tags: [MD, Provisional]
detail: "The credit spread of a particular security is often quoted in relation to the yield on a credit risk-free benchmark security or reference rate. Further Notes There are several measures of credit spread, including Z-spread and option-adjusted spread. Old definition (Algo) The spread between the credit rating of something and its maturity. THis is now defined as a different term pending further review with Algorithmics. Update from SMER. difference between risk free price (price of govt bond) and the price of this security. (matches Wikipedia definition above) i.e. price of this credit versus the price of a (near) risk free credit. The latter is a reference security with low risk such as a Treasury Bond. Is this between prices or between yields? can be expressed as either wrt price or yield, and this is detemined by context for different markets. Try and get a list. This is more generic - the meaning is not that it is speciufically wrt yield as such. Debt Price Spread is in context of price, whereas this is more generic."
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/YieldSpread.md", provenance: fibo}
  - {type: has-argument, target: "/IND/InterestRates/InterestRates/ReferenceInterestRate.md", provenance: fibo}
---

yield spread that reflects the additional net yield an investor can earn from a security with more credit risk relative to one with less credit risk

### Relationships
- is-a: [YieldSpread](/FBC/FinancialInstruments/InstrumentPricing/YieldSpread.md)
- has-argument: [ReferenceInterestRate](/IND/InterestRates/InterestRates/ReferenceInterestRate.md)
