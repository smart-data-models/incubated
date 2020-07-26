Airline:
  - required:
    - id
    - type
    - name
    - codeIATA
    - codeICAO
  - type: "object"
    - allOf:
      - $ref: "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/GSMA-Commons"
      - $ref: "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/Location-Commons"
   - description: >
      ## Description
      Airline entity contains a description of a generic airline with the standard parameters used by the airline industry.
      ## Data Model
  - properties:
    - codeIATA:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"
    - codeICAO:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"
    - callsign:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"
      - description: >
         Airline identifier in radio communication
    - name:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"
    - alternateName:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"
    - address:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/address"
      - $ref: "https://github.com/smart-data-models/data-models/blob/master/common-schema.md#/Address"