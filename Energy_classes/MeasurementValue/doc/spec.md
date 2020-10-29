# MeasurementValue
type: "object"
description : >
## Description
The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.

## Data Model
  - properties:
    - timeStamp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The time when the value was last updated Default: ''
    - sensorAccuracy:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions. Default: 0.0
    - MeasurementValueQuality:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : A MeasurementValue has a MeasurementValueQuality associated with it. Default: None
    - MeasurementValueSource:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The MeasurementValues updated by the source. Default: None
