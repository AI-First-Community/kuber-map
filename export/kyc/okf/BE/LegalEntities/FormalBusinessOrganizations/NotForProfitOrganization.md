---
type: FIBO Class
title: "not for profit organization"
description: "organization that uses its surplus revenues to further achieve its purpose rather than distributing its surplus income to the organization's owners (directors, investors, and equivalents) as profit / dividends"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/NotForProfitOrganization
tags: [BE, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
detail: "In the US, a nonprofit organization is an association that explicitly is not required to pay taxes on its income. Such organizations are qualified for this exemption due to their socially desirable objective (e.g. hospitals, charitable organizations, etc., or because they meet some set of requirements as determined by the US Internal Revenue Service. The nonprofit landscape is highly varied, although many people have come to associate NPOs with charitable organizations. Although charities do comprise an often high profile or visible aspect of the sector, there are many other types of nonprofits. Overall, they tend to be either member-serving or community-serving. Member-serving organizations include mutual societies, cooperatives, trade unions, credit unions, industry associations, sports clubs, retired serviceman's clubs and other organizations that benefit a particular group of people - the members of the organization. Typically, community-serving organizations are focused on providing services to the community in general, either globally or locally: organizations delivering human services programs or projects, aid and development programs, medical research, education and health services, and so on."
examples:
  - "A community foundation that reinvests any surplus in its mission."
examples_provenance: curated
synonyms:
  - "non-profit organization"
relations:
  - {type: is-a, target: "/CMNS/Organizations/FormalOrganization.md", provenance: fibo}
  - {type: has-objective, target: "/BE/LegalEntities/LegalPersons/NotForProfitObjective.md", provenance: fibo}
---

organization that uses its surplus revenues to further achieve its purpose rather than distributing its surplus income to the organization's owners (directors, investors, and equivalents) as profit / dividends

### Relationships
- is-a: [FormalOrganization](/CMNS/Organizations/FormalOrganization.md)
- has-objective: [NotForProfitObjective](/BE/LegalEntities/LegalPersons/NotForProfitObjective.md)
