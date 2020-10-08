# Substation
type: "object"
description : >
## Description
A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.

## Data Model
  - properties:
    - DCConverterUnit:
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
      - description: : The SubGeographicalRegion containing the substation. Default: None
    - VoltageLevels:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The voltage levels within this substation. Default: "list"
