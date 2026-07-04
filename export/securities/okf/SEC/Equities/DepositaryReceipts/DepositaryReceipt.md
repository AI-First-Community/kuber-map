---
type: FIBO Class
title: "depositary receipt"
description: "negotiable financial instrument issued by a trust company, security depositary, or bank that is evidence of the deposit of publicly traded securities and that facilitates the ownership of securities traded in other jurisdictions"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/DepositaryReceipt
tags: [SEC, Release]
detail: "Depositary receipts are widely used in order to allow the trading of securities in jurisdictions other than the one where the original securities were issued, such as in a local market. Depositary receipts facilitate buying securities in foreign companies, because the securities do not have to leave the home country. They enable domestic investors to buy securities of foreign companies without the accompanying risks or inconveniences of cross-border and cross-currency transactions."
examples:
  - "A receipt representing shares of a foreign company held by a depositary bank."
examples_provenance: curated
synonyms:
  - "DR"
  - "depositary receipt"
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
  - {type: has-traded-security, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
---

negotiable financial instrument issued by a trust company, security depositary, or bank that is evidence of the deposit of publicly traded securities and that facilitates the ownership of securities traded in other jurisdictions

### Relationships
- is-a: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- has-traded-security: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
