---
type: FIBO Class
title: "callable bond"
description: "bond that includes a stipulation allowing the issuer the right to repurchase and retire the bond at the call price after the call protection period"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CallableBond
tags: [SEC, Release]
core: true
examples:
  - "A corporate bond the issuer may redeem after five years if interest rates fall."
examples_provenance: curated
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/Bond.md", provenance: fibo}
  - {type: has-call-feature, target: "/SEC/Debt/DebtInstruments/CallFeature.md", provenance: fibo}
  - {type: has-extraordinary-redemption-provision, target: "/SEC/Debt/Bonds/ExtraordinaryRedemptionProvision.md", provenance: fibo}
---

bond that includes a stipulation allowing the issuer the right to repurchase and retire the bond at the call price after the call protection period

### Relationships
- is-a: [Bond](/SEC/Debt/Bonds/Bond.md)
- has-call-feature: [CallFeature](/SEC/Debt/DebtInstruments/CallFeature.md)
- has-extraordinary-redemption-provision: [ExtraordinaryRedemptionProvision](/SEC/Debt/Bonds/ExtraordinaryRedemptionProvision.md)
