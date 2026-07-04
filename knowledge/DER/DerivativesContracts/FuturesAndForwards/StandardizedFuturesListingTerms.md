---
type: FIBO Class
title: "standardized futures listing terms"
description: "contract terms established by a derivatives exchange that apply to any listing of a futures contract on that exchange."
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/StandardizedFuturesListingTerms
tags: [DER, Release]
detail: "Individual listings will take on these standard terms but they are not contractual terms of the futures contract, they are facts about that listing on that exchange."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/StandardizedTerms.md", provenance: fibo}
  - {type: applies-to, target: "/SEC/Securities/SecuritiesListings/Listing.md", provenance: fibo}
  - {type: has-publisher, target: "/FBC/FunctionalEntities/Markets/DesignatedContractMarket.md", provenance: fibo}
---

contract terms established by a derivatives exchange that apply to any listing of a futures contract on that exchange.

### Relationships
- is-a: [DerivativeTerms](/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms.md)
- is-a: [StandardizedTerms](/FBC/FinancialInstruments/FinancialInstruments/StandardizedTerms.md)
- applies-to: [Listing](/SEC/Securities/SecuritiesListings/Listing.md)
- has-publisher: [DesignatedContractMarket](/FBC/FunctionalEntities/Markets/DesignatedContractMarket.md)
