# Conductance
type: "object"
description : >
## Description
Factor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance.

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
