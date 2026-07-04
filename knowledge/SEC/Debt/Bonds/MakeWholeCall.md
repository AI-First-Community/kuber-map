---
type: FIBO Class
title: "make whole call"
description: "call allowing the issuer to pay off remaining debt early"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MakeWholeCall
tags: [SEC, Release]
detail: "The issuer typically has to make a lump sum payment to the investor(s) derived from a formula based on the net present value (NPV) of future coupon payments that will not be paid incrementally because of the call combined with the principal payment the investor would have received at maturity."
relations:
  - {type: is-a, target: "/SEC/Debt/DebtInstruments/CallEvent.md", provenance: fibo}
---

call allowing the issuer to pay off remaining debt early

### Relationships
- is-a: [CallEvent](/SEC/Debt/DebtInstruments/CallEvent.md)
