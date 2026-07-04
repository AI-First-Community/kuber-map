---
type: FIBO Class
title: "repurchase agreement"
description: "agreement between two parties whereby one party lends the other a security at a specified price with a commitment to take the security back at a later date for another specified price"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/RepurchaseAgreement
tags: [SEC, Release]
detail: "Most repos are overnight transactions, with the sale taking place one day and being reversed the next day. Long-term repos - called term repos - can extend for a month or more. Usually, repos are for a fixed period of time, but open-ended deals are also possible. Reverse repo is a term used to describe the opposite side of a repo transaction. The party who sells and later repurchases a security is said to perform a repo. The other party - who purchases and later resells the security - is said to perform a reverse repo. While a repo functions like the sale and subsequent repurchase of a security, but the legal reality and the economic effect is that of a secured loan. This is a loan as the original owner retains the rights to the cashflows of the underlying security. Economically, the party purchasing the security makes funds available to the seller and holds the security as collateral. If the repurchased security pays a dividend, coupon or partial redemptions during the repo, the funds are returned to the original owner. The difference between the sale and repurchase prices paid for the security represent interest on the loan. Indeed, repos are quoted as interest rates. A repo always pays interest at maturity, i.e. there are no periodic interest payments."
synonyms:
  - "REPO"
relations:
  - {type: is-a, target: "/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument.md", provenance: fibo}
  - {type: has-duration, target: "/CMNS/DatesAndTimes/Duration.md", provenance: fibo}
---

agreement between two parties whereby one party lends the other a security at a specified price with a commitment to take the security back at a later date for another specified price

### Relationships
- is-a: [MoneyMarketInstrument](/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument.md)
- has-duration: [Duration](/CMNS/DatesAndTimes/Duration.md)
