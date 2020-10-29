# ConformLoadGroup
type: "object"
description : >
## Description
A group of loads conforming to an allocation pattern.

## Data Model
  - properties:
    - EnergyConsumers:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Conform loads assigned to this ConformLoadGroup. Default: "list"
    - ConformLoadSchedules:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The ConformLoadSchedules in the ConformLoadGroup. Default: "list"
