# ExcSCRX
type: "object"
description : >
## Description
Simple excitation system model representing generic characteristics of many excitation systems; intended for use where negative field current may be a problem.

## Data Model
  - properties:
    - tatb:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Ta/Tb - gain reduction ratio of lag-lead element (TaTb). The parameter Ta is not defined explicitly.  Typical Value = 0.1. Default: 0.0
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
      - description: : Gain (K) (>0).  Typical Value = 200. Default: 0.0
    - te:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant of gain block (Te) (>0).  Typical Value = 0.02. Default: 0
    - emin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum field voltage output (Emin).  Typical Value = 0. Default: 0.0
    - emax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum field voltage output (Emax).  Typical Value = 5. Default: 0.0
    - cswitch:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Power source switch (Cswitch). true = fixed voltage of 1.0 PU false = generator terminal voltage. Default: False
    - rcrfd:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Rc/Rfd - ratio of field discharge resistance to field winding resistance (RcRfd).  Typical Value = 0. Default: 0.0
