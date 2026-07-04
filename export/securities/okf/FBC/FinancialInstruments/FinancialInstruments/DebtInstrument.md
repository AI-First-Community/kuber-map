---
type: FIBO Class
title: "debt instrument"
description: "financial instrument and credit agreement evidencing monies owed by the issuer to the holder on terms as specified"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument
tags: [FBC, Release]
core: true
use_cases:
  - "Securities Instruments & Issuance (capital markets)"
examples:
  - "A 10-year US Treasury note paying semi-annual interest."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CreditAgreement.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md", provenance: fibo}
  - {type: has-borrower, target: "/FBC/DebtAndEquities/Debt/Borrower.md", provenance: fibo}
  - {type: has-call-feature, target: "/SEC/Debt/DebtInstruments/CallFeature.md", provenance: fibo}
  - {type: has-interest-payment-terms, target: "/FBC/DebtAndEquities/Debt/InterestPaymentTerms.md", provenance: fibo}
  - {type: has-lender, target: "/FBC/DebtAndEquities/Debt/Lender.md", provenance: fibo}
  - {type: has-offering, target: "/SEC/Debt/DebtInstruments/DebtOffering.md", provenance: fibo}
  - {type: has-put-feature, target: "/SEC/Debt/DebtInstruments/PutFeature.md", provenance: fibo}
  - {type: has-redemption-terms, target: "/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md", provenance: fibo}
  - {type: has-repayment-terms, target: "/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms.md", provenance: fibo}
---

financial instrument and credit agreement evidencing monies owed by the issuer to the holder on terms as specified

### Relationships
- is-a: [CreditAgreement](/FBC/DebtAndEquities/Debt/CreditAgreement.md)
- is-a: [FinancialInstrument](/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)
- has-borrower: [Borrower](/FBC/DebtAndEquities/Debt/Borrower.md)
- has-call-feature: [CallFeature](/SEC/Debt/DebtInstruments/CallFeature.md)
- has-interest-payment-terms: [InterestPaymentTerms](/FBC/DebtAndEquities/Debt/InterestPaymentTerms.md)
- has-lender: [Lender](/FBC/DebtAndEquities/Debt/Lender.md)
- has-offering: [DebtOffering](/SEC/Debt/DebtInstruments/DebtOffering.md)
- has-put-feature: [PutFeature](/SEC/Debt/DebtInstruments/PutFeature.md)
- has-redemption-terms: [RedemptionProvision](/FBC/FinancialInstruments/FinancialInstruments/RedemptionProvision.md)
- has-repayment-terms: [PrincipalRepaymentTerms](/FBC/DebtAndEquities/Debt/PrincipalRepaymentTerms.md)
