# DiscExcContIEEEDEC3A
type: "object"
description : >
## Description
The class represents IEEE Type DEC3A model. In some systems, the stabilizer output is disconnected from the regulator immediately following a severe fault to prevent the stabilizer from competing with action of voltage regulator during the first swing.  Reference: IEEE Standard 421.5-2005 Section 12.4.

## Data Model
  - properties:
    - vtmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Terminal undervoltage comparison level (). Default: 0.0
    - tdr:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Reset time delay (). Default: 0
