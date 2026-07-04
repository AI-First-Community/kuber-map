---
type: FIBO Class
title: "credit default swap"
description: "bilateral contract in which one party (protection seller) agrees to provide payment to the other party (protection buyer) should a credit event occur against the underlying, which could be a specified debt (the reference obligation), a specific debt issuer (reference entity), a basket of reference entities and/or reference obligations, or a credit index (reference index)"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap
tags: [DER, Release]
detail: "According to a 2022 working paper from the Federal Reserve, 'credit default swaps (CDS) are, by far, the most common type of credit derivative. They are financial instruments that allow the transfer of credit risk among market participants, potentially facilitating greater efficiency in the pricing and distribution of credit risk. In its most basic form, a CDS is a contract where a 'protection buyer' agrees to make periodic payments (the CDS 'spread' or premium) over a predetermined number of years (the maturity or term of the CDS) to a 'protection seller' in exchange for a payment from the protection seller in the event of default by a 'reference entity.' CDS premiums tend to be paid quarterly and are set as a percentage of the total amount of protection bought (the 'notional amount' of the contract). CDS maturities generally range from one to ten years, with the five-year maturity being particularly common.' See https://www.federalreserve.gov/econres/feds/files/2022023pap.pdf for more detail. Note that the effective date of the contract indicates the starting date of the credit protection defined therein."
synonyms:
  - "CDS"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/DerivativesBasics/CreditDerivative.md", provenance: fibo}
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/Swap.md", provenance: fibo}
  - {type: has-contract-price, target: "/FND/Accounting/CurrencyAmount/MonetaryPrice.md", provenance: fibo}
  - {type: has-contractual-element, target: "/DER/CreditDerivatives/CreditDefaultSwaps/CreditProtectionTerms.md", provenance: fibo}
  - {type: has-occurrence, target: "/DER/CreditDerivatives/CreditDefaultSwaps/SettlementAuction.md", provenance: fibo}
  - {type: specifies, target: "/DER/CreditDerivatives/CreditDefaultSwaps/TriggeringEvent.md", provenance: fibo}
---

bilateral contract in which one party (protection seller) agrees to provide payment to the other party (protection buyer) should a credit event occur against the underlying, which could be a specified debt (the reference obligation), a specific debt issuer (reference entity), a basket of reference entities and/or reference obligations, or a credit index (reference index)

### Relationships
- is-a: [CreditDerivative](/DER/DerivativesContracts/DerivativesBasics/CreditDerivative.md)
- is-a: [Swap](/DER/DerivativesContracts/Swaps/Swap.md)
- has-contract-price: [MonetaryPrice](/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- has-contractual-element: [CreditProtectionTerms](/DER/CreditDerivatives/CreditDefaultSwaps/CreditProtectionTerms.md)
- has-occurrence: [SettlementAuction](/DER/CreditDerivatives/CreditDefaultSwaps/SettlementAuction.md)
- specifies: [TriggeringEvent](/DER/CreditDerivatives/CreditDefaultSwaps/TriggeringEvent.md)
