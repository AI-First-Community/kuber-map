---
type: FIBO Class
title: "redeemable preferred share"
description: "preferred share that gives the issuer the right to redeem the stock under specified conditions"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/RedeemablePreferredShare
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/PreferredShare.md", provenance: fibo}
  - {type: has-redemption-terms, target: "/SEC/Equities/EquityInstruments/EquityRedemptionProvision.md", provenance: fibo}
---

preferred share that gives the issuer the right to redeem the stock under specified conditions

### Relationships
- is-a: [PreferredShare](/SEC/Equities/EquityInstruments/PreferredShare.md)
- has-redemption-terms: [EquityRedemptionProvision](/SEC/Equities/EquityInstruments/EquityRedemptionProvision.md)
