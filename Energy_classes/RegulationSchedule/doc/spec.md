# RegulationSchedule
type: "object"
description : >
## Description
A pre-established pattern over time for a controlled variable, e.g., busbar voltage.

## Data Model
  - properties:
    - RegulatingControl:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Regulating controls that have this Schedule. Default: None
