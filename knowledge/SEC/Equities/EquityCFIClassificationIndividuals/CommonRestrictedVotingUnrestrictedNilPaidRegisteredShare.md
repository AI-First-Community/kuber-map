---
type: FIBO Class
title: "common, restricted voting, unrestricted, nil paid, registered share"
description: "common share that confers less than one vote per share, is unrestricted from a sales / transfer perspective, is nil paid and is registered"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityCFIClassificationIndividuals/CommonRestrictedVotingUnrestrictedNilPaidRegisteredShare
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/CommonShare.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/NilPaidShare.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/RestrictedVotingShare.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/UnrestrictedShare.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Securities/SecuritiesListings/RegisteredSecurity.md", provenance: fibo}
  - {type: is-classified-by, target: "/SEC/Equities/EquityCFIClassificationIndividuals/ESRUOR.md", provenance: fibo}
---

common share that confers less than one vote per share, is unrestricted from a sales / transfer perspective, is nil paid and is registered

### Relationships
- is-a: [CommonShare](/SEC/Equities/EquityInstruments/CommonShare.md)
- is-a: [NilPaidShare](/SEC/Equities/EquityInstruments/NilPaidShare.md)
- is-a: [RestrictedVotingShare](/SEC/Equities/EquityInstruments/RestrictedVotingShare.md)
- is-a: [UnrestrictedShare](/SEC/Equities/EquityInstruments/UnrestrictedShare.md)
- is-a: [RegisteredSecurity](/SEC/Securities/SecuritiesListings/RegisteredSecurity.md)
- is-classified-by: [ESRUOR](/SEC/Equities/EquityCFIClassificationIndividuals/ESRUOR.md)
