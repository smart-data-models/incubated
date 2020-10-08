# Frequency
type: "object"
description : >
## Description
Cycles per second.

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
