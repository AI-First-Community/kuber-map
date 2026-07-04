---
type: FIBO Class
title: "master agreement"
description: "contract between named parties that outlines the terms and conditions designed to apply to a number of accounts, transactions, or other activities between the parties, and that consolidates and provides overarching terms for separate but related agreements"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MasterAgreement
tags: [FND, Release]
detail: "A master agreement can be used to set out standard terms and conditions so that any new agreements don't need to cover the same information again."
examples:
  - "A master services agreement governs the terms between a service provider and client. Typically, clients will use Statements of Work that point back to the master agreement so they don't have to recreate a new contract with new terms each time there is a new project, or to cover common terms across services, warranties, and deliveries."
  - "Some credit facilities and many brokerage arrangements are master agreements."
synonyms:
  - "master contract"
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/WrittenContract.md", provenance: fibo}
  - {type: governs, target: "/FND/Agreements/Contracts/Contract.md", provenance: fibo}
---

contract between named parties that outlines the terms and conditions designed to apply to a number of accounts, transactions, or other activities between the parties, and that consolidates and provides overarching terms for separate but related agreements

### Relationships
- is-a: [WrittenContract](/FND/Agreements/Contracts/WrittenContract.md)
- governs: [Contract](/FND/Agreements/Contracts/Contract.md)
