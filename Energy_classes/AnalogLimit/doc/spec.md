# AnalogLimit
type: "object"
description : >
## Description
Limit values for Analog measurements.

## Data Model
  - properties:
    - value:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The value to supervise against. Default: 0.0
    - LimitSet:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The limit values used for supervision of Measurements. Default: None
