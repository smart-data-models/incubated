# PerLengthDCLineParameter
type: "object"
description : >
## Description


## Data Model
  - properties:
    - DCLineSegments:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : All line segments described by this set of per-length parameters. Default: "list"
    - capacitance:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Capacitance per unit of length of the DC line segment; significant for cables only. Default: 0.0
    - inductance:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Inductance per unit of length of the DC line segment. Default: 0.0
    - resistance:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Resistance per length of the DC line segment. Default: 0.0
