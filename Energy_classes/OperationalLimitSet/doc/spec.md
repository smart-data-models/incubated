# OperationalLimitSet
type: "object"
description : >
## Description
A set of limits associated with equipment.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain different severities of limit levels that would apply to the same equipment. The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.

## Data Model
  - properties:
    - Terminal:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: :  Default: None
    - Equipment:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The equipment to which the limit set applies. Default: None
    - OperationalLimitValue:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The limit set to which the limit values belong. Default: "list"
