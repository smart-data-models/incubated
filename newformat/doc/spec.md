Weather Observed:
  - required:
    - id
    - type
    - dateObserved
    - location
  - type: "object"
    - allOf:
      - $ref: "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/GSMA-Commons"
      - $ref: "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/Location-Commons"
      - $ref: "https://smart-data-models.github.io/dataModel.Weather/weather-schema.json#/definitions/Weather-Commons"  
   - description: >
      ## Description
      An observation of weather conditions at a certain place and time. This data model has been developed 
      in cooperation with mobile operators and the [GSMA](https://www.gsma.com/iot/iot-big-data/).
        
      ## Data Model
  - properties:  
    - dataProvider:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
        - format: "URL"
      - description: >
        Specifies the URL to information about the provider of this information
    - name:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - $ref: "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/GSMA-Commons/name"
    - location:
      - x-ngsi:
        - type: "Property"
        - model: "https://tools.ietf.org/html/rfc7946"
      - $ref: "https://smart-data-models.github.io/data-modelscommon-schema.json#/Location-Commons/location"
    - address:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/address"
      - $ref: "https://smart-data-models.github.io/data-modelscommon-schema.json#/Location-Commons/address"
    - dateObserved:
        - type: "Property"
        - model: "https://schema.org/DateTime"
       - type: "string"
         - format : "date-time"
    - source:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text", "https://schema.org/URL"
      - type: "string"
      - description: >
            A sequence of characters giving the source of the entity data.     
    - refDevice:
      - x-ngsi:
       - type: "Relationship"
      - type: "string"
        - format: "URL"
      - description: >
            A reference to the device(s) which captured this observation.    
     - refPointOfInterest:
      - x-ngsi:
       - type: "Relationship"
      - type: "string"
        - format: "URL"
      - description: >
            A reference to a point of interest (usually a weather station) associated to this observation.
    - weatherType: 
     - x-ngsi:
       - type: "Property"
     - type: array
       - items: 
         - type: string
         - enum:
           - clearNight
           - cloudy
           - drizzle
           - fog
           - hail
           - hailShower
           - heavyRain
           - heavyRainShower
           - heavySnowShower
           - heavySnow
           - highClouds
           - lightRain
           - lightRainShower
           - lightSnow
           - mist
           - overcast
           - partlyCloudy
           - sleet
           - sleetShower
           - slightlyCloudy
           - shower
           - snow
           - sunnyDay
           - thunderShower
           - thunder
           - veryCloudy
       - description: >
         The observed weather type. It is represented by a comma
         separated list of weather statuses, for instance `overcast, lightRain`
     - dewPoint:
       - x-ngsi:
         - type: "Property"
         - model: "https://schema.org/Number"
       - type:Number
       - description:  The dew point encoded as a number. Celsius degrees. 
     - visibility: 
       - x-ngsi:
         - type: "Property"
       - type: string
         - enum: 
           - excellent
           - good
           - moderate
           - poor
           - veryGood
           - veryPoor
     - temperature:
       - x-ngsi:
         - type: "Property"
         - model: "https://schema.org/Number"
       - type:Number
       - description:  Air's temperature observed. Celsius degrees. 
     - relativeHumidity:
       - x-ngsi:
         - type: "Property"
         - model: "https://schema.org/Number"
       - type:Number
         - minimum: 0
         - maximum: 1
       - description:  Air's relative humidity observed (percentage, expressed
         in parts per one).  
      - precipitation:
       - x-ngsi:
         - type: "Property"
         - model: "https://schema.org/Number"
       - type:Number
       - description:  Air's temperature observed. Liters per square meter. 
     - windDirection:
       - x-ngsi:
         - type: "Property"
         - model: "https://schema.org/Number"
       - type:Number
         - minimum: 0
         - maximum: 360
       - description:  The wind direction expressed in decimal degrees compared
         to geographic North (measured clockwise), encoded as a Number.
     - windSpeed:
       - x-ngsi:
         - type: "Property"
         - model: "https://schema.org/Number"
       - type:Number
         - minimum: 0
       - description:  The observed wind speed in m/s, encoded as a Number.  
     - atmosphericPressure:
       - x-ngsi:
         - type: "Property"
         - model: "https://schema.org/Number"
       - type:Number
         - minimum: 0
       - description: The atmospheric pressure observed measured in Hecto
         Pascals.
     - pressureTendency: 
       - x-ngsi:
         - type: "Property"
       - type: string
         - enum: 
           - falling
           - raising
           - steady
       - description: Is the pressure rising or falling? It can be expressed
         in quantitative terms or qualitative terms.
     - solarRadiation:
       - x-ngsi:
         - type: "Property"
         - model: "https://schema.org/Number"
       - type:Number
         - minimum: 0
       - description: The solar radiation observed measured in Watts per square
         meter.
     - illuminance:
       - x-ngsi:
         - type: "Property"
         - model: "https://schema.org/Number"
       - type:Number
         - minimum: 0
       - description: (https://en.wikipedia.org/wiki/Illuminance) observed measured
         in lux (lx) or lumens per square metre (cd·sr·m−2).
     - streamGauge:
       - x-ngsi:
         - type: "Property"
         - model: "https://schema.org/Number"
       - type:Number
         - minimum: 0
       - description: The water level surface elevation observed by Hydrometric
         measurement sensors, namely a [Stream Gauge](https://en.wikipedia.org/wiki/Stream_gauge),
         expressed in centimeters.
     - snowHeight:
       - x-ngsi:
         - type: "Property"
         - model: "https://schema.org/Number"
       - type:Number
         - minimum: 0
       - description: The snow height observed by generic snow depth measurement
         sensors, expressed in centimeters    
     - uVIndexMax:
       - x-ngsi:
         - type: "Property"
         - model: "https://schema.org/Number"
       - type:Number
         - minimum: 0
       - description: The maximum UV index for the period, based on the World
    Health Organization's UV Index measure. [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/)