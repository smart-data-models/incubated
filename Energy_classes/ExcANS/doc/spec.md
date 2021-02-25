# ExcANS


## Description
Italian excitation system. It represents static field voltage or excitation current feedback excitation system.

## Data Model
  - properties:
    - k3:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : AVR gain (K).  Typical Value = 1000. Default: 0.0
    - k2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Exciter gain (K).  Typical Value = 20. Default: 0.0
    - kce:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Ceiling factor (K).  Typical Value = 1. Default: 0.0
    - t3:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant (T).  Typical Value = 1.6. Default: 0
    - t2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant (T).  Typical Value = 0.05. Default: 0
    - t1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant (T).  Typical Value = 20. Default: 0
    - blint:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Governor Control Flag (BLINT).  0 = lead-lag regulator 1 = proportional integral regulator. Typical Value = 0. Default: 0
    - kvfif:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Rate feedback signal flag (K).  0 = output voltage of the exciter 1 = exciter field current. Typical Value = 0. Default: 0
    - ifmn:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum exciter current (I).  Typical Value = -5.2. Default: 0.0
    - ifmx:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum exciter current (I).  Typical Value = 6.5. Default: 0.0
    - vrmn:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum AVR output (V).  Typical Value = -5.2. Default: 0.0
    - vrmx:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum AVR output (V).  Typical Value = 6.5. Default: 0.0
    - krvecc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Feedback enabling (K).  0 = Open loop control 1 = Closed loop control. Typical Value = 1. Default: 0
    - tb:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Exciter time constant (T).  Typical Value = 0.04. Default: 0