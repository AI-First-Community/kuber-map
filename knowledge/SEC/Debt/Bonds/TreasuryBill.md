---
type: FIBO Class
title: "treasury bill"
description: "short-term zero coupon treasury obligation with a maturity ranging from one to twelve months"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/TreasuryBill
tags: [SEC, Release]
core: true
detail: "The pricing of T-bills is unique among U.S. government debt issues. Treasury bills are offered in multiples of $100 and in terms ranging from a few days to 52 weeks. Rather than providing interest payments as Treasury Bonds or Notes do, T-bills are sold at a discount, and the entire return is realized upon maturity. The price of a bill is determined at auction. The annualized interest rate earned on T-bills is equal to the difference between the purchase price and maturity value, divided by the maturity value."
examples:
  - "A 13-week US Treasury bill sold at a discount to its US$1,000 face value."
examples_provenance: curated
synonyms:
  - "T-bill"
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/USTreasurySecurity.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument.md", provenance: fibo}
  - {type: has-interest-rate, target: "/IND/InterestRates/InterestRates/ReferenceInterestRate.md", provenance: fibo}
  - {type: has-relative-price-at-issue, target: "/SEC/Debt/DebtInstruments/AtADiscount.md", provenance: fibo}
  - {type: has-relative-price-at-maturity, target: "/SEC/Debt/DebtInstruments/ParValue.md", provenance: fibo}
---

short-term zero coupon treasury obligation with a maturity ranging from one to twelve months

### Relationships
- is-a: [USTreasurySecurity](/SEC/Debt/Bonds/USTreasurySecurity.md)
- is-a: [MoneyMarketInstrument](/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument.md)
- has-interest-rate: [ReferenceInterestRate](/IND/InterestRates/InterestRates/ReferenceInterestRate.md)
- has-relative-price-at-issue: [AtADiscount](/SEC/Debt/DebtInstruments/AtADiscount.md)
- has-relative-price-at-maturity: [ParValue](/SEC/Debt/DebtInstruments/ParValue.md)
