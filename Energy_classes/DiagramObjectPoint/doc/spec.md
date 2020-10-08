# DiagramObjectPoint
type: "object"
description : >
## Description
A point in a given space defined by 3 coordinates and associated to a diagram object.  The coordinates may be positive or negative as the origin does not have to be in the corner of a diagram.

## Data Model
  - properties:
    - DiagramObject:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The diagram object with which the points are associated. Default: None
    - DiagramObjectGluePoint:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : A diagram object glue point is associated with 2 or more object points that are considered to be `glued` together. Default: None
    - sequenceNumber:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The sequence position of the point, used for defining the order of points for diagram objects acting as a polyline or polygon with more than one point. Default: 0
    - xPosition:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The X coordinate of this point. Default: 0.0
    - yPosition:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The Y coordinate of this point. Default: 0.0
    - zPosition:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The Z coordinate of this point. Default: 0.0
