[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: CoolingTower  
================https://github.com/smart-data-models/incubated/SAREF/
  

[Open License](http://smart-data-models.kmd.dk/flat/s4bldg/CoolingTower/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **A cooling tower is a device which rejects heat to ambient air by circulating a fluid such as water through it to reduce its temperature by partial evaporation.**  

version: 0.0.2  


## List of properties  


- `address`: The mailing address  
- `alternateName`: An alternative name for this item  
- `ambientDesignDryBulbTemperature`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `ambientDesignWetBulbTemperature`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `areaServed`: The geographic area where a service or offered item is provided  
- `basinReserveVolume`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `capacityControl`: FanCycling: Fan is cycled on and off to control duty. TwoSpeedFan: Fan is switched between low and high speed to control duty. VariableSpeedFan: Fan speed is varied to control duty. DampersControl: Dampers modulate the air flow to control duty. BypassValveControl: Bypass valve modulates the water flow to control duty. MultipleSeriesPumps: Turn on/off multiple series pump to control duty. TwoSpeedPump: Switch between high/low pump speed to control duty. VariableSpeedPump: vary pump speed to control duty.  
- `circuitType`: OpenCircuit: Exposes water directly to the cooling atmosphere. CloseCircuit: The fluid is separated from the atmosphere by a heat exchanger. Wet: The air stream or the heat exchange surface is evaporatively cooled. Dry: No evaporation into the air stream. DryWet: A combination of a dry tower and a wet tower.  
- `controlStrategy`: FixedExitingWaterTemp: The capacity is controlled to maintain a fixed exiting water temperature. WetBulbTempReset: The set-point is reset based on the wet-bulb temperature.  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `flowArrangement`: CounterFlow: Air and water flow enter in different directions. CrossFlow: Air and water flow are perpendicular. ParallelFlow: air and water flow enter in same directions.  
- `hasManufacturer`: A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hasModel`: A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `id`: Unique identifier of the entity  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `liftElevationDifference`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `nominalCapacity`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `numberOfCells`: Number of cells in one cooling tower unit.  
- `operationTemperatureMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `operationTemperatureMin`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `sprayType`: SprayFilled: Water is sprayed into airflow. SplashTypeFill: water cascades over successive rows of splash bars. FilmTypeFill: water flows in a thin layer over closely spaced sheets.  
- `type`: It must be equal to `CoolingTower`.  
- `waterRequirement`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
CoolingTower:
    
  description: A cooling tower is a device which rejects heat to ambient air by circulating a fluid such as water through it to reduce its temperature by partial evaporation.
    
  properties:
    
    address:
    
      description: The mailing address
    
      properties:
    
        addressCountry:
    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''
    
          type: string
    
        addressLocality:
    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''
    
          type: string
    
        addressRegion:
    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''
    
          type: string
    
        district:
    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'
    
          type: string
    
        postOfficeBoxNumber:
    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''
    
          type: string
    
        postalCode:
    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''
    
          type: string
    
        streetAddress:
    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''
    
          type: string
    
        streetNr:
    
          description: Number identifying a specific property on a public street.
    
          type: string
    
      type: object
    
      x-ngsi:
    
        model: https://schema.org/address
    
        type: Property
    
    alternateName:
    
      description: An alternative name for this item
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    ambientDesignDryBulbTemperature:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
        observedAt:
    
          description: Property. A relationship stating the timestamp of an entity (e.g. a measurement).
    
          format: date-time
    
          type: string
    
        unitCode:
    
          description: Property. A relationship identifying the unit of measure used for a certain entity.
    
          type: string
    
        value:
    
          description: 'Property. A relationship defining the value of a certain property, e.g., energy or power. Note that, even if numeric values are expected to enable reasoning, measurement values could use other datatypes.'
    
          type: number
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    ambientDesignWetBulbTemperature:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    areaServed:
    
      description: The geographic area where a service or offered item is provided
    
      type: string
    
      x-ngsi:
    
        model: https://schema.org/Text
    
        type: Property
    
    basinReserveVolume:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    capacityControl:
    
      description: 'FanCycling: Fan is cycled on and off to control duty. TwoSpeedFan: Fan is switched between low and high speed to control duty. VariableSpeedFan: Fan speed is varied to control duty. DampersControl: Dampers modulate the air flow to control duty. BypassValveControl: Bypass valve modulates the water flow to control duty. MultipleSeriesPumps: Turn on/off multiple series pump to control duty. TwoSpeedPump: Switch between high/low pump speed to control duty. VariableSpeedPump: vary pump speed to control duty.'
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    circuitType:
    
      description: 'OpenCircuit: Exposes water directly to the cooling atmosphere. CloseCircuit: The fluid is separated from the atmosphere by a heat exchanger. Wet: The air stream or the heat exchange surface is evaporatively cooled. Dry: No evaporation into the air stream. DryWet: A combination of a dry tower and a wet tower.'
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    controlStrategy:
    
      description: 'FixedExitingWaterTemp: The capacity is controlled to maintain a fixed exiting water temperature. WetBulbTempReset: The set-point is reset based on the wet-bulb temperature.'
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    dataProvider:
    
      description: A sequence of characters identifying the provider of the harmonised data entity.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    dateCreated:
    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.
    
      format: date-time
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    dateModified:
    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.
    
      format: date-time
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    description:
    
      description: A description of this item
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    flowArrangement:
    
      description: 'CounterFlow: Air and water flow enter in different directions. CrossFlow: Air and water flow are perpendicular. ParallelFlow: air and water flow enter in same directions.'
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    hasManufacturer:
    
      description: 'A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.'
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    hasModel:
    
      description: 'A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.'
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    id:
    
      anyOf:
    
        - description: Property. Identifier format of any NGSI entity
    
          maxLength: 256
    
          minLength: 1
    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$
    
          type: string
    
        - description: Property. Identifier format of any NGSI entity
    
          format: uri
    
          type: string
    
      description: Unique identifier of the entity
    
      x-ngsi:
    
        type: Property
    
    isContainedInBuildingSpace:
    
      anyOf:
    
      description: Unique identifier of the entity
    
      x-ngsi:
    
        type: Property
    
    isContainedInPhysicalObject:
    
      anyOf:
    
      description: Unique identifier of the entity
    
      x-ngsi:
    
        type: Property
    
    isSubSystemOf:
    
      description: A reference to a system(s) that this Physical Object is part of.
    
      items:
    
        anyOf:
    
        description: Property. Unique identifier of the entity
    
      type: array
    
      x-ngsi:
    
        type: Relationship
    
    liftElevationDifference:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    location:
    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'
    
      oneOf:
    
        - description: Geoproperty. Geojson reference to the item. Point
    
          properties:
    
            bbox:
    
              items:
    
                type: number
    
              minItems: 4
    
              type: array
    
            coordinates:
    https://github.com/smart-data-models/incubated/SAREF/
              items:
    
                type: number
    
              minItems: 2
    
              type: array
    
            type:
    
              enum:
    
                - Point
    
              type: string
    
          required:
    
            - type
    
            - coordinates
    
          title: GeoJSON Point
    
          type: object
    
        - description: Geoproperty. Geojson reference to the item. LineString
    
          properties:
    
            bbox:
    
              items:
    
                type: number
    
              minItems: 4
    
              type: array
    
            coordinates:
    
              items:
    
                items:
    
                  type: number
    
                minItems: 2
    
                type: array
    
              minItems: 2
    
              type: array
    
            type:
    
              enum:
    
                - LineString
    
              type: string
    
          required:
    
            - type
    
            - coordinates
    
          title: GeoJSON LineString
    
          type: object
    
        - description: Geoproperty. Geojson reference to the item. Polygon
    
          properties:
    
            bbox:
    
              items:
    
                type: number
    
              minItems: 4
    
              type: array
    
            coordinates:
    
              items:
    
                items:
    
                  items:
    
                    type: number
    
                  minItems: 2
    
                  type: array
    
                minItems: 4
    
                type: array
    
              type: array
    
            type:
    
              enum:
    
                - Polygon
    
              type: string
    
          required:
    
            - type
    
            - coordinates
    
          title: GeoJSON Polygon
    
          type: object
    
        - description: Geoproperty. Geojson reference to the item. MultiPoint
    
          properties:
    
            bbox:
    
              items:
    
                type: number
    
              minItems: 4
    
              type: array
    
            coordinates:
    
              items:
    
                items:
    
                  type: number
    
                minItems: 2
    
                type: array
    
              type: array
    
            type:
    
              enum:
    
                - MultiPoint
    
              type: string
    
          required:
    
            - type
    
            - coordinates
    
          title: GeoJSON MultiPoint
    
          type: object
    
        - description: Geoproperty. Geojson reference to the item. MultiLineString
    
          properties:
    
            bbox:
    
              items:
    
                type: number
    
              minItems: 4
    
              type: array
    
            coordinates:
    
              items:
    
                items:
    
                  items:
    
                    type: number
    
                  minItems: 2
    
                  type: array
    
                minItems: 2
    
                type: array
    
              type: array
    
            type:
    
              enum:
    
                - MultiLineString
    
              type: string
    
          required:
    
            - type
    
            - coordinates
    
          title: GeoJSON MultiLineString
    
          type: object
    
        - description: Geoproperty. Geojson reference to the item. MultiLineString
    
          properties:
    
            bbox:
    
              items:
    
                type: number
    
              minItems: 4
    
              type: array
    
            coordinates:
    
              items:
    
                items:
    
                  items:
    
                    items:
    
                      type: number
    
                    minItems: 2
    
                    type: array
    
                  minItems: 4
    
                  type: array
    
                type: array
    
              type: array
    
            type:
    
              enum:
    
                - MultiPolygon
    
              type: string
    
          required:
    
            - type
    
            - coordinates
    
          title: GeoJSON MultiPolygon
    
          type: object
    
      x-ngsi:
    
        type: Geoproperty
    
    name:
    
      description: The name of this item.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    nominalCapacity:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    numberOfCells:
    
      description: Number of cells in one cooling tower unit.
    
      type: number
    
      x-ngsi:
    
        type: Property
    
    operationTemperatureMax:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    operationTemperatureMin:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    owner:
    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)
    
      items:
    
        anyOf:
    
        description: Property. Unique identifier of the entity
    
      type: array
    
      x-ngsi:
    
        type: Property
    
    seeAlso:
    
      description: list of uri pointing to additional resources about the item
    
      oneOf:
    
        - items:
    
            format: uri
    
            type: string
    
          minItems: 1
    
          type: array
    
        - format: uri
    
          type: string
    
      x-ngsi:
    
        type: Property
    
    source:
    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    sprayType:
    
      description: 'SprayFilled: Water is sprayed into airflow. SplashTypeFill: water cascades over successive rows of splash bars. FilmTypeFill: water flows in a thin layer over closely spaced sheets.'
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    type:
    
      description: It must be equal to `CoolingTower`.
    
      enum:
    
        - CoolingTower
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    waterRequirement:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
  required:
    
    - id
    
    - type
    
  type: object
    
  x-derived-from: ""
    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'
    
  x-license-url: http://smart-data-models.kmd.dk/flat/s4bldg/CoolingTower/LICENSE.md
    
  x-model-schema: http://smart-data-models.kmd.dk/CoolingTowers/CoolingTower
    
  x-model-tags: SAREF CoolingTower SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### CoolingTower NGSI-v2 key-values Example    

Here is an example of a CoolingTower in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:CoolingTower:c628d24d-5b25-4b99-838e-35676956d307",
  
  "type": "CoolingTower",
  
  "ambientDesignDryBulbTemperature": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T20:47:51Z",
  
      "value": 0.7275209381168831
  
    }
  
  },
  
  "ambientDesignWetBulbTemperature": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T11:05:35Z",
  
      "value": 0.8419497776651206
  
    }
  
  },
  
  "basinReserveVolume": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3",
  
      "observedAt": "2023-01-26T04:46:46Z",
  
      "value": 0.9886525691530367
  
    }
  
  },
  
  "capacityControl": "Lead",
  
  "circuitType": "virtual",
  
  "controlStrategy": "Harbors",
  
  "flowArrangement": "Extensions",
  
  "liftElevationDifference": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T21:14:37Z",
  
      "value": 0.9337996577856725
  
    }
  
  },
  
  "nominalCapacity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-25T22:06:57Z",
  
      "value": 0.8043496896372141
  
    }
  
  },
  
  "numberOfCells": 0.03361385186991317,
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T02:09:02Z",
  
      "value": 0.7125610456321683
  
    }
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T20:02:00Z",
  
      "value": 0.3015974804386986
  
    }
  
  },
  
  "sprayType": "programming",
  
  "waterRequirement": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-25T18:26:38Z",
  
      "value": 0.1817597423361893
  
    }
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:6871b1ec-cfce-4a60-83c2-9f07b13d1703",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:e2a48930-276e-4972-9283-82fbc22faf85",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:aea47887-bc5b-47c3-aeb0-870506d76580",
  
    "urn:ngsi-ld:System:2791b628-8fc1-4ec1-91a7-26efbbc892a3",
  
    "urn:ngsi-ld:System:c0623c49-ae1f-4772-9323-a94078dbdb86"
  
  ],
  
  "hasManufacturer": "CoolingTower Company Inc.",
  
  "hasModel": "CoolingTower 0.1.2",
  
  "dateCreated": "2023-01-26T12:17:43Z",
  
  "dateModified": "2023-01-25T16:13:00Z",
  
  "source": "Import",
  
  "name": "CoolingTower",
  
  "alternateName": "CoolingTower type 2",
  
  "description": "CoolingTower of limited CoolingTower types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### CoolingTower NGSI-v2 normalized Example    

Here is an example of a CoolingTower in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:CoolingTower:7995c5cf-c8c3-4e42-92db-6dd840796eae",
  
  "type": "CoolingTower",
  
  "ambientDesignDryBulbTemperature": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T07:40:19Z",
  
      "value": 0.36789185492213194
  
    }
  
  },
  
  "ambientDesignWetBulbTemperature": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T19:11:41Z",
  
      "value": 0.1490037569659941
  
    }
  
  },
  
  "basinReserveVolume": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3",
  
      "observedAt": "2023-01-25T14:48:53Z",
  
      "value": 0.9142388286093716
  
    }
  
  },
  
  "capacityControl": {
  
    "type": "Text",
  
    "value": "next-generation"
  
  },
  
  "circuitType": {
  
    "type": "Text",
  
    "value": "morph"
  
  },
  
  "controlStrategy": {
  
    "type": "Text",
  
    "value": "Concrete"
  
  },
  
  "flowArrangement": {
  
    "type": "Text",
  
    "value": "access"
  
  },
  
  "liftElevationDifference": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T09:39:09Z",
  
      "value": 0.6134421322995507
  
    }
  
  },
  
  "nominalCapacity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-26T05:03:06Z",
  
      "value": 0.14285208313177855
  
    }
  
  },
  
  "numberOfCells": {
  
    "type": "Float",
  
    "value": 0.9307947920697038
  
  },
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T18:14:22Z",
  
      "value": 0.33271163839338236
  
    }
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T09:07:51Z",
  
      "value": 0.8346930607066967
  
    }
  
  },
  
  "sprayType": {
  
    "type": "Text",
  
    "value": "synthesizing"
  
  },
  
  "waterRequirement": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-25T15:22:56Z",
  
      "value": 0.6749365729986966
  
    }
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:e1c9dc03-9887-49df-9577-a24218339c39"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:d6e1c0cc-a656-4343-8572-21de93d365ba"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:972d1b4b-ab6d-474c-a742-c75822d6c7b8"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:8c7d509c-66b4-4504-ad2e-d7ec82146ba2"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:42d552ca-9fdd-4838-804e-41f34d6f61f7"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "CoolingTower Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "CoolingTower 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T21:28:15.4871264+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T13:03:39.0857574+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "CoolingTower"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "CoolingTower type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "CoolingTower of limited CoolingTower types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### CoolingTower NGSI-LD key-values Example    

Here is an example of a CoolingTower in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:CoolingTower:42305ac9-82b6-48fb-a540-87dbc3567c22",
  
  "type": "CoolingTower",
  
  "ambientDesignDryBulbTemperature": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T18:51:47Z",
  
    "value": 0.5890652985721293
  
  },
  
  "ambientDesignWetBulbTemperature": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T23:04:21Z",
  
    "value": 0.9076620781761984
  
  },
  
  "basinReserveVolume": {
  
    "type": "Measurement",
  
    "unitCode": "m3",
  
    "observedAt": "2023-01-26T03:15:22Z",
  
    "value": 0.6741001627186924
  
  },
  
  "capacityControl": "Yen",
  
  "circuitType": "Dale",
  
  "controlStrategy": "Director",
  
  "flowArrangement": "Handmade Soft Gloves",
  
  "liftElevationDifference": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T19:23:48Z",
  
    "value": 0.5728618928743563
  
  },
  
  "nominalCapacity": {
  
    "type": "Measurement",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-25T18:23:34Z",
  
    "value": 0.16091934885340586
  
  },
  
  "numberOfCells": 0.8147015333959876,
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T05:29:06Z",
  
    "value": 0.06861236793353775
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T09:07:37Z",
  
    "value": 0.9177498939432773
  
  },
  
  "sprayType": "invoice",
  
  "waterRequirement": {
  
    "type": "Measurement",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-25T14:32:23Z",
  
    "value": 0.19911600465349444
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:3c7df09d-3c54-479c-80fb-e11bbe82a8e1",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:01544e49-cc22-4258-a857-7a48ce0bdcad",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:57b523f8-dd75-46d7-843e-e1afb96b3964",
  
    "urn:ngsi-ld:System:3e6b8398-a786-4006-8ada-dd5b76ef392e",
  
    "urn:ngsi-ld:System:cdcdb557-53e2-48f7-8288-43224cc2cc8d"
  
  ],
  
  "hasManufacturer": "CoolingTower Company Inc.",
  
  "hasModel": "CoolingTower 0.1.2",
  
  "dateCreated": "2023-01-26T12:23:09Z",
  
  "dateModified": "2023-01-26T12:30:54Z",
  
  "source": "Import",
  
  "name": "CoolingTower",
  
  "alternateName": "CoolingTower type 2",
  
  "description": "CoolingTower of limited CoolingTower types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://smartdatamodels.blob.core.windows.net/models/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### CoolingTower NGSI-LD normalized Example    

Here is an example of a CoolingTower in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:CoolingTower:eb831bd2-82be-42c3-a0c9-a6c0a231e316",
  
  "type": "CoolingTower",
  
  "ambientDesignDryBulbTemperature": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T08:09:09Z",
  
    "value": 0.9762464796853121
  
  },
  
  "ambientDesignWetBulbTemperature": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T14:29:40Z",
  
    "value": 0.3062794162138128
  
  },
  
  "basinReserveVolume": {
  
    "type": "Property",
  
    "unitCode": "m3",
  
    "observedAt": "2023-01-26T01:28:50Z",
  
    "value": 0.9472477891325785
  
  },
  
  "capacityControl": {
  
    "type": "Property",
  
    "value": "input"
  
  },
  
  "circuitType": {
  
    "type": "Property",
  
    "value": "Mauritania"
  
  },
  
  "controlStrategy": {
  
    "type": "Property",
  
    "value": "Investor"
  
  },
  
  "flowArrangement": {
  
    "type": "Property",
  
    "value": "Direct"
  
  },
  
  "liftElevationDifference": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T02:02:47Z",
  
    "value": 0.36539365901818843
  
  },
  
  "nominalCapacity": {
  
    "type": "Property",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-25T22:40:21Z",
  
    "value": 0.3624642546775261
  
  },
  
  "numberOfCells": {
  
    "type": "Property",
  
    "value": 0.5588013730579288
  
  },
  
  "operationTemperatureMax": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T23:30:50Z",
  
    "value": 0.660338038211496
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T23:56:27Z",
  
    "value": 0.0877235060077185
  
  },
  
  "sprayType": {
  
    "type": "Property",
  
    "value": "Money Market Account"
  
  },
  
  "waterRequirement": {
  
    "type": "Property",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-25T16:48:25Z",
  
    "value": 0.40722633971933253
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:61ad4f84-a577-49d5-a088-aa301efa4ec6"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:f02a5bc4-2f87-4ff7-8dd7-fb61243128a1"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:b9323186-933c-46fd-815f-7f025b04ca80"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:1cea31ba-2978-4af2-b717-5c2a98a431b4"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:13dbe647-863b-4b1f-b10c-1737310d7c51"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "CoolingTower Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "CoolingTower 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-25T23:05:59Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-25T18:47:19Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "CoolingTower"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "CoolingTower type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "CoolingTower of limited CoolingTower types"
  
  },
  
  "dataProvider": {
  
    "type": "Property",
  
    "value": "IFC file"
  
  },
  
  "@context": [
  
    "https://smartdatamodels.blob.core.windows.net/models/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
