# LinearShuntCompensator
type: "object"
description : >
## Description
A linear shunt compensator has banks or sections with equal admittance values.

## Data Model
  - properties:
    - bPerSection:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Positive sequence shunt (charging) susceptance per section Default: 0.0
    - gPerSection:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Positive sequence shunt (charging) conductance per section Default: 0.0
    - b0PerSection:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Zero sequence shunt (charging) susceptance per section Default: 0.0
    - g0PerSection:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Zero sequence shunt (charging) conductance per section Default: 0.0
