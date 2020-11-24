Aircraft:
  - required:
    - id
    - type
    - registration
  - type: "object"
    - allOf:
      - $ref: "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/GSMA-Commons"
      - $ref: "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/Location-Commons"
   - description: >
      ## Description
      Aircraft entity contains a description of a generic aircraft with the standard parameters used by the airline industry.
      ## Data Model
  - properties:
    - registration:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"
      - description: Aircraft registration identifier
    - speed:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Number"
      - type: "number"
      - description: Flight speed, expressed in kilometre per hour
    - location:
      - x-ngsi:
        - type: "Property"
        - model: "https://tools.ietf.org/html/rfc7946"
      - $ref: "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/Location-Commons/location"
    - aircraftModel:
      - x-ngsi:
        - type: "Relationship"
      - type: "string"
        - format: "URL"
      - description: A reference to the aircraft model