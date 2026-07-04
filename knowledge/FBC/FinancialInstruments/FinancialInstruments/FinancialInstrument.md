---
type: FIBO Class
title: "financial instrument"
description: "written contract that gives rise to both a financial asset of one entity and a financial liability of another entity"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument
tags: [FBC, Release]
detail: "A financial instrument can be thought of as a template that defines an arrangement structure that remains to be fleshed out with terms and parameters in order to establish a specific instance of the contract."
examples:
  - "Examples of financial instruments include: cash, evidence of an ownership interest in an entity, or a contractual right to receive (or deliver) cash, or another financial instrument."
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/WrittenContract.md", provenance: fibo}
  - {type: has-financial-instrument-short-name, target: "/SEC/Securities/SecuritiesIssuance/FinancialInstrumentShortName.md", provenance: fibo}
  - {type: has-nominal-value, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-restriction, target: "/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction.md", provenance: fibo}
  - {type: is-classified-by, target: "/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md", provenance: fibo}
  - {type: is-classified-by, target: "/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md", provenance: fibo}
  - {type: is-denominated-in, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
  - {type: is-identified-by, target: "/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md", provenance: fibo}
  - {type: is-issued-by, target: "/FBC/FinancialInstruments/FinancialInstruments/Issuer.md", provenance: fibo}
  - {type: is-legally-recorded-in, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
---

written contract that gives rise to both a financial asset of one entity and a financial liability of another entity

### Relationships
- is-a: [WrittenContract](/FND/Agreements/Contracts/WrittenContract.md)
- has-financial-instrument-short-name: [FinancialInstrumentShortName](/SEC/Securities/SecuritiesIssuance/FinancialInstrumentShortName.md)
- has-nominal-value: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-restriction: [SecuritiesRestriction](/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction.md)
- is-classified-by: [IndustrySectorClassifier](/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md)
- is-classified-by: [FinancialInstrumentClassifier](/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md)
- is-denominated-in: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
- is-identified-by: [FinancialInstrumentIdentifier](/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md)
- is-issued-by: [Issuer](/FBC/FinancialInstruments/FinancialInstruments/Issuer.md)
- is-legally-recorded-in: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
