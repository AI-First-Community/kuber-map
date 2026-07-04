---
type: FIBO Class
title: "debt instrument"
description: "financial instrument and credit agreement evidencing monies owed by the issuer to the holder on terms as specified"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CreditAgreement.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md", provenance: fibo}
  - {type: has-borrower, target: "/FBC/DebtAndEquities/Debt/Borrower.md", provenance: fibo}
  - {type: has-lender, target: "/FBC/DebtAndEquities/Debt/Lender.md", provenance: fibo}
---

financial instrument and credit agreement evidencing monies owed by the issuer to the holder on terms as specified

### Relationships
- is-a: [CreditAgreement](/FBC/DebtAndEquities/Debt/CreditAgreement.md)
- is-a: [FinancialInstrument](/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)
- has-borrower: [Borrower](/FBC/DebtAndEquities/Debt/Borrower.md)
- has-lender: [Lender](/FBC/DebtAndEquities/Debt/Lender.md)
