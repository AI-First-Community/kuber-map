---
type: FIBO Class
title: "trading status message"
description: "A message about trading status."
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/TradingStatusMessage
tags: [CAE, Provisional]
detail: "There are a number of such messages. Events v Status: See e.g. Active: this relates to one state OR two transitions (transition from pre-issuance to Trading, or from Suspended to Trading)."
relations:
  - {type: is-a, target: "/CMNS/Documents/Notice.md", provenance: fibo}
  - {type: is-about, target: "/MD/TemporalCore/SecurityTradingStatuses/SecurityTradingStatus.md", provenance: fibo}
  - {type: refers-to, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
---

A message about trading status.

### Relationships
- is-a: [Notice](/CMNS/Documents/Notice.md)
- is-about: [SecurityTradingStatus](/MD/TemporalCore/SecurityTradingStatuses/SecurityTradingStatus.md)
- refers-to: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
