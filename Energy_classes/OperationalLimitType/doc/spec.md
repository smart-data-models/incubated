# OperationalLimitType
type: "object"
description : >
## Description
The operational meaning of a category of limits.

## Data Model
  - properties:
    - OperationalLimit:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The operational limits associated with this type of limit. Default: "list"
    - acceptableDuration:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed. Default: 0
    - limitType:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Types of limits defined in the ENTSO-E Operational Handbook Policy 3. Default: None
    - direction:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The direction of the limit. Default: None
