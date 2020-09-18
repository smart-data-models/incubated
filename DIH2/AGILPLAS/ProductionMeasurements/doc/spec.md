ProductionMeasurements
  - required:
    - id
    - type
  - type: "object"
    - allOf:
      - $ref: "https://jason-fox.github.io/swagger-datamodel-test/common.yaml#/Common"
      - $ref: "https://jason-fox.github.io/swagger-datamodel-test/common.yaml#/Movable"
  - description: >
      ## Description
      This entity contains several measurements used to calculate OEE.
      ## Data model
  - properties:
    - plannedTime:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Number"
      - type: "number"
      - description: >
            Total amount of scheduled time during which the machine could have been working.
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
            Amount of time during which the machine has not been working.
    - theoreticalCycleTime:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Number"
      - type: "number"
      - description: >
            The minimum amount of time of a cycle in which the process is expected to take place under optimal circumstances.
    - actualMachineSpeed:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Integer"
      - type: "integer"
      - description: >
            Actual amount of pieces produced per cycle.
    - theoreticalMachineSpeed:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Integer"
      - type: "integer"
      - description: >
            Theoretical amount of pieces produced per cycle.
    - totalProduction:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Integer"
      - type: "integer"
      - description: >
            Total amount of units produced.
    - validProduction:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Integer"
      - type: "integer"
      - description: >
            Total amount of good units produced.
    - defectiveProduction:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Integer"
      - type: "integer"
      - description: >
            Total amount of defective units produced.
