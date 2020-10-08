# OverexcLimIEEE
type: "object"
description : >
## Description
The over excitation limiter model is intended to represent the significant features of OELs necessary for some large-scale system studies. It is the result of a pragmatic approach to obtain a model that can be widely applied with attainable data from generator owners. An attempt to include all variations in the functionality of OELs and duplicate how they interact with the rest of the excitation systems would likely result in a level of application insufficient for the studies for which they are intended.  Reference: IEEE OEL 421.5-2005 Section 9.

## Data Model
  - properties:
    - itfpu:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : OEL timed field current limiter pickup level (I).  Typical Value = 1.05. Default: 0.0
    - ifdmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : OEL instantaneous field current limit (I).  Typical Value = 1.5. Default: 0.0
    - ifdlim:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : OEL timed field current limit (I).  Typical Value = 1.05. Default: 0.0
    - hyst:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : OEL pickup/drop-out hysteresis (HYST).  Typical Value = 0.03. Default: 0.0
    - kcd:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : OEL cooldown gain (K).  Typical Value = 1. Default: 0.0
    - kramp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : OEL ramped limit rate (K).  Unit = PU/sec.  Typical Value = 10. Default: 0.0
