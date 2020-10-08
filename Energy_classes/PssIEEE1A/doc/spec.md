# PssIEEE1A
type: "object"
description : >
## Description
The class represents IEEE Std 421.5-2005 type PSS1A power system stabilizer model. PSS1A is the generalized form of a PSS with a single input. Some common stabilizer input signals are speed, frequency, and power.  Reference: IEEE 1A 421.5-2005 Section 8.1.

## Data Model
  - properties:
    - inputSignalType:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Type of input signal.  Typical Value = rotorAngularFrequencyDeviation. Default: None
    - a1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : PSS signal conditioning frequency filter constant (A1).  Typical Value = 0.061. Default: 0.0
    - a2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : PSS signal conditioning frequency filter constant (A2).  Typical Value = 0.0017. Default: 0.0
    - t1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Lead/lag time constant (T1).  Typical Value = 0.3. Default: 0
    - t2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Lead/lag time constant (T2).  Typical Value = 0.03. Default: 0
    - t3:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Lead/lag time constant (T3).  Typical Value = 0.3. Default: 0
    - t4:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Lead/lag time constant (T4).  Typical Value = 0.03. Default: 0
    - t5:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Washout time constant (T5).  Typical Value = 10. Default: 0
    - t6:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Transducer time constant (T6).  Typical Value = 0.01. Default: 0
    - ks:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Stabilizer gain (Ks).  Typical Value = 5. Default: 0.0
    - vrmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum stabilizer output (Vrmax).  Typical Value = 0.05. Default: 0.0
    - vrmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum stabilizer output (Vrmin).  Typical Value = -0.05. Default: 0.0
