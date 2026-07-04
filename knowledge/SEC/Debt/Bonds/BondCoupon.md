---
type: FIBO Class
title: "bond coupon"
description: "interest rate on a debt security that the issuer promises to pay to the holder until maturity, expressed as an annual percentage of the face value"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondCoupon
tags: [SEC, Release]
core: true
use_cases:
  - "Securities Instruments & Issuance (capital markets)"
examples:
  - "The semi-annual 2% interest payment on a bond with a 4% annual coupon."
examples_provenance: curated
synonyms:
  - "coupon percent rate"
  - "coupon rate"
  - "nominal yield"
relations:
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/InterestRate.md", provenance: fibo}
---

interest rate on a debt security that the issuer promises to pay to the holder until maturity, expressed as an annual percentage of the face value

### Relationships
- is-a: [InterestRate](/FND/Accounting/CurrencyAmount/InterestRate.md)
