---
type: FIBO Class
title: "pool-backed security"
description: "debt instrument that derives its cashflow from an underlying pool of mortgage loans or other receivables"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity
tags: [SEC, Release]
detail: "If the security is a component of a collateralized debt obligation, then the underlying pool is typically segmented into various tranches, each of which provides cash flows to hedge particular risks, or that offset other gains by time to maturity or other factors."
relations:
  - {type: is-a, target: "/SEC/Debt/DebtInstruments/TradableDebtInstrument.md", provenance: fibo}
  - {type: is-based-on, target: "/SEC/Securities/Pools/InstrumentPool.md", provenance: fibo}
  - {type: is-characterized-by, target: "/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md", provenance: fibo}
  - {type: is-estimated-value-of, target: "/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate.md", provenance: fibo}
---

debt instrument that derives its cashflow from an underlying pool of mortgage loans or other receivables

### Relationships
- is-a: [TradableDebtInstrument](/SEC/Debt/DebtInstruments/TradableDebtInstrument.md)
- is-based-on: [InstrumentPool](/SEC/Securities/Pools/InstrumentPool.md)
- is-characterized-by: [DebtPoolStatisticalMeasure](/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)
- is-estimated-value-of: [CollateralValueAsOfDate](/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate.md)
