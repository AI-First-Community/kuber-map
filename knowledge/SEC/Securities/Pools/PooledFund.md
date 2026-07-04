---
type: FIBO Class
title: "pooled fund"
description: "pool of funds that a group of investors combines for common benefit"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PooledFund
tags: [SEC, Release]
detail: "A fund can be established for any purpose, such as a municipality setting aside money for a construction project, monies designated to endow a university chair or for scholarships, or funds set aside by insurance companies to settle claims. The US Securities and Exchange Commission describes a fund as an entity created to pool money from multiple investors."
examples:
  - "An investment club pools the funds of its members, giving them the opportunity to share in a portfolio offering greater diversification and the hope of a better return on their money than they could get individually."
synonyms:
  - "fund"
relations:
  - {type: is-a, target: "/FND/Accounting/AccountingEquity/FinancialAsset.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Securities/Pools/Pool.md", provenance: fibo}
  - {type: has-date-established, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: has-objective, target: "/FND/GoalsAndObjectives/Objectives/InvestmentObjective.md", provenance: fibo}
  - {type: has-part, target: "/SEC/Funds/Funds/FundUnit.md", provenance: fibo}
---

pool of funds that a group of investors combines for common benefit

### Relationships
- is-a: [FinancialAsset](/FND/Accounting/AccountingEquity/FinancialAsset.md)
- is-a: [Pool](/SEC/Securities/Pools/Pool.md)
- has-date-established: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- has-objective: [InvestmentObjective](/FND/GoalsAndObjectives/Objectives/InvestmentObjective.md)
- has-part: [FundUnit](/SEC/Funds/Funds/FundUnit.md)
