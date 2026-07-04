---
type: FIBO Class
title: "composition"
description: "distinct thing resulting from bringing together other things, possibly in specific roles, for a particular purpose"
resource: https://www.omg.org/spec/Commons/RolesAndCompositions/Composition
tags: [CMNS]
detail: "The composition may be specified based on the roles that the things play in the composition, such as the roles that various ingredients play in a recipe or pharmaceutical product, and such things may or may not be transformed in some way through the process of combining them. Quantification including the nature and amount of each thing, potentially including the ratio of the quantities, may be required depending kind of composition. The properties hasConstituent and hasRole are included in value restrictions rather than via number restrictions to facilitate their use in complex property chains and other axioms as needed for some applications."
relations:
  - {type: has-constituent, target: "/CMNS/Collections/Constituent.md", provenance: fibo}
  - {type: has-role, target: "/CMNS/RolesAndCompositions/Role.md", provenance: fibo}
  - {type: is-applicable-in, target: "/CMNS/ContextualDesignators/Context.md", provenance: fibo}
---

distinct thing resulting from bringing together other things, possibly in specific roles, for a particular purpose

### Relationships
- has-constituent: [Constituent](/CMNS/Collections/Constituent.md)
- has-role: [Role](/CMNS/RolesAndCompositions/Role.md)
- is-applicable-in: [Context](/CMNS/ContextualDesignators/Context.md)
