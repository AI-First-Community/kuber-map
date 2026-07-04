---
type: FIBO Class
title: "fund unit"
description: "quantified share of beneficial interest in a pooled fund, representing a proportional claim on the fund's assets, income, or entitlements"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundUnit
tags: [SEC, Release]
detail: "A fund unit may be tradable or non-tradable depending on the legal form, regulatory status, and operational framework of the fund. Fund units are allocated to a participant, investor, or beneficiary according to the fund's governing structure. If it is a closed fund, you can still trade the units. You trade back with the fund. Not with a counterparty. Therefore this is a tradable contract, though it may not necessarily be a transferable contract."
relations:
  - {type: is-a, target: "/FND/Law/LegalCapacity/ContractualInterest.md", provenance: fibo}
  - {type: has-currency, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
  - {type: has-details, target: "/SEC/Funds/CollectiveInvestmentVehicles/NetAssetValueCalculationMethod.md", provenance: fibo}
  - {type: has-fund-processing-terms, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingGeneralTerms.md", provenance: fibo}
  - {type: has-fund-processing-terms, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundRedemptionTerms.md", provenance: fibo}
  - {type: is-part-of, target: "/SEC/Securities/Pools/PooledFund.md", provenance: fibo}
---

quantified share of beneficial interest in a pooled fund, representing a proportional claim on the fund's assets, income, or entitlements

### Relationships
- is-a: [ContractualInterest](/FND/Law/LegalCapacity/ContractualInterest.md)
- has-currency: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
- has-details: [NetAssetValueCalculationMethod](/SEC/Funds/CollectiveInvestmentVehicles/NetAssetValueCalculationMethod.md)
- has-fund-processing-terms: [FundProcessingGeneralTerms](/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingGeneralTerms.md)
- has-fund-processing-terms: [FundRedemptionTerms](/SEC/Funds/CollectiveInvestmentVehicles/FundRedemptionTerms.md)
- is-part-of: [PooledFund](/SEC/Securities/Pools/PooledFund.md)
