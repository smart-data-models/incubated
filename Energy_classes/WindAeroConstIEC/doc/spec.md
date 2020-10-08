# WindAeroConstIEC
type: "object"
description : >
## Description
The constant aerodynamic torque model assumes that the aerodynamic torque is constant.  Reference: IEC Standard 61400-27-1 Section 6.6.1.1.

## Data Model
  - properties:
    - WindGenTurbineType1IEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind turbine type 1 model with which this wind aerodynamic model is associated. Default: None
