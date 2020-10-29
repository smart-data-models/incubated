# DCGround
type: "object"
description : >
## Description
A ground within a DC system.

## Data Model
  - properties:
    - inductance:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Inductance to ground. Default: 0.0
    - r:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Resistance to ground. Default: 0.0
