---
type: FIBO Class
title: "offshore depositary receipt"
description: "depositary receipt issued under SEC Regulation S"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/OffshoreDepositaryReceipt
tags: [SEC, Release]
detail: "This regulation means that the securities are not, and will not be registered with any U.S. securities regulation authority. Regulation S shares cannot be held or traded by any 'U.S. person' as defined by SEC Regulation S rules. The shares are registered and issued to offshore, non-U.S. residents."
relations:
  - {type: is-a, target: "/SEC/Equities/DepositaryReceipts/SponsoredDepositaryReceipt.md", provenance: fibo}
  - {type: has-restriction, target: "/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/RegulationS.md", provenance: fibo}
---

depositary receipt issued under SEC Regulation S

### Relationships
- is-a: [SponsoredDepositaryReceipt](/SEC/Equities/DepositaryReceipts/SponsoredDepositaryReceipt.md)
- has-restriction: [RegulationS](/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/RegulationS.md)
