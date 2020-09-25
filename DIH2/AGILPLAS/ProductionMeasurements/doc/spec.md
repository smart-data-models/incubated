ProductionMeasurements
  - required:
    - id
    - type
  - type: "object"
    - allOf:
      - $ref: "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/GSMA-Commons"
      - $ref: "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/Location-Commons"
  - description: >
      ## Description
      This entity contains several measurements used to calculate the [overall equipment effectiveness (OEE)](https://www.oee.com/).
      More information on OEE and how the calculation is performed can be found [here](https://www.oee.com/calculating-oee.html).
      ## Data model
  - properties:
    - plannedProductionTime:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Number"
      - type: "number"
      - description: >
            Total amount of time that the machine is expected to produce.
    - operatingTime:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Number"
      - type: "number"
      - description: >
            Actual amount of operating time of the machine.
    - lostTime:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Number"
      - type: "number"
      - description: >
            Amount of time where the machine was expected to be producing but was not due to planned or unplanned stops.
    - theoreticalCycleTime:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Number"
      - type: "number"
      - description: >
            Theoretical minimum amount of time to produce one piece.
    - theoreticalOutputRate:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Integer"
      - type: "integer"
      - description: >
            Theoretical maximum production rate per unit of time.
    - totalProduction:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Integer"
      - type: "integer"
      - description: >
            Total amount of pieces produced, including the defective ones.
    - validProduction:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Integer"
      - type: "integer"
      - description: >
            Total amount of produced pieces that meet the quality standards.
    - rejectedProduction:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Integer"
      - type: "integer"
      - description: >
            Total amount of defective pieces produced.
