---
type: FIBO Class
title: "rights exercise event"
description: "Exercising the right to purchase the shares. Furhter Notes: This is an action on the part of the holder. SWIFT: Call/exercise on nil-paid securities/rights resulting from a rights distribution (RHDI) (To be used for the second event in case rights issue is dealt with in 2 events, first event being the RHDI)."
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/RightsExerciseEvent
tags: [CAE, Provisional]
detail: "There is a rights trading period overlaps with rights subscriptiuon period (you can trade the rights) Rights exercise period - expiry date. Some time after the expiry the new shares are distributed. This is the distribution."
relations:
  - {type: is-a, target: "/CAE/CorporateEvents/CorporateActions/CorporateAction.md", provenance: fibo}
---

Exercising the right to purchase the shares. Furhter Notes: This is an action on the part of the holder. SWIFT: Call/exercise on nil-paid securities/rights resulting from a rights distribution (RHDI) (To be used for the second event in case rights issue is dealt with in 2 events, first event being the RHDI).

### Relationships
- is-a: [CorporateAction](/CAE/CorporateEvents/CorporateActions/CorporateAction.md)
