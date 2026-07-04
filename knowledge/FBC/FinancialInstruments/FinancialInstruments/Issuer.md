---
type: FIBO Class
title: "issuer"
description: "role of a party that issues (or proposes to issue in a formal filing) one or more financial instruments"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Issuer
tags: [FBC, Release]
core: true
detail: "An issuer can be any legal person, including a legally competent natural person, company, government, or political subdivision, agency, or instrumentality of a government, depending on the nature of the instrument. A person might provide a loan directly to another party, but most instruments are issued by legal entities. With respect to certificates of deposit for securities, voting-trust certificates, or collateral- trust certificates, or with respect to certificates of interest or shares in an unincorporated investment trust not having a board of directors or of the fixed, restricted management, or unit type, the term issuer means the person or persons performing the acts and assuming the duties of depositor or manager pursuant to the provisions of the trust or other agreement or instrument under which such securities are issued; and except that with respect to equipment-trust certificates or like securities, the term issuer means the person by whom the equipment or property is, or is to be, used."
examples:
  - "Apple Inc., the issuer of AAPL shares and its corporate bonds."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractPrincipal.md", provenance: fibo}
---

role of a party that issues (or proposes to issue in a formal filing) one or more financial instruments

### Relationships
- is-a: [ContractPrincipal](/FND/Agreements/Contracts/ContractPrincipal.md)
