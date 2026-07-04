---
type: FIBO Class
title: "product disclosure requirement"
description: "A requirement governing what representations can be made about a product, as it affects the consumer."
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/ProductDisclosureRequirement
tags: [LOAN, Provisional]
core: true
use_cases:
  - "Regulatory Reporting & Compliance (supervisory filing)"
detail: "There are also rules which encompass limitations on how you might attach loans and liens to principle dwellings, e.g. when or whether you can foreclose on someone's principal dwelling with impunity; what rights the consumer has - this last will be a separate kind of regulation."
examples:
  - "A requirement to provide a Key Facts document for a mortgage product."
examples_provenance: curated
relations:
  - {type: is-a, target: "/LOAN/LoansGeneral/LoansRegulatory/DisclosureRequirement.md", provenance: fibo}
  - {type: governs, target: "/LOAN/LoansGeneral/LoansRegulatory/GoodFaithEstimate.md", provenance: fibo}
  - {type: governs, target: "/LOAN/LoansGeneral/LoansRegulatory/LoanProductRepresentations.md", provenance: fibo}
---

A requirement governing what representations can be made about a product, as it affects the consumer.

### Relationships
- is-a: [DisclosureRequirement](/LOAN/LoansGeneral/LoansRegulatory/DisclosureRequirement.md)
- governs: [GoodFaithEstimate](/LOAN/LoansGeneral/LoansRegulatory/GoodFaithEstimate.md)
- governs: [LoanProductRepresentations](/LOAN/LoansGeneral/LoansRegulatory/LoanProductRepresentations.md)
