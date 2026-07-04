---
type: FIBO Class
title: "tender offer"
description: "corporate action involving an offer made to shareholders, normally by a third party, requesting them to sell (tender) or exchange their equities"
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/TenderOffer
tags: [CAE, Provisional]
synonyms:
  - "acquisition"
  - "buyback"
  - "purchase offer"
  - "takeover"
relations:
  - {type: is-a, target: "/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction.md", provenance: fibo}
  - {type: applies-to, target: "/SEC/Equities/EquityInstruments/Share.md", provenance: fibo}
---

corporate action involving an offer made to shareholders, normally by a third party, requesting them to sell (tender) or exchange their equities

### Relationships
- is-a: [VoluntaryCorporateAction](/CAE/CorporateEvents/CorporateActions/VoluntaryCorporateAction.md)
- applies-to: [Share](/SEC/Equities/EquityInstruments/Share.md)
