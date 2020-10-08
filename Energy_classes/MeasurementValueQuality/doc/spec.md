# MeasurementValueQuality
type: "object"
description : >
## Description
Measurement quality flags. Bits 0-10 are defined for substation automation in draft IEC 61850 part 7-3. Bits 11-15 are reserved for future expansion by that document. Bits 16-31 are reserved for EMS applications.

## Data Model
  - properties:
    - MeasurementValue:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : A MeasurementValue has a MeasurementValueQuality associated with it. Default: None
