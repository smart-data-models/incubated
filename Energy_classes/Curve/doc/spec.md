# Curve
type: "object"
description : >
## Description
A multi-purpose curve or functional relationship between an independent variable (X-axis) and dependent (Y-axis) variables.

## Data Model
  - properties:
    - curveStyle:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The style or shape of the curve. Default: None
    - xUnit:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The X-axis units of measure. Default: None
    - y1Unit:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The Y1-axis units of measure. Default: None
    - y2Unit:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The Y2-axis units of measure. Default: None
    - CurveDatas:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The curve of  this curve data point. Default: "list"
