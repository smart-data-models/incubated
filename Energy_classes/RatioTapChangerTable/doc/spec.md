# RatioTapChangerTable
type: "object"
description : >
## Description
Describes a curve for how the voltage magnitude and impedance varies with the tap step.

## Data Model
  - properties:
    - RatioTapChanger:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The tap ratio table for this ratio  tap changer. Default: "list"
    - RatioTapChangerTablePoint:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Table of this point. Default: "list"
