---
type: FIBO Class
title: "call feature"
description: "redemption provision defining the rights of the issuer to buy back a security at a call price after a call protection period"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallFeature
tags: [SEC, Release]
detail: "Most corporate and municipal bonds have ten-year call features (termed call protection by holders); government securities typically have none."
synonyms:
  - "call provision"
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md", provenance: fibo}
  - {type: comprises, target: "/SEC/Debt/DebtInstruments/CallSchedule.md", provenance: fibo}
  - {type: has-notification-provision, target: "/SEC/Debt/DebtInstruments/CallNotificationProvision.md", provenance: fibo}
---

redemption provision defining the rights of the issuer to buy back a security at a call price after a call protection period

### Relationships
- is-a: [RedemptionProvision](/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md)
- comprises: [CallSchedule](/SEC/Debt/DebtInstruments/CallSchedule.md)
- has-notification-provision: [CallNotificationProvision](/SEC/Debt/DebtInstruments/CallNotificationProvision.md)
