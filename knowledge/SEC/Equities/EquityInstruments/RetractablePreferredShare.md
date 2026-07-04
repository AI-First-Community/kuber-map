---
type: FIBO Class
title: "retractable preferred share"
description: "preferred share that gives the owner (shareholder) the right to redeem the stock under specified conditions"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/RetractablePreferredShare
tags: [SEC, Release]
detail: "When retractable preferred shares reach maturity, the shareholder has the right to sell them back to the stock issuer at the price stated on the agreement. In some cases, the issuer can force the shareholder to sell, and may have the option of exchanging retractable preferred shares for common shares instead of cash."
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/PreferredShare.md", provenance: fibo}
  - {type: has-redemption-terms, target: "/SEC/Equities/EquityInstruments/EquityRedemptionProvision.md", provenance: fibo}
---

preferred share that gives the owner (shareholder) the right to redeem the stock under specified conditions

### Relationships
- is-a: [PreferredShare](/SEC/Equities/EquityInstruments/PreferredShare.md)
- has-redemption-terms: [EquityRedemptionProvision](/SEC/Equities/EquityInstruments/EquityRedemptionProvision.md)
