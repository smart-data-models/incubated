# NonConformLoad
type: "object"
description : >
## Description
NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.

## Data Model
  - properties:
    - LoadGroup:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Conform loads assigned to this ConformLoadGroup. Default: None
