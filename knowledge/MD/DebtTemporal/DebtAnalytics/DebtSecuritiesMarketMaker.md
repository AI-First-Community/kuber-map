---
type: FIBO Class
title: "debt securities market maker"
description: "An actor which has the role of Market Maker in a given market."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtSecuritiesMarketMaker
tags: [MD, Provisional]
relations:
  - {type: is-a, target: "/CMNS/Organizations/ServiceProvider.md", provenance: fibo}
  - {type: determines-market-price-for-debt, target: "/MD/DebtTemporal/DebtAnalytics/OTCBondMarketPrice.md", provenance: fibo}
---

An actor which has the role of Market Maker in a given market.

### Relationships
- is-a: [ServiceProvider](/CMNS/Organizations/ServiceProvider.md)
- determines-market-price-for-debt: [OTCBondMarketPrice](/MD/DebtTemporal/DebtAnalytics/OTCBondMarketPrice.md)
