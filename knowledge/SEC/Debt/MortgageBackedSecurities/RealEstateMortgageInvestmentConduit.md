---
type: FIBO Class
title: "real estate mortgage investment conduit"
description: "special purpose vehicle that pools mortgage loans together and issues mortgage-backed securities"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/RealEstateMortgageInvestmentConduit
tags: [SEC, Provisional]
detail: "A real estate mortgage investment conduit may be organized as a partnership, a trust, a corporation, or an association and is exempt from federal taxes."
synonyms:
  - "REMIC"
relations:
  - {type: is-a, target: "/BE/LegalEntities/LegalPersons/SpecialPurposeVehicle.md", provenance: fibo}
  - {type: owns, target: "/SEC/Debt/MortgageBackedSecurities/MortgagePool.md", provenance: fibo}
---

special purpose vehicle that pools mortgage loans together and issues mortgage-backed securities

### Relationships
- is-a: [SpecialPurposeVehicle](/BE/LegalEntities/LegalPersons/SpecialPurposeVehicle.md)
- owns: [MortgagePool](/SEC/Debt/MortgageBackedSecurities/MortgagePool.md)
