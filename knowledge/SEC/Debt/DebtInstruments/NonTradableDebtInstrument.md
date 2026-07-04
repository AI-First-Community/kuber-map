---
type: FIBO Class
title: "non-tradable debt instrument"
description: "a debt instrument that may not be bought or sold"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/NonTradableDebtInstrument
tags: [SEC, Release]
detail: "Generally, a nonnegotiable instrument may be redeemed by the issuer, but this is often subject to some limitations."
examples:
  - "Low-risk instruments such as savings bonds are examples of nonnegotiable debt instruments."
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Contracts/WrittenContract.md", provenance: fibo}
  - {type: has-redemption-terms, target: "/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md", provenance: fibo}
  - {type: has-relative-price-at-issue, target: "/SEC/Debt/DebtInstruments/RelativePrice.md", provenance: fibo}
  - {type: has-relative-price-at-redemption, target: "/SEC/Debt/DebtInstruments/RelativePrice.md", provenance: fibo}
---

a debt instrument that may not be bought or sold

### Relationships
- is-a: [DebtInstrument](/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md)
- is-a: [WrittenContract](/FND/Agreements/Contracts/WrittenContract.md)
- has-redemption-terms: [RedemptionProvision](/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md)
- has-relative-price-at-issue: [RelativePrice](/SEC/Debt/DebtInstruments/RelativePrice.md)
- has-relative-price-at-redemption: [RelativePrice](/SEC/Debt/DebtInstruments/RelativePrice.md)
