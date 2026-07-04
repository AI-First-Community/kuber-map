---
type: FIBO Class
title: "fund processing terms"
description: "Formal terms for processing of the fund. These set out what the investor and the fund may or may not do. These include terms for redemption and subscription processing as well as general processing terms. ISO FIBIM definition: Processing characteristics linked to the instrument, ie, not to the market."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingTerms
tags: [SEC, Provisional]
detail: "These include Fund Subscription Terms, Fund Redemption Terms. and terms which relate to general processing and restrictions or otherwise on the holder. FPP notes: FPP presentation identifies many of these terms under the heading of Valuation Dealing characteristics. May need to revise which goes where in line with FPP. See also terms under NAV Valuation Calculation Method. Others of these terms appear in FPP under Instrument Restrictions. These cover the subscription, redemption and holding amounts and units and minimum holding period."
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractualCommitment.md", provenance: fibo}
  - {type: defines-main-fund-order-desk-account, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingAccount.md", provenance: fibo}
  - {type: has-default-settlement-convention, target: "/FBC/FinancialInstruments/Settlement/SettlementConvention.md", provenance: fibo}
---

Formal terms for processing of the fund. These set out what the investor and the fund may or may not do. These include terms for redemption and subscription processing as well as general processing terms. ISO FIBIM definition: Processing characteristics linked to the instrument, ie, not to the market.

### Relationships
- is-a: [ContractualCommitment](/FND/Agreements/Contracts/ContractualCommitment.md)
- defines-main-fund-order-desk-account: [FundsProcessingAccount](/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingAccount.md)
- has-default-settlement-convention: [SettlementConvention](/FBC/FinancialInstruments/Settlement/SettlementConvention.md)
