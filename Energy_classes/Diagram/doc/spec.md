# Diagram
type: "object"
description : >
## Description
The diagram being exchanged.  The coordinate system is a standard Cartesian coordinate system and the orientation attribute defines the orientation.

## Data Model
  - properties:
    - DiagramStyle:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : A Diagram may have a DiagramStyle. Default: None
    - orientation:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Coordinate system orientation of the diagram. Default: None
    - x1InitialView:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : X coordinate of the first corner of the initial view. Default: 0.0
    - x2InitialView:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : X coordinate of the second corner of the initial view. Default: 0.0
    - y1InitialView:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Y coordinate of the first corner of the initial view. Default: 0.0
    - y2InitialView:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Y coordinate of the second corner of the initial view. Default: 0.0
    - DiagramElements:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : A diagram is made up of multiple diagram objects. Default: "list"
