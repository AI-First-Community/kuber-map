---
type: FIBO Class
title: "interest rate adjustment"
description: "Scheduled change to the coupon rate for a floating or adjustable rate security."
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/InterestRateAdjustment
tags: [CAE, Provisional]
detail: "The SWIFT definition as given defines the notification of the interest rate change, not the adjustment. Adjusted to describe the event. REVIEW: Is this really an action? Usually consider that it's expected. Given definition was for the announcement. SWIFT full definition 'Announcement of the current coupon rate for a floating or adjustable rate security.'"
relations:
  - {type: is-a, target: "/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md", provenance: fibo}
  - {type: applies-to, target: "/SEC/Debt/Bonds/VariableCouponBond.md", provenance: fibo}
---

Scheduled change to the coupon rate for a floating or adjustable rate security.

### Relationships
- is-a: [MandatoryCorporateAction](/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md)
- applies-to: [VariableCouponBond](/SEC/Debt/Bonds/VariableCouponBond.md)
