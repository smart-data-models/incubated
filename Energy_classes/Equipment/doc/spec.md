# Equipment
type: "object"
description : >
## Description
The parts of a power system that are physical devices, electronic or mechanical.

## Data Model
  - properties:
    - aggregate:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The single instance of equipment represents multiple pieces of equipment that have been modeled together as an aggregate.  Examples would be power transformers or synchronous machines operating in parallel modeled as a single aggregate power transformer or aggregate synchronous machine.  This is not to be used to indicate equipment that is part of a group of interdependent equipment produced by a network production program. Default: False
    - EquipmentContainer:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Container of this equipment. Default: None
    - OperationalLimitSet:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The operational limit sets associated with this equipment. Default: "list"
