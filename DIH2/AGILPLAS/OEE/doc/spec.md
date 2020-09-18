OEE
  - required:
    - id
    - type
    - OEE
    - refProductionMeasurements
  - type: "object"
    - allOf:
      - $ref: "https://jason-fox.github.io/swagger-datamodel-test/common.yaml#/Common"
      - $ref: "https://jason-fox.github.io/swagger-datamodel-test/common.yaml#/Movable"
  - description: >
      ## Description
      This entity contains an OEE metric, associated with the production measurements used on its calculation.
      ## Data model
  - properties:
    - OEE:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Number"
      - type: "number"
      - description: >
            The overall equipment effectiveness (OEE) metric
    - refProductionMeasurements:
      - x-ngsi:
        - type: "Property. Reference to a ProductionMeasurements entity"
      - description: >
            Reference to the measurements used to calculate the OEE.
