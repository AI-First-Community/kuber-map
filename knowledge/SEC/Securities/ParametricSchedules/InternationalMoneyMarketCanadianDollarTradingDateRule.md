---
type: FIBO Class
title: "International Money Market (IMM) Canadian Dollar (CAD) trading date rule"
description: "trading date rule defined as the last trading day / expiration day of the Canadian Derivatives Exchange (Bourse do Montreal Inc.), three month Bankers' Acceptance Futures (Ticker symbol BAX), the second London banking day prior to the third Wednesday of the contract month"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/InternationalMoneyMarketCanadianDollarTradingDateRule
tags: [SEC, Release]
detail: "If the determined day is a bourse or bank holiday in Toronto or Montreal, the last trading day shall be the previous bank business day, per the Canadian Derivatives Exchange BAX contract specification. The above description implies a Date Roll Rule which is presumably referenced by referring to this rule, so that when this rule is referenced, there would be no Date Roll Rule defined in the FpML message. Semantically, this is still a Date Roll Rule, specifically a 'Roll forward' rule with no modification (the third Wednesday of a month will never roll forward to a day in the following month so no Modified rule is required)."
synonyms:
  - "IMM CAD trading date rule"
relations:
  - {type: is-a, target: "/SEC/Securities/ParametricSchedules/TradingDateRule.md", provenance: fibo}
  - {type: has-business-day-convention, target: "/FND/DatesAndTimes/BusinessDates/BusinessDayPreceding.md", provenance: fibo}
---

trading date rule defined as the last trading day / expiration day of the Canadian Derivatives Exchange (Bourse do Montreal Inc.), three month Bankers' Acceptance Futures (Ticker symbol BAX), the second London banking day prior to the third Wednesday of the contract month

### Relationships
- is-a: [TradingDateRule](/SEC/Securities/ParametricSchedules/TradingDateRule.md)
- has-business-day-convention: [BusinessDayPreceding](/FND/DatesAndTimes/BusinessDates/BusinessDayPreceding.md)
