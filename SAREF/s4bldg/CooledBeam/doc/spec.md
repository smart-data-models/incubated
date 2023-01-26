[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: CooledBeam  
================https://github.com/smart-data-models/incubated/SAREF/
  

[Open License](http://smart-data-models.kmd.dk/flat/s4bldg/CooledBeam/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **A cooled beam (or chilled beam) is a device typically used to cool air by circulating a fluid such as chilled water through exposed finned tubes above a space. Typically mounted overhead near or within a ceiling, the cooled beam uses convection to cool the space below it by acting as a heat sink for the naturally rising warm air of the space. Once cooled, the air naturally drops back to the floor where the cycle begins again.**  

version: 0.0.2  


## List of properties  


- `address`: The mailing address  
- `alternateName`: An alternative name for this item  
- `areaServed`: The geographic area where a service or offered item is provided  
- `coilLength`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `coilWidth`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `finishColor`: Finish color for cooled beam.  
- `hasManufacturer`: A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hasModel`: A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `id`: Unique identifier of the entity  
- `integratedLightingType`: Integrated lighting in cooled beam.  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isFreeHanging`: Is it free hanging type (not mounted in a false ceiling)?  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `nominalCoolingCapacity`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalHeatingCapacity`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalReturnWaterTemperatureCooling`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalReturnWaterTemperatureHeating`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalSorroundingHumidityCooling`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalSorroundingTemperatureCooling`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalSorroundingTemperatureHeating`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalSupplyWaterTemperatureCooling`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalSupplyWaterTemperatureHeating`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalWaterFlowCooling`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalWaterFlowHeating`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `pipeConnectionEnum`: The manner in which the pipe connection is made to the cooled beam.  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type`: It must be equal to `CooledBeam`.  
- `waterFlowControlSystemType`: Factory fitted waterflow control system.  
- `waterPressureMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `waterPressureMin`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
CooledBeam:
    
  description: 'A cooled beam (or chilled beam) is a device typically used to cool air by circulating a fluid such as chilled water through exposed finned tubes above a space. Typically mounted overhead near or within a ceiling, the cooled beam uses convection to cool the space below it by acting as a heat sink for the naturally rising warm air of the space. Once cooled, the air naturally drops back to the floor where the cycle begins again.'
    
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
    
    coilLength:
    
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
    
    coilWidth:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
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
    
    finishColor:
    
      description: Finish color for cooled beam.
    
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
    
    integratedLightingType:
    
      description: Integrated lighting in cooled beam.
    
      type: string
    
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
    
    isFreeHanging:
    
      description: 'Is it free hanging type (not mounted in a false ceiling)?'
    
      type: boolean
    
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
    
              typhttps://github.com/smart-data-models/incubated/SAREF/
    
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
    
    nominalCoolingCapacity:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalHeatingCapacity:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalReturnWaterTemperatureCooling:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalReturnWaterTemperatureHeating:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalSorroundingHumidityCooling:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalSorroundingTemperatureCooling:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalSorroundingTemperatureHeating:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalSupplyWaterTemperatureCooling:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalSupplyWaterTemperatureHeating:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalWaterFlowCooling:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalWaterFlowHeating:
    
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
    
    pipeConnectionEnum:
    
      description: The manner in which the pipe connection is made to the cooled beam.
    
      type: string
    
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
    
      description: It must be equal to `CooledBeam`.
    
      enum:
    
        - CooledBeam
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    waterFlowControlSystemType:
    
      description: Factory fitted waterflow control system.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    waterPressureMax:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    waterPressureMin:
    
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
    
  x-license-url: http://smart-data-models.kmd.dk/flat/s4bldg/CooledBeam/LICENSE.md
    
  x-model-schema: http://smart-data-models.kmd.dk/CooledBeams/CooledBeam
    
  x-model-tags: SAREF CooledBeam SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### CooledBeam NGSI-v2 key-values Example    

Here is an example of a CooledBeam in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:CooledBeam:82040ca8-778f-478d-a8fd-28485704919f",
  
  "type": "CooledBeam",
  
  "coilLength": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T09:20:14Z",
  
      "value": 0.12136965337189098
  
    }
  
  },
  
  "coilWidth": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m",
  
      "observedAt": "2023-01-26T12:54:53Z",
  
      "value": 0.9739362570796377
  
    }
  
  },
  
  "finishColor": "deposit",
  
  "integratedLightingType": "Metrics",
  
  "isFreeHanging": false,
  
  "nominalCoolingCapacity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-25T15:29:27Z",
  
      "value": 0.25517130161811685
  
    }
  
  },
  
  "nominalHeatingCapacity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-25T20:14:08Z",
  
      "value": 0.979299961039553
  
    }
  
  },
  
  "nominalReturnWaterTemperatureCooling": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T15:44:26Z",
  
      "value": 0.8331575990645163
  
    }
  
  },
  
  "nominalReturnWaterTemperatureHeating": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T16:53:52Z",
  
      "value": 0.8257910510708837
  
    }
  
  },
  
  "nominalSorroundingHumidityCooling": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T03:02:04Z",
  
      "value": 0.08831404123432451
  
    }
  
  },
  
  "nominalSorroundingTemperatureCooling": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T17:00:05Z",
  
      "value": 0.8951747110468832
  
    }
  
  },
  
  "nominalSorroundingTemperatureHeating": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T05:37:05Z",
  
      "value": 0.7722529144575002
  
    }
  
  },
  
  "nominalSupplyWaterTemperatureCooling": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T10:49:58Z",
  
      "value": 0.510069259798832
  
    }
  
  },
  
  "nominalSupplyWaterTemperatureHeating": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T02:21:24Z",
  
      "value": 0.9682117435710755
  
    }
  
  },
  
  "nominalWaterFlowCooling": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-26T06:02:20Z",
  
      "value": 0.640621498291464
  
    }
  
  },
  
  "nominalWaterFlowHeating": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-26T10:32:59Z",
  
      "value": 0.3754874763938201
  
    }
  
  },
  
  "pipeConnectionEnum": "Falls",
  
  "waterFlowControlSystemType": "Forks",
  
  "waterPressureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-26T02:48:22Z",
  
      "value": 0.6809509740238233
  
    }
  
  },
  
  "waterPressureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-25T17:32:58Z",
  
      "value": 0.3372474470208946
  
    }
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:29882bc5-9d20-4d25-b276-5bdf4f6981e1",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:13d83cbf-6e67-4d40-85da-46a7032fbde9",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:dfeed4f8-88d6-4475-89b3-71faa705f8a4",
  
    "urn:ngsi-ld:System:23813ba9-d7b1-475b-b245-c32d08798cc3",
  
    "urn:ngsi-ld:System:daa546ea-d20c-4761-98b2-e17e050b4625"
  
  ],
  
  "hasManufacturer": "CooledBeam Company Inc.",
  
  "hasModel": "CooledBeam 0.1.2",
  
  "dateCreated": "2023-01-26T05:29:03Z",
  
  "dateModified": "2023-01-26T10:03:56Z",
  
  "source": "Import",
  
  "name": "CooledBeam",
  
  "alternateName": "CooledBeam type 2",
  
  "description": "CooledBeam of limited CooledBeam types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### CooledBeam NGSI-v2 normalized Example    

Here is an example of a CooledBeam in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:CooledBeam:38dcdd25-ae94-441c-8409-218ec91e3006",
  
  "type": "CooledBeam",
  
  "coilLength": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T16:20:23Z",
  
      "value": 0.4277226249853211
  
    }
  
  },
  
  "coilWidth": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m",
  
      "observedAt": "2023-01-26T03:32:03Z",
  
      "value": 0.6183775851562611
  
    }
  
  },
  
  "finishColor": {
  
    "type": "Text",
  
    "value": "Associate"
  
  },
  
  "integratedLightingType": {
  
    "type": "Text",
  
    "value": "Washington"
  
  },
  
  "isFreeHanging": {
  
    "type": "Boolean",
  
    "value": false
  
  },
  
  "nominalCoolingCapacity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-25T14:46:39Z",
  
      "value": 0.45857043485420457
  
    }
  
  },
  
  "nominalHeatingCapacity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-26T07:50:13Z",
  
      "value": 0.37812382267356337
  
    }
  
  },
  
  "nominalReturnWaterTemperatureCooling": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T03:32:44Z",
  
      "value": 0.973742767691913
  
    }
  
  },
  
  "nominalReturnWaterTemperatureHeating": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T22:36:59Z",
  
      "value": 0.6848085584395665
  
    }
  
  },
  
  "nominalSorroundingHumidityCooling": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T13:03:01Z",
  
      "value": 0.4100986776385609
  
    }
  
  },
  
  "nominalSorroundingTemperatureCooling": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T15:25:27Z",
  
      "value": 0.039909771141081074
  
    }
  
  },
  
  "nominalSorroundingTemperatureHeating": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T09:14:22Z",
  
      "value": 0.3023923557796515
  
    }
  
  },
  
  "nominalSupplyWaterTemperatureCooling": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T18:36:07Z",
  
      "value": 0.7562940127899793
  
    }
  
  },
  
  "nominalSupplyWaterTemperatureHeating": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T05:13:59Z",
  
      "value": 0.31198678394809454
  
    }
  
  },
  
  "nominalWaterFlowCooling": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-25T17:41:15Z",
  
      "value": 0.40924277893308847
  
    }
  
  },
  
  "nominalWaterFlowHeating": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-26T07:55:59Z",
  
      "value": 0.9345939456733873
  
    }
  
  },
  
  "pipeConnectionEnum": {
  
    "type": "Text",
  
    "value": "extensible"
  
  },
  
  "waterFlowControlSystemType": {
  
    "type": "Text",
  
    "value": "Interactions"
  
  },
  
  "waterPressureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-25T23:01:09Z",
  
      "value": 0.07837257218461391
  
    }
  
  },
  
  "waterPressureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-25T22:43:40Z",
  
      "value": 0.03742669539477306
  
    }
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:3e03fe30-3728-4867-ab51-b147c2d3e63b"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:cfd9df05-18b1-44f4-b1ee-da55226255e9"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:a4b0cda0-b373-4ae9-b2c7-e2cff5429e1e"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:216f6f83-8bd1-456f-9bed-36dbec41a3aa"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:d19ccffa-f134-46fc-8f9f-77656bb91649"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "CooledBeam Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "CooledBeam 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T21:51:06.7954024+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T00:15:46.9435362+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "CooledBeam"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "CooledBeam type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "CooledBeam of limited CooledBeam types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### CooledBeam NGSI-LD key-values Example    

Here is an example of a CooledBeam in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:CooledBeam:b9a827e2-fa4f-44a9-a772-32d1e277d131",
  
  "type": "CooledBeam",
  
  "coilLength": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T04:36:34Z",
  
    "value": 0.973603236585636
  
  },
  
  "coilWidth": {
  
    "type": "Measurement",
  
    "unitCode": "m",
  
    "observedAt": "2023-01-26T00:17:45Z",
  
    "value": 0.6716208123553327
  
  },
  
  "finishColor": "National",
  
  "integratedLightingType": "Rhode Island",
  
  "isFreeHanging": true,
  
  "nominalCoolingCapacity": {
  
    "type": "Measurement",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-26T05:32:03Z",
  
    "value": 0.22824788134369234
  
  },
  
  "nominalHeatingCapacity": {
  
    "type": "Measurement",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-26T06:50:53Z",
  
    "value": 0.7358522133930573
  
  },
  
  "nominalReturnWaterTemperatureCooling": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T09:38:34Z",
  
    "value": 0.48434358288699564
  
  },
  
  "nominalReturnWaterTemperatureHeating": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T16:15:42Z",
  
    "value": 0.23458721245001934
  
  },
  
  "nominalSorroundingHumidityCooling": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T05:03:17Z",
  
    "value": 0.015972693641019275
  
  },
  
  "nominalSorroundingTemperatureCooling": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T14:19:14Z",
  
    "value": 0.5654958299454678
  
  },
  
  "nominalSorroundingTemperatureHeating": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T10:06:19Z",
  
    "value": 0.7445355110572658
  
  },
  
  "nominalSupplyWaterTemperatureCooling": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T05:43:17Z",
  
    "value": 0.780329827269151
  
  },
  
  "nominalSupplyWaterTemperatureHeating": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T13:04:24Z",
  
    "value": 0.8672620282115548
  
  },
  
  "nominalWaterFlowCooling": {
  
    "type": "Measurement",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-25T19:42:05Z",
  
    "value": 0.20202118255376544
  
  },
  
  "nominalWaterFlowHeating": {
  
    "type": "Measurement",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-26T01:04:47Z",
  
    "value": 0.39118103627579903
  
  },
  
  "pipeConnectionEnum": "Key",
  
  "waterFlowControlSystemType": "intangible",
  
  "waterPressureMax": {
  
    "type": "Measurement",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-25T22:13:00Z",
  
    "value": 0.318666185517553
  
  },
  
  "waterPressureMin": {
  
    "type": "Measurement",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T05:59:56Z",
  
    "value": 0.7788409024396181
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:983ceba6-dea5-449b-88b3-ed3b63b5b0c6",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:c53f01eb-a689-4d62-8a8a-0d0a1afb9ab9",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:2cc6c3b8-671c-4e19-876c-07b180e91a85",
  
    "urn:ngsi-ld:System:4c7fae5b-2e6e-4027-bfe1-df6d2ad5b9d8",
  
    "urn:ngsi-ld:System:b288aee6-a0cf-4d04-9a32-2a45a09bfaca"
  
  ],
  
  "hasManufacturer": "CooledBeam Company Inc.",
  
  "hasModel": "CooledBeam 0.1.2",
  
  "dateCreated": "2023-01-25T22:41:48Z",
  
  "dateModified": "2023-01-25T16:10:31Z",
  
  "source": "Import",
  
  "name": "CooledBeam",
  
  "alternateName": "CooledBeam type 2",
  
  "description": "CooledBeam of limited CooledBeam types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://smartdatamodels.blob.core.windows.net/models/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### CooledBeam NGSI-LD normalized Example    

Here is an example of a CooledBeam in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:CooledBeam:baa66543-6434-4e28-8e85-20b2b260d404",
  
  "type": "CooledBeam",
  
  "coilLength": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T18:59:14Z",
  
    "value": 0.45413352830053977
  
  },
  
  "coilWidth": {
  
    "type": "Property",
  
    "unitCode": "m",
  
    "observedAt": "2023-01-26T07:44:01Z",
  
    "value": 0.2692385089640058
  
  },
  
  "finishColor": {
  
    "type": "Property",
  
    "value": "indigo"
  
  },
  
  "integratedLightingType": {
  
    "type": "Property",
  
    "value": "Graphical User Interface"
  
  },
  
  "isFreeHanging": {
  
    "type": "Property",
  
    "value": false
  
  },
  
  "nominalCoolingCapacity": {
  
    "type": "Property",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-26T09:40:29Z",
  
    "value": 0.3030442126473498
  
  },
  
  "nominalHeatingCapacity": {
  
    "type": "Property",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-26T02:43:04Z",
  
    "value": 0.7091959285173477
  
  },
  
  "nominalReturnWaterTemperatureCooling": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T10:09:02Z",
  
    "value": 0.4048762377790246
  
  },
  
  "nominalReturnWaterTemperatureHeating": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T08:24:33Z",
  
    "value": 0.33261295327987683
  
  },
  
  "nominalSorroundingHumidityCooling": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T12:36:33Z",
  
    "value": 0.5632800434491262
  
  },
  
  "nominalSorroundingTemperatureCooling": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T11:31:42Z",
  
    "value": 0.47265451181389695
  
  },
  
  "nominalSorroundingTemperatureHeating": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T18:37:57Z",
  
    "value": 0.18090042184548072
  
  },
  
  "nominalSupplyWaterTemperatureCooling": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T21:17:20Z",
  
    "value": 0.9122743224756777
  
  },
  
  "nominalSupplyWaterTemperatureHeating": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T17:52:00Z",
  
    "value": 0.9207552089629301
  
  },
  
  "nominalWaterFlowCooling": {
  
    "type": "Property",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-25T15:05:33Z",
  
    "value": 0.06592489938443258
  
  },
  
  "nominalWaterFlowHeating": {
  
    "type": "Property",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-26T13:42:04Z",
  
    "value": 0.3446198206084118
  
  },
  
  "pipeConnectionEnum": {
  
    "type": "Property",
  
    "value": "SSL"
  
  },
  
  "waterFlowControlSystemType": {
  
    "type": "Property",
  
    "value": "supply-chains"
  
  },
  
  "waterPressureMax": {
  
    "type": "Property",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-25T17:35:39Z",
  
    "value": 0.8610847602415933
  
  },
  
  "waterPressureMin": {
  
    "type": "Property",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T03:28:09Z",
  
    "value": 0.9088584704707019
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:6689ca11-b361-48b4-950d-07edf1182e97"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:2e350952-8c19-46a2-a2c2-8d30c54d03cb"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:cf124c7e-8f71-424a-93b5-64643c889f30"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:a72f7b54-3f5c-4b66-9463-f20f7127cff6"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:ce488063-f9a9-44c4-ac0f-f79e2977a2d4"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "CooledBeam Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "CooledBeam 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-25T23:43:55Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-25T20:21:43Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "CooledBeam"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "CooledBeam type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "CooledBeam of limited CooledBeam types"
  
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
