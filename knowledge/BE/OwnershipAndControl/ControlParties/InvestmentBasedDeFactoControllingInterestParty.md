---
type: FIBO Class
title: "investment-based de facto controlling interest party"
description: "party that holds investment-based control over some other party"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/InvestmentBasedDeFactoControllingInterestParty
tags: [BE, Release]
relations:
  - {type: is-a, target: "/BE/OwnershipAndControl/ControlParties/DeFactoControllingInterestParty.md", provenance: fibo}
  - {type: is-a, target: "/BE/OwnershipAndControl/OwnershipParties/Investor.md", provenance: fibo}
  - {type: is-controlling-party-in, target: "/BE/OwnershipAndControl/ControlParties/InvestmentBasedDeFactoControl.md", provenance: fibo}
---

party that holds investment-based control over some other party

### Relationships
- is-a: [DeFactoControllingInterestParty](/BE/OwnershipAndControl/ControlParties/DeFactoControllingInterestParty.md)
- is-a: [Investor](/BE/OwnershipAndControl/OwnershipParties/Investor.md)
- is-controlling-party-in: [InvestmentBasedDeFactoControl](/BE/OwnershipAndControl/ControlParties/InvestmentBasedDeFactoControl.md)
