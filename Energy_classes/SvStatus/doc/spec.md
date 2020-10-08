# SvStatus
type: "object"
description : >
## Description
State variable for status.

## Data Model
  - properties:
    - ConductingEquipment:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The conducting equipment associated with the status state variable. Default: None
    - inService:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The in service status as a result of topology processing. Default: False
