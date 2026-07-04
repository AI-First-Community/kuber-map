# Grounding context — Securities Instruments & Issuance (capital markets)

Curated FIBO concepts and cross-domain bridges that ground this agent. Cite the
`resource` IRI on every claim. `provenance: fibo` = from FIBO; `provenance: curated`
= authored by this project (grounded in FIBO's structure).

## Bonds & debt securities

### bond  [SEC/Release]
- **definition:** tradable debt instrument representing a loan in which the issuer owes the holder(s) a debt
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
- **relations:** is-a → credit agreement repaid at maturity; is-a → tradable debt instrument; has-interest-payment-terms → coupon payment terms; has-repayment-terms → bond principal repayment terms

### bond coupon  [SEC/Release]
- **definition:** interest rate on a debt security that the issuer promises to pay to the holder until maturity, expressed as an annual percentage of the face value
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/BondCoupon
- **relations:** is-a → interest rate

### callable bond  [SEC/Release]
- **definition:** bond that includes a stipulation allowing the issuer the right to repurchase and retire the bond at the call price after the call protection period
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CallableBond
- **relations:** is-a → bond; has-call-feature → call feature; has-extraordinary-redemption-provision → extraordinary redemption provision

### commercial paper  [SEC/Release]
- **definition:** an unsecured short-term debt instrument typically issued by a bank, corporation, or foreign government to obtain funds to meet short-term debt obligations, such as accounts receivable, inventories, or payroll, backed only by an issuing bank or company promise to pay the face amount on the maturity date specified on the note
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/CommercialPaper
- **relations:** is-a → money market instrument; has-relative-price-at-issue → AtADiscount; has-relative-price-at-maturity → ParValue

### convertible bond  [SEC/Release]
- **definition:** bond that gives the holder the right to convert the bond into a fixed number of shares (conversion ratio) if the equity price rises above a specified level (strike price)
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ConvertibleBond
- **relations:** is-a → bond; is-a → convertible security; has-contractual-element → bond conversion terms

### corporate bond  [SEC/Release]
- **definition:** bond issued by a company in order to raise financing
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CorporateBond
- **relations:** is-a → bond

### fixed coupon bond  [SEC/Release]
- **definition:** bond whose coupon rate and principal amount are fixed at the time of origination or sale and remain constant while the security is outstanding
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FixedCouponBond
- **relations:** is-a → bond; is-a → fixed income security; has-interest-payment-terms → fixed coupon terms

### floating rate note  [SEC/Release]
- **definition:** bond with a variable interest rate based on a published reference interest rate
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/FloatingRateNote
- **relations:** is-a → variable coupon bond; has-interest-rate → reference interest rate

### government bond  [SEC/Release]
- **definition:** debt security issued by a government to fund government spending
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/GovernmentBond
- **relations:** is-a → bond; is-a → government issued debt security

### municipal bond  [SEC/Release]
- **definition:** government bond that may be issued by a regional, rather than national, authority
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalBond
- **relations:** is-a → government bond; is-a → municipal security

### sovereign debt instrument  [SEC/Release]
- **definition:** debt security issued by the government of a country
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SovereignDebtInstrument
- **relations:** is-a → government issued debt security

### treasury bill  [SEC/Release]
- **definition:** short-term zero coupon treasury obligation with a maturity ranging from one to twelve months
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/TreasuryBill
- **relations:** is-a → U.S. Treasury security; is-a → money market instrument; has-interest-rate → reference interest rate; has-relative-price-at-issue → AtADiscount; has-relative-price-at-maturity → ParValue

### zero coupon bond  [SEC/Release]
- **definition:** bond issued with a coupon rate of zero and that trades at a deep discount to face value
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/ZeroCouponBond
- **relations:** is-a → bond; is-a → fixed income security; has-interest-payment-terms → zero coupon terms; has-original-issue-discount-amount → monetary amount; has-relative-price-at-maturity → ParValue

## Equity & shares

### American depositary receipt  [SEC/Release]
- **definition:** depositary receipt that represents securities of a foreign company and allows that company's securities to trade in the U.S. financial markets
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceipt
- **relations:** is-a → depositary receipt; is-classified-by → American depositary receipt level; is-legally-recorded-in → UnitedStatesJurisdiction

### common share  [SEC/Release]
- **definition:** share that signifies a unit of ownership in a corporation and represents a claim on part of the corporation's assets and earnings
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/CommonShare
- **relations:** is-a → share; has-dividend → ordinary dividend

### depositary receipt  [SEC/Release]
- **definition:** negotiable financial instrument issued by a trust company, security depositary, or bank that is evidence of the deposit of publicly traded securities and that facilitates the ownership of securities traded in other jurisdictions
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/DepositaryReceipt
- **relations:** is-a → security; has-traded-security → security

### dividend  [SEC/Release]
- **definition:** announced commitment to make a specific distribution of a portion of earnings to shareholders, prorated by class of security
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Dividend
- **relations:** is-a → commitment; has-distribution-method → dividend distribution method; has-payment-amount → monetary amount; has-schedule → dividend schedule

### fixed rate dividend  [SEC/Release]
- **definition:** dividend that provides a specified annual return on the nominal value (and any premium) paid on shares
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/FixedRateDividend
- **relations:** is-a → preferred dividend; has-fixed-dividend-rate → percentage monetary amount

### global depositary receipt  [SEC/Release]
- **definition:** depositary receipt where a certificate issued by a depositary bank, which purchases securities of foreign companies, creates a security on a local exchange backed by those securities
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/GlobalDepositaryReceipt
- **relations:** is-a → depositary receipt

### non-voting share  [SEC/Release]
- **definition:** share that has no voting right
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/NonVotingShare
- **relations:** is-a → share

### partially paid share  [SEC/Release]
- **definition:** share whose payment status indicates that only a portion of the market value has been received by the company for the shares
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PartiallyPaidShare
- **relations:** is-a → share; has-share-payment-status → PartiallyPaidShareStatus

### preferred share  [SEC/Release]
- **definition:** share that pays dividends at a specified rate and has preference over common shares in the payment of dividends and liquidation of corporate assets
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShare
- **relations:** is-a → share; has-maturity-date → explicit date; is-senior-to → common share

### share yield  [SEC/Release]
- **definition:** ratio of the annualized dividend per share divided by the (current) price per share
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ShareYield
- **relations:** is-a → yield

## Funds & collective investment

### collective investment vehicle  [SEC/Release]
- **definition:** assets pooled by investors whose share capital remains separate from the assets of the vehicle
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/CollectiveInvestmentVehicle
- **relations:** is-a → pooled fund; administered-by → fund administrator; advised-by → registered investment advisor; distributed-by → fund distributor; fund-has-related-party → funds processing party; has-additional-information → other investment fund information; has-auditor → external auditor; has-currency → currency; has-data-provider → market data provider; has-depository → fund depositary; has-fund-policy → fund investment policy; has-legal-structure → legal fund structure; has-management-company → fund manager; has-related-fund-terms → fund processing terms; has-strategy → fund unit distribution method; has-subscription-terms → fund subscription terms; has-transfer-agent → fund transfer agent; is-described-by → prospectus; is-issued-by → unit issuer; is-legally-recorded-in → jurisdiction; supervised-by → fund supervisory authority

### equity fund  [SEC/Provisional]
- **definition:** A fund which invests in at least 85% shares.
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/EquityFund
- **relations:** is-a → collective investment vehicle; comprises → equity portfolio

### exchange-traded fund  [SEC/Release]
- **definition:** investment fund whose fund units are traded on an exchange, much like stocks
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/ExchangeTradedFund
- **relations:** is-a → open-end investment

### fund unit  [SEC/Release]
- **definition:** quantified share of beneficial interest in a pooled fund, representing a proportional claim on the fund's assets, income, or entitlements
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundUnit
- **relations:** is-a → contractual interest; has-currency → currency; has-details → net asset value calculation method; has-fund-processing-terms → fund processing general terms; has-fund-processing-terms → fund redemption terms; is-part-of → pooled fund

### hedge fund  [SEC/Release]
- **definition:** investment fund that pursues a total return and is usually open to qualified investors only
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/HedgeFund
- **relations:** is-a → open-end investment

### mutual fund  [SEC/Release]
- **definition:** open-end professionally managed investment fund established for the purpose of investing in securities such as stocks, bonds, money market instruments and similar assets
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/MutualFund
- **relations:** is-a → open-end investment

## Identification, listing & holdings

### basket of securities  [SEC/Release]
- **definition:** basket composed of securities, typically of a particular asset class such as equities or bonds
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Baskets/BasketOfSecurities
- **relations:** is-a → weighted basket; is-a → dated structured collection; has-member → securities basket constituent

### international securities identification number  [SEC/Release]
- **definition:** security identifier that is defined as specified in ISO 6166, Securities and related financial instruments -- International securities identification numbering system (ISIN)
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/InternationalSecuritiesIdentificationNumber
- **relations:** is-a → security identifier; is-a → structured identifier; comprises → National Securities Identifying Number; comprises → Alpha2Code

### listing  [SEC/Release]
- **definition:** catalog entry for a securities offering managed by an exchange that provides the terms under which that security is made available on that exchange
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/Listing
- **relations:** is-a → security registry entry; has-currency → currency; has-last-trading-date-and-time → date time; has-registration-status → registration status; has-restriction → securities restriction; has-tick-size → monetary amount; lists → securities offering

### portfolio  [SEC/Release]
- **definition:** collection of investments (financial assets) such as stocks, bonds and cash equivalents, as well as mutual funds, real estate, and so forth
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecurityAssets/Portfolio
- **relations:** is-a → financial asset; is-a → collection; comprises → asset

### redemption event  [SEC/Release]
- **definition:** a prescriptive event involving the return of an investor's principal in a fixed-income security, such as a preferred stock or bond, or the sale of units in a mutual fund
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/RedemptionEvent
- **relations:** is-a → prescriptive event

### redemption schedule  [SEC/Release]
- **definition:** repayment schedule whereby a given percentage of a bond issue is redeemed on predefined dates
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/RedemptionSchedule
- **relations:** is-a → payment schedule; comprises → redemption event

### security registry  [SEC/Release]
- **definition:** registry used to manage security identifiers and related information
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityRegistry
- **relations:** is-a → registry; comprises → security registry entry; is-characterized-by → security identification scheme; is-managed-by → registration authority

### weighted average maturity  [SEC/Release]
- **definition:** weighted average amount of time until the maturities on mortgages in a mortgage-backed security (MBS)
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageMaturity
- **relations:** is-a → arithmetic mean; is-a → debt pool statistical measure

### yield  [FBC/Release]
- **definition:** return on the investor's capital investment
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/Yield
- **relations:** is-a → percentage; has-applicable-period → date period; has-currency → currency; refers-to → security

## Issuance, parties & offering

### issuer  [FBC/Release]
- **definition:** role of a party that issues (or proposes to issue in a formal filing) one or more financial instruments
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Issuer
- **relations:** is-a → contract principal

### m b s issuer  [SEC/Provisional]
- **definition:** The issuer of a Mortgage Backed Security.
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MBSIssuer
- **relations:** is-a → issuer

### prospectus  [SEC/Release]
- **definition:** formal, written offering document to sell securities that provides the facts an investor needs to make an informed investment decision
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/Prospectus
- **relations:** is-a → offering document; outlines → fund investment objective

### security underwriter  [SEC/Release]
- **definition:** party that has purchased from an issuer with a view to, or sells for an issuer in connection with, the distribution of any security, or participates or has a direct or indirect participation in any such undertaking, or participates or has a participation in the direct or indirect underwriting of any such undertaking
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecurityUnderwriter
- **relations:** is-a → underwriter; is-a → third-party agent; is-a → contract third party

### security underwriting arrangement  [SEC/Release]
- **definition:** underwriting agreement between an organization (typically an investment bank) and a securities issuer that commits the underwriter to assuming risk involved in buying a new issue of securities and reselling it to the public
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecurityUnderwritingArrangement
- **relations:** is-a → underwriting arrangement; has-party-role → security underwriter

### share issuer  [SEC/Release]
- **definition:** issuer of securities that represent an ownership interest in something
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ShareIssuer
- **relations:** is-a → issuer; issues → share

### underwriter  [FBC/Release]
- **definition:** financial service provider that evaluates and assumes another party's risk for a fee, such as a commission, premium, spread or interest
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter
- **relations:** is-a → financial service provider

## Securities (roots & forms)

### debt instrument  [FBC/Release]
- **definition:** financial instrument and credit agreement evidencing monies owed by the issuer to the holder on terms as specified
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument
- **relations:** is-a → credit agreement; is-a → financial instrument; has-borrower → borrower; has-call-feature → call feature; has-interest-payment-terms → interest payment terms; has-lender → lender; has-offering → debt offering; has-put-feature → put feature; has-redemption-terms → redemption provision; has-repayment-terms → principal repayment terms

### equity instrument  [FBC/Release]
- **definition:** financial instrument representing an ownership interest in an entity or pool of assets
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/EquityInstrument
- **relations:** is-a → security

### listed security  [SEC/Release]
- **definition:** registered security listed on at least one exchange
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/ListedSecurity
- **relations:** is-a → registered security; has-home-exchange → exchange; has-original-place-of-listing → exchange; is-listed-via → listing

### security  [FBC/Release]
- **definition:** financial instrument that can be bought or sold
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
- **relations:** is-a → financial instrument; is-issued-in-form → security form; is-legally-recorded-in → jurisdiction; is-registered → registration authority

### security form  [SEC/Release]
- **definition:** nature of the proof of ownership of a security
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecurityForm
- **relations:** is-a → contract document; applies-to → security; exemplifies → financial asset

### share  [SEC/Release]
- **definition:** financial instrument that signifies a unit of equity ownership in a corporation, or a unit of ownership in a mutual fund, or interest in a general or limited partnership, or a unit of ownership in a structured product, such as a real estate investment trust
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
- **relations:** is-a → equity instrument; confers-ownership-of → shareholders' equity; has-share-payment-status → share payment status; has-shares-authorized → nonNegativeInteger; number-of-votes-per-share → decimal

### tradable debt instrument  [SEC/Release]
- **definition:** a debt instrument that is also a security, i.e., that can be bought and sold by the holder
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/TradableDebtInstrument
- **relations:** is-a → debt instrument; is-a → security; has-guarantor → guarantor; has-yield → debt instrument yield

## Securitized & structured

### asset-backed security  [SEC/Release]
- **definition:** debt instrument backed by receivables other than those arising out of real estate loans or mortgages
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity
- **relations:** is-a → pool-backed security; has-tranche-type → tranche type

### c d o pool  [SEC/Provisional]
- **definition:** A pool of CDO securities. The underlying of the CDO Squared is a pool of CDO instruments.
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOPool
- **relations:** is-a → debt pool

### collateralized debt obligation  [SEC/Provisional]
- **definition:** structured finance constructed from a portfolio of fixed income assets including corporate loans and mortgage backed securities. A special purpose vehicle (SPV) issues notes to investors in order to raise funds that are invested in a portfolio of those fixed income assets, held by the SPV as collateral for the notes. Further notes: Collateralized Debt Obligation, for example, ABS CDO which consists of a portfolio of different ABS bonds, and the payments to the holders of these trust certificates are derived from the cash flows of the ABS bonds. This CDO instrument is part of a CDO issue, consisting of individual CDO instruments of a given seniority. Often referred to as tranches and slices (Investopedia). Investopedia: Similar in structure to a collateralized mortgage obligation (CMO) or collateralized bond obligation (CBO), CDOs are unique in that they represent different types of debt and credit risk. In the case of CDOs, these different types of debt are often referred to as 'tranches' or 'slices'. Each slice has a different maturity and risk associated with it. The higher the risk, the more the CDO pays. Further details: Collateralized Debt obligations are securitized interests in pools of - generally non-mortgage - assets. Assets - called collateral - usually comprise loans or debt instruments. A CDO may be called a collateralized loan obligation (CLO) or collateralized bond obligation (CBO) if it holds only loans or bonds, respectively. Investors bear the credit risk of the collateral. Multiple tranches of securities are issued by the CDO, offering investors various maturity and credit risk characteristics.
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation
- **relations:** is-a → structured finance instrument

### m b s pool  [SEC/Provisional]
- **definition:** A pool investment consisting of a collection of MBS instruments.
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MBSPool
- **relations:** is-a → debt pool

### mortgage-backed security  [SEC/Provisional]
- **definition:** debt obligations that represent claims to the cash flows from pools of mortgage loans, most commonly on residential property
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity
- **relations:** is-a → pool-backed security; has-wac → weighted average coupon; is-characterized-by → weighted average remaining term; is-issued-by → m b s issuer

### pool  [SEC/Release]
- **definition:** combination of resources for a common purpose or benefit
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/Pool
- **relations:** is-a → collection; has-member → pool constituent

### tranche  [SEC/Release]
- **definition:** segment of a pool of securities, typically debt instruments
- **cite:** https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/Tranche
- **relations:** is-a → structured finance instrument; has-attachment-point → attachment point; has-detachment-point → detachment point; is-estimated-value-of → collateral value as of date

## Cross-domain bridges (curated)

### mortgage-backed security → mortgage  _(cross-domain (SEC->LOAN))_
- **relation:** mortgage-backed security —[backed-by]→ mortgage _(provenance: curated)_
- **rationale:** A mortgage-backed security represents claims on the cash flows from an underlying pool of mortgage loans. FIBO models the security (SEC) and the mortgage instrument (LOAN) in separate domains but does not draw the edge from the MBS to the mortgage loans that back it, which securitization and loan-level disclosure analysis need.
- **cite:** SEC Regulation AB, 17 CFR 229.1100 (asset-backed securities, loan-level data)

### asset-backed security → loan  _(cross-domain (SEC->LOAN))_
- **relation:** asset-backed security —[backed-by]→ loan _(provenance: curated)_
- **rationale:** An asset-backed security is collateralized by a pool of receivables such as auto or consumer loans. FIBO defines the ABS in SEC and the loan in LOAN but leaves the backing relationship between the security and its underlying loans implicit.
- **cite:** SEC Regulation AB, 17 CFR 229.1100; securitization structuring

### issuer → legal entity identifier  _(cross-domain (FBC->BE))_
- **relation:** issuer —[identified-by]→ legal entity identifier _(provenance: curated)_
- **rationale:** For securities issuance and regulatory reporting a securities issuer is identified by its Legal Entity Identifier. FIBO defines the Issuer role (FBC) and the LegalEntityIdentifier (BE) but does not connect an issuer to its LEI.
- **cite:** ISO 17442 (LEI); MiFID II / ESMA and SEC issuer identification
