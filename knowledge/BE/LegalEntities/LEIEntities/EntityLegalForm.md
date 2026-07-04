---
type: FIBO Class
title: "entity legal form"
description: "a classifier for a legal entity that indicates the nature of that entity as defined from a legal or regulatory perspective, in the jurisdiction in which it was established"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/EntityLegalForm
tags: [BE, Release]
relations:
  - {type: is-a, target: "/CMNS/Classifiers/Classifier.md", provenance: fibo}
  - {type: classifies, target: "/CMNS/Organizations/LegalPerson.md", provenance: fibo}
  - {type: is-applicable-in, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
  - {type: is-defined-in, target: "/BE/LegalEntities/LEIEntities/EntityLegalFormScheme.md", provenance: fibo}
---

a classifier for a legal entity that indicates the nature of that entity as defined from a legal or regulatory perspective, in the jurisdiction in which it was established

### Relationships
- is-a: [Classifier](/CMNS/Classifiers/Classifier.md)
- classifies: [LegalPerson](/CMNS/Organizations/LegalPerson.md)
- is-applicable-in: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
- is-defined-in: [EntityLegalFormScheme](/BE/LegalEntities/LEIEntities/EntityLegalFormScheme.md)
