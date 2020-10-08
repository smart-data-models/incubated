# PowerSystemResource
type: "object"
description : >
## Description
A power system resource can be an item of equipment such as a switch, an equipment container containing many individual items of equipment such as a substation, or an organisational entity such as sub-control area. Power system resources can have measurements associated.

## Data Model
  - properties:
    - Controls:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Regulating device governed by this control output. Default: "list"
    - Measurements:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The power system resource that contains the measurement. Default: "list"
    - Location:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Location of this power system resource. Default: None
