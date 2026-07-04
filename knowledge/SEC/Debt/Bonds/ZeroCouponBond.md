---
type: FIBO Class
title: "zero coupon bond"
description: "bond issued with a coupon rate of zero and that trades at a deep discount to face value"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ZeroCouponBond
tags: [SEC, Release]
detail: "Fannie Mae also issues zero-coupon callable debt securities. Zero-coupon notes are debt securities on which no coupon interest is paid to the investor. Rather, the security is purchased at a discounted dollar price and matures at par. If the option on a callable zero-coupon security is exercised, it is redeemed at a higher dollar price than the original issue price. The yield for a callable zero-coupon security is based on the difference between the original discounted price and the principal payment at the call date. The principal amount accretes over time at a constant accrual rate and is redeemed at full face value at maturity. In effect, the accrual rate is the coupon rate or yield which is added to the outstanding principal rather than being paid out to investors."
synonyms:
  - "z-bond"
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/Bond.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md", provenance: fibo}
  - {type: has-interest-payment-terms, target: "/SEC/Debt/Bonds/ZeroCouponTerms.md", provenance: fibo}
  - {type: has-original-issue-discount-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-relative-price-at-maturity, target: "/SEC/Debt/DebtInstruments/ParValue.md", provenance: fibo}
---

bond issued with a coupon rate of zero and that trades at a deep discount to face value

### Relationships
- is-a: [Bond](/SEC/Debt/Bonds/Bond.md)
- is-a: [FixedIncomeSecurity](/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md)
- has-interest-payment-terms: [ZeroCouponTerms](/SEC/Debt/Bonds/ZeroCouponTerms.md)
- has-original-issue-discount-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-relative-price-at-maturity: [ParValue](/SEC/Debt/DebtInstruments/ParValue.md)
