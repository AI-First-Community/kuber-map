---
type: FIBO Class
title: "prospectus"
description: "formal, written offering document to sell securities that provides the facts an investor needs to make an informed investment decision"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/Prospectus
tags: [SEC, Release]
detail: "A prospectus may specify the facts about an offering of securities, mutual funds, or limited partnerships for investments in oil, gas, equipment leasing, or other kinds of limited partnerships. In the United States, a prospectus may be a formal legal document, required by and filed with the Securities and Exchange Commission, if it provides details about an investment offering for sale to the public. This document includes facts about the fund investment objective, investment focus and other details of the fund. Some of this information becomes binding on the fund once it is issued, while other information is guidelines only."
examples:
  - "The prospectus filed with the SEC for an initial public offering."
examples_provenance: curated
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesIssuance/OfferingDocument.md", provenance: fibo}
  - {type: outlines, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundInvestmentObjective.md", provenance: fibo}
---

formal, written offering document to sell securities that provides the facts an investor needs to make an informed investment decision

### Relationships
- is-a: [OfferingDocument](/SEC/Securities/SecuritiesIssuance/OfferingDocument.md)
- outlines: [FundInvestmentObjective](/SEC/Funds/CollectiveInvestmentVehicles/FundInvestmentObjective.md)
