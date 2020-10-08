# NonConformLoadSchedule
type: "object"
description : >
## Description
An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled).

## Data Model
  - properties:
    - NonConformLoadGroup:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The NonConformLoadGroup where the NonConformLoadSchedule belongs. Default: None
