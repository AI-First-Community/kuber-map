---
type: FIBO Class
title: "make securities available in market"
description: "What happens here? e.g. notices / marketing (phone calls) Structured Finance: There's not really notices in the newspaper, it's a very small market and it's all based on relationships so there's no public notice. So you would get an email from the sales person at the bank who has just closed the deal and is now selling these (this bank is the broker/dealer who bought it?) There's not really much of a secondary market - the initial investors would often hold on to these. There is something around Bloomberg - you can go there and see what's available, if someone has a number of notes from a iven tranche, that they are willing to sell. So there's no transpoarency (!!) Sales would be OTC but less transparent e.g. if you look up a normal OTC stock, you would be able to see more of this information, than in these (non Agency) MBS issues and other SF. DOES THIS APPLY IN ALL MBS??."
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/MakeSecuritiesAvailableInMarket
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity.md", provenance: fibo}
  - {type: is-issue-of, target: "/SEC/Debt/CollateralizedDebtObligations/TranchedMBSDeal.md", provenance: fibo}
  - {type: requires, target: "/SEC/Debt/CollateralizedDebtObligations/TranchedMBSDealProspectus.md", provenance: fibo}
---

What happens here? e.g. notices / marketing (phone calls) Structured Finance: There's not really notices in the newspaper, it's a very small market and it's all based on relationships so there's no public notice. So you would get an email from the sales person at the bank who has just closed the deal and is now selling these (this bank is the broker/dealer who bought it?) There's not really much of a secondary market - the initial investors would often hold on to these. There is something around Bloomberg - you can go there and see what's available, if someone has a number of notes from a iven tranche, that they are willing to sell. So there's no transpoarency (!!) Sales would be OTC but less transparent e.g. if you look up a normal OTC stock, you would be able to see more of this information, than in these (non Agency) MBS issues and other SF. DOES THIS APPLY IN ALL MBS??.

### Relationships
- is-a: [IssuanceProcessActivity](/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity.md)
- is-issue-of: [TranchedMBSDeal](/SEC/Debt/CollateralizedDebtObligations/TranchedMBSDeal.md)
- requires: [TranchedMBSDealProspectus](/SEC/Debt/CollateralizedDebtObligations/TranchedMBSDealProspectus.md)
