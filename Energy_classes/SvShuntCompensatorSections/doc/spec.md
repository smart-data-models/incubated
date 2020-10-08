# SvShuntCompensatorSections
type: "object"
description : >
## Description
State variable for the number of sections in service for a shunt compensator.

## Data Model
  - properties:
    - sections:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The number of sections in service as a continous variable. To get integer value scale with ShuntCompensator.bPerSection. Default: 0.0
    - ShuntCompensator:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The shunt compensator for which the state applies. Default: None
