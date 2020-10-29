# WindTurbineType4bIEC
type: "object"
description : >
## Description
Wind turbine IEC Type 4A.  Reference: IEC Standard 61400-27-1, section 6.5.5.3.

## Data Model
  - properties:
    - WindContPType4bIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind control P type 4B model associated with this wind turbine type 4B model. Default: None
    - WindMechIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind mechanical model associated with this wind turbine Type 4B model. Default: None
