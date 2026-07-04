---
type: FIBO Class
title: "synthetic debt s p v"
description: "A Special Purpose Vehicle set up for the issuance of synthetics CDOs. This entity (like all SPVs) its itself registered as some kind of legal entity, distinct from the sponsoring organization. It becomes the Issuer of Synthetic CDO issues."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticDebtSPV
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/BE/LegalEntities/LegalPersons/SpecialPurposeVehicle.md", provenance: fibo}
  - {type: holds, target: "/SEC/Debt/SyntheticCDOs/SyntheticDebtInstrumentPoolFundingAsset.md", provenance: fibo}
---

A Special Purpose Vehicle set up for the issuance of synthetics CDOs. This entity (like all SPVs) its itself registered as some kind of legal entity, distinct from the sponsoring organization. It becomes the Issuer of Synthetic CDO issues.

### Relationships
- is-a: [SpecialPurposeVehicle](/BE/LegalEntities/LegalPersons/SpecialPurposeVehicle.md)
- holds: [SyntheticDebtInstrumentPoolFundingAsset](/SEC/Debt/SyntheticCDOs/SyntheticDebtInstrumentPoolFundingAsset.md)
