---
type: FIBO Class
title: "co-maker"
description: "party that signs a borrower's promissory note, providing additional security and potentially improving the quality of the debt"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Comaker
tags: [LOAN, Release]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
detail: "Differences between a co-maker and co-borrower include: (1) a co-maker is not listed on the title of the asset to which the loan applies, (2) a co-maker does not have any legal ownership rights to the asset, and (3) the co-maker does not make regular payments on the loan unless the primary borrower(s) fails to do so. The co-maker's liability is similar to that of an endorser or guarantor, but with additional risk/exposure, as they can be compelled to honor the debt much sooner and regardless of whether certain conditions are met."
examples:
  - "A parent who co-signs a child's mortgage note."
examples_provenance: curated
synonyms:
  - "comaker"
  - "cosigner"
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractThirdParty.md", provenance: fibo}
---

party that signs a borrower's promissory note, providing additional security and potentially improving the quality of the debt

### Relationships
- is-a: [ContractThirdParty](/FND/Agreements/Contracts/ContractThirdParty.md)
