---
type: FIBO Class
title: "project"
description: "state of affairs and unique and temporary organization, designed to deliver a tangible output"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/Project
tags: [FND, Release]
detail: "A project has a fixed - generally fairly short - timeframe, and a project manager is responsible for delivering the output on time and on budget."
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Situation.md", provenance: fibo}
  - {type: has-goal, target: "/FND/GoalsAndObjectives/Objectives/Goal.md", provenance: fibo}
  - {type: has-name, target: "/FND/GoalsAndObjectives/Objectives/ProjectName.md", provenance: fibo}
  - {type: has-objective, target: "/FND/GoalsAndObjectives/Objectives/Objective.md", provenance: fibo}
  - {type: is-identified-by, target: "/FND/GoalsAndObjectives/Objectives/ProjectIdentifier.md", provenance: fibo}
  - {type: is-member-of, target: "/FND/GoalsAndObjectives/Objectives/Program.md", provenance: fibo}
---

state of affairs and unique and temporary organization, designed to deliver a tangible output

### Relationships
- is-a: [Situation](/CMNS/PartiesAndSituations/Situation.md)
- has-goal: [Goal](/FND/GoalsAndObjectives/Objectives/Goal.md)
- has-name: [ProjectName](/FND/GoalsAndObjectives/Objectives/ProjectName.md)
- has-objective: [Objective](/FND/GoalsAndObjectives/Objectives/Objective.md)
- is-identified-by: [ProjectIdentifier](/FND/GoalsAndObjectives/Objectives/ProjectIdentifier.md)
- is-member-of: [Program](/FND/GoalsAndObjectives/Objectives/Program.md)
