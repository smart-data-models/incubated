# WindContPType4bIEC
type: "object"
description : >
## Description
P control model Type 4B.  Reference: IEC Standard 61400-27-1 Section 6.6.5.5.

## Data Model
  - properties:
    - dpmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum wind turbine power ramp rate (). It is project dependent parameter. Default: 0.0
    - tpaero:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant in aerodynamic power response (). It is type dependent parameter. Default: 0
    - tpord:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant in power order lag (). It is type dependent parameter. Default: 0
    - tufilt:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Voltage measurement filter time constant (). It is type dependent parameter. Default: 0
    - WindTurbineType4bIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind turbine type 4B model with which this wind control P type 4B model is associated. Default: None
