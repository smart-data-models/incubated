# ConformLoad
type: "object"
description : >
## Description
ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.

## Data Model
  - properties:
    - LoadGroup:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Group of this ConformLoad. Default: None
