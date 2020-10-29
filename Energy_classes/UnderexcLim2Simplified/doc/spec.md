# UnderexcLim2Simplified
type: "object"
description : >
## Description
This model can be derived from UnderexcLimIEEE2. The limit characteristic (look -up table) is a single straight-line, the same as UnderexcLimIEEE2 (see Figure 10.4 (p 32), IEEE 421.5-2005 Section 10.2).

## Data Model
  - properties:
    - q0:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Segment Q initial point (Q0).  Typical Value = -0.31. Default: 0.0
    - q1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Segment Q end point (Q1).  Typical Value = -0.1. Default: 0.0
    - p0:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Segment P initial point (P0).  Typical Value = 0. Default: 0.0
    - p1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Segment P end point (P1).  Typical Value = 1. Default: 0.0
    - kui:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain Under excitation limiter (Kui).  Typical Value = 0.1. Default: 0.0
    - vuimin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum error signal (V).  Typical Value = 0. Default: 0.0
    - vuimax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum error signal (V).  Typical Value = 1. Default: 0.0
