---
type: FIBO Class
title: "put feature"
description: "redemption provision giving the holder the right, but not the obligation, to sell a specified amount of the debt instrument (i.e., redeem it), prior to maturity"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PutFeature
tags: [SEC, Release]
synonyms:
  - "put provision"
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/DebtTerms.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md", provenance: fibo}
  - {type: comprises, target: "/SEC/Debt/DebtInstruments/PutSchedule.md", provenance: fibo}
  - {type: has-notification-provision, target: "/SEC/Debt/DebtInstruments/PutNotificationProvision.md", provenance: fibo}
---

redemption provision giving the holder the right, but not the obligation, to sell a specified amount of the debt instrument (i.e., redeem it), prior to maturity

### Relationships
- is-a: [DebtTerms](/FBC/DebtAndEquities/Debt/DebtTerms.md)
- is-a: [RedemptionProvision](/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md)
- comprises: [PutSchedule](/SEC/Debt/DebtInstruments/PutSchedule.md)
- has-notification-provision: [PutNotificationProvision](/SEC/Debt/DebtInstruments/PutNotificationProvision.md)
