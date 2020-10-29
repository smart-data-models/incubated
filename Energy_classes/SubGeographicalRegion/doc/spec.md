# SubGeographicalRegion
type: "object"
description : >
## Description
A subset of a geographical region of a power system network model.

## Data Model
  - properties:
    - DCLines:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: :  Default: "list"
    - Region:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The geographical region to which this sub-geographical region is within. Default: None
    - Lines:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The lines within the sub-geographical region. Default: "list"
    - Substations:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The substations in this sub-geographical region. Default: "list"
