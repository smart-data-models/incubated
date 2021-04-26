OEEMetric
  - required:
    - id
    - type
    - createdTime
    - goodProductCount
    - productionBreakDuration
    - productionIdealDuration
  - type: "object"
    - allOf:
      - $ref: "https://github.com/ts-exsensio/DataModel/common-schema.json#/definitions/EntityIdentifierType"
      - $ref: "https://github.com/ts-exsensio/DataModel/common-schema.json#/definitions/TimeSpan"
  - description: >
      ## Description
      This entity contains several measurements used to calculate the [overall equipment effectiveness (OEE)](https://www.oee.com/).
      More information on OEE and how the calculation is performed can be found [here](https://www.oee.com/calculating-oee.html).
      ## Data model
  - properties:
    - createdTime:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/DateTime"
      - type: "dateCreated"
      - description: >
            Date when the record was created in ISO 8601 format.
    - goodProductCount:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Integer"
      - type: "integer"
      - description: >
            Produced parts that meet quality standards (without rework). The quantity of Good Parts is referred to as Good Count which is used to calculate OEE Quality.
    - productionBreakDuration:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "text"
      - description: >
            Unproductive time where the process is scheduled not to run because the crew is scheduled to be away from the line. Breaks are typically excluded from OEE calculations.
    - productionIdealDuration
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "text"
      - description: >
            Theoretical minimum time to produce one part. The inverse of Ideal Run Rate. Used to calculate OEE Performance. A variation of the calculation uses Ideal Run Rate instead.
