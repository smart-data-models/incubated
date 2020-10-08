# DCTopologicalNode
type: "object"
description : >
## Description
DC bus.

## Data Model
  - properties:
    - DCTopologicalIsland:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: :  Default: None
    - DCTerminals:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : See association end Terminal.TopologicalNode. Default: "list"
    - DCEquipmentContainer:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: :  Default: None
    - DCNodes:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : See association end ConnectivityNode.TopologicalNode. Default: "list"
