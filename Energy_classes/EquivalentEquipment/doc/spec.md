# EquivalentEquipment
type: "object"
description : >
## Description
The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.

## Data Model
  - properties:
    - EquivalentNetwork:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The associated reduced equivalents. Default: None
