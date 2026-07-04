---
type: FIBO Class
title: "financial instrument"
description: "written contract that gives rise to both a financial asset of one entity and a financial liability of another entity"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/WrittenContract.md", provenance: fibo}
  - {type: has-nominal-value, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: is-denominated-in, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
  - {type: is-identified-by, target: "/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md", provenance: fibo}
  - {type: is-issued-by, target: "/FBC/FinancialInstruments/FinancialInstruments/Issuer.md", provenance: fibo}
  - {type: is-legally-recorded-in, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
---

written contract that gives rise to both a financial asset of one entity and a financial liability of another entity

### Relationships
- is-a: [WrittenContract](/FND/Agreements/Contracts/WrittenContract.md)
- has-nominal-value: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- is-denominated-in: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
- is-identified-by: [FinancialInstrumentIdentifier](/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md)
- is-issued-by: [Issuer](/FBC/FinancialInstruments/FinancialInstruments/Issuer.md)
- is-legally-recorded-in: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
