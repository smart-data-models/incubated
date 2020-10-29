# PhaseTapChangerTable
type: "object"
description : >
## Description
Describes a tabular curve for how the phase angle difference and impedance varies with the tap step.

## Data Model
  - properties:
    - PhaseTapChangerTablePoint:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The points of this table. Default: "list"
    - PhaseTapChangerTabular:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The phase tap changers to which this phase tap table applies. Default: "list"
