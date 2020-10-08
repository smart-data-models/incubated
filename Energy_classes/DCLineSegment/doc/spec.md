# DCLineSegment
type: "object"
description : >
## Description
A wire or combination of wires not insulated from one another, with consistent electrical characteristics, used to carry direct current between points in the DC region of the power system.

## Data Model
  - properties:
    - capacitance:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Capacitance of the DC line segment. Significant for cables only. Default: 0.0
    - inductance:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Inductance of the DC line segment. Neglectable compared with DCSeriesDevice used for smoothing. Default: 0.0
    - resistance:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Resistance of the DC line segment. Default: 0.0
    - length:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Segment length for calculating line section capabilities. Default: 0.0
    - PerLengthParameter:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Set of per-length parameters for this line segment. Default: None
