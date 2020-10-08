# VAdjIEEE
type: "object"
description : >
## Description
The class represents IEEE Voltage Adjuster which is used to represent the voltage adjuster in either a power factor or var control system.  Reference: IEEE Standard 421.5-2005 Section 11.1.

## Data Model
  - properties:
    - vadjf:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Set high to provide a continuous raise or lower (). Default: 0.0
    - adjslew:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Rate at which output of adjuster changes ().  Unit = sec./PU.  Typical Value = 300. Default: 0.0
    - vadjmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum output of the adjuster ().  Typical Value = 1.1. Default: 0.0
    - vadjmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum output of the adjuster ().  Typical Value = 0.9. Default: 0.0
    - taon:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time that adjuster pulses are on ().  Typical Value = 0.1. Default: 0
    - taoff:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time that adjuster pulses are off ().  Typical Value = 0.5. Default: 0
