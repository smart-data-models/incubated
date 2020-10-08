# DCNode
type: "object"
description : >
## Description
DC nodes are points where terminals of DC conducting equipment are connected together with zero impedance.

## Data Model
  - properties:
    - DCTerminals:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: :  Default: "list"
    - DCEquipmentContainer:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: :  Default: None
    - DCTopologicalNode:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : See association end TopologicalNode.ConnectivityNodes. Default: None
