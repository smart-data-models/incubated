# ExcSEXS
type: "object"
description : >
## Description
Simplified Excitation System Model.

## Data Model
  - properties:
    - tatb:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Ta/Tb - gain reduction ratio of lag-lead element (TaTb).  Typical Value = 0.1. Default: 0.0
    - tb:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Denominator time constant of lag-lead block (Tb).  Typical Value = 10. Default: 0
    - k:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain (K) (>0).  Typical Value = 100. Default: 0.0
    - te:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant of gain block (Te).  Typical Value = 0.05. Default: 0
    - emin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum field voltage output (Emin).  Typical Value = -5. Default: 0.0
    - emax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum field voltage output (Emax).  Typical Value = 5. Default: 0.0
    - kc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : PI controller gain (Kc).  Typical Value = 0.08. Default: 0.0
    - tc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : PI controller phase lead time constant (Tc).  Typical Value = 0. Default: 0
    - efdmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Field voltage clipping minimum limit (Efdmin).  Typical Value = -5. Default: 0.0
    - efdmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Field voltage clipping maximum limit (Efdmax).  Typical Value = 5. Default: 0.0
