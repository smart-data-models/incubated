# EquivalentShunt
type: "object"
description : >
## Description
The class represents equivalent shunts.

## Data Model
  - properties:
    - b:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Positive sequence shunt susceptance. Default: 0.0
    - g:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Positive sequence shunt conductance. Default: 0.0
