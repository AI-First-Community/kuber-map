---
type: FIBO Class
title: "examiner"
description: "party empowered as an official representative by a regulatory agency to investigate and review specified documents for accuracy and truthfulness"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/Examiner
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/BusinessAuthorizations/ResponsibleParty.md", provenance: fibo}
  - {type: is-authorized-by, target: "/CMNS/RegulatoryAgencies/RegulatoryAgency.md", provenance: fibo}
  - {type: is-played-by, target: "/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md", provenance: fibo}
---

party empowered as an official representative by a regulatory agency to investigate and review specified documents for accuracy and truthfulness

### Relationships
- is-a: [ResponsibleParty](/CMNS/BusinessAuthorizations/ResponsibleParty.md)
- is-authorized-by: [RegulatoryAgency](/CMNS/RegulatoryAgencies/RegulatoryAgency.md)
- is-played-by: [LegallyCompetentNaturalPerson](/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)
