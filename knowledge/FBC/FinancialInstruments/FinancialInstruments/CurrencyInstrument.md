---
type: FIBO Class
title: "currency instrument"
description: "financial instrument used for the purposes of currency trading"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/CurrencyInstrument
tags: [FBC, Release]
examples:
  - "Example currencies include UK pounds, US dollars, Euro. An example currency instrument is spot currency instrument."
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md", provenance: fibo}
  - {type: has-buying-currency, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
  - {type: has-selling-currency, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
---

financial instrument used for the purposes of currency trading

### Relationships
- is-a: [FinancialInstrument](/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)
- has-buying-currency: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
- has-selling-currency: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
