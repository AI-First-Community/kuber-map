---
type: FIBO Class
title: "privately placed depositary receipt"
description: "depositary receipt that represents shares in a private placement under the SEC Rule 144-A"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/PrivatelyPlacedDepositaryReceipt
tags: [SEC, Release]
detail: "Some foreign companies will set up an ADR program under SEC Rule 144-A. This provision makes the issuance of shares a private placement. Shares of companies registered under Rule 144-A are restricted stock and may only be issued to or traded by qualified institutional buyers (QIBs). U.S. public shareholders are generally not permitted to invest in these ADR programs, and most are held exclusively through the Depository Trust & Clearing Corporation, so there is often very little information on these companies."
relations:
  - {type: is-a, target: "/SEC/Equities/DepositaryReceipts/SponsoredDepositaryReceipt.md", provenance: fibo}
  - {type: has-restriction, target: "/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/Rule144A.md", provenance: fibo}
---

depositary receipt that represents shares in a private placement under the SEC Rule 144-A

### Relationships
- is-a: [SponsoredDepositaryReceipt](/SEC/Equities/DepositaryReceipts/SponsoredDepositaryReceipt.md)
- has-restriction: [Rule144A](/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/Rule144A.md)
