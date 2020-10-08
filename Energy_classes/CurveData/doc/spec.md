# CurveData
type: "object"
description : >
## Description
Multi-purpose data points for defining a curve.  The use of this generic class is discouraged if a more specific class  can be used to specify the x and y axis values along with their specific data types.

## Data Model
  - properties:
    - Curve:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The point data values that define this curve. Default: None
    - xvalue:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The data value of the X-axis variable,  depending on the X-axis units. Default: 0.0
    - y1value:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The data value of the  first Y-axis variable, depending on the Y-axis units. Default: 0.0
    - y2value:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The data value of the second Y-axis variable (if present), depending on the Y-axis units. Default: 0.0
