---
type: FIBO Class
title: "stock split"
description: "corporate action involving an increase in a corporation's number of outstanding equities without any change in the shareholder's equity or the aggregate market value at the time of the split"
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/StockSplit
tags: [CAE, Provisional]
detail: "Equity price and nominal value are reduced accordingly."
synonyms:
  - "change in nominal value"
  - "subdivision"
relations:
  - {type: is-a, target: "/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md", provenance: fibo}
  - {type: applies-to, target: "/SEC/Equities/EquityInstruments/Share.md", provenance: fibo}
---

corporate action involving an increase in a corporation's number of outstanding equities without any change in the shareholder's equity or the aggregate market value at the time of the split

### Relationships
- is-a: [MandatoryCorporateAction](/CAE/CorporateEvents/CorporateActions/MandatoryCorporateAction.md)
- applies-to: [Share](/SEC/Equities/EquityInstruments/Share.md)
