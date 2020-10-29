# SvVoltage
type: "object"
description : >
## Description
State variable for voltage.

## Data Model
  - properties:
    - angle:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The voltage angle of the topological node complex voltage with respect to system reference. Default: 0.0
    - v:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The voltage magnitude of the topological node. Default: 0.0
    - TopologicalNode:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The state voltage associated with the topological node. Default: None
