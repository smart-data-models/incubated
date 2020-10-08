# VoltageLimit
type: "object"
description : >
## Description
Operational limit applied to voltage.

## Data Model
  - properties:
    - value:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Limit on voltage. High or low limit nature of the limit depends upon the properties of the operational limit type. Default: 0.0
