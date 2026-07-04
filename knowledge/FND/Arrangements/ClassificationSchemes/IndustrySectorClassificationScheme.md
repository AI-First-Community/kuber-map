---
type: FIBO Class
title: "industry sector classification scheme"
description: "system for allocating classifiers to organizations by industry sector"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/IndustrySectorClassificationScheme
tags: [FND, Release]
examples:
  - "Examples include the North American Industry Classification System (NAICS) and Standardized Industry Classification (SIC) in the U.S. and Canada, and the NACE (Nomenclature Générale des Activités Économiques dans les Communautés Européennes) in the EU, developed by governments to classify industries. They also include commercial classification schemes, such as the Global Industry Standard Classification (GICS) developed jointly by Morgan Stanley Capital International (MSCI) and Standard and Poor's, and competing schemes including the Industry Classification Benchmark (ICB) system, maintained by Dow Jones and London's FTSE Group, among others."
relations:
  - {type: is-a, target: "/CMNS/Classifiers/ClassificationScheme.md", provenance: fibo}
  - {type: defines, target: "/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md", provenance: fibo}
---

system for allocating classifiers to organizations by industry sector

### Relationships
- is-a: [ClassificationScheme](/CMNS/Classifiers/ClassificationScheme.md)
- defines: [IndustrySectorClassifier](/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md)
