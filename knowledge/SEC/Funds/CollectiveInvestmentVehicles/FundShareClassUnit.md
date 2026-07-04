---
type: FIBO Class
title: "fund share class unit"
description: "The legal structure in which you can purchase part of an investment pool, defined by a variety of characteristics like investor type, minimum size of investment, distribution type, fee and currency. A fund unit which gives the holder an equity stake in the fund."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundShareClassUnit
tags: [SEC, Provisional]
detail: "From review sessions: Theoretically you can buy a fraction of a share in a fund. This would depend on the legal structure of the fund, e.g. a minimum investment. There is always a distribution plan."
relations:
  - {type: is-a, target: "/SEC/Funds/Funds/FundUnit.md", provenance: fibo}
  - {type: has-strategy, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundUnitDistributionPolicy.md", provenance: fibo}
---

The legal structure in which you can purchase part of an investment pool, defined by a variety of characteristics like investor type, minimum size of investment, distribution type, fee and currency. A fund unit which gives the holder an equity stake in the fund.

### Relationships
- is-a: [FundUnit](/SEC/Funds/Funds/FundUnit.md)
- has-strategy: [FundUnitDistributionPolicy](/SEC/Funds/CollectiveInvestmentVehicles/FundUnitDistributionPolicy.md)
