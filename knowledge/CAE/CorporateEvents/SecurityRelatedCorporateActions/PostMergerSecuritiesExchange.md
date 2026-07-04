---
type: FIBO Class
title: "post-merger securities exchange"
description: "corporate action that involves the exchange of outstanding securities, initiated by the issuer which may include options, as the result of two or more companies combining assets, that is, an external, third party company"
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/PostMergerSecuritiesExchange
tags: [CAE, Provisional]
detail: "This is an action as a result of the merger, not the merger itself, and may be mandatory or voluntary. Cash payments may accompany share exchange."
relations:
  - {type: is-a, target: "/CAE/CorporateEvents/CorporateActions/CorporateAction.md", provenance: fibo}
  - {type: converts-from, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
  - {type: converts-to, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
  - {type: has-monetary-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

corporate action that involves the exchange of outstanding securities, initiated by the issuer which may include options, as the result of two or more companies combining assets, that is, an external, third party company

### Relationships
- is-a: [CorporateAction](/CAE/CorporateEvents/CorporateActions/CorporateAction.md)
- converts-from: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- converts-to: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- has-monetary-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
