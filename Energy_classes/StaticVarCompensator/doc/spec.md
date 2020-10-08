# StaticVarCompensator
type: "object"
description : >
## Description
A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode. When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.

## Data Model
  - properties:
    - capacitiveRating:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum available capacitive reactance. Default: 0.0
    - inductiveRating:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum available inductive reactance. Default: 0.0
    - slope:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint. Default: 0.0
    - sVCControlMode:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : SVC control mode. Default: None
    - voltageSetPoint:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero. Default: 0.0
    - q:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. Default: 0.0
