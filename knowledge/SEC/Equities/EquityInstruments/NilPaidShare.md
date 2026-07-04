---
type: FIBO Class
title: "nil paid share"
description: "share whose payment status indicates that none of the market value has been received by the company for the shares"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/NilPaidShare
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/Share.md", provenance: fibo}
  - {type: has-share-payment-status, target: "/SEC/Equities/EquityInstruments/NilPaidShareStatus.md", provenance: fibo}
---

share whose payment status indicates that none of the market value has been received by the company for the shares

### Relationships
- is-a: [Share](/SEC/Equities/EquityInstruments/Share.md)
- has-share-payment-status: [NilPaidShareStatus](/SEC/Equities/EquityInstruments/NilPaidShareStatus.md)
