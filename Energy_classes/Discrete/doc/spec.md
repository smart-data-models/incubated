# Discrete
type: "object"
description : >
## Description
Discrete represents a discrete Measurement, i.e. a Measurement representing discrete values, e.g. a Breaker position.

## Data Model
  - properties:
    - DiscreteValues:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Measurement to which this value is connected. Default: "list"
    - ValueAliasSet:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The ValueAliasSet used for translation of a MeasurementValue.value to a name. Default: None
