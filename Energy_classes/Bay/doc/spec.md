# Bay
type: "object"
description : >
## Description
A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.  A bay typically represents a physical grouping related to modularization of equipment.

## Data Model
  - properties:
    - VoltageLevel:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The voltage level containing this bay. Default: None
