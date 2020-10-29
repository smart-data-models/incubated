# WindGenTurbineType3aIEC
type: "object"
description : >
## Description
IEC Type 3A generator set model.  Reference: IEC Standard 61400-27-1 Section 6.6.3.2.

## Data Model
  - properties:
    - kpc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Current PI controller proportional gain (K). It is type dependent parameter. Default: 0.0
    - xs:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Electromagnetic transient reactance (x). It is type dependent parameter. Default: 0.0
    - tic:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Current PI controller integration time constant (T). It is type dependent parameter. Default: 0
