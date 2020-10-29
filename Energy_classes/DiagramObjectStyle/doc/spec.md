# DiagramObjectStyle
type: "object"
description : >
## Description
A reference to a style used by the originating system for a diagram object.  A diagram object style describes information such as line thickness, shape such as circle or rectangle etc, and color.

## Data Model
  - properties:
    - StyledObjects:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : A style can be assigned to multiple diagram objects. Default: "list"
