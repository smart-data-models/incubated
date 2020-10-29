# LimitSet
type: "object"
description : >
## Description
Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.

## Data Model
  - properties:
    - isPercentageLimits:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls. Default: False
