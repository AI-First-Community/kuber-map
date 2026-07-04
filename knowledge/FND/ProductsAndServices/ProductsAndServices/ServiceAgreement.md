---
type: FIBO Class
title: "service agreement"
description: "written contract between a client and service provider whereby the service provider supplies some service in the form of time, effort, and/or expertise in exchange for compensation"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/ServiceAgreement
tags: [FND, Release]
synonyms:
  - "service contract"
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/WrittenContract.md", provenance: fibo}
  - {type: governs, target: "/CMNS/Organizations/Service.md", provenance: fibo}
  - {type: has-contract-party, target: "/CMNS/Organizations/ServiceProvider.md", provenance: fibo}
---

written contract between a client and service provider whereby the service provider supplies some service in the form of time, effort, and/or expertise in exchange for compensation

### Relationships
- is-a: [WrittenContract](/FND/Agreements/Contracts/WrittenContract.md)
- governs: [Service](/CMNS/Organizations/Service.md)
- has-contract-party: [ServiceProvider](/CMNS/Organizations/ServiceProvider.md)
