# RaiseLowerCommand
type: "object"
description : >
## Description
An analog control that increase or decrease a set point value with pulses.

## Data Model
  - properties:
    - ValueAliasSet:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The ValueAliasSet used for translation of a Control value to a name. Default: None
