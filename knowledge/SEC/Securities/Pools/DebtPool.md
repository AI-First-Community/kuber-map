---
type: FIBO Class
title: "debt pool"
description: "pool consisting of debt instruments, such as bonds, loans or mortgages"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/DebtPool
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Securities/Pools/InstrumentPool.md", provenance: fibo}
  - {type: has-analytic, target: "/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md", provenance: fibo}
  - {type: has-default-rate, target: "/SEC/Debt/PoolBackedSecurities/DefaultRate.md", provenance: fibo}
  - {type: has-factor, target: "/MD/DebtTemporal/DebtAnalytics/PoolFactor.md", provenance: fibo}
  - {type: has-measure, target: "/SEC/Debt/PoolBackedSecurities/PrepaymentSpeed.md", provenance: fibo}
  - {type: has-member, target: "/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md", provenance: fibo}
---

pool consisting of debt instruments, such as bonds, loans or mortgages

### Relationships
- is-a: [InstrumentPool](/SEC/Securities/Pools/InstrumentPool.md)
- has-analytic: [DebtPoolStatisticalMeasure](/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)
- has-default-rate: [DefaultRate](/SEC/Debt/PoolBackedSecurities/DefaultRate.md)
- has-factor: [PoolFactor](/MD/DebtTemporal/DebtAnalytics/PoolFactor.md)
- has-measure: [PrepaymentSpeed](/SEC/Debt/PoolBackedSecurities/PrepaymentSpeed.md)
- has-member: [DebtInstrument](/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md)
