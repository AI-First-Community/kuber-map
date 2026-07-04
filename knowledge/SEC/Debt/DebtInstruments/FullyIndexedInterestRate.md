---
type: FIBO Class
title: "fully-indexed interest rate"
description: "a variable interest rate that is calculated by adding a margin to a specified index rate"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/FullyIndexedInterestRate
tags: [SEC, Release]
detail: "Fully indexed interest rates are used for variable rate credit products. The interest rate on a variable (adjustable) rate mortgage corresponds to a specific benchmark (often the prime rate, but sometimes LIBOR, the one-year constant-maturity Treasury, or other benchmarks) plus a spread (also called the margin. The margin on a fully indexed interest rate product is determined by the underwriter and based on the borrower's credit quality."
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/FloatingInterestRate.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Expression.md", provenance: fibo}
  - {type: has-argument, target: "/IND/InterestRates/InterestRates/BaseRate.md", provenance: fibo}
  - {type: has-argument, target: "/SEC/Debt/DebtInstruments/Margin.md", provenance: fibo}
---

a variable interest rate that is calculated by adding a margin to a specified index rate

### Relationships
- is-a: [FloatingInterestRate](/FBC/DebtAndEquities/Debt/FloatingInterestRate.md)
- is-a: [Expression](/CMNS/QuantitiesAndUnits/Expression.md)
- has-argument: [BaseRate](/IND/InterestRates/InterestRates/BaseRate.md)
- has-argument: [Margin](/SEC/Debt/DebtInstruments/Margin.md)
