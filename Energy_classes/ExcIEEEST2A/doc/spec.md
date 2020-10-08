# ExcIEEEST2A
type: "object"
description : >
## Description
The class represents IEEE Std 421.5-2005 type ST2A model. Some static systems utilize both current and voltage sources (generator terminal quantities) to comprise the power source.  The regulator controls the exciter output through controlled saturation of the power transformer components.  These compound-source rectifier excitation systems are designated Type ST2A and are represented by ExcIEEEST2A.  Reference: IEEE Standard 421.5-2005 Section 7.2.

## Data Model
  - properties:
    - ka:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Voltage regulator gain (K).  Typical Value = 120. Default: 0.0
    - ta:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Voltage regulator time constant (T).  Typical Value = 0.15. Default: 0
    - vrmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum voltage regulator outputs (V).  Typical Value = 1. Default: 0.0
    - vrmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum voltage regulator outputs (V).  Typical Value = 0. Default: 0.0
    - ke:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Exciter constant related to self-excited field (K).  Typical Value = 1. Default: 0.0
    - te:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.5. Default: 0
    - kf:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Excitation control system stabilizer gains (K).  Typical Value = 0.05. Default: 0.0
    - tf:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Excitation control system stabilizer time constant (T).  Typical Value = 1. Default: 0
    - kp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Potential circuit gain coefficient (K).  Typical Value = 4.88. Default: 0.0
    - ki:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Potential circuit gain coefficient (K).  Typical Value = 8. Default: 0.0
    - kc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Rectifier loading factor proportional to commutating reactance (K). Typical Value = 1.82. Default: 0.0
    - efdmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum field voltage (E).  Typical Value = 99. Default: 0.0
    - uelin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : UEL input (UELin). true = HV gate false = add to error signal. Typical Value = true. Default: False
