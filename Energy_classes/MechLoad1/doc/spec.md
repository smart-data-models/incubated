# MechLoad1
type: "object"
description : >
## Description
Mechanical load model type 1.

## Data Model
  - properties:
    - a:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Speed squared coefficient (a). Default: 0.0
    - b:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Speed coefficient (b). Default: 0.0
    - d:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Speed to the exponent coefficient (d). Default: 0.0
    - e:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Exponent (e). Default: 0.0
