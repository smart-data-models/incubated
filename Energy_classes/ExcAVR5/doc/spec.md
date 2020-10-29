# ExcAVR5
type: "object"
description : >
## Description
Manual excitation control with field circuit resistance. This model can be used as a very simple representation of manual voltage control.

## Data Model
  - properties:
    - ka:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain (Ka). Default: 0.0
    - ta:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant (Ta). Default: 0
    - rex:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Effective Output Resistance (Rex). Rex represents the effective output resistance seen by the excitation system. Default: 0.0
