Pen:
  - required:
    - lastUpdate
  - type: "object"
    - allOf:
      - $ref: "https://jason-fox.github.io/swagger-datamodel-test/common.yaml#/Common"
      - $ref: "https://jason-fox.github.io/swagger-datamodel-test/common.yaml#/Movable"  
   - description: >

   - properties:  
    - address:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/address"
      - $ref: "https://github.com/smart-data-models/data-models/blob/master/common-schema.md#/Address"
    - category:
      - x-ngsi:
        - type: "EnumProperty"
      - type: "string"

    - arrivalTimestamp :
      - x-ngsi:
        - type: "Relationship"
        - model: "https://schema.org/URL
