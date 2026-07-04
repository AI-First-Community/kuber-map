---
type: FIBO Class
title: "security underwriting arrangement"
description: "underwriting agreement between an organization (typically an investment bank) and a securities issuer that commits the underwriter to assuming risk involved in buying a new issue of securities and reselling it to the public"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecurityUnderwritingArrangement
tags: [SEC, Release]
core: true
detail: "Sales may be made either directly or through third-party dealers."
examples:
  - "A firm-commitment underwriting agreement for an initial public offering."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/FinancialServicesEntities/UnderwritingArrangement.md", provenance: fibo}
  - {type: has-party-role, target: "/SEC/Securities/SecuritiesIssuance/SecurityUnderwriter.md", provenance: fibo}
---

underwriting agreement between an organization (typically an investment bank) and a securities issuer that commits the underwriter to assuming risk involved in buying a new issue of securities and reselling it to the public

### Relationships
- is-a: [UnderwritingArrangement](/FBC/FunctionalEntities/FinancialServicesEntities/UnderwritingArrangement.md)
- has-party-role: [SecurityUnderwriter](/SEC/Securities/SecuritiesIssuance/SecurityUnderwriter.md)
