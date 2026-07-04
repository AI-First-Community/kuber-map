---
type: FIBO Class
title: "retractable preferred share with extendable maturity date"
description: "retractable preferred share with a fixed maturity date whose issuer and/or holders have the option to extend the maturity date"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/RetractablePreferredShareWithExtendableMaturityDate
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/PreferredShareWithFixedMaturityDate.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/RetractablePreferredShare.md", provenance: fibo}
  - {type: has-extension-provision, target: "/FND/Agreements/Contracts/ExtensionProvision.md", provenance: fibo}
---

retractable preferred share with a fixed maturity date whose issuer and/or holders have the option to extend the maturity date

### Relationships
- is-a: [PreferredShareWithFixedMaturityDate](/SEC/Equities/EquityInstruments/PreferredShareWithFixedMaturityDate.md)
- is-a: [RetractablePreferredShare](/SEC/Equities/EquityInstruments/RetractablePreferredShare.md)
- has-extension-provision: [ExtensionProvision](/FND/Agreements/Contracts/ExtensionProvision.md)
