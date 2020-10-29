OEE
  - required:
    - id
    - type
    - OEE
    - refProductionMeasurements
  - type: "object"
    - allOf:
      - $ref: "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/GSMA-Commons"
      - $ref: "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/Location-Commons"
  - description: >
      ## Description
      This entity contains an [overall equipment effectiveness (OEE)](https://www.oee.com/) metric, associated with the production measurements used on its calculation.
      More information on OEE and how the calculation is performed can be found [here](https://www.oee.com/calculating-oee.html).
      ## Data model
  - properties:
    - OEE:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Number"
      - type: "number"
      - description: >
            The overall equipment effectiveness (OEE) metric.
    - refProductionMeasurements:
      - x-ngsi:
        - type: "Property. Reference to a ProductionMeasurements entity"
      - description: >
            Reference to the measurements used to calculate the OEE.
