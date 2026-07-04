---
type: FIBO Class
title: "equity redemption provision"
description: "redemption provision that specifies the conditions under which the issuer or shareholder may redeem the shares"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EquityRedemptionProvision
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md", provenance: fibo}
  - {type: has-earliest-redemption-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: has-minimum-redemption-price, target: "/FND/Accounting/CurrencyAmount/MonetaryPrice.md", provenance: fibo}
  - {type: has-redemption-premium, target: "/FND/Accounting/CurrencyAmount/MonetaryPrice.md", provenance: fibo}
---

redemption provision that specifies the conditions under which the issuer or shareholder may redeem the shares

### Relationships
- is-a: [RedemptionProvision](/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md)
- has-earliest-redemption-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- has-minimum-redemption-price: [MonetaryPrice](/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- has-redemption-premium: [MonetaryPrice](/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
