---
type: FIBO Class
title: "common, non-voting, restricted, nil paid, registered share"
description: "common share that confers exactly 0 votes per share, is restricted from a sales / transfer perspective, is nil paid and is registered"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityCFIClassificationIndividuals/CommonNonVotingRestrictedNilPaidRegisteredShare
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/CommonShare.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/NilPaidShare.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/NonVotingShare.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/RestrictedShare.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Securities/SecuritiesListings/RegisteredSecurity.md", provenance: fibo}
  - {type: is-classified-by, target: "/SEC/Equities/EquityCFIClassificationIndividuals/ESNTOR.md", provenance: fibo}
---

common share that confers exactly 0 votes per share, is restricted from a sales / transfer perspective, is nil paid and is registered

### Relationships
- is-a: [CommonShare](/SEC/Equities/EquityInstruments/CommonShare.md)
- is-a: [NilPaidShare](/SEC/Equities/EquityInstruments/NilPaidShare.md)
- is-a: [NonVotingShare](/SEC/Equities/EquityInstruments/NonVotingShare.md)
- is-a: [RestrictedShare](/SEC/Equities/EquityInstruments/RestrictedShare.md)
- is-a: [RegisteredSecurity](/SEC/Securities/SecuritiesListings/RegisteredSecurity.md)
- is-classified-by: [ESNTOR](/SEC/Equities/EquityCFIClassificationIndividuals/ESNTOR.md)
