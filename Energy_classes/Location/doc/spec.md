# Location
type: "object"
description : >
## Description
The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It can be defined with one or more postition points (coordinates) in a given coordinate system.

## Data Model
  - properties:
    - CoordinateSystem:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Coordinate system used to describe position points of this location. Default: None
    - PowerSystemResources:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : All power system resources at this location. Default: None
    - PositionPoints:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Sequence of position points describing this location, expressed in coordinate system `Location.CoordinateSystem`. Default: "list"
