# DiagramStyle
type: "object"
description : >
## Description
The diagram style refer to a style used by the originating system for a diagram.  A diagram style describes information such as schematic, geographic, bus-branch etc.

## Data Model
  - properties:
    - Diagram:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : A DiagramStyle can be used by many Diagrams. Default: "list"
