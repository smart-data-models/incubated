# DiscExcContIEEEDEC2A
type: "object"
description : >
## Description
The class represents IEEE Type DEC2A model for the discontinuous excitation control. This system provides transient excitation boosting via an open-loop control as initiated by a trigger signal generated remotely.  Reference: IEEE Standard 421.5-2005 Section 12.3.

## Data Model
  - properties:
    - vk:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Discontinuous controller input reference (). Default: 0.0
    - td1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Discontinuous controller time constant (). Default: 0
    - td2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Discontinuous controller washout time constant (). Default: 0
    - vdmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Limiter (). Default: 0.0
    - vdmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Limiter (). Default: 0.0
