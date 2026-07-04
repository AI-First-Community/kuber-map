---
type: FIBO Class
title: "action classification scheme"
description: "scheme for classifying the kinds of actions and events that may be announced, initiated or carried out by an organization that affects a legal entity or the securities it issues"
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/ActionClassificationScheme
tags: [CAE, Release]
detail: "The set of corporate actions and income events included herein are a subset of those specified in a combination of ISO 15022 Securities - Scheme for Messages (Data Field Dictionary) and the GLEIF LEI-related corporate actions. Other schemes that are specific to a custodian, depository, or regulatory agency may also be important, and should take a similar approach with respect to classification."
relations:
  - {type: is-a, target: "/CMNS/Classifiers/ClassificationScheme.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/CodesAndCodeSets/CodeSet.md", provenance: fibo}
  - {type: defines, target: "/CAE/CorporateEvents/CorporateActions/ActionClassifier.md", provenance: fibo}
  - {type: has-member, target: "/CAE/CorporateEvents/CorporateActions/ActionClassifier.md", provenance: fibo}
---

scheme for classifying the kinds of actions and events that may be announced, initiated or carried out by an organization that affects a legal entity or the securities it issues

### Relationships
- is-a: [ClassificationScheme](/CMNS/Classifiers/ClassificationScheme.md)
- is-a: [CodeSet](/CMNS/CodesAndCodeSets/CodeSet.md)
- defines: [ActionClassifier](/CAE/CorporateEvents/CorporateActions/ActionClassifier.md)
- has-member: [ActionClassifier](/CAE/CorporateEvents/CorporateActions/ActionClassifier.md)
