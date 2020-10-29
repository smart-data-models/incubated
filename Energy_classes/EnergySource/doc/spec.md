# EnergySource
type: "object"
description : >
## Description
A generic equivalent for an energy supplier on a transmission or distribution voltage level.

## Data Model
  - properties:
    - EnergySchedulingType:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Energy Source of a particular Energy Scheduling Type Default: None
    - nominalVoltage:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Phase-to-phase nominal voltage. Default: 0.0
    - r:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Positive sequence Thevenin resistance. Default: 0.0
    - r0:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Zero sequence Thevenin resistance. Default: 0.0
    - rn:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Negative sequence Thevenin resistance. Default: 0.0
    - voltageAngle:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Phase angle of a-phase open circuit. Default: 0.0
    - voltageMagnitude:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Phase-to-phase open circuit voltage magnitude. Default: 0.0
    - x:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Positive sequence Thevenin reactance. Default: 0.0
    - x0:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Zero sequence Thevenin reactance. Default: 0.0
    - xn:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Negative sequence Thevenin reactance. Default: 0.0
    - activePower:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : High voltage source active injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 0.0
    - reactivePower:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : High voltage source reactive injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for steady state solutions. Default: 0.0
    - WindTurbineType3or4Dynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind generator Type 3 or 4 dynamics model associated with this energy source. Default: None
