# GenICompensationForGenJ
type: "object"
description : >
## Description
This class provides the resistive and reactive components of compensation for the generator associated with the IEEE Type 2 voltage compensator for current flow out of one of the other generators in the interconnection.

## Data Model
  - properties:
    - SynchronousMachineDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Standard synchronous machine out of which current flow is being compensated for. Default: None
    - VcompIEEEType2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The standard IEEE Type 2 voltage compensator of this compensation. Default: None
    - rcij:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: :  Default: 0.0
    - xcij:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: :  Default: 0.0
