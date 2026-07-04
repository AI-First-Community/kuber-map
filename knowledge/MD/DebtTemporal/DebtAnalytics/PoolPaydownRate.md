---
type: FIBO Class
title: "pool paydown rate"
description: "The rate at which the pool is paying down. This is based on observed factor. CPR, SMM, etc. etc. Measured differently for different kinds of security. CBO might have a prepayment rate for example if the underlying bond is callable. with a non agency mortgge dela, defualts will effect this. so for instance there is principal is no lnger inthe pool because the mortgagee defaults. With agency these are not taken out in the case of default but for non agency these mortgages are removed from the pool if and when a mortgagee defualts."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/PoolPaydownRate
tags: [MD, Provisional]
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Ratio.md", provenance: fibo}
  - {type: is-based-on, target: "/MD/DebtTemporal/DebtAnalytics/PoolFactor.md", provenance: fibo}
---

The rate at which the pool is paying down. This is based on observed factor. CPR, SMM, etc. etc. Measured differently for different kinds of security. CBO might have a prepayment rate for example if the underlying bond is callable. with a non agency mortgge dela, defualts will effect this. so for instance there is principal is no lnger inthe pool because the mortgagee defaults. With agency these are not taken out in the case of default but for non agency these mortgages are removed from the pool if and when a mortgagee defualts.

### Relationships
- is-a: [Ratio](/CMNS/QuantitiesAndUnits/Ratio.md)
- is-based-on: [PoolFactor](/MD/DebtTemporal/DebtAnalytics/PoolFactor.md)
