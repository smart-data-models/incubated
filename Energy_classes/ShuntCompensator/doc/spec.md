# ShuntCompensator
type: "object"
description : >
## Description
A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.

## Data Model
  - properties:
    - aVRDelay:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time delay required for the device to be connected or disconnected by automatic voltage regulation (AVR). Default: 0
    - grounded:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Used for Yn and Zn connections. True if the neutral is solidly grounded. Default: False
    - maximumSections:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The maximum number of sections that may be switched in. Default: 0
    - nomU:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The voltage at which the nominal reactive power may be calculated. This should normally be within 10% of the voltage at which the capacitor is connected to the network. Default: 0.0
    - normalSections:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The normal number of sections switched in. Default: 0
    - switchOnCount:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The switch on count since the capacitor count was last reset or initialized. Default: 0
    - switchOnDate:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The date and time when the capacitor bank was last switched on. Default: ''
    - voltageSensitivity:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive power. Default: 0.0
    - sections:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Shunt compensator sections in use. Starting value for steady state solution. Non integer values are allowed to support continuous variables. The reasons for continuous value are to support study cases where no discrete shunt compensators has yet been designed, a solutions where a narrow voltage band force the sections to oscillate or accommodate for a continuous solution as input. Default: 0.0
    - SvShuntCompensatorSections:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The state for the number of shunt compensator sections in service. Default: None
