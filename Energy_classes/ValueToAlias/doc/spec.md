# ValueToAlias
type: "object"
description : >
## Description
Describes the translation of one particular value into a name, e.g. 1 as "Open".

## Data Model
  - properties:
    - ValueAliasSet:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The ValueToAlias mappings included in the set. Default: None
    - value:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The value that is mapped. Default: 0
