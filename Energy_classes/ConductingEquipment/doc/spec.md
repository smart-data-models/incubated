# ConductingEquipment
type: "object"
description : >
## Description
The parts of the AC power system that are designed to carry current or that are conductively connected through terminals.

## Data Model
  - properties:
    - BaseVoltage:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : All conducting equipment with this base voltage.  Use only when there is no voltage level container used and only one base voltage applies.  For example, not used for transformers. Default: None
    - Terminals:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Conducting equipment have terminals that may be connected to other conducting equipment terminals via connectivity nodes or topological nodes. Default: "list"
    - SvStatus:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The status state variable associated with this conducting equipment. Default: None
