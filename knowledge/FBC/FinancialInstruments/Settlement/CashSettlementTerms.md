---
type: FIBO Class
title: "cash settlement terms"
description: "contractual commitment to settle in cash"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/CashSettlementTerms
tags: [FBC, Release]
detail: "Note that the security price represents a price per share or per lot, whereas the settlement amount represents a total. Note that the valuation determined via the appraisal of the underlying asset may include a quotation that is either an upper limit to the outstanding principal balance of the reference obligation for which the quote should be obtained, or a floating rate payer calculation amount."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/DerivativesBasics/ValuationTerms.md", provenance: fibo}
  - {type: has-minimum-quotation-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-price, target: "/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md", provenance: fibo}
  - {type: has-quotation-method, target: "/DER/CreditDerivatives/CreditDefaultSwaps/CashSettlementMethod.md", provenance: fibo}
  - {type: has-settlement-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-settlement-method, target: "/FBC/FinancialInstruments/Settlement/DeliveryInCash.md", provenance: fibo}
---

contractual commitment to settle in cash

### Relationships
- is-a: [SettlementTerms](/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md)
- comprises: [ValuationTerms](/DER/DerivativesContracts/DerivativesBasics/ValuationTerms.md)
- has-minimum-quotation-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-price: [SecurityPrice](/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
- has-quotation-method: [CashSettlementMethod](/DER/CreditDerivatives/CreditDefaultSwaps/CashSettlementMethod.md)
- has-settlement-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-settlement-method: [DeliveryInCash](/FBC/FinancialInstruments/Settlement/DeliveryInCash.md)
