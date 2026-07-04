---
type: FIBO Class
title: "real property"
description: "physical asset defined as land together with any structures that are permanently attached to that land, such as houses, trees, fences and improvements"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealProperty
tags: [FND, Release]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
detail: "Real property may be classified according to its general use as residential, commercial, agricultural, industrial, or special purpose. This term is sometimes used synonymously with 'real estate', though not in all circumstances under US law. Real property typically encompasses both the physical land and everything that lies above, below, or on its surface, including any fixed structures, natural resources, and rights or interests (e.g., mineral rights). There are cases, such as condominiums, in which the interior of the structure is owned by a party that may not own the land. There are also cases in which certain long-term leases have similar characteristics to ownership, but are time-bound."
examples:
  - "A single-family house and the land it sits on."
examples_provenance: curated
synonyms:
  - "parcel"
relations:
  - {type: is-a, target: "/FND/Accounting/AccountingEquity/PhysicalAsset.md", provenance: fibo}
  - {type: is-a, target: "/FND/Places/RealProperty/RealEstate.md", provenance: fibo}
  - {type: is-classified-by, target: "/LOAN/RealEstateLoans/MortgageOrigination/DwellingCapacity.md", provenance: fibo}
  - {type: is-classified-by, target: "/LOAN/RealEstateLoans/MortgageOrigination/ManufacturedHomeLegalClassification.md", provenance: fibo}
  - {type: is-evaluated-by, target: "/FND/Places/RealProperty/RealPropertyAppraisal.md", provenance: fibo}
---

physical asset defined as land together with any structures that are permanently attached to that land, such as houses, trees, fences and improvements

### Relationships
- is-a: [PhysicalAsset](/FND/Accounting/AccountingEquity/PhysicalAsset.md)
- is-a: [RealEstate](/FND/Places/RealProperty/RealEstate.md)
- is-classified-by: [DwellingCapacity](/LOAN/RealEstateLoans/MortgageOrigination/DwellingCapacity.md)
- is-classified-by: [ManufacturedHomeLegalClassification](/LOAN/RealEstateLoans/MortgageOrigination/ManufacturedHomeLegalClassification.md)
- is-evaluated-by: [RealPropertyAppraisal](/FND/Places/RealProperty/RealPropertyAppraisal.md)
