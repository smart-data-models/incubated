# WindGenTurbineType3bIEC
type: "object"
description : >
## Description
IEC Type 3B generator set model.  Reference: IEC Standard 61400-27-1 Section 6.6.3.3.

## Data Model
  - properties:
    - fducw:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Crowbar duration versus voltage variation look-up table (f()). It is case dependent parameter. Default: 0.0
    - tg:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Current generation Time constant (). It is type dependent parameter. Default: 0
    - two:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant for crowbar washout filter (). It is case dependent parameter. Default: 0
    - mwtcwp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Crowbar control mode ().   The parameter is case dependent parameter. Default: False
    - xs:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Electromagnetic transient reactance (x). It is type dependent parameter. Default: 0.0
