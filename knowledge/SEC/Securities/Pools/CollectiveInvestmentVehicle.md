---
type: FIBO Class
title: "collective investment vehicle"
description: "assets pooled by investors whose share capital remains separate from the assets of the vehicle"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/CollectiveInvestmentVehicle
tags: [SEC, Release]
core: true
detail: "A fund is an entity created to pool money from multiple investors - often referred to as limited partners. Each investor makes an investment in the fund by purchasing an interest in the fund entity, and the adviser uses that money to make investments on behalf of the fund. Collective investment vehicles are typically organized and operated by management companies, banks, or trust companies. Shares or units are issued in the form of unit trusts, mutual funds, or other similar contracts. Common kinds of funds include pension funds, insurance funds, foundations, and endowments. Such pools are often invested and professionally managed, including investment pools, umbrella pools, share class pools, etc. From EFAMA DD: The word fund can refer to either an investment pool, umbrella or share class, and is commonly refered to as a collective investment vehicle (can have ISIN or not). The meaning here is for the investment pool (of which an Umbrella fund is also one such) and not to the share class."
examples:
  - "A UCITS fund that pools money from many investors."
examples_provenance: curated
relations:
  - {type: is-a, target: "/SEC/Securities/Pools/PooledFund.md", provenance: fibo}
  - {type: administered-by, target: "/SEC/Funds/Funds/FundAdministrator.md", provenance: fibo}
  - {type: advised-by, target: "/FBC/FunctionalEntities/FinancialServicesEntities/RegisteredInvestmentAdvisor.md", provenance: fibo}
  - {type: distributed-by, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundDistributor.md", provenance: fibo}
  - {type: fund-has-related-party, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingParty.md", provenance: fibo}
  - {type: has-additional-information, target: "/SEC/Funds/CollectiveInvestmentVehicles/OtherInvestmentFundInformation.md", provenance: fibo}
  - {type: has-auditor, target: "/BE/OwnershipAndControl/Executives/ExternalAuditor.md", provenance: fibo}
  - {type: has-currency, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
  - {type: has-data-provider, target: "/BE/FunctionalEntities/Publishers/MarketDataProvider.md", provenance: fibo}
  - {type: has-depository, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundDepositary.md", provenance: fibo}
  - {type: has-fund-policy, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundInvestmentPolicy.md", provenance: fibo}
  - {type: has-legal-structure, target: "/SEC/Funds/Funds/LegalFundStructure.md", provenance: fibo}
  - {type: has-management-company, target: "/SEC/Funds/Funds/FundManager.md", provenance: fibo}
  - {type: has-related-fund-terms, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingTerms.md", provenance: fibo}
  - {type: has-strategy, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundUnitDistributionMethod.md", provenance: fibo}
  - {type: has-subscription-terms, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundSubscriptionTerms.md", provenance: fibo}
  - {type: has-transfer-agent, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundTransferAgent.md", provenance: fibo}
  - {type: is-described-by, target: "/SEC/Securities/SecuritiesIssuance/Prospectus.md", provenance: fibo}
  - {type: is-issued-by, target: "/SEC/Funds/CollectiveInvestmentVehicles/UnitIssuer.md", provenance: fibo}
  - {type: is-legally-recorded-in, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
  - {type: supervised-by, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundSupervisoryAuthority.md", provenance: fibo}
---

assets pooled by investors whose share capital remains separate from the assets of the vehicle

### Relationships
- is-a: [PooledFund](/SEC/Securities/Pools/PooledFund.md)
- administered-by: [FundAdministrator](/SEC/Funds/Funds/FundAdministrator.md)
- advised-by: [RegisteredInvestmentAdvisor](/FBC/FunctionalEntities/FinancialServicesEntities/RegisteredInvestmentAdvisor.md)
- distributed-by: [FundDistributor](/SEC/Funds/CollectiveInvestmentVehicles/FundDistributor.md)
- fund-has-related-party: [FundsProcessingParty](/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingParty.md)
- has-additional-information: [OtherInvestmentFundInformation](/SEC/Funds/CollectiveInvestmentVehicles/OtherInvestmentFundInformation.md)
- has-auditor: [ExternalAuditor](/BE/OwnershipAndControl/Executives/ExternalAuditor.md)
- has-currency: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
- has-data-provider: [MarketDataProvider](/BE/FunctionalEntities/Publishers/MarketDataProvider.md)
- has-depository: [FundDepositary](/SEC/Funds/CollectiveInvestmentVehicles/FundDepositary.md)
- has-fund-policy: [FundInvestmentPolicy](/SEC/Funds/CollectiveInvestmentVehicles/FundInvestmentPolicy.md)
- has-legal-structure: [LegalFundStructure](/SEC/Funds/Funds/LegalFundStructure.md)
- has-management-company: [FundManager](/SEC/Funds/Funds/FundManager.md)
- has-related-fund-terms: [FundProcessingTerms](/SEC/Funds/CollectiveInvestmentVehicles/FundProcessingTerms.md)
- has-strategy: [FundUnitDistributionMethod](/SEC/Funds/CollectiveInvestmentVehicles/FundUnitDistributionMethod.md)
- has-subscription-terms: [FundSubscriptionTerms](/SEC/Funds/CollectiveInvestmentVehicles/FundSubscriptionTerms.md)
- has-transfer-agent: [FundTransferAgent](/SEC/Funds/CollectiveInvestmentVehicles/FundTransferAgent.md)
- is-described-by: [Prospectus](/SEC/Securities/SecuritiesIssuance/Prospectus.md)
- is-issued-by: [UnitIssuer](/SEC/Funds/CollectiveInvestmentVehicles/UnitIssuer.md)
- is-legally-recorded-in: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
- supervised-by: [FundSupervisoryAuthority](/SEC/Funds/CollectiveInvestmentVehicles/FundSupervisoryAuthority.md)
