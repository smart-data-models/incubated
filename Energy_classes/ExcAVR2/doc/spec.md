# ExcAVR2
type: "object"
description : >
## Description
Italian excitation system corresponding to IEEE (1968) Type 2 Model. It represents alternator and rotating diodes and electromechanic voltage regulators.

## Data Model
  - properties:
    - ka:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : AVR gain (K).  Typical Value = 500. Default: 0.0
    - vrmn:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum AVR output (V).  Typical Value = -6. Default: 0.0
    - vrmx:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum AVR output (V).  Typical Value = 7. Default: 0.0
    - ta:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : AVR time constant (T).  Typical Value = 0.02. Default: 0
    - tb:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : AVR time constant (T).  Typical Value = 0. Default: 0
    - te:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Exciter time constant (T).  Typical Value = 1. Default: 0
    - e1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Field voltage value 1 (E1).  Typical Value = 4.18. Default: 0.0
    - se1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Saturation factor at E1 (S(E1)).  Typical Value = 0.1. Default: 0.0
    - e2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Field voltage value 2 (E2).  Typical Value = 3.14. Default: 0.0
    - se2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Saturation factor at E2 (S(E2)).  Typical Value = 0.03. Default: 0.0
    - kf:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Rate feedback gain (K).  Typical Value = 0.02. Default: 0.0
    - tf1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Rate feedback time constant (T).  Typical Value = 1. Default: 0
    - tf2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Rate feedback time constant (T).  Typical Value = 1. Default: 0
