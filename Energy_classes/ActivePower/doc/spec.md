# ActivePower
type: "object"
description : >
## Description
Product of RMS value of the voltage and the RMS value of the in-phase component of the current.

## Data Model
  - properties:
    - value:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: :  Default: 0.0
    - unit:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: :  Default: None
    - multiplier:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: :  Default: None
