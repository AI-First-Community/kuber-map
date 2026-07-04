# Cross-domain bridges — FIBO contribution proposal

**15 curated cross-domain relations** that FIBO does not currently draw, surfaced while building learner-first, agent-grounding maps of FIBO for four financial use cases. Each is offered back to the EDM Council for consideration.

*Author:* Sanjeev Azad <sanjeev.azad@gmail.com> · *License:* MIT · *Source project:* Kuber Map for FIBO.

## How these were derived (and why they are safe to review)

Every bridge passed an automated grounding gate (`etl/bridges.py`) before inclusion:

1. **Both endpoints are real FIBO classes** — resolved against an extract of the pinned FIBO source (see `fibo-source.pin`); no invented IRIs.
2. **FIBO does not already assert the edge** — the resolver rejects any relation FIBO already draws (source → target), so nothing here duplicates existing FIBO.
3. **Each carries a rationale + an external citation** (regulation or standard), so a reviewer can trace the real-world basis of the proposed link.

Proposed relations are expressed in a neutral `kmb:` namespace in the accompanying `fibo-bridges.ttl`; we deliberately do **not** assert unverified FIBO object properties. The intent is to identify the *gap*; mapping each edge to the right FIBO property (or minting one) is the reviewer's call.

## Proposed relations (edges)

| edge | proposed property |
|---|---|
| backed-by | `kmb:backedBy` |
| beneficial-owner-of | `kmb:beneficialOwnerOf` |
| filed-by | `kmb:filedBy` |
| identified-by | `kmb:identifiedBy` |
| played-by | `kmb:playedBy` |
| reported-in | `kmb:reportedIn` |
| required-by | `kmb:requiredBy` |
| submitted-to | `kmb:submittedTo` |

## Loan origination & underwriting  (4)

### HMDA covered loan contract —[reported-in]→ HMDA report
- **kind:** intra-domain gap
- **source:** `https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-CoveredLoanContract`
- **target:** `https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-Report`
- **rationale:** HMDA requires every covered loan/application to be recorded on the institution's Loan/Application Register that constitutes the HMDA report. FIBO models both HMDA-CoveredLoanContract and HMDA-Report but does not connect the reported loan to the report that reports it.
- **citation:** 12 CFR 1003.4 (Regulation C — compilation of reportable data)

### HMDA report —[filed-by]→ financial institution
- **kind:** cross-domain (LOAN->FBC)
- **source:** `https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-Report`
- **target:** `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution`
- **rationale:** A HMDA report is filed by a covered financial institution. FIBO links HMDA-Report to the RegulatoryAgency it is submitted-to, but not to the filing institution — leaving the filer unresolved.
- **citation:** 12 CFR 1003.2 (covered institution); 12 CFR 1003.5 (reporting)

### financial institution —[identified-by]→ legal entity identifier
- **kind:** cross-domain (FBC->BE)
- **source:** `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution`
- **target:** `https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifier`
- **rationale:** For KYC / entity resolution a financial institution is identified by its Legal Entity Identifier. FIBO defines LegalEntityIdentifier in BE but does not connect FinancialInstitution to it.
- **citation:** ISO 17442 (LEI); FIBO BE LegalEntityIdentifier

### lender —[played-by]→ financial institution
- **kind:** role->entity gap (FBC)
- **source:** `https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Lender`
- **target:** `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution`
- **rationale:** Lender is modeled as a party role (is-a ContractParty/Creditor); FinancialInstitution is the legal-entity type that plays it. FIBO leaves the role-to-entity link implicit, blocking resolution of 'the lender' to a regulated institution.
- **citation:** FIBO FBC party-role vs entity modeling

## KYC & beneficial ownership  (4)

### legal entity —[identified-by]→ legal entity identifier
- **kind:** cross-domain (CMNS->BE)
- **source:** `https://www.omg.org/spec/Commons/Organizations/LegalEntity`
- **target:** `https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifier`
- **rationale:** For KYC and entity resolution a legal entity is identified by its Legal Entity Identifier (ISO 17442). FIBO defines LegalEntityIdentifier and applies it to LEI-registered entities, but does not link the base LegalEntity class to it, leaving generic entity-to-LEI resolution implicit.
- **citation:** ISO 17442 (LEI); FATF Recommendation 24

### beneficial owner —[beneficial-owner-of]→ legal entity
- **kind:** cross-domain (BE->CMNS)
- **source:** `https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner`
- **target:** `https://www.omg.org/spec/Commons/Organizations/LegalEntity`
- **rationale:** A beneficial owner is the party that ultimately owns or controls a legal entity. FIBO models BeneficialOwnership as a situation but draws no direct edge from the BeneficialOwner role to the legal entity owned, which KYC / ultimate-beneficial-owner resolution needs.
- **citation:** FATF Recommendations 24 & 25; US CDD rule 31 CFR 1010.230

### customer —[played-by]→ legal person
- **kind:** role->entity gap (FND->CMNS)
- **source:** `https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Customer`
- **target:** `https://www.omg.org/spec/Commons/Organizations/LegalPerson`
- **rationale:** A customer is a party role played by a legal person (or a natural person). Resolving 'the customer' to the underlying legal entity is core to KYC onboarding, but FIBO leaves the role-to-entity link implicit.
- **citation:** FIBO FND party-role vs entity modeling; KYC customer onboarding

### account holder —[identified-by]→ legal entity identifier
- **kind:** cross-domain (FBC->BE)
- **source:** `https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder`
- **target:** `https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifier`
- **rationale:** An institutional account holder is identified for KYC by its Legal Entity Identifier. FIBO models accounts and their holders but does not connect an account holder to its LEI.
- **citation:** ISO 17442 (LEI); KYC / CDD account onboarding

## Regulatory reporting & compliance  (4)

### reporting party —[identified-by]→ legal entity identifier
- **kind:** cross-domain (FND->BE)
- **source:** `https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/ReportingParty`
- **target:** `https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifier`
- **rationale:** In supervisory and transaction reporting the party that submits a report is identified by its Legal Entity Identifier. FIBO defines the ReportingParty role (FND) and the LegalEntityIdentifier (BE) but does not connect a reporting party to its LEI.
- **citation:** ISO 17442 (LEI); MiFID II / ESMA transaction reporting; CFTC swap reporting

### regulatory report —[submitted-to]→ regulatory agency
- **kind:** intra-domain gap (CMNS)
- **source:** `https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryReport`
- **target:** `https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency`
- **rationale:** A regulatory report is submitted to the regulatory agency that requires it. FIBO defines both RegulatoryReport and RegulatoryAgency in Commons but does not draw the edge from a report to the agency it is filed with.
- **citation:** General supervisory-reporting practice; e.g. HMDA filing to the CFPB, MiFID II reporting to national competent authorities

### regulatory report —[required-by]→ regulation
- **kind:** cross-domain (CMNS->FND)
- **source:** `https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryReport`
- **target:** `https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Regulation`
- **rationale:** A regulatory report exists because a regulation mandates it. FIBO models RegulatoryReport (CMNS) and Regulation (FND) separately but leaves the report-to-mandating-regulation link implicit.
- **citation:** Reporting obligations arise from regulations, e.g. HMDA report required by Regulation C

### securities trades reporting —[submitted-to]→ trade reporting facility
- **kind:** cross-domain (BP->FBC)
- **source:** `https://spec.edmcouncil.org/fibo/ontology/BP/Process/FinancialContextAndProcess/SecuritiesTradesReporting`
- **target:** `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/TradeReportingFacility`
- **rationale:** Executed off-exchange securities trades are reported to a trade reporting facility. FIBO models the securities-trades-reporting process (BP) and the TradeReportingFacility (FBC) but does not connect the reporting activity to the facility it reports to.
- **citation:** FINRA Trade Reporting Facility rules; MiFID II APA reporting

## Securities instruments & issuance  (3)

### mortgage-backed security —[backed-by]→ mortgage
- **kind:** cross-domain (SEC->LOAN)
- **source:** `https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity`
- **target:** `https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/Mortgage`
- **rationale:** A mortgage-backed security represents claims on the cash flows from an underlying pool of mortgage loans. FIBO models the security (SEC) and the mortgage instrument (LOAN) in separate domains but does not draw the edge from the MBS to the mortgage loans that back it, which securitization and loan-level disclosure analysis need.
- **citation:** SEC Regulation AB, 17 CFR 229.1100 (asset-backed securities, loan-level data)

### asset-backed security —[backed-by]→ loan
- **kind:** cross-domain (SEC->LOAN)
- **source:** `https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity`
- **target:** `https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Loan`
- **rationale:** An asset-backed security is collateralized by a pool of receivables such as auto or consumer loans. FIBO defines the ABS in SEC and the loan in LOAN but leaves the backing relationship between the security and its underlying loans implicit.
- **citation:** SEC Regulation AB, 17 CFR 229.1100; securitization structuring

### issuer —[identified-by]→ legal entity identifier
- **kind:** cross-domain (FBC->BE)
- **source:** `https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Issuer`
- **target:** `https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifier`
- **rationale:** For securities issuance and regulatory reporting a securities issuer is identified by its Legal Entity Identifier. FIBO defines the Issuer role (FBC) and the LegalEntityIdentifier (BE) but does not connect an issuer to its LEI.
- **citation:** ISO 17442 (LEI); MiFID II / ESMA and SEC issuer identification
