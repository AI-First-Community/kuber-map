# Grounding context — Loan Origination & Underwriting (residential mortgage)

Curated FIBO concepts and cross-domain bridges that ground this agent. Cite the
`resource` IRI on every claim. `provenance: fibo` = from FIBO; `provenance: curated`
= authored by this project (grounded in FIBO's structure).

## Amounts, ratios & terms

### amortization type  [LOAN/Provisional]
- **definition:** classifier of amortization algorithms
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/AmortizationType
- **relations:** is-a → Classifier

### borrower monthly income  [LOAN/Provisional]
- **definition:** total monthly qualifying income of a potential borrower
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/BorrowerMonthlyIncome
- **relations:** is-a → income; is-a → monetary amount; has-party-role → borrower

### combined loan-to-value ratio  [LOAN/Release]
- **definition:** ratio of the total amount of debt that is secured by the asset(s) and the appraised value of the asset(s) securing the financing
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/CombinedLoanToValueRatio
- **relations:** is-a → percentage monetary amount; applies-to → asset; has-argument → appraised value; has-argument → total outstanding principal; refers-to → appraisal

### good faith estimate  [LOAN/Provisional]
- **definition:** GFE - representation by the lender on the costs and implications of settlement (early termination) of the loan.
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/GoodFaithEstimate
- **relations:** is-a → loan product representations

### income  [FND/Release]
- **definition:** revenue received during a period of time
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/AccountingEquity/Income
- **relations:** is-a → monetary amount; has-date-period → DatePeriod

### loan payment schedule  [LOAN/Release]
- **definition:** regular or explicit (ad hoc) payment schedule associated with a given loan-specific account
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/LoanPaymentSchedule
- **relations:** is-a → payment schedule; applies-to → loan-specific customer account; has-anticipated-number-of-payments → positiveInteger

### loan-to-value ratio  [LOAN/Release]
- **definition:** ratio, expressed as a percentage, between the principal amount of the loan and the appraised value of the asset securing the financing
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/LoanToValueRatio
- **relations:** is-a → percentage monetary amount; applies-to → asset; has-argument → principal; has-argument → appraised value; refers-to → appraisal

### monetary amount  [FND/Release]
- **definition:** measure that is an amount of money specified in monetary units
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
- **relations:** is-a → ScalarQuantityValue; has-currency → currency

### pre-payment terms  [LOAN/Release]
- **definition:** principal repayment terms related to payment of the loan prior to maturity
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/PrepaymentTerms
- **relations:** is-a → principal repayment terms; has-pre-payment-penalty-term → ExplicitDuration

### total debt expense ratio  [LOAN/Provisional]
- **definition:** ratio of all monthly debt payments of all borrowers, including proposed expenses, with respect to the income of the borrowers as relied upon to make a credit decision
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/TotalDebtExpenseRatio
- **relations:** is-a → percentage monetary amount

### total outstanding principal  [LOAN/Release]
- **definition:** the principal balance of all loans secured by the property
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/TotalOutstandingPrincipal
- **relations:** is-a → principal

## Application & process

### loan application  [LOAN/Provisional]
- **definition:** request by a potential borrower to a potential lender to borrow money containing information used to decide whether to grant the loan
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/LoanApplication
- **relations:** is-a → Document; comprises → all borrowers' monthly income; comprises → borrower monthly income; comprises → total debt expense ratio; comprises → combined loan-to-value ratio; comprises → loan-to-value ratio; has-application-date → ExplicitDate; has-date-received → ExplicitDate; is-pre-approval-requested → boolean; is-submitted-by → requester

### loan application phase  [LOAN/Provisional]
- **definition:** distinct phase in the lifecycle of a loan application, such as pre-qualification, application intake, underwriting, or decisioning _(definition: curated)_
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/LoanApplicationPhase
- **relations:** is-a → lifecycle stage

### loan application status  [LOAN/Provisional]
- **definition:** classifier indicating the state of a loan application at a particular point in its lifecycle, such as submitted, under review, approved, declined, or withdrawn _(definition: curated)_
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/LoanApplicationStatus
- **relations:** is-a → lifecycle status

### loan phase  [LOAN/Provisional]
- **definition:** distinct phase in the lifecycle of a loan, such as origination, disbursement, repayment, or closure _(definition: curated)_
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/LoanPhase
- **relations:** is-a → lifecycle stage

### pre-approval contract  [LOAN/Provisional]
- **definition:** written commitment to lend when specified conditions are met, such as finding suitable property, and unchanged creditworthiness
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PreApprovalContract
- **relations:** is-a → written contract; has-approved-amount → monetary amount; has-interest-rate → interest rate

### pre-approval request  [LOAN/Provisional]
- **definition:** request from a potential borrower that a lender commit to pre-approving the borrower for a loan of up to a specified amount of money
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PreApprovalRequest
- **relations:** is-a → request activity; has-borrower → borrower; has-requested-amount → monetary amount

### repayment phase  [LOAN/Provisional]
- **definition:** phase in a loan's lifecycle during which the borrower repays outstanding principal and interest according to the loan's payment schedule _(definition: curated)_
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/RepaymentPhase
- **relations:** is-a → loan phase

## Collateral & property

### appraisal  [FND/Release]
- **definition:** written estimate of the market value of something as of some point in time, typically provided by a qualified appraiser
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Appraisal
- **relations:** is-a → assessment report; estimates-value-at → appraised value; evaluates → asset; is-generated-by → appraiser

### appraised value  [FND/Release]
- **definition:** estimated value of some asset as of a given point in time
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AppraisedValue
- **relations:** is-a → market value

### collateral  [FBC/Release]
- **definition:** something pledged as security to ensure fulfillment of an obligation to another party, to lend money, extend credit, or provision securities
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Collateral
- **relations:** is-a → Undergoer; is-collateralization-of → asset

### lender lien position  [LOAN/Release]
- **definition:** classifier indicating whether the lender has the primary lien position with respect to an asset used as collateral for the loan
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/LenderLienPosition
- **relations:** is-a → Classifier

### ownership interest  [LOAN/Release]
- **definition:** classifier indicating the nature of the applicant's or borrower's ownership or leasehold interest in an asset used as collateral for the loan
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/OwnershipInterest
- **relations:** is-a → Classifier; classifies → ownership

### property usage  [LOAN/Provisional]
- **definition:** a category indicating the manner in which the borrower intends to utilize the property
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/PropertyUsage
- **relations:** is-a → Classifier

### real property  [FND/Release]
- **definition:** physical asset defined as land together with any structures that are permanently attached to that land, such as houses, trees, fences and improvements
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealProperty
- **relations:** is-a → physical asset; is-a → real estate; has-number-of-affordable-dwelling-units → positiveInteger; has-number-of-dwelling-units → positiveInteger; is-classified-by → dwelling capacity; is-classified-by → manufactured home legal classification; is-evaluated-by → real property appraisal

## Contract & obligations

### credit agreement  [FBC/Release]
- **definition:** contractual agreement in which a debtor receives something of value and typically agrees to repay the creditor by some date in the future, in some form (e.g., cash, securities, etc.), generally with interest
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreement
- **relations:** is-a → written contract; has-contract-party → creditor; has-contract-party → debtor; has-contractual-element → debt terms; has-contractual-element → use of proceeds provision; has-corresponding-account → loan or credit account; has-currency → currency; has-initial-exchange-date → ExplicitDate; has-maturity-date → ExplicitDate; is-collateralized-by → collateral

### disclosure provision  [FND/Release]
- **definition:** contractual provision that outlines the requirements and responsibilities of one or both parties to reveal certain information to each other
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/DisclosureProvision
- **relations:** is-a → contractual commitment

### legal obligation  [FND/Release]
- **definition:** an obligation or duty that is enforceable by a court
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalObligation
- **relations:** is-a → duty; is-applicable-in → Jurisdiction

### loan or credit account  [FBC/Release]
- **definition:** account associated with a service in which the account holder receives funds from the account provider under certain terms and conditions for repayment
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount
- **relations:** is-a → account

### payment  [FND/Release]
- **definition:** delivery of money in fulfillment of an obligation, such as to satisfy a claim or debt
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/Payment
- **relations:** is-a → occurrence; has-payment-amount → monetary amount

### principal  [FBC/Release]
- **definition:** with respect to a debt: the value of an obligation, such as a bond or loan, raised and that must be repaid at maturity; for investments: the original amount of money invested, separate from any associated interest, dividends or capital gains
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Principal
- **relations:** is-a → Aspect; is-principal-of → debt

### use of proceeds provision  [FND/Release]
- **definition:** contract provision specifying how funds obtained through financing, such as through a credit agreement, offering, warrant, or other instrument are intended to be used
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/UseOfProceedsProvision
- **relations:** is-a → contractual commitment

## Instrument

### closed-end mortgage loan  [LOAN/Release]
- **definition:** loan secured by real estate with no ability for the borrower to receive additional funds under the loan at a later date
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/ClosedEndMortgageLoan
- **relations:** is-a → closed-end credit; is-a → loan secured by real estate

### collateralized loan  [LOAN/Release]
- **definition:** secured loan that is secured with cash or other acceptable collateral (real property, securities or other assets) provided by the borrower as specified in the collateral agreement
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/CollateralizedLoan
- **relations:** is-a → secured loan; is-collateralized-by → collateral; is-primary-contract-for → collateral agreement

### home equity line of credit  [LOAN/Release]
- **definition:** line of credit granted to a homeowner secured by the equity value in a borrower's home or other property
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/HomeEquityLineOfCredit
- **relations:** is-a → revolving line of credit; is-a → secured consumer loan; is-a → loan secured by real estate

### loan  [LOAN/Release]
- **definition:** debt instrument whereby one party extends money or credit to another party (or parties) with the understanding that the borrowed money will be repaid according to the terms of the contract
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Loan
- **relations:** is-a → credit agreement repaid periodically; is-a → debt instrument; has-corresponding-account → loan-specific customer account; has-guarantor → guarantor; has-maturity-date → ExplicitDate; has-principal-amount → monetary amount; has-third-party → contract third party; has-total-closing-costs → monetary amount; has-total-points-and-fees → monetary amount; is-classified-by → lender lien position; is-classified-by → loan market category; is-performed-by → servicer

### loan offering  [LOAN/Provisional]
- **definition:** offering related to a loan product that may be a tailored to particular circumstances, aimed at a group of borrowers or individual borrower
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LoanProductOffering
- **relations:** is-a → offering; applies-to → loan product; has-member → line item

### loan product  [LOAN/Provisional]
- **definition:** financial product that is realized as a loan that a party may acquire from a lending institution with specific characteristics and terms
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LoanProduct
- **relations:** is-a → credit facility; is-a → financial product; has-preconditions → condition precedent; is-exemplified-by → loan; refers-to → collateral

### loan secured by real estate  [LOAN/Release]
- **definition:** loan that, at origination, is secured wholly or substantially by a lien or liens on real property for which the lien or liens are central to the extension of the credit - that is, the borrower would not have been extended credit in the same amount or on terms as favorable without the lien or liens on real property
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate
- **relations:** is-a → collateralized loan; has-contractual-element → disclosure provision; has-contractual-element → use of proceeds provision; has-guarantor → mortgage indemnity guarantor; has-initial-funding-date → transaction date; is-collateralized-by → real property; is-performed-by → servicer; refers-to → security agreement

### mortgage  [LOAN/Release]
- **definition:** grant of financial interest in real property to a party that is not an owner of that real property and is recorded by a registration authority
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/Mortgage
- **relations:** is-a → security agreement; is-collateralized-by → real property

### mortgage product  [LOAN/Provisional]
- **definition:** loan product, offered by a lender, that is realized as a mortgage — a loan secured by real property — with specific eligibility criteria, characteristics, and terms _(definition: curated)_
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/MortgageProduct
- **relations:** is-a → loan product; is-exemplified-by → loan secured by real estate

### open-end mortgage loan  [LOAN/Release]
- **definition:** loan secured by real estate with a provision that the outstanding loan amount may be increased upon mutual agreement of the lender and the borrower
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/OpenEndMortgageLoan
- **relations:** is-a → open-end credit; is-a → loan secured by real estate

### reverse mortgage loan  [LOAN/Release]
- **definition:** loan secured by real estate that pays money to the borrower against a set principal limit based on the value of existing equity in the underlying collateral
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/ReverseMortgageLoan
- **relations:** is-a → loan secured by real estate; has-credit-limit → monetary amount

### secured loan  [LOAN/Release]
- **definition:** loan in which the borrower pledges some asset via a security agreement as collateral for the loan, or that is secured via third-party guarantee
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/SecuredLoan
- **relations:** is-a → loan

## Parties & roles

### borrower  [FBC/Release]
- **definition:** party to a credit agreement that is obligated to repay the amount borrowed (principal) with interest and other fees according to the terms of the instrument
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Borrower
- **relations:** is-a → debtor; is-a → contract party; is-a → customer; owes → debt

### co-maker  [LOAN/Release]
- **definition:** party that signs a borrower's promissory note, providing additional security and potentially improving the quality of the debt
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Comaker
- **relations:** is-a → contract third party

### creditor  [FBC/Release]
- **definition:** a party to whom an obligation, such as an amount of money, or good, or performance of some service exists
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Creditor
- **relations:** is-a → obligee; is-owed → debt; is-played-by → LegalPerson

### financial institution  [FBC/Release]
- **definition:** financial service provider identified as either a government agency or privately owned entity that collects funds from the public and from other institutions, and invests those funds in financial assets, such as loans, securities, bank deposits, and income-generating property
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
- **relations:** is-a → financial service provider; is-regulated-by → RegulatoryAgency; provides → financial service

### guarantor  [FBC/Release]
- **definition:** party that guarantees, endorses, or provides indemnity for some obligation on behalf of some other party
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guarantor
- **relations:** is-a → de jure controlling interest party; is-a → contract third party; is-played-by → LegalPerson

### lender  [FBC/Release]
- **definition:** a party that extends credit or money to a borrower with the expectation of being repaid, usually with interest
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Lender
- **relations:** is-a → creditor; is-a → contract party

### mortgage indemnity guarantor  [LOAN/Provisional]
- **definition:** guarantor and insurer that provides mortgage insurance in the form of a mortgage indemnity guarantee (MIG)
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityGuarantor
- **relations:** is-a → guarantor; is-a → insurer

### servicer  [LOAN/Release]
- **definition:** party that collects principal and interest payments on behalf of the lender
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Servicer
- **relations:** is-a → financial service provider; is-a → contract third party

## Purpose

### loan purpose  [LOAN/Provisional]
- **definition:** A selection of different types of loan purpose, being the purpose for which and manner in which loan (credit) draw-down amounts are to be used. This shows the purpose for which credit is to be used, and implies certain kinds of fact that relate to that specific type of loan e.g. mortgages. These are also identified as tranche types in tranches of a credit facility.
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LoanPurpose
- **relations:** is-a → objective

### mortgage loan purpose  [LOAN/Provisional]
- **definition:** the purpose for which mortgage loan proceeds will be used, such as real property purchase, dwelling construction, or loan refinancing
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/MortgageLoanPurpose
- **relations:** is-a → loan purpose; is-a → Classifier

## Regulatory & disclosure (US)

### HMDA covered loan contract  [LOAN/Provisional]
- **definition:** a closed-end mortgage loan or open-end line of credit that is not an excluded transaction for HMDA reporting under US section 1003.3(c) of the Revised Home Mortgage Disclosure Act of 2015
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-CoveredLoanContract
- **relations:** is-a → loan secured by real estate; is-classified-by → how submitted

### HMDA report  [LOAN/Provisional]
- **definition:** a report prepared to satisfy HMDA regulatory reporting requirements as described US section 1003.3(c) of the Revised Home Mortgage Disclosure Act of 2015
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-Report
- **relations:** is-a → report; has-number-of-entries → positiveInteger; is-submitted-to → RegulatoryAgency

### Nationwide Mortgage Licensing System and Registry Identifier  [LOAN/Provisional]
- **definition:** the number permanently assigned by the Nationwide Mortgage Licensing System and Registry (NMLS) for each company, branch, and individual that maintains a single account on NMLS.
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/NMLSR-ID
- **relations:** is-a → license identifier

### borrower disclosure requirement  [LOAN/Provisional]
- **definition:** regulatory requirement that a lender disclose specified information to a borrower or prospective borrower — such as the terms and costs of a loan product — conferring a corresponding right to that information and governing how the borrower is assessed _(definition: curated)_
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/BorrowerDisclosureRequirement
- **relations:** is-a → disclosure requirement; confers → product disclosure right; governs → borrower assessment

### consumer credit protection law  [LOAN/Provisional]
- **definition:** consumer protection law that regulates the extension of credit to consumers — governing matters such as disclosure of terms and costs, fair lending, and borrower rights (for example, in the US, the Consumer Credit Protection Act and its implementing regulations) _(definition: curated)_
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/ConsumerCreditProtectionLaw
- **relations:** is-a → consumer protection law

### loan regulatory requirement  [LOAN/Provisional]
- **definition:** A regulatory requirement defined in regulations by a comsumer credit act or other legislation.
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/LoanRegulatoryRequirement
- **relations:** is-a → legal obligation; administered-by → RegulatoryAgency; is-mandated-by → consumer credit protection law; regulates → loan

### reg b  [LOAN/Provisional]
- **definition:** US regulation concerning "Equal credit opportunity act" Electronic delivery of disclosures
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/RegB
- **relations:** is-a → consumer credit equal treatment requirement; is-a → disclosure requirement

### reg z  [LOAN/Provisional]
- **definition:** US Fed regulation "Truth in Lending Act" uniform standards for electronic delivery of disclosures
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/RegZ
- **relations:** is-a → product disclosure requirement

### universal loan identifier  [LOAN/Provisional]
- **definition:** unique identifier given to unequivocally identify a specific loan secured by real estate
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/UniversalLoanIdentifier
- **relations:** is-a → financial instrument identifier; comprises → legal entity identifier; identifies → loan secured by real estate

## Underwriting & assessment

### automated underwriting system  [LOAN/Provisional]
- **definition:** software system that collects the information necessary to approve a loan application and supports a mortgage lender's analysis of a new loan application
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/AutomatedUnderwritingSystem
- **relations:** is-a → automated system

### borrower assessment  [LOAN/Provisional]
- **definition:** assessment report detailing information about the borrower and their credit history that may be relevant to the loan application
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/BorrowerAssessment
- **relations:** is-a → assessment report; comprises → income verification report; comprises → individual person credit rating; comprises → payment history; has-date-of-assessment → ExplicitDate; is-about → borrower; is-about → loan application

### collateral valuation  [LOAN/Provisional]
- **definition:** assessment activity resulting in the valuation of real property as collateral
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/CollateralValuation
- **relations:** is-a → assessment activity; evaluates → collateral; is-provided-by → appraiser

### credit risk assessment  [LOAN/Provisional]
- **definition:** risk assessment that focuses on determining the likelihood of a potential borrower repaying a loan
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/CreditRiskAssessment
- **relations:** is-a → assessment activity; applies-to → loan; has-input → credit report; has-input → pre-approval contract; has-input → pre-approval request; has-input → public record; has-output → underwriting decision; uses-factor → all borrowers' monthly income; uses-factor → borrower monthly income; uses-factor → total debt expense ratio; uses-factor → combined loan-to-value ratio

### income verification report  [LOAN/Provisional]
- **definition:** report providing the methodology and supporting documentation used to verify the borrower's income
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/IncomeVerificationReport
- **relations:** is-a → assessment report

### individual person credit rating  [LOAN/Provisional]
- **definition:** credit rating that provides an opinion of the creditworthiness of a person
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/IndividualPersonCreditRating
- **relations:** is-a → credit rating

### payment history  [LOAN/Release]
- **definition:** record of actual payments of principal, interest, and other related amounts made by a borrower to a lender or servicer in order to fulfill their re-payment obligation
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/PaymentHistory
- **relations:** is-a → transaction record; applies-to-account → loan-specific customer account; has-individual-payment → individual payment transaction

### underwriting decision  [LOAN/Provisional]
- **definition:** classifier providing a loan approval recommendation determined either manually or by an automated underwriting system
- **cite:** https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/UnderwritingDecision
- **relations:** is-a → Classifier

## Cross-domain bridges (curated)

### HMDA covered loan contract → HMDA report  _(intra-domain gap)_
- **relation:** HMDA covered loan contract —[reported-in]→ HMDA report _(provenance: curated)_
- **rationale:** HMDA requires every covered loan/application to be recorded on the institution's Loan/Application Register that constitutes the HMDA report. FIBO models both HMDA-CoveredLoanContract and HMDA-Report but does not connect the reported loan to the report that reports it.
- **cite:** 12 CFR 1003.4 (Regulation C — compilation of reportable data)

### HMDA report → financial institution  _(cross-domain (LOAN->FBC))_
- **relation:** HMDA report —[filed-by]→ financial institution _(provenance: curated)_
- **rationale:** A HMDA report is filed by a covered financial institution. FIBO links HMDA-Report to the RegulatoryAgency it is submitted-to, but not to the filing institution — leaving the filer unresolved.
- **cite:** 12 CFR 1003.2 (covered institution); 12 CFR 1003.5 (reporting)

### financial institution → legal entity identifier  _(cross-domain (FBC->BE))_
- **relation:** financial institution —[identified-by]→ legal entity identifier _(provenance: curated)_
- **rationale:** For KYC / entity resolution a financial institution is identified by its Legal Entity Identifier. FIBO defines LegalEntityIdentifier in BE but does not connect FinancialInstitution to it.
- **cite:** ISO 17442 (LEI); FIBO BE LegalEntityIdentifier

### lender → financial institution  _(role->entity gap (FBC))_
- **relation:** lender —[played-by]→ financial institution _(provenance: curated)_
- **rationale:** Lender is modeled as a party role (is-a ContractParty/Creditor); FinancialInstitution is the legal-entity type that plays it. FIBO leaves the role-to-entity link implicit, blocking resolution of 'the lender' to a regulated institution.
- **cite:** FIBO FBC party-role vs entity modeling
