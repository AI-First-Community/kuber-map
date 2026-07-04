---
type: FIBO Class
title: "investor"
description: "party that owns some stake in some organization by way of investment"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/Investor
tags: [BE, Release]
relations:
  - {type: is-a, target: "/BE/OwnershipAndControl/OwnershipParties/EntityOwner.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractParty.md", provenance: fibo}
  - {type: holds, target: "/BE/OwnershipAndControl/OwnershipParties/InvestmentEquity.md", provenance: fibo}
---

party that owns some stake in some organization by way of investment

### Relationships
- is-a: [EntityOwner](/BE/OwnershipAndControl/OwnershipParties/EntityOwner.md)
- is-a: [ContractParty](/FND/Agreements/Contracts/ContractParty.md)
- holds: [InvestmentEquity](/BE/OwnershipAndControl/OwnershipParties/InvestmentEquity.md)
