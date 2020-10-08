# NonConformLoadGroup
type: "object"
description : >
## Description
Loads that do not follow a daily and seasonal load variation pattern.

## Data Model
  - properties:
    - EnergyConsumers:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Group of this ConformLoad. Default: "list"
    - NonConformLoadSchedules:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The NonConformLoadSchedules in the NonConformLoadGroup. Default: "list"
