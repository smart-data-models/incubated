[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: Fan  
===========https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](http://smart-data-models.kmd.dk/flat/s4bldg/Fan/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **A fan is a device which imparts mechanical work on a gas. A typical usage of a fan is to induce airflow in a building services air distribution system.**  

version: 0.0.2  


## List of properties  


- `address`: The mailing address  
- `alternateName`: An alternative name for this item  
- `areaServed`: The geographic area where a service or offered item is provided  
- `capacityControlType`: InletVane: Control by adjusting inlet vane. VariableSpeedDrive: Control by variable speed drive. BladePitchAngle: Control by adjusting blade pitch angle. TwoSpeed: Control by switch between high and low speed. DischargeDamper: Control by modulating discharge damper.  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `hasManufacturer`: A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hasModel`: A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `id`: Unique identifier of the entity  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `motorDriveType`: Motor drive type: DIRECTDRIVE: Direct drive. BELTDRIVE: Belt drive. COUPLING: Coupling. OTHER: Other type of motor drive. UNKNOWN: Unknown motor drive type.   
- `name`: The name of this item.  
- `nominalAirFlowRate`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalPowerRate`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalRotationSpeed`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalStaticPressure`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalTotalPressure`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `operationMode`: Operation mode of this fan.  
- `operationTemperatureMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `operationTemperatureMin`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `operationalRiterial`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type`: It must be equal to `Fan`.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
Fan:
    
  description: A fan is a device which imparts mechanical work on a gas. A typical usage of a fan is to induce airflow in a building services air distribution system.
    
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
    
    areaServed:
    
      description: The geographic area where a service or offered item is provided
    
      type: string
    
      x-ngsi:
    
        model: https://schema.org/Text
    
        type: Property
    
    capacityControlType:
    
      description: 'InletVane: Control by adjusting inlet vane. VariableSpeedDrive: Control by variable speed drive. BladePitchAngle: Control by adjusting blade pitch angle. TwoSpeed: Control by switch between high and low speed. DischargeDamper: Control by modulating discharge damper.'
    
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
    
                thttps://github.com/smart-data-models/incubated/tree/master/SAREF/
    
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
    
    motorDriveType:
    
      description: 'Motor drive type: DIRECTDRIVE: Direct drive. BELTDRIVE: Belt drive. COUPLING: Coupling. OTHER: Other type of motor drive. UNKNOWN: Unknown motor drive type. '
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    name:
    
      description: The name of this item.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    nominalAirFlowRate:
    
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
    
    nominalPowerRate:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalRotationSpeed:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalStaticPressure:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalTotalPressure:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    operationMode:
    
      description: Operation mode of this fan.
    
      enum:
    
        - supply
    
        - exhaust
    
      type: string
    
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
    
    operationalRiterial:
    
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
    
    type:
    
      description: It must be equal to `Fan`.
    
      enum:
    
        - Fan
    
      type: string
    
      x-ngsi:
    
        type: Property
    
  required:
    
    - id
    
    - type
    
  type: object
    
  x-derived-from: ""
    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'
    
  x-license-url: http://smart-data-models.kmd.dk/flat/s4bldg/Fan/LICENSE.md
    
  x-model-schema: http://smart-data-models.kmd.dk/Fans/Fan
    
  x-model-tags: SAREF Fan SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### Fan NGSI-v2 key-values Example    

Here is an example of a Fan in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Fan:7cfafc6e-ab2a-4af0-94b0-d4ed9c92e2d9",
  
  "type": "Fan",
  
  "capacityControlType": "e-markets",
  
  "motorDriveType": "gold",
  
  "nominalAirFlowRate": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-25T20:49:08Z",
  
      "value": 0.5484285000109488
  
    }
  
  },
  
  "nominalPowerRate": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-26T01:40:13Z",
  
      "value": 0.4651302623864956
  
    }
  
  },
  
  "nominalRotationSpeed": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "cycles/s",
  
      "observedAt": "2023-01-25T19:12:35Z",
  
      "value": 0.586889938002957
  
    }
  
  },
  
  "nominalStaticPressure": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-25T15:31:18Z",
  
      "value": 0.3508757713471129
  
    }
  
  },
  
  "nominalTotalPressure": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-25T21:25:00Z",
  
      "value": 0.7008373891464377
  
    }
  
  },
  
  "operationalRiterial": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "time",
  
      "observedAt": "2023-01-26T03:58:20Z",
  
      "value": 0.3901575132094196
  
    }
  
  },
  
  "operationMode": "supply",
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T13:04:35Z",
  
      "value": 0.9178812499585061
  
    }
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T09:52:47Z",
  
      "value": 0.5225885446624712
  
    }
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:38fc3969-81c7-4c67-a564-fdbe6353726a",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:722ffa89-4091-423f-832c-3af82a48d406",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:624b2008-bd0a-4bf6-98bd-a8fc2979af6b",
  
    "urn:ngsi-ld:System:4096cc3a-d7c0-4491-b5e1-a0b97a8db924",
  
    "urn:ngsi-ld:System:0dd0f326-6f31-4676-8996-7c591e57a81f"
  
  ],
  
  "hasManufacturer": "Fan Company Inc.",
  
  "hasModel": "Fan 0.1.2",
  
  "dateCreated": "2023-01-26T11:05:33Z",
  
  "dateModified": "2023-01-26T13:15:57Z",
  
  "source": "Import",
  
  "name": "Fan",
  
  "alternateName": "Fan type 2",
  
  "description": "Fan of limited Fan types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### Fan NGSI-v2 normalized Example    

Here is an example of a Fan in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Fan:0da82317-969a-4395-8eb2-f98b9cd16de8",
  
  "type": "Fan",
  
  "capacityControlType": {
  
    "type": "Text",
  
    "value": "solutions"
  
  },
  
  "motorDriveType": {
  
    "type": "Text",
  
    "value": "hard drive"
  
  },
  
  "nominalAirFlowRate": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-26T05:09:22Z",
  
      "value": 0.3551507592337234
  
    }
  
  },
  
  "nominalPowerRate": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-26T01:35:41Z",
  
      "value": 0.49309444253514245
  
    }
  
  },
  
  "nominalRotationSpeed": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "cycles/s",
  
      "observedAt": "2023-01-26T13:36:08Z",
  
      "value": 0.07199495596164263
  
    }
  
  },
  
  "nominalStaticPressure": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-26T10:59:49Z",
  
      "value": 0.024615829657942068
  
    }
  
  },
  
  "nominalTotalPressure": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-25T18:31:01Z",
  
      "value": 0.3030820859504
  
    }
  
  },
  
  "operationalRiterial": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "time",
  
      "observedAt": "2023-01-25T15:00:30Z",
  
      "value": 0.21730931831819922
  
    }
  
  },
  
  "operationMode": {
  
    "type": "FanOperationMode",
  
    "value": "supply"
  
  },
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T19:02:11Z",
  
      "value": 0.6593703010837063
  
    }
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T06:46:04Z",
  
      "value": 0.23220611636698574
  
    }
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:179a46d2-4adc-49bc-81ad-55bf8d570c04"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:1324382c-8a0d-4481-b501-20ced593647d"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:7bb675a4-c933-494f-9e7a-1ad7777c40c3"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:2122d54b-df0b-490a-8d2c-9611433a6950"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:bb112446-5445-482a-aacc-ca87dc610bd5"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "Fan Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "Fan 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T01:05:02.0601436+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T15:45:36.2919235+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "Fan"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "Fan type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "Fan of limited Fan types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### Fan NGSI-LD key-values Example    

Here is an example of a Fan in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Fan:61cb9cb0-7073-4776-a2ec-0668b9a2468f",
  
  "type": "Fan",
  
  "capacityControlType": "Associate",
  
  "motorDriveType": "web-enabled",
  
  "nominalAirFlowRate": {
  
    "type": "Measurement",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-26T05:02:42Z",
  
    "value": 0.5265305819359596
  
  },
  
  "nominalPowerRate": {
  
    "type": "Measurement",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-25T18:06:00Z",
  
    "value": 0.8169941167407072
  
  },
  
  "nominalRotationSpeed": {
  
    "type": "Measurement",
  
    "unitCode": "cycles/s",
  
    "observedAt": "2023-01-25T16:40:42Z",
  
    "value": 0.6794056510336206
  
  },
  
  "nominalStaticPressure": {
  
    "type": "Measurement",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T04:17:40Z",
  
    "value": 0.2715550432429147
  
  },
  
  "nominalTotalPressure": {
  
    "type": "Measurement",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-25T23:01:41Z",
  
    "value": 0.033987433019642466
  
  },
  
  "operationalRiterial": {
  
    "type": "Measurement",
  
    "unitCode": "time",
  
    "observedAt": "2023-01-26T09:52:18Z",
  
    "value": 0.9840792192910335
  
  },
  
  "operationMode": "exhaust",
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T09:44:13Z",
  
    "value": 0.7504321388364997
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T05:24:26Z",
  
    "value": 0.5963228399642907
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:61fea75c-4925-4949-9afa-47164b4cd0bf",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:fcacb3ea-eaec-4793-8b65-cc438033e464",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:f3bf7e75-1cc2-4961-891f-c16a84c284d9",
  
    "urn:ngsi-ld:System:0b21e702-dc19-453f-8b97-2c9f97e4ebbf",
  
    "urn:ngsi-ld:System:0ff1b2ab-8a47-4cbb-a968-33670e3ccc3a"
  
  ],
  
  "hasManufacturer": "Fan Company Inc.",
  
  "hasModel": "Fan 0.1.2",
  
  "dateCreated": "2023-01-26T02:08:20Z",
  
  "dateModified": "2023-01-26T06:51:57Z",
  
  "source": "Import",
  
  "name": "Fan",
  
  "alternateName": "Fan type 2",
  
  "description": "Fan of limited Fan types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### Fan NGSI-LD normalized Example    

Here is an example of a Fan in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Fan:77858a3b-1931-4dba-a9af-2eb53daaa2ba",
  
  "type": "Fan",
  
  "capacityControlType": {
  
    "type": "Property",
  
    "value": "Jamaica"
  
  },
  
  "motorDriveType": {
  
    "type": "Property",
  
    "value": "Handmade Rubber Pants"
  
  },
  
  "nominalAirFlowRate": {
  
    "type": "Property",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-25T20:05:36Z",
  
    "value": 0.24193379349820043
  
  },
  
  "nominalPowerRate": {
  
    "type": "Property",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-26T00:02:52Z",
  
    "value": 0.9909189253853895
  
  },
  
  "nominalRotationSpeed": {
  
    "type": "Property",
  
    "unitCode": "cycles/s",
  
    "observedAt": "2023-01-25T18:57:22Z",
  
    "value": 0.31786177757080614
  
  },
  
  "nominalStaticPressure": {
  
    "type": "Property",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-25T20:44:04Z",
  
    "value": 0.9226814968179932
  
  },
  
  "nominalTotalPressure": {
  
    "type": "Property",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T08:36:40Z",
  
    "value": 0.7120424039244743
  
  },
  
  "operationalRiterial": {
  
    "type": "Property",
  
    "unitCode": "time",
  
    "observedAt": "2023-01-25T22:23:39Z",
  
    "value": 0.858472652447435
  
  },
  
  "operationMode": {
  
    "type": "Property",
  
    "value": "supply"
  
  },
  
  "operationTemperatureMax": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T17:43:31Z",
  
    "value": 0.6990158373086164
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T22:43:03Z",
  
    "value": 0.070852494560947
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:4e9dc2df-6361-4376-979d-fb3f96ba8a2f"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:d80ed04b-6f2d-45eb-bcf9-f94ed0564d8f"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:e79640ab-b497-40a8-b020-23d2799cdb87"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:9c3ebe76-cc20-45d1-b436-759778c41424"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:b8bb079a-9cb2-4f4e-8f22-2e5ecbc4a37e"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "Fan Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "Fan 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-26T01:34:08Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-26T12:21:35Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "Fan"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "Fan type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "Fan of limited Fan types"
  
  },
  
  "dataProvider": {
  
    "type": "Property",
  
    "value": "IFC file"
  
  },
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
