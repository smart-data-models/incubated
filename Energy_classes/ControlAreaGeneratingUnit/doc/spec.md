# ControlAreaGeneratingUnit
type: "object"
description : >
## Description
A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.

## Data Model
  - properties:
    - GeneratingUnit:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once. Default: None
    - ControlArea:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The parent control area for the generating unit specifications. Default: None
