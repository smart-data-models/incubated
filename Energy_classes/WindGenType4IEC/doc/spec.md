# WindGenType4IEC
type: "object"
description : >
## Description
IEC Type 4 generator set model.  Reference: IEC Standard 61400-27-1 Section 6.6.3.4.

## Data Model
  - properties:
    - dipmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum active current ramp rate (di). It is project dependent parameter. Default: 0.0
    - diqmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum reactive current ramp rate (d). It is case dependent parameter. Default: 0.0
    - diqmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum reactive current ramp rate (di). It is project dependent parameter. Default: 0.0
    - tg:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant (T). It is type dependent parameter. Default: 0
