---
type: FIBO Class
title: "universal loan identifier"
description: "unique identifier given to unequivocally identify a specific loan secured by real estate"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/UniversalLoanIdentifier
tags: [LOAN, Provisional]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
  - "Regulatory Reporting & Compliance (supervisory filing)"
detail: "In the US, the structure of this identifier is defined in the 2015 revision to the Home Mortgage Disclosure Act."
examples:
  - "The Universal Loan Identifier (ULI) assigned to a mortgage for HMDA reporting."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md", provenance: fibo}
  - {type: comprises, target: "/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md", provenance: fibo}
---

unique identifier given to unequivocally identify a specific loan secured by real estate

### Relationships
- is-a: [FinancialInstrumentIdentifier](/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md)
- comprises: [LegalEntityIdentifier](/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md)
- identifies: [LoanSecuredByRealEstate](/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md)
