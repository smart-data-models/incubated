# NonlinearShuntCompensator
type: "object"
description : >
## Description
A non linear shunt compensator has bank or section admittance values that differs.

## Data Model
  - properties:
    - NonlinearShuntCompensatorPoints:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : All points of the non-linear shunt compensator. Default: "list"
