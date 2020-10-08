# TurbLCFB1
type: "object"
description : >
## Description
Turbine Load Controller model developed in the WECC.  This model represents a supervisory turbine load controller that acts to maintain turbine power at a set value by continuous adjustment of the turbine governor speed-load reference. This model is intended to represent slow reset 'outer loop' controllers managing the action of the turbine governor.

## Data Model
  - properties:
    - mwbase:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0
    - speedReferenceGovernor:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Type of turbine governor reference (Type). true = speed reference governor false = load reference governor. Typical Value = true. Default: False
    - db:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Controller dead band (db).  Typical Value = 0. Default: 0.0
    - emax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum control error (Emax) (note 4).  Typical Value = 0.02. Default: 0.0
    - fb:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Frequency bias gain (Fb).  Typical Value = 0. Default: 0.0
    - kp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Proportional gain (Kp).  Typical Value = 0. Default: 0.0
    - ki:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Integral gain (Ki).  Typical Value = 0. Default: 0.0
    - fbf:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Frequency bias flag (Fbf). true = enable frequency bias false = disable frequency bias. Typical Value = false. Default: False
    - pbf:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Power controller flag (Pbf). true = enable load controller false = disable load controller. Typical Value = false. Default: False
    - tpelec:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Power transducer time constant (Tpelec).  Typical Value = 0. Default: 0
    - irmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum turbine speed/load reference bias (Irmax) (note 3).  Typical Value = 0. Default: 0.0
    - pmwset:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Power controller setpoint (Pmwset) (note 1).  Unit = MW. Typical Value = 0. Default: 0.0
