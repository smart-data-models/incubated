# GovSteam0
type: "object"
description : >
## Description
A simplified steam turbine governor model.

## Data Model
  - properties:
    - mwbase:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Base for power values (MWbase)  (>0).  Unit = MW. Default: 0.0
    - r:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Permanent droop (R).  Typical Value = 0.05. Default: 0.0
    - t1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Steam bowl time constant (T1).  Typical Value = 0.5. Default: 0
    - vmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum valve position, PU of mwcap (Vmax).  Typical Value = 1. Default: 0.0
    - vmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum valve position, PU of mwcap (Vmin).  Typical Value = 0. Default: 0.0
    - t2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Numerator time constant of T2/T3 block (T2).  Typical Value = 3. Default: 0
    - t3:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Reheater time constant (T3).  Typical Value = 10. Default: 0
    - dt:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Turbine damping coefficient (Dt).  Unit = delta P / delta speed. Typical Value = 0. Default: 0.0
