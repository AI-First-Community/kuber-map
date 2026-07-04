---
type: FIBO Class
title: "share"
description: "financial instrument that signifies a unit of equity ownership in a corporation, or a unit of ownership in a mutual fund, or interest in a general or limited partnership, or a unit of ownership in a structured product, such as a real estate investment trust"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
tags: [SEC, Release]
core: true
examples:
  - "One share of Tesla, Inc. common stock."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/EquityInstrument.md", provenance: fibo}
  - {type: confers-ownership-of, target: "/FND/Accounting/AccountingEquity/ShareholdersEquity.md", provenance: fibo}
  - {type: has-share-payment-status, target: "/SEC/Equities/EquityInstruments/SharePaymentStatus.md", provenance: fibo}
---

financial instrument that signifies a unit of equity ownership in a corporation, or a unit of ownership in a mutual fund, or interest in a general or limited partnership, or a unit of ownership in a structured product, such as a real estate investment trust

### Relationships
- is-a: [EquityInstrument](/FBC/FinancialInstruments/FinancialInstruments/EquityInstrument.md)
- confers-ownership-of: [ShareholdersEquity](/FND/Accounting/AccountingEquity/ShareholdersEquity.md)
- has-share-payment-status: [SharePaymentStatus](/SEC/Equities/EquityInstruments/SharePaymentStatus.md)
