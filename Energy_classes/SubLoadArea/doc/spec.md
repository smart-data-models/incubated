# SubLoadArea
type: "object"
description : >
## Description
The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.

## Data Model
  - properties:
    - LoadArea:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The LoadArea where the SubLoadArea belongs. Default: None
    - LoadGroups:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The Loadgroups in the SubLoadArea. Default: "list"
