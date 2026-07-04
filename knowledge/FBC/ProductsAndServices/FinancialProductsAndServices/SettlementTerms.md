---
type: FIBO Class
title: "settlement terms"
description: "contract terms that define the commitment to and mechanism for settling one or more sides of a transaction"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractualCommitment.md", provenance: fibo}
  - {type: applies-to, target: "/FBC/FinancialInstruments/Settlement/Settlement.md", provenance: fibo}
  - {type: has-settlement-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: has-settlement-method, target: "/FBC/FinancialInstruments/Settlement/DeliveryMethod.md", provenance: fibo}
  - {type: specifies, target: "/FBC/FinancialInstruments/Settlement/SettlementConvention.md", provenance: fibo}
---

contract terms that define the commitment to and mechanism for settling one or more sides of a transaction

### Relationships
- is-a: [ContractualCommitment](/FND/Agreements/Contracts/ContractualCommitment.md)
- applies-to: [Settlement](/FBC/FinancialInstruments/Settlement/Settlement.md)
- has-settlement-date: [Date](/CMNS/DatesAndTimes/Date.md)
- has-settlement-method: [DeliveryMethod](/FBC/FinancialInstruments/Settlement/DeliveryMethod.md)
- specifies: [SettlementConvention](/FBC/FinancialInstruments/Settlement/SettlementConvention.md)
