# TapChanger
type: "object"
description : >
## Description
Mechanism for changing transformer winding tap positions.

## Data Model
  - properties:
    - highStep:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Highest possible tap step position, advance from neutral. The attribute shall be greater than lowStep. Default: 0
    - lowStep:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Lowest possible tap step position, retard from neutral Default: 0
    - ltcFlag:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Specifies whether or not a TapChanger has load tap changing capabilities. Default: False
    - neutralStep:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The neutral tap step position for this winding. The attribute shall be equal or greater than lowStep and equal or less than highStep. Default: 0
    - neutralU:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Voltage at which the winding operates at the neutral tap setting. Default: 0.0
    - normalStep:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The tap step position used in `normal` network operation for this winding. For a `Fixed` tap changer indicates the current physical tap setting. The attribute shall be equal or greater than lowStep and equal or less than highStep. Default: 0
    - TapChangerControl:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The tap changers that participates in this regulating tap control scheme. Default: None
    - TapSchedules:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : A TapSchedule is associated with a TapChanger. Default: "list"
    - controlEnabled:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Specifies the regulation status of the equipment.  True is regulating, false is not regulating. Default: False
    - step:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Tap changer position. Starting step for a steady state solution. Non integer values are allowed to support continuous tap variables. The reasons for continuous value are to support study cases where no discrete tap changers has yet been designed, a solutions where a narrow voltage band force the tap step to oscillate or accommodate for a continuous solution as input. The attribute shall be equal or greater than lowStep and equal or less than highStep. Default: 0.0
    - SvTapStep:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The tap step state associated with the tap changer. Default: None
