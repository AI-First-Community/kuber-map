---
type: FIBO Class
title: "bond"
description: "tradable debt instrument representing a loan in which the issuer owes the holder(s) a debt"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
tags: [SEC, Release]
detail: "Depending on the terms of the contract, the issuer is obliged to pay interest (the coupon) and/or to repay the principal at maturity. The most common bonds are corporate or governmental, typically used to finance specific projects or operations."
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CreditAgreementRepaidAtMaturity.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/DebtInstruments/TradableDebtInstrument.md", provenance: fibo}
  - {type: has-interest-payment-terms, target: "/SEC/Debt/Bonds/CouponPaymentTerms.md", provenance: fibo}
  - {type: has-repayment-terms, target: "/SEC/Debt/Bonds/BondPrincipalRepaymentTerms.md", provenance: fibo}
---

tradable debt instrument representing a loan in which the issuer owes the holder(s) a debt

### Relationships
- is-a: [CreditAgreementRepaidAtMaturity](/FBC/DebtAndEquities/Debt/CreditAgreementRepaidAtMaturity.md)
- is-a: [TradableDebtInstrument](/SEC/Debt/DebtInstruments/TradableDebtInstrument.md)
- has-interest-payment-terms: [CouponPaymentTerms](/SEC/Debt/Bonds/CouponPaymentTerms.md)
- has-repayment-terms: [BondPrincipalRepaymentTerms](/SEC/Debt/Bonds/BondPrincipalRepaymentTerms.md)
