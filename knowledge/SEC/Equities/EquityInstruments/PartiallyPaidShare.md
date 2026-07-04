---
type: FIBO Class
title: "partially paid share"
description: "share whose payment status indicates that only a portion of the market value has been received by the company for the shares"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PartiallyPaidShare
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/Share.md", provenance: fibo}
  - {type: has-share-payment-status, target: "/SEC/Equities/EquityInstruments/PartiallyPaidShareStatus.md", provenance: fibo}
---

share whose payment status indicates that only a portion of the market value has been received by the company for the shares

### Relationships
- is-a: [Share](/SEC/Equities/EquityInstruments/Share.md)
- has-share-payment-status: [PartiallyPaidShareStatus](/SEC/Equities/EquityInstruments/PartiallyPaidShareStatus.md)
