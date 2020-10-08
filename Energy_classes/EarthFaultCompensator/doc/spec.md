# EarthFaultCompensator
type: "object"
description : >
## Description
A conducting equipment used to represent a connection to ground which is typically used to compensate earth faults..   An earth fault compensator device modeled with a single terminal implies a second terminal solidly connected to ground.  If two terminals are modeled, the ground is not assumed and normal connection rules apply.

## Data Model
  - properties:
    - r:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Nominal resistance of device. Default: 0.0
