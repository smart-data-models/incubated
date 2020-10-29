# BaseVoltage
type: "object"
description : >
## Description
Defines a system base voltage which is referenced.

## Data Model
  - properties:
    - nominalVoltage:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The power system resource`s base voltage. Default: 0.0
    - ConductingEquipment:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Base voltage of this conducting equipment.  Use only when there is no voltage level container used and only one base voltage applies.  For example, not used for transformers. Default: "list"
    - VoltageLevel:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The voltage levels having this base voltage. Default: "list"
    - TransformerEnds:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Transformer ends at the base voltage.  This is essential for PU calculation. Default: "list"
    - TopologicalNode:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The topological nodes at the base voltage. Default: "list"
