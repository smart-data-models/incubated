# VsCapabilityCurve
type: "object"
description : >
## Description
The P-Q capability curve for a voltage source converter, with P on x-axis and Qmin and Qmax on y1-axis and y2-axis.

## Data Model
  - properties:
    - VsConverterDCSides:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Capability curve of this converter. Default: "list"
