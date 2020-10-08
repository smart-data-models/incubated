# GovGAST
type: "object"
description : >
## Description
Single shaft gas turbine.

## Data Model
  - properties:
    - mwbase:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Base for power values (MWbase) (> 0). Default: 0.0
    - r:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Permanent droop (R).  Typical Value = 0.04. Default: 0.0
    - t1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Governor mechanism time constant (T1).  T1 represents the natural valve positioning time constant of the governor for small disturbances, as seen when rate limiting is not in effect.  Typical Value = 0.5. Default: 0
    - t2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Turbine power time constant (T2).  T2 represents delay due to internal energy storage of the gas turbine engine. T2 can be used to give a rough approximation to the delay associated with acceleration of the compressor spool of a multi-shaft engine, or with the compressibility of gas in the plenum of a the free power turbine of an aero-derivative unit, for example.  Typical Value = 0.5. Default: 0
    - t3:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Turbine exhaust temperature time constant (T3).  Typical Value = 3. Default: 0
    - at:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Ambient temperature load limit (Load Limit).  Typical Value = 1. Default: 0.0
    - kt:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Temperature limiter gain (Kt).  Typical Value = 3. Default: 0.0
    - vmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum turbine power, PU of MWbase (Vmax).  Typical Value = 1. Default: 0.0
    - vmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum turbine power, PU of MWbase (Vmin).  Typical Value = 0. Default: 0.0
    - dturb:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Turbine damping factor (Dturb).  Typical Value = 0.18. Default: 0.0
