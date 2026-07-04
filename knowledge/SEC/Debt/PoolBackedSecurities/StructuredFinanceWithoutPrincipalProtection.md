---
type: FIBO Class
title: "structured finance without principal protection"
description: "structured finance that is a short-term note linked to an underlying asset that offers a steady stream of income"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection
tags: [SEC, Release]
detail: "The redemption at the end of the term is determined on the basis of the performance and final fixing of the underlying asset: a redemption at the nominal value is guaranteed as long as the underlying asset has not touched its barrier during relevant barrier monitoring. If the underlying asset has touched its barrier but is again above the strike price at final fixing, the nominal price is also repaid. Nevertheless, if the underlying asset has touched its barrier during barrier monitoring and closes below the strike price at final fixing, the underlying asset is delivered or cash compensation paid, provided that no credit event by the reference entity has occurred. Depending on the characteristics of the product, either a coupon or a discount to the underlying asset can apply. A coupon is paid out regardless of the performance of the underlying asset, provided that no credit event by the reference entity has occurred."
synonyms:
  - "structured finance without capital protection"
relations:
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md", provenance: fibo}
---

structured finance that is a short-term note linked to an underlying asset that offers a steady stream of income

### Relationships
- is-a: [StructuredFinanceInstrument](/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md)
