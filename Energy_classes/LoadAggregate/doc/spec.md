# LoadAggregate
type: "object"
description : >
## Description
Standard aggregate load model comprised of static and/or dynamic components.  A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage. A dynamic load model can used to represent the aggregate response of the motor components of the load.

## Data Model
  - properties:
    - LoadStatic:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Aggregate static load associated with this aggregate load. Default: None
    - LoadMotor:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Aggregate motor (dynamic) load associated with this aggregate load. Default: None
