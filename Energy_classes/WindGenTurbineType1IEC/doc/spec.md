# WindGenTurbineType1IEC
type: "object"
description : >
## Description
Wind turbine IEC Type 1.  Reference: IEC Standard 61400-27-1, section 6.5.2.

## Data Model
  - properties:
    - WindAeroConstIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind aerodynamic model associated with this wind turbine type 1 model. Default: None
