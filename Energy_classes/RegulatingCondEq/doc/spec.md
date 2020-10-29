# RegulatingCondEq
type: "object"
description : >
## Description
A type of conducting equipment that can regulate a quantity (i.e. voltage or flow) at a specific point in the network.

## Data Model
  - properties:
    - RegulatingControl:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The regulating control scheme in which this equipment participates. Default: None
    - controlEnabled:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Specifies the regulation status of the equipment.  True is regulating, false is not regulating. Default: False
