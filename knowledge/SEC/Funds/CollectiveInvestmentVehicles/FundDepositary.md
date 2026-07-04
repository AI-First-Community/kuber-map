---
type: FIBO Class
title: "fund depositary"
description: "The party that holds and safeguards holdings owned by a fund. It is also responsible for compliance of the portfolio with legal ratios etc."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundDepositary
tags: [SEC, Provisional]
detail: "The depository may delegate custody to another entity (custodian). Definition origin:EFAMA DD"
relations:
  - {type: is-a, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingParty.md", provenance: fibo}
  - {type: provides-depositary-service-for, target: "/SEC/Funds/Funds/FundUnit.md", provenance: fibo}
---

The party that holds and safeguards holdings owned by a fund. It is also responsible for compliance of the portfolio with legal ratios etc.

### Relationships
- is-a: [FundsProcessingParty](/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingParty.md)
- provides-depositary-service-for: [FundUnit](/SEC/Funds/Funds/FundUnit.md)
