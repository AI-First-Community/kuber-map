---
type: FIBO Class
title: "original issue discount bond"
description: "interest-bearing bond issued at a deep discount to face value"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/OriginalIssueDiscountBond
tags: [SEC, Release]
detail: "An original issue discount (OID) is the discount in price from a bond's face value at the time a bond or other debt instrument is first issued. The OID is the amount of discount or the difference between the original face value and the price paid for the bond. The principal amount accretes over time at a constant accrual rate and is redeemed at full face value at maturity."
synonyms:
  - "OID bond"
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/Bond.md", provenance: fibo}
  - {type: has-original-issue-discount-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-relative-price-at-maturity, target: "/SEC/Debt/DebtInstruments/ParValue.md", provenance: fibo}
---

interest-bearing bond issued at a deep discount to face value

### Relationships
- is-a: [Bond](/SEC/Debt/Bonds/Bond.md)
- has-original-issue-discount-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-relative-price-at-maturity: [ParValue](/SEC/Debt/DebtInstruments/ParValue.md)
