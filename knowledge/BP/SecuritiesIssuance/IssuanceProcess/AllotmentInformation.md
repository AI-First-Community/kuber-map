---
type: FIBO Class
title: "allotment information"
description: "Information about the allotment of quantities of the issue to different subscribers. This relates a single instrument allotment against the subscription amounts allotted to each Subscriber."
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/AllotmentInformation
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/IssuanceProcess/TradedInstrumentIssuanceProcessInformation.md", provenance: fibo}
  - {type: comprises, target: "/BP/SecuritiesIssuance/IssuanceProcess/SubscriptionClosingInformation.md", provenance: fibo}
  - {type: describes-allotment-of, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
---

Information about the allotment of quantities of the issue to different subscribers. This relates a single instrument allotment against the subscription amounts allotted to each Subscriber.

### Relationships
- is-a: [TradedInstrumentIssuanceProcessInformation](/BP/SecuritiesIssuance/IssuanceProcess/TradedInstrumentIssuanceProcessInformation.md)
- comprises: [SubscriptionClosingInformation](/BP/SecuritiesIssuance/IssuanceProcess/SubscriptionClosingInformation.md)
- describes-allotment-of: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
