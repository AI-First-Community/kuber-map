---
type: FIBO Class
title: "unit issuer"
description: "The party which issues the Fund Unit."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/UnitIssuer
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingParty.md", provenance: fibo}
  - {type: is-played-by, target: "/BE/LegalEntities/CorporateBodies/Corporation.md", provenance: fibo}
  - {type: issues, target: "/SEC/Funds/Funds/FundUnit.md", provenance: fibo}
---

The party which issues the Fund Unit.

### Relationships
- is-a: [FundsProcessingParty](/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingParty.md)
- is-played-by: [Corporation](/BE/LegalEntities/CorporateBodies/Corporation.md)
- issues: [FundUnit](/SEC/Funds/Funds/FundUnit.md)
