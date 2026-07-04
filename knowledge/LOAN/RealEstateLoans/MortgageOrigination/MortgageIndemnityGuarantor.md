---
type: FIBO Class
title: "mortgage indemnity guarantor"
description: "guarantor and insurer that provides mortgage insurance in the form of a mortgage indemnity guarantee (MIG)"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityGuarantor
tags: [LOAN, Provisional]
core: true
detail: "SME Review notes 16 Sept: Guaranty - mortgage insurance e.g. insure up to 80% exposure. When you get into indemnification, then for instance if the product doesn't meet the investor's requirement such that if it doesn't get paid then the lender steps in and takes the hit for the loan - this is usually a precondition for securitizing (issuing) the loan in a pool. If the loan is not going to be sold on the secondary market there would be no need to indemnify that loan so this term would not apply. Indemnification is insurance for the investor, while the lender is the one providing that indemnification."
examples:
  - "A private mortgage insurer providing PMI / MIG cover."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Guaranty/Guarantor.md", provenance: fibo}
  - {type: is-a, target: "/FBC/DebtAndEquities/Guaranty/Insurer.md", provenance: fibo}
---

guarantor and insurer that provides mortgage insurance in the form of a mortgage indemnity guarantee (MIG)

### Relationships
- is-a: [Guarantor](/FBC/DebtAndEquities/Guaranty/Guarantor.md)
- is-a: [Insurer](/FBC/DebtAndEquities/Guaranty/Insurer.md)
