# PhaseTapChangerTablePoint
type: "object"
description : >
## Description
Describes each tap step in the phase tap changer tabular curve.

## Data Model
  - properties:
    - PhaseTapChangerTable:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The table of this point. Default: None
    - angle:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The angle difference in degrees. Default: 0.0
