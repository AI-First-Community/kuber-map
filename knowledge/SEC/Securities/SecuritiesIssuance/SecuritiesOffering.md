---
type: FIBO Class
title: "securities offering"
description: "offering of a security (or securities) for sale"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecuritiesOffering
tags: [SEC, Release]
detail: "If the offering is public, then it can only be made after regulatory registration requirements have been met. The securities may be new or a secondary offering of a previously issued security, and may include stock, multiple classes of equity shares, municipal or other government bonds, and so forth. Offerings, especially to the investment public, are typically made by an investment banker, or syndicate of investment bankers."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Offering.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Agreements/Agreement.md", provenance: fibo}
  - {type: applies-to, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
  - {type: final-state-described-in, target: "/BP/SecuritiesIssuance/IssuanceDocuments/FinalProspectus.md", provenance: fibo}
  - {type: has-governing-jurisdiction, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
  - {type: has-offering-price, target: "/FND/Accounting/CurrencyAmount/MonetaryPrice.md", provenance: fibo}
  - {type: has-party-role, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent.md", provenance: fibo}
  - {type: is-evidenced-by, target: "/SEC/Securities/SecuritiesIssuance/OfferingDocument.md", provenance: fibo}
  - {type: is-identified-by, target: "/SEC/Securities/SecuritiesIdentification/ListedSecurityIdentifier.md", provenance: fibo}
  - {type: is-underwritten-by, target: "/SEC/Securities/SecuritiesIssuance/SecurityUnderwriter.md", provenance: fibo}
---

offering of a security (or securities) for sale

### Relationships
- is-a: [Offering](/FBC/ProductsAndServices/FinancialProductsAndServices/Offering.md)
- is-a: [Agreement](/FND/Agreements/Agreements/Agreement.md)
- applies-to: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- final-state-described-in: [FinalProspectus](/BP/SecuritiesIssuance/IssuanceDocuments/FinalProspectus.md)
- has-governing-jurisdiction: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
- has-offering-price: [MonetaryPrice](/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- has-party-role: [ThirdPartyAgent](/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent.md)
- is-evidenced-by: [OfferingDocument](/SEC/Securities/SecuritiesIssuance/OfferingDocument.md)
- is-identified-by: [ListedSecurityIdentifier](/SEC/Securities/SecuritiesIdentification/ListedSecurityIdentifier.md)
- is-underwritten-by: [SecurityUnderwriter](/SEC/Securities/SecuritiesIssuance/SecurityUnderwriter.md)
