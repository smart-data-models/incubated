# GeographicalRegion
type: "object"
description : >
## Description
A geographical region of a power system network model.

## Data Model
  - properties:
    - Regions:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : All sub-geograhpical regions within this geographical region. Default: "list"
