---
type: FIBO Class
title: "o t c bond market price"
description: "The price determined for the marketplace for a bond which is traded over the counter."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/OTCBondMarketPrice
tags: [MD, Provisional]
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md", provenance: fibo}
  - {type: has-pricing-source, target: "/MD/DebtTemporal/DebtAnalytics/DebtSecuritiesMarketMaker.md", provenance: fibo}
---

The price determined for the marketplace for a bond which is traded over the counter.

### Relationships
- is-a: [SecurityPrice](/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
- has-pricing-source: [DebtSecuritiesMarketMaker](/MD/DebtTemporal/DebtAnalytics/DebtSecuritiesMarketMaker.md)
