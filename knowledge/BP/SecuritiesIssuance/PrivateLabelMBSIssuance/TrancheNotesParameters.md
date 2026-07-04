---
type: FIBO Class
title: "tranche notes parameters"
description: "One set of information defining the notes breakdown of one tranche. Covers denominations and amounts that you can byu of the instrument in this tranche. Q: Is this really defined in the prospectus? A: yes The prospectus lists the characteristics including e.g. 'The notes will be sold in denominations of X AND Increuemtns of Y e.g. $250 000 incremented by $1000. Parameters include: Denominations Minimum amounts what else? Term origin:MBS PoC Reviews"
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TrancheNotesParameters
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSIssueProspectusPart.md", provenance: fibo}
  - {type: is-about, target: "/SEC/Debt/CollateralizedDebtObligations/MBSTrancheNote.md", provenance: fibo}
  - {type: maximum-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

One set of information defining the notes breakdown of one tranche. Covers denominations and amounts that you can byu of the instrument in this tranche. Q: Is this really defined in the prospectus? A: yes The prospectus lists the characteristics including e.g. "The notes will be sold in denominations of X AND Increuemtns of Y e.g. $250 000 incremented by $1000. Parameters include: Denominations Minimum amounts what else? Term origin:MBS PoC Reviews

### Relationships
- is-a: [TranchedMBSIssueProspectusPart](/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSIssueProspectusPart.md)
- is-about: [MBSTrancheNote](/SEC/Debt/CollateralizedDebtObligations/MBSTrancheNote.md)
- maximum-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
