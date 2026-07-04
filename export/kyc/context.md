# Grounding context — KYC & Beneficial Ownership (entity resolution)

Curated FIBO concepts and cross-domain bridges that ground this agent. Cite the
`resource` IRI on every claim. `provenance: fibo` = from FIBO; `provenance: curated`
= authored by this project (grounded in FIBO's structure).

## Customer & parties

### account holder  [FBC/Release]
- **definition:** party that owns an account
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder
- **relations:** is-a → owner; holds → account

### agent  [CMNS/n/a]
- **definition:** something autonomous that can adapt to and interact with its environment
- **cite:** https://www.omg.org/spec/Commons/PartiesAndSituations/Agent
- **relations:** has-name → contextual name

### client  [FND/Release]
- **definition:** party that purchases professional services from, or has a formal relationship to purchase services from another party
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Client
- **relations:** is-a → party role

### contract party  [FND/Release]
- **definition:** legally competent party that has entered into a binding agreement, accepting and conceding obligations, responsibilities, and benefits as specified
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractParty
- **relations:** is-a → party role; is-played-by → legal person

### customer  [FND/Release]
- **definition:** party that receives or consumes products (goods or services) and has the ability to choose between different products and suppliers
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Customer
- **relations:** is-a → buyer; buys-from → supplier

### customer account  [FBC/Release]
- **definition:** account that represents an identified, named collection of balances and cumulative totals used to summarize customer transaction-related activity over a designated period of time
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount
- **relations:** is-a → account; is-defined-in → service agreement; is-held-by → customer account holder; is-identified-by → account identifier

### customer account holder  [FBC/Release]
- **definition:** party that owns a customer account
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccountHolder
- **relations:** is-a → account holder; holds → customer account

### legally competent natural person  [BE/Release]
- **definition:** person who is considered competent, under the circumstances, to enter into a contract, conduct business, or participate in other activities that generally require the mental ability to understand problems and make decisions on his or her own behalf
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson
- **relations:** is-a → person; is-a → legal person

### party  [CMNS/n/a]
- **definition:** person or organization
- **cite:** https://www.omg.org/spec/Commons/PartiesAndSituations/Party
- **relations:** is-a → agent; has-address → physical address; has-mailing-address → physical address

### person  [FND/Release]
- **definition:** individual human being, with consciousness of self
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
- **relations:** is-a → party; has-age → age; has-citizenship → country; has-date-of-birth → date of birth; has-date-of-death → date of death; has-name → person name; has-place-of-birth → place of birth; has-residence → conventional street address

### person name  [FND/Release]
- **definition:** designation by which someone is known in some context
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/PersonName
- **relations:** is-a → contextual name; is-name-of → person

## Identity & identifiers

### business identifier code  [FBC/Release]
- **definition:** international identifier for financial and non-financial institutions used to facilitate automated processing of information for financial services
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCode
- **relations:** is-a → code element; is-a → structured identifier; is-a → organization identifier; comprises → business party prefix; comprises → business party suffix; comprises → organization sub-unit identifier; comprises → Alpha2Code; denotes → formal organization; is-member-of → business identifier code scheme

### client identifier  [FND/Release]
- **definition:** sequence of characters uniquely identifying a client within the context of some organization
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/ClientIdentifier
- **relations:** is-a → party role identifier; identifies → client

### customer identifier  [FND/Release]
- **definition:** sequence of characters uniquely identifying a customer within the context of some organization
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/CustomerIdentifier
- **relations:** is-a → party role identifier; identifies → customer

### driver's license identifier  [FND/Release]
- **definition:** identifier associated with a drivers' or operating license for operating a motor vehicle or non-driver identification card
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DriversLicenseIdentifier
- **relations:** is-a → identifier; identifies → driver's license; is-defined-in → driver's license identification scheme

### entity legal form identifier  [BE/Release]
- **definition:** code that denotes an entity legal form as defined in ISO 20275
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/EntityLegalFormIdentifier
- **relations:** is-a → code element; denotes → entity legal form; is-defined-in → entity legal form scheme

### identity document  [FND/Release]
- **definition:** any legal document which may be used to verify aspects of a person's identity
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/IdentityDocument
- **relations:** is-a → legal document; has-date-of-issuance → date; has-expiration-date → date; identifies → person; is-evidence-for → date of birth; is-evidence-for → place of birth; is-evidence-for → physical address; is-identified-by → identifier; is-issued-by → government

### legal entity identifier  [BE/Release]
- **definition:** an organization identifier that uniquely identifies a legal person as defined in ISO 17442
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifier
- **relations:** is-a → organization identifier; is-a → registered identifier; identifies → legal person; is-defined-in → legal entity identifier scheme

### legal entity identifier scheme  [BE/Release]
- **definition:** a scheme that specifies the elements of an unambiguous legal entity identifier (LEI) scheme to identify the legal entities relevant to any financial transaction
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifierScheme
- **relations:** is-a → organization identification scheme; defines → legal entity identifier

## Legal persons & entity types

### LEI registered entity  [BE/Release]
- **definition:** a legal person that has registered for and is identified by a legal entity identifier
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LEIRegisteredEntity
- **relations:** is-a → legal person

### chartered legal person  [BE/Release]
- **definition:** a legal person created by a royal charter or decree
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/CharteredLegalPerson
- **relations:** is-a → legal entity

### corporation  [BE/Release]
- **definition:** formal organization that is a legal entity (artificial person) distinct from its owners, created under the jurisdiction of the laws of a state or nation
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/Corporation
- **relations:** is-a → legal entity; has-legal-name → string; is-constituted-by → instrument of incorporation; is-incorporated-in → jurisdiction

### for profit corporation  [BE/Release]
- **definition:** corporation whose objective is to make money, i.e., to ensure realization of a financial benefit such that the amount of revenue gained from a business activity exceeds the expenses, costs and taxes needed to sustain that activity
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/ForProfitCorporation
- **relations:** is-a → corporation; has-objective → profit objective

### formal organization  [CMNS/n/a]
- **definition:** organization that is recognized in some legal jurisdiction, with associated rights and responsibilities
- **cite:** https://www.omg.org/spec/Commons/Organizations/FormalOrganization
- **relations:** is-a → organization; is-classified-by → North American Industry Classification System code; is-classified-by → standard industrial classification code; is-domiciled-in → geopolitical entity

### legal entity  [CMNS/n/a]
- **definition:** legal person that is a partnership, corporation, or other organization having the capacity to negotiate contracts, assume financial obligations, and pay off debts, organized under the laws of some jurisdiction
- **cite:** https://www.omg.org/spec/Commons/Organizations/LegalEntity
- **relations:** is-a → formal organization; is-a → legal person; has-entity-expiration-reason → entity expiration reason; has-entity-status → entity status; has-headquarters-address → physical address; has-legal-address → conventional street address; has-legal-form → entity legal form; is-classified-by → North American Industry Classification System code; is-classified-by → standard industrial classification code; is-classified-by → industry sector classifier; is-governed-by → organization covering agreement; is-organized-in → jurisdiction

### legal person  [CMNS/n/a]
- **definition:** party that is recognized as having rights and obligations under the law, including but not limited to the right to sue and be sued, enter into contracts, own property, and incur financial and other obligations
- **cite:** https://www.omg.org/spec/Commons/Organizations/LegalPerson
- **relations:** is-a → party; is-identified-by → legal entity identifier; is-recognized-in → jurisdiction

### non-governmental organization  [BE/Release]
- **definition:** not-for-profit organization that functions independently of government
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/NonGovernmentalOrganization
- **relations:** is-a → not for profit organization; has-objective → public purpose

### not for profit organization  [BE/Release]
- **definition:** organization that uses its surplus revenues to further achieve its purpose rather than distributing its surplus income to the organization's owners (directors, investors, and equivalents) as profit / dividends
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/NotForProfitOrganization
- **relations:** is-a → formal organization; has-objective → not for profit objective

### not-for-profit corporation  [BE/Release]
- **definition:** corporation approved by its jurisdictional oversight and tax authorities as operating for educational, charitable, social, religious, civic or humanitarian purposes
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/NotForProfitCorporation
- **relations:** is-a → corporation; is-a → not for profit organization

### organization  [CMNS/n/a]
- **definition:** framework of authority within which a person, persons, or groups of people act, or are designated to act, towards some purpose, such as to meet a need or pursue collective goals
- **cite:** https://www.omg.org/spec/Commons/Organizations/Organization
- **relations:** is-a → party; has-goal → goal; has-member → party; has-name → organization name

## Ownership & control

### beneficial owner  [BE/Release]
- **definition:** party that enjoys the benefits of ownership (such as receipt of income) of something even though its ownership (title) may be in the name of another party (called a nominee or registered owner)
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner
- **relations:** is-a → owner; delegates-control-to → controlling nominee; is-beneficial-owner-of → asset; is-played-by → legally competent natural person

### beneficial ownership  [BE/Release]
- **definition:** situation linking party that enjoys the benefits of ownership (such as receipt of income) of something even though its ownership (title) may be in the name of another party (called a nominee or registered owner) to the asset that they own
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwnership
- **relations:** is-a → ownership; has-owned-asset → asset; has-owning-party → beneficial owner

### board composition control  [BE/Release]
- **definition:** situation in which a voting shareholder, entity owner, or some other party in the case of a not-for-profit organization, appoints and/or nominates someone to the board of directors of an organization for some period of time
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardCompositionControl
- **relations:** is-a → control; involves-controlled-thing → board member

### contractual control  [BE/Release]
- **definition:** control established through the terms of some contract
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/ContractualControl
- **relations:** is-a → de jure control; is-conferred-by → contract

### control  [FND/Release]
- **definition:** situation in which some party has the power to direct or strongly influence the direction of the management and policies related to something
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/Control
- **relations:** is-a → situation; has-party-in-control → controlling party; involves-controlled-thing → controlled thing

### controlled party  [BE/Release]
- **definition:** person or organization over which some party exercises some form of authority or influence with respect to some situation
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/ControlledParty
- **relations:** is-a → controlled thing; is-played-by → party

### controlling equity  [BE/Release]
- **definition:** shareholders's equity that formally confers control in the entity, either by law or as explicitly stated in a corresponding equity instrument
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/ControllingEquity
- **relations:** is-a → shareholders' equity; confers → de jure control

### controlling party  [FND/Release]
- **definition:** actor that exercises some form of control in the context of some situation
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControllingParty
- **relations:** is-a → actor; is-controlling-party-in → control; is-party-controlling → controlled thing

### de facto control  [FND/Release]
- **definition:** control that exists informally and is accepted, although not formally recognized
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/DeFactoControl
- **relations:** is-a → control

### de facto controlling interest party  [BE/Release]
- **definition:** party that exercises some control over an entity other than via explicit, legal means
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/DeFactoControllingInterestParty
- **relations:** is-a → controlling party; is-controlling-party-in → de facto control; nominates → board member

### de jure control  [FND/Release]
- **definition:** control that exists as a matter of law, i.e., legitimate, legal control of something
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/DeJureControl
- **relations:** is-a → legal construct; is-a → control

### de jure controlling interest party  [BE/Release]
- **definition:** party that has the legal authority to exercise control
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty
- **relations:** is-a → controlling party; is-controlling-party-in → de jure control

### entity controlling party  [BE/Release]
- **definition:** party that has the authority to control some legal entity
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/EntityControllingParty
- **relations:** is-a → controlling party; is-controlling-party-of → legal entity

### entity ownership  [BE/Release]
- **definition:** ownership by some party of an interest in some non-governmental formal organization
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/EntityOwnership
- **relations:** is-a → ownership; has-owning-entity → legal person; is-classified-by → relationship status; is-qualified-by → relationship qualifier

### majority controlling party  [BE/Release]
- **definition:** controlling party that possesses, either directly or indirectly, the power to direct or cause the direction of the management and policies of a legal person, whether through the ownership of a majority of voting securities, by contract, or otherwise
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/MajorityControllingParty
- **relations:** is-a → entity controlling party

### ownership  [FND/Release]
- **definition:** situation in which some party holds the legal title to something (explicitly or implicitly) and has the right to transfer that title and/or possession
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Ownership
- **relations:** is-a → situation; has-owned-asset → asset; has-owning-party → owner

### ownership control situation  [FND/Release]
- **definition:** situation in which some party owns and controls something
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/OwnershipAndControl/OwnershipControlSituation
- **relations:** is-a → situation

## Partnerships & trusts

### general partnership  [BE/Release]
- **definition:** partnership that has at least two general partners that agree to share in all assets, profits, and financial and legal liabilities of the business
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/GeneralPartnership
- **relations:** is-a → partnership; has-general-partner → general partner

### irrevocable trust  [BE/Release]
- **definition:** trust that cannot be modified, amended or terminated except under certain legal circumstances and typically not without the permission of the grantor's named beneficiary or beneficiaries
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/IrrevocableTrust
- **relations:** is-a → trust

### limited liability partnership  [BE/Release]
- **definition:** partnership that has general partners but provides its individual partners some level of protection against personal liability for certain partnership liabilities
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/LimitedLiabilityPartnership
- **relations:** is-a → partnership; has-general-partner → general partner

### limited partnership  [BE/Release]
- **definition:** partnership that has at least one general partner and at least one limited partner
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/LimitedPartnership
- **relations:** is-a → partnership; has-general-partner → general partner; has-limited-partner → limited partner

### living trust  [BE/Release]
- **definition:** trust created during an individual's lifetime where a designated person, the trustee, is given responsibility for managing that individual's assets for the benefit of the eventual beneficiary
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/LivingTrust
- **relations:** is-a → trust

### partnership  [BE/Release]
- **definition:** association of two or more legal persons to carry on as co-owners a business for profit
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/Partnership
- **relations:** is-a → business entity; is-a → legal entity; has-objective → profit objective; is-governed-by → partnership agreement

### trust  [BE/Release]
- **definition:** fiduciary relationship and legal entity in which one party, known as a trustor, gives another party, the trustee, the right to hold title to and manage assets for the benefit of a third party, the beneficiary
- **cite:** https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trust
- **relations:** is-a → business entity; is-a → legal entity; has-party-role → trust beneficiary; has-party-role → trustee; has-party-role → trustor; is-governed-by → trust agreement

## Registration authorities

### business register identifier  [FBC/Release]
- **definition:** identifier that uniquely identifies a business register, such as a register identified by the Global Legal Entity Identifier Foundation (GLEIF) registration authorities list
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegisterIdentifier
- **relations:** is-a → identifier; identifies → business registry; is-registered-by → business registration authority

### business registration authority  [FBC/Release]
- **definition:** registration authority that is responsible for maintaining a registry of business entities
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority
- **relations:** is-a → registrar; is-a → registration authority; manages → business registry; registers → registration identifier

### legal entity identifier registry  [FBC/Release]
- **definition:** registry for registering and maintaining information about business entities for a particular jurisdiction
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LegalEntityIdentifierRegistry
- **relations:** is-a → business registry; comprises → legal entity identifier registry entry

### registration authority code  [FBC/Release]
- **definition:** identifier that uniquely identifies a business registry, and is associated with a registration authority and jurisdiction, issued by the Global Legal Entity Identifier Foundation (GLEIF)
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/RegistrationAuthorityCode
- **relations:** is-a → code element; is-a → registered identifier; identifies → business registry

## Cross-domain bridges (curated)

### legal entity → legal entity identifier  _(cross-domain (CMNS->BE))_
- **relation:** legal entity —[identified-by]→ legal entity identifier _(provenance: curated)_
- **rationale:** For KYC and entity resolution a legal entity is identified by its Legal Entity Identifier (ISO 17442). FIBO defines LegalEntityIdentifier and applies it to LEI-registered entities, but does not link the base LegalEntity class to it, leaving generic entity-to-LEI resolution implicit.
- **cite:** ISO 17442 (LEI); FATF Recommendation 24

### beneficial owner → legal entity  _(cross-domain (BE->CMNS))_
- **relation:** beneficial owner —[beneficial-owner-of]→ legal entity _(provenance: curated)_
- **rationale:** A beneficial owner is the party that ultimately owns or controls a legal entity. FIBO models BeneficialOwnership as a situation but draws no direct edge from the BeneficialOwner role to the legal entity owned, which KYC / ultimate-beneficial-owner resolution needs.
- **cite:** FATF Recommendations 24 & 25; US CDD rule 31 CFR 1010.230

### customer → legal person  _(role->entity gap (FND->CMNS))_
- **relation:** customer —[played-by]→ legal person _(provenance: curated)_
- **rationale:** A customer is a party role played by a legal person (or a natural person). Resolving 'the customer' to the underlying legal entity is core to KYC onboarding, but FIBO leaves the role-to-entity link implicit.
- **cite:** FIBO FND party-role vs entity modeling; KYC customer onboarding

### account holder → legal entity identifier  _(cross-domain (FBC->BE))_
- **relation:** account holder —[identified-by]→ legal entity identifier _(provenance: curated)_
- **rationale:** An institutional account holder is identified for KYC by its Legal Entity Identifier. FIBO models accounts and their holders but does not connect an account holder to its LEI.
- **cite:** ISO 17442 (LEI); KYC / CDD account onboarding
