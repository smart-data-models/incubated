# DynamicsFunctionBlock
type: "object"
description : >
## Description
Abstract parent class for all Dynamics function blocks.

## Data Model
  - properties:
    - enabled:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Function block used indicator. true = use of function block is enabled false = use of function block is disabled. Default: False
