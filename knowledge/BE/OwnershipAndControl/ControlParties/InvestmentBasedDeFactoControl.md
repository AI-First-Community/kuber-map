---
type: FIBO Class
title: "investment-based de facto control"
description: "control that arises through some investment in some entity, other than via the holding of constitutional equity (shares etc.) in that entity"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/InvestmentBasedDeFactoControl
tags: [BE, Release]
relations:
  - {type: is-a, target: "/FND/OwnershipAndControl/Control/DeFactoControl.md", provenance: fibo}
  - {type: has-party-in-control, target: "/BE/OwnershipAndControl/ControlParties/InvestmentBasedDeFactoControllingInterestParty.md", provenance: fibo}
  - {type: is-conferred-by, target: "/BE/OwnershipAndControl/OwnershipParties/InvestmentEquity.md", provenance: fibo}
---

control that arises through some investment in some entity, other than via the holding of constitutional equity (shares etc.) in that entity

### Relationships
- is-a: [DeFactoControl](/FND/OwnershipAndControl/Control/DeFactoControl.md)
- has-party-in-control: [InvestmentBasedDeFactoControllingInterestParty](/BE/OwnershipAndControl/ControlParties/InvestmentBasedDeFactoControllingInterestParty.md)
- is-conferred-by: [InvestmentEquity](/BE/OwnershipAndControl/OwnershipParties/InvestmentEquity.md)
