# EquipmentContainer
type: "object"
description : >
## Description
A modeling construct to provide a root class for containing equipment.

## Data Model
  - properties:
    - Equipments:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Contained equipment. Default: "list"
