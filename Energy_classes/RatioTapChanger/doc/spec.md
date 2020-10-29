# RatioTapChanger
type: "object"
description : >
## Description
A tap changer that changes the voltage ratio impacting the voltage magnitude but not the phase angle across the transformer.

## Data Model
  - properties:
    - tculControlMode:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger. Default: None
    - stepVoltageIncrement:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Tap step increment, in per cent of nominal voltage, per step position. Default: 0.0
    - RatioTapChangerTable:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The ratio tap changer of this tap ratio table. Default: None
    - TransformerEnd:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Ratio tap changer associated with this transformer end. Default: None
