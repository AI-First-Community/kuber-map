---
type: FIBO Class
title: "lender"
description: "a party that extends credit or money to a borrower with the expectation of being repaid, usually with interest"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Lender
tags: [FBC, Release]
core: true
examples:
  - "A mortgage bank or credit union extending a home loan."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/Creditor.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractParty.md", provenance: fibo}
---

a party that extends credit or money to a borrower with the expectation of being repaid, usually with interest

### Relationships
- is-a: [Creditor](/FBC/DebtAndEquities/Debt/Creditor.md)
- is-a: [ContractParty](/FND/Agreements/Contracts/ContractParty.md)
