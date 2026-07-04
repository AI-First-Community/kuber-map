---
type: FIBO Class
title: "swap leg"
description: "terms defining and the commitment to fulfill cashflow requirements (e.g., interest payments, coupon payments, etc.) for a component of a swap"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLeg
tags: [DER, Release]
detail: "A one-leg financing swap (also known as a single-leg financing swap) is a type of financial derivative, typically used by institutional investors or corporations, in which one party makes a series of fixed or floating payments to another party in exchange for a single upfront cash payment or financing. A three-leg financial swap is a more complex type of swap agreement where three different payment streams (or 'legs') are involved, as opposed to the traditional two-leg swaps (like fixed-for-floating interest rate swaps). This structure can be useful for sophisticated risk management or hedging strategies, particularly when exposure to multiple interest rates or currencies is desired. A two-leg financial swap is the most common type of swap agreement, where two counterparties exchange cash flows or obligations based on different financial variables. Each leg represents a stream of payments or flows tied to specific terms, such as fixed or floating interest rates, currencies, or commodities. The classic example of a two-leg swap is the interest rate swap, where one party pays a fixed interest rate while the other pays a floating interest rate. For some swaps this may be a commitment to net up the difference between a strike and an outcome, rather than to make a series of cashflows over time. For credit default swaps there are conditional commitments, contingent on the occurrence of a credit event. In most cases, a swap has two legs, one expressing the obligations of the seller and one expressing the obligations of the buyer. However, it is possible to represent more complex swaps, with one, three or more legs. The legs can be almost anything but usually one leg involves cash flows based on a notional principal amount that both parties agree to."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/DerivativesBasics/CashflowTerms.md", provenance: fibo}
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/SwapTerms.md", provenance: fibo}
  - {type: has-buyer, target: "/DER/DerivativesContracts/Swaps/SwapPayingParty.md", provenance: fibo}
  - {type: has-effective-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: has-seller, target: "/DER/DerivativesContracts/Swaps/SwapReceivingParty.md", provenance: fibo}
  - {type: has-termination-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: is-denominated-in, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
  - {type: is-leg-of, target: "/DER/DerivativesContracts/Swaps/Swap.md", provenance: fibo}
---

terms defining and the commitment to fulfill cashflow requirements (e.g., interest payments, coupon payments, etc.) for a component of a swap

### Relationships
- is-a: [CashflowTerms](/DER/DerivativesContracts/DerivativesBasics/CashflowTerms.md)
- is-a: [SwapTerms](/DER/DerivativesContracts/Swaps/SwapTerms.md)
- has-buyer: [SwapPayingParty](/DER/DerivativesContracts/Swaps/SwapPayingParty.md)
- has-effective-date: [Date](/CMNS/DatesAndTimes/Date.md)
- has-seller: [SwapReceivingParty](/DER/DerivativesContracts/Swaps/SwapReceivingParty.md)
- has-termination-date: [Date](/CMNS/DatesAndTimes/Date.md)
- is-denominated-in: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
- is-leg-of: [Swap](/DER/DerivativesContracts/Swaps/Swap.md)
