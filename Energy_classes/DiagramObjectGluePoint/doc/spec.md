# DiagramObjectGluePoint
type: "object"
description : >
## Description
This is used for grouping diagram object points from different diagram objects that are considered to be glued together in a diagram even if they are not at the exact same coordinates.

## Data Model
  - properties:
    - DiagramObjectPoints:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The `glue` point to which this point is associated. Default: "list"
