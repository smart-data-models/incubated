# TapChangerControl
type: "object"
description : >
## Description
Describes behavior specific to tap changers, e.g. how the voltage at the end of a line varies with the load level and compensation of the voltage drop by tap adjustment.

## Data Model
  - properties:
    - TapChanger:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The regulating control scheme in which this tap changer participates. Default: "list"
