Station
  - required:
    - id
    - type
    - name
  - type: "object"
    - allOf:
      - $ref: "https://github.com/ts-exsensio/DataModel/common-schema.json#/definitions/EntityIdentifierType"
      - $ref: "https://github.com/ts-exsensio/DataModel/common-schema.json#/definitions/TimeSpan"
  - description: >
      ## Description
      This entity contains station information used as a relationship to product measurements data.
      ## Data model
  - properties:
    - name:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "text"
      - description: >
            Name of the station.