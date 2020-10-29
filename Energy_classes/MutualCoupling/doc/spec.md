# MutualCoupling
type: "object"
description : >
## Description
This class represents the zero sequence line mutual coupling.

## Data Model
  - properties:
    - First_Terminal:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments. Default: None
    - Second_Terminal:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The starting terminal for the calculation of distances along the second branch of the mutual coupling. Default: None
    - b0ch:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section. Default: 0.0
    - distance11:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Distance to the start of the coupled region from the first line`s terminal having sequence number equal to 1. Default: 0.0
    - distance12:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Distance to the end of the coupled region from the first line`s terminal with sequence number equal to 1. Default: 0.0
    - distance21:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Distance to the start of coupled region from the second line`s terminal with sequence number equal to 1. Default: 0.0
    - distance22:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Distance to the end of coupled region from the second line`s terminal with sequence number equal to 1. Default: 0.0
    - g0ch:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section. Default: 0.0
    - r0:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Zero sequence branch-to-branch mutual impedance coupling, resistance. Default: 0.0
    - x0:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Zero sequence branch-to-branch mutual impedance coupling, reactance. Default: 0.0
