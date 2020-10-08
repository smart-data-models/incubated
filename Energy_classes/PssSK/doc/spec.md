# PssSK
type: "object"
description : >
## Description
PSS Slovakian type - three inputs.

## Data Model
  - properties:
    - k1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain P (K1).  Typical Value = -0.3. Default: 0.0
    - k2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain fe (K2).  Typical Value = -0.15. Default: 0.0
    - k3:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain If (K3).  Typical Value = 10. Default: 0.0
    - t1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Denominator time constant (T1).  Typical Value = 0.3. Default: 0
    - t2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Filter time constant (T2).  Typical Value = 0.35. Default: 0
    - t3:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Denominator time constant (T3).  Typical Value = 0.22. Default: 0
    - t4:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Filter time constant (T4).  Typical Value = 0.02. Default: 0
    - t5:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Denominator time constant (T5).  Typical Value = 0.02. Default: 0
    - t6:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Filter time constant (T6).  Typical Value = 0.02. Default: 0
    - vsmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Stabilizer output max limit (Vsmax).  Typical Value = 0.4. Default: 0.0
    - vsmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Stabilizer output min limit (Vsmin).  Typical Value = -0.4. Default: 0.0
