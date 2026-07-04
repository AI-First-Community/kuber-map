# Grounding context — Regulatory Reporting & Compliance (supervisory filing)

Curated FIBO concepts and cross-domain bridges that ground this agent. Cite the
`resource` IRI on every claim. `provenance: fibo` = from FIBO; `provenance: curated`
= authored by this project (grounded in FIBO's structure).

## Registration, filing & identifiers

### Nationwide Mortgage Licensing System and Registry Identifier  [LOAN/Provisional]
- **definition:** the number permanently assigned by the Nationwide Mortgage Licensing System and Registry (NMLS) for each company, branch, and individual that maintains a single account on NMLS.
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/NMLSR-ID
- **relations:** is-a → license identifier

### business register identifier  [FBC/Release]
- **definition:** identifier that uniquely identifies a business register, such as a register identified by the Global Legal Entity Identifier Foundation (GLEIF) registration authorities list
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegisterIdentifier
- **relations:** is-a → identifier; identifies → business registry; is-registered-by → business registration authority

### filing details  [BP/Provisional]
- **definition:** Document capturing the particulars of a regulatory filing, such as what was filed, when, and with which authority. _(definition: curated)_
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/FilingDetails
- **relations:** is-a → document

### legal entity identifier  [BE/Release]
- **definition:** an organization identifier that uniquely identifies a legal person as defined in ISO 17442
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifier
- **relations:** is-a → organization identifier; is-a → registered identifier; identifies → legal person; is-defined-in → legal entity identifier scheme

### legal entity identifier registry  [FBC/Release]
- **definition:** registry for registering and maintaining information about business entities for a particular jurisdiction
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LegalEntityIdentifierRegistry
- **relations:** is-a → business registry; comprises → legal entity identifier registry entry

### register with regulatory authority  [BP/Provisional]
- **definition:** Process step in which an issuer registers a securities offering with the relevant regulatory authority before it can be listed or sold. _(definition: curated)_
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/RegisterWithRegulatoryAuthority
- **relations:** is-a → initial public offering process step; is-provided-by → exchange

### universal loan identifier  [LOAN/Provisional]
- **definition:** unique identifier given to unequivocally identify a specific loan secured by real estate
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/UniversalLoanIdentifier
- **relations:** is-a → financial instrument identifier; comprises → legal entity identifier; identifies → loan secured by real estate

## Regulations, rules & law

### consumer credit protection law  [LOAN/Provisional]
- **definition:** Consumer protection law that regulates the extension of consumer credit, requiring fair terms and disclosure to borrowers, such as the US Consumer Credit Protection Act. _(definition: curated)_
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/ConsumerCreditProtectionLaw
- **relations:** is-a → consumer protection law

### financial markets regulation  [BP/Provisional]
- **definition:** Body of rules and requirements, set by regulators, that governs the conduct of financial markets and their participants (e.g. MiFID II). _(definition: curated)_
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BP/Process/FinancialContextAndProcess/FinancialMarketsRegulation
- **relations:** is-a → financial industry context

### legal obligation  [FND/Release]
- **definition:** an obligation or duty that is enforceable by a court
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalObligation
- **relations:** is-a → duty; is-applicable-in → jurisdiction

### reg b  [LOAN/Provisional]
- **definition:** US regulation concerning "Equal credit opportunity act" Electronic delivery of disclosures
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/RegB
- **relations:** is-a → consumer credit equal treatment requirement; is-a → disclosure requirement

### reg z  [LOAN/Provisional]
- **definition:** US Fed regulation "Truth in Lending Act" uniform standards for electronic delivery of disclosures
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/RegZ
- **relations:** is-a → product disclosure requirement

### regulation  [FND/Release]
- **definition:** a rule used to carry out a law
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Regulation
- **relations:** is-a → legal construct; is-applicable-in → jurisdiction; is-conferred-by → law; is-issued-by → regulatory agency

### regulation identification scheme  [FBC/Release]
- **definition:** a scheme for organizing information and allocating identifiers to regulations
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/RegulationIdentificationScheme
- **relations:** is-a → identification scheme; has-member → regulation identifier

### regulation identifier  [FBC/Release]
- **definition:** an identifier associated with a regulation
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/RegulationIdentifier
- **relations:** is-a → identifier; identifies → regulation; is-member-of → regulation identification scheme

## Regulators & authorities

### business registration authority  [FBC/Release]
- **definition:** registration authority that is responsible for maintaining a registry of business entities
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority
- **relations:** is-a → registrar; is-a → registration authority; manages → business registry; registers → registration identifier

### fund supervisory authority  [SEC/Provisional]
- **definition:** party that supervises the fund or fund industry
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundSupervisoryAuthority
- **relations:** is-a → party role

### government agency  [BE/Release]
- **definition:** permanent or semi-permanent organization, often an appointed commission, in the machinery of government that is responsible for the oversight and administration of specific functions
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentAgency
- **relations:** is-a → government body; is-managed-by → government appointee

### government body  [BE/Release]
- **definition:** formal organization that is an agency, instrumentality, or other body of a supranational, national, federal, state, or local government, including certain multijurisdictional agencies and departments that carry out the business of government
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentBody
- **relations:** is-a → formal organization; has-objective → public purpose

### primary federal regulator  [FBC/Release]
- **definition:** federal regulatory agency that is designated as the main agency responsible for oversight of a given institution for an institution
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/PrimaryFederalRegulator
- **relations:** is-a → regulatory agency; is-played-by → government body

### regulated exchange  [FBC/Release]
- **definition:** regulated market that is operated by and/or managed by a market operator that brings together or facilitates the bringing together of multiple third-party buying and selling interests in financial instruments
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/RegulatedExchange
- **relations:** is-a → exchange; is-classified-by → MarketCategoryClassifier-RMKT; is-governed-by → jurisdiction; is-regulated-by → regulatory agency

### regulatory agency  [CMNS/n/a]
- **definition:** public authority or government agency responsible for exercising authority over something in a regulatory or supervisory capacity
- **cite:** https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency
- **relations:** is-a → authorizing party; is-a → service provider; has-jurisdiction → jurisdiction; is-played-by → formal organization; issues → government-issued license; provides → regulatory service

### regulatory capacity  [FBC/Release]
- **definition:** the capacity of some natural person to regulate some industry, organization, or product by virtue of some certification program on behalf of some regulatory agency
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/RegulatoryCapacity
- **relations:** is-a → legal capacity

### regulatory service  [CMNS/n/a]
- **definition:** service provided by a regulatory agency, which may include, but not be limited to, examination, monitoring, supervision, testing, or other capabilities required to ensure the integrity, fairness, safety, or other capacity of a given industry, organization, or product
- **cite:** https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryService
- **relations:** is-a → service; is-provided-by → regulatory agency

### self-regulating organization  [FBC/Release]
- **definition:** non-governmental organization that has the power to create and exercise some degree of regulatory authority over an industry or profession in some country or group of countries
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/SelfRegulatingOrganization
- **relations:** is-a → regulatory agency; is-played-by → non-governmental organization

## Regulatory actions & rating agencies

### HMDA covered loan contract  [LOAN/Provisional]
- **definition:** a closed-end mortgage loan or open-end line of credit that is not an excluded transaction for HMDA reporting under US section 1003.3(c) of the Revised Home Mortgage Disclosure Act of 2015
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-CoveredLoanContract
- **relations:** is-a → loan secured by real estate; is-classified-by → how submitted

### credit rating agency  [FBC/Provisional]
- **definition:** rating agency that publishes reports assessing the creditworthiness of a borrower or legal entity, either generally or with respect to a specific obligation
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency
- **relations:** is-a → financial service provider; is-a → rating agency; issues → credit rating; manages → credit rating scale

### disclosure action  [CAE/Release]
- **definition:** corporate action involving a request for holders or beneficial owners to disclose their name, location and holdings of any issue to the issuer
- **cite:** https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/DisclosureAction
- **relations:** is-a → voluntary corporate action

### rating agency  [FND/Release]
- **definition:** rating issuer that is also a rating scale publisher, frequently but not always an independent rating service
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingAgency
- **relations:** is-a → rating issuer; is-a → rating scale publisher; is-played-by → formal organization

### regulatory action  [CAE/Release]
- **definition:** action initiated by a regulatory agency that affects a legal entity or the securities it issues and may have a material impact on that entity's stakeholders, such as shareholders and creditors
- **cite:** https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/RegulatoryAction
- **relations:** is-a → action

## Reporting mechanisms & parties

### approved reporting mechanism  [FBC/Release]
- **definition:** data reporting services provider that is authorized to provide the service of reporting details of transactions to competent authorities or ESMA (the European Securities and Markets Authority) on behalf of investment firms
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/ApprovedReportingMechanism
- **relations:** is-a → data reporting services provider; is-classified-by → MarketCategoryClassifier-ARMS

### data reporting services provider  [FBC/Release]
- **definition:** market data provider and reporting party that reports and/or publishes data on securities transactions, including required regulatory reporting for such transactions, and as such is subject to regulatory supervision
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/DataReportingServicesProvider
- **relations:** is-a → market data provider; is-a → reporting party; is-identified-by → market identifier; operates-in-country → country; operates-in-municipality → municipality

### reporting accountant  [BP/Provisional]
- **definition:** Party role of an accountant responsible for preparing or attesting to the financial information in a regulatory report or filing. _(definition: curated)_
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/EquitiesIPOIssuance/ReportingAccountant
- **relations:** is-a → party role

### reporting party  [FND/Release]
- **definition:** party providing a report, typically in response to some contractual, legal, regulatory or other business requirement
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/ReportingParty
- **relations:** is-a → party role; provides → report

### securities trade date position reporting  [BP/Provisional]
- **definition:** Reporting of a party's securities positions as of a given trade date, used for regulatory position and transparency reporting. _(definition: curated)_
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BP/Process/FinancialContextAndProcess/SecuritiesTradeDatePositionReporting
- **relations:** is-a → securities trade

### securities trades reporting  [BP/Provisional]
- **definition:** Post-trade process of reporting executed securities trades to a trade repository or regulator. _(definition: curated)_
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BP/Process/FinancialContextAndProcess/SecuritiesTradesReporting
- **relations:** is-a → securities post trade

### trade reporting facility  [FBC/Release]
- **definition:** facility that provides a mechanism for the reporting of transactions effected otherwise than on an exchange
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/TradeReportingFacility
- **relations:** is-a → facility; is-classified-by → MarketCategoryClassifier-TRFS; is-identified-by → market identifier; is-managed-by → financial service provider; operates-in-country → country; operates-in-municipality → municipality

## Reporting requirements

### borrower disclosure requirement  [LOAN/Provisional]
- **definition:** Disclosure requirement obliging a lender to give a borrower specified information about a loan product, conferring the borrower's product disclosure right. _(definition: curated)_
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/BorrowerDisclosureRequirement
- **relations:** is-a → disclosure requirement; confers → product disclosure right; governs → borrower assessment

### consumer credit requirement  [LOAN/Provisional]
- **definition:** Requirement set out on the lender about how they must treat the appliction to a loan
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/ConsumerCreditRequirement
- **relations:** is-a → legal obligation; confers → consumer right; overseen-by → consumer protection agency

### data protection requirement  [LOAN/Provisional]
- **definition:** Requirements defining how data about individuals is held. Example is the EU DA directive and laws, which make the data the property of the individual that data is about. Covers - what information i sheld - who information can be divulged to. - the individual's rights in respect of that information Privacy regulations cover most of this. EU defines "Personal Data" and "Sensitive Personal Data". For credit reference agencies the latter would be covered. More detail about whether they can divulge facts which are not subject to formal judgements etc.
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/DataProtectionRequirement
- **relations:** is-a → legal obligation

### disclosure requirement  [LOAN/Provisional]
- **definition:** Requirement for disclosure to borrowers or potential borrowers. There are two kinds of disclosure requirement: 1. Disclosure about the information held on the borrower 2. Disclsure about the product.
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/DisclosureRequirement
- **relations:** is-a → consumer credit requirement

### loan regulatory requirement  [LOAN/Provisional]
- **definition:** A regulatory requirement defined in regulations by a comsumer credit act or other legislation.
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/LoanRegulatoryRequirement
- **relations:** is-a → legal obligation; administered-by → regulatory agency; is-mandated-by → consumer credit protection law; regulates → loan

### product disclosure requirement  [LOAN/Provisional]
- **definition:** A requirement governing what representations can be made about a product, as it affects the consumer.
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/ProductDisclosureRequirement
- **relations:** is-a → disclosure requirement; governs → good faith estimate; governs → loan product representations

## Reports & disclosures

### HMDA report  [LOAN/Provisional]
- **definition:** a report prepared to satisfy HMDA regulatory reporting requirements as described US section 1003.3(c) of the Revised Home Mortgage Disclosure Act of 2015
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-Report
- **relations:** is-a → report; has-number-of-entries → positiveInteger; is-submitted-to → regulatory agency

### credit report  [FBC/Provisional]
- **definition:** report describing the creditworthiness and related credit attributes of a borrower
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditReport
- **relations:** is-a → rating report; comprises → credit inquiry; comprises → credit message; comprises → credit rating; comprises → credit tradeline; concerns-party → party; exemplifies → credit report product; has-as-of-date → date; has-coverage-period → date period; is-classified-by → credit report category; is-identified-by → identifier; is-produced-by → credit rating agency

### credit report product  [FBC/Provisional]
- **definition:** branded credit report offered in the marketplace
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditReportProduct
- **relations:** is-a → financial product; is-a → off-the-shelf product; is-produced-by → credit rating agency

### disclosure provision  [FND/Release]
- **definition:** contractual provision that outlines the requirements and responsibilities of one or both parties to reveal certain information to each other
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/DisclosureProvision
- **relations:** is-a → contractual commitment

### income verification report  [LOAN/Provisional]
- **definition:** report providing the methodology and supporting documentation used to verify the borrower's income
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/IncomeVerificationReport
- **relations:** is-a → assessment report

### rating report  [FND/Release]
- **definition:** report describing a set of ratings
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/RatingReport
- **relations:** is-a → assessment report; reports-on → rating

### regulatory report  [CMNS/n/a]
- **definition:** document required to support operational transparency that demonstrates compliance with some specification, law, policy, restriction, or other rule specified by a regulatory agency
- **cite:** https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryReport
- **relations:** is-a → report; is-a → record; is-a → reference document

### remittance report  [BP/Provisional]
- **definition:** Report containing a specific and limited set of information about the Deal. Term origin:MBS PoC Reviews
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/RemittanceReport
- **relations:** is-a → report

### report  [FND/Release]
- **definition:** document that provides a structured description of something, prepared on ad hoc, periodic, recurring, regular, or as required basis
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Report
- **relations:** is-a → document; has-report-date → explicit date; has-report-date-time → date time; has-reporting-period → date period; is-provided-by → reporting party; is-reported-to → party role; is-submitted-by → submitter; is-submitted-to → party role

## Cross-domain bridges (curated)

### reporting party → legal entity identifier  _(cross-domain (FND->BE))_
- **relation:** reporting party —[identified-by]→ legal entity identifier _(provenance: curated)_
- **rationale:** In supervisory and transaction reporting the party that submits a report is identified by its Legal Entity Identifier. FIBO defines the ReportingParty role (FND) and the LegalEntityIdentifier (BE) but does not connect a reporting party to its LEI.
- **cite:** ISO 17442 (LEI); MiFID II / ESMA transaction reporting; CFTC swap reporting

### regulatory report → regulatory agency  _(intra-domain gap (CMNS))_
- **relation:** regulatory report —[submitted-to]→ regulatory agency _(provenance: curated)_
- **rationale:** A regulatory report is submitted to the regulatory agency that requires it. FIBO defines both RegulatoryReport and RegulatoryAgency in Commons but does not draw the edge from a report to the agency it is filed with.
- **cite:** General supervisory-reporting practice; e.g. HMDA filing to the CFPB, MiFID II reporting to national competent authorities

### regulatory report → regulation  _(cross-domain (CMNS->FND))_
- **relation:** regulatory report —[required-by]→ regulation _(provenance: curated)_
- **rationale:** A regulatory report exists because a regulation mandates it. FIBO models RegulatoryReport (CMNS) and Regulation (FND) separately but leaves the report-to-mandating-regulation link implicit.
- **cite:** Reporting obligations arise from regulations, e.g. HMDA report required by Regulation C

### securities trades reporting → trade reporting facility  _(cross-domain (BP->FBC))_
- **relation:** securities trades reporting —[submitted-to]→ trade reporting facility _(provenance: curated)_
- **rationale:** Executed off-exchange securities trades are reported to a trade reporting facility. FIBO models the securities-trades-reporting process (BP) and the TradeReportingFacility (FBC) but does not connect the reporting activity to the facility it reports to.
- **cite:** FINRA Trade Reporting Facility rules; MiFID II APA reporting
