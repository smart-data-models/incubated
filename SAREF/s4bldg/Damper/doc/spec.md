[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: Damper  
==============https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](http://smart-data-models.kmd.dk/flat/s4bldg/Damper/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **A damper typically participates in an HVAC duct distribution system and is used to control or modulate the flow of air.**  

version: 0.0.2  


## List of properties  


- `address`: The mailing address  
- `airFlowRateMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `alternateName`: An alternative name for this item  
- `areaServed`: The geographic area where a service or offered item is provided  
- `bladeAction`: Blade action.  
- `bladeEdge`: Blade edge.  
- `bladeShape`: Blade shape. Flat means triple V-groove.  
- `bladeThickness`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `closeOffRating`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `faceArea`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `frameDepth`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `frameThickness`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `frameType`: The type of frame used by the damper (e.g., Standard, Single Flange, Single Reversed Flange, Double Flange, etc.).  
- `hasManufacturer`: A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hasModel`: A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `id`: Unique identifier of the entity  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `leakageFullyClosed`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `nominalAirFlowRate`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `numberOfBlades`: Number of blades.  
- `openPressureDrop`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `operation`: The operational mechanism for the damper operation.  
- `operationMode`: Operation mode of this damper.  
- `operationTemperatureMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `operationTemperatureMin`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `orientation`: The intended orientation for the damper as specified by the manufacturer.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `temperatureRating`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `type`: It must be equal to `Damper`.  
- `workingPressureMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
Damper:
    
  description: A damper typically participates in an HVAC duct distribution system and is used to control or modulate the flow of air.
    
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
    
    airFlowRateMax:
    
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
    
    bladeAction:
    
      description: Blade action.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    bladeEdge:
    
      description: Blade edge.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    bladeShape:
    
      description: Blade shape. Flat means triple V-groove.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    bladeThickness:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    closeOffRating:
    
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
    
    faceArea:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    frameDepth:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    frameThickness:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    frameType:
    
      description: 'The type of frame used by the damper (e.g., Standard, Single Flange, Single Reversed Flange, Double Flange, etc.).'
    
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
    
    leakageFullyClosed:
    
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
    https://github.com/smart-data-models/incubated/tree/master/SAREF/
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
    
    nominalAirFlowRate:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    numberOfBlades:
    
      description: Number of blades.
    
      type: number
    
      x-ngsi:
    
        type: Property
    
    openPressureDrop:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    operation:
    
      description: The operational mechanism for the damper operation.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    operationMode:
    
      description: Operation mode of this damper.
    
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
    
    orientation:
    
      description: The intended orientation for the damper as specified by the manufacturer.
    
      type: string
    
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
    
    temperatureRating:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    type:
    
      description: It must be equal to `Damper`.
    
      enum:
    
        - Damper
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    workingPressureMax:
    
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
    
  x-license-url: http://smart-data-models.kmd.dk/flat/s4bldg/Damper/LICENSE.md
    
  x-model-schema: http://smart-data-models.kmd.dk/Dampers/Damper
    
  x-model-tags: SAREF Damper SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### Damper NGSI-v2 key-values Example    

Here is an example of a Damper in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Damper:65c94159-bfe6-416d-b02c-283479048fe3",
  
  "type": "Damper",
  
  "airFlowRateMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-25T14:35:45Z",
  
      "value": 0.5927918101987754
  
    }
  
  },
  
  "bladeAction": "Belize Dollar",
  
  "bladeEdge": "frictionless",
  
  "bladeShape": "intermediate",
  
  "bladeThickness": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T23:29:21Z",
  
      "value": 0.5665758025960763
  
    }
  
  },
  
  "closeOffRating": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-25T21:49:32Z",
  
      "value": 0.8924252696459434
  
    }
  
  },
  
  "faceArea": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m2",
  
      "observedAt": "2023-01-26T07:52:23Z",
  
      "value": 0.45839947738381925
  
    }
  
  },
  
  "frameDepth": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T01:24:51Z",
  
      "value": 0.6687870848219263
  
    }
  
  },
  
  "frameThickness": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T15:44:05Z",
  
      "value": 0.6594470368135407
  
    }
  
  },
  
  "frameType": "Ergonomic",
  
  "leakageFullyClosed": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-26T09:27:24Z",
  
      "value": 0.052627216627954665
  
    }
  
  },
  
  "nominalAirFlowRate": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-26T07:15:24Z",
  
      "value": 0.7333602290466408
  
    }
  
  },
  
  "numberOfBlades": 0.3476917428528077,
  
  "openPressureDrop": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-26T02:45:22Z",
  
      "value": 0.8991384789588308
  
    }
  
  },
  
  "operation": "Implemented",
  
  "operationMode": "supply",
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T08:00:16Z",
  
      "value": 0.07772736087657628
  
    }
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T17:36:18Z",
  
      "value": 0.4857292385786113
  
    }
  
  },
  
  "orientation": "reboot",
  
  "temperatureRating": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T11:23:30Z",
  
      "value": 0.4909792118139581
  
    }
  
  },
  
  "workingPressureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-26T01:11:17Z",
  
      "value": 0.10839736205746486
  
    }
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c25bebe3-d546-4942-be72-9468ce218070",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:326da1c1-440d-4200-b598-a84e3bf5fdc1",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:007e61a9-027a-4662-a7a0-1e9e48f57886",
  
    "urn:ngsi-ld:System:59945456-4e66-4c84-b637-7c771479a9f3",
  
    "urn:ngsi-ld:System:023e0706-8d3d-411b-9e97-994a870341cd"
  
  ],
  
  "hasManufacturer": "Damper Company Inc.",
  
  "hasModel": "Damper 0.1.2",
  
  "dateCreated": "2023-01-25T18:10:59Z",
  
  "dateModified": "2023-01-26T07:49:53Z",
  
  "source": "Import",
  
  "name": "Damper",
  
  "alternateName": "Damper type 2",
  
  "description": "Damper of limited Damper types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### Damper NGSI-v2 normalized Example    

Here is an example of a Damper in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Damper:30830dab-6aa5-4dd1-9e48-d6ac7e24e4bf",
  
  "type": "Damper",
  
  "airFlowRateMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-26T09:53:25Z",
  
      "value": 0.13813389168852752
  
    }
  
  },
  
  "bladeAction": {
  
    "type": "Text",
  
    "value": "Spur"
  
  },
  
  "bladeEdge": {
  
    "type": "Text",
  
    "value": "Personal Loan Account"
  
  },
  
  "bladeShape": {
  
    "type": "Text",
  
    "value": "Human"
  
  },
  
  "bladeThickness": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T09:32:44Z",
  
      "value": 0.35230461364031296
  
    }
  
  },
  
  "closeOffRating": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-26T13:43:21Z",
  
      "value": 0.171775838539866
  
    }
  
  },
  
  "faceArea": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m2",
  
      "observedAt": "2023-01-25T22:27:41Z",
  
      "value": 0.4212393478883142
  
    }
  
  },
  
  "frameDepth": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T13:33:52Z",
  
      "value": 0.8035081586701794
  
    }
  
  },
  
  "frameThickness": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T09:44:48Z",
  
      "value": 0.28946308913206176
  
    }
  
  },
  
  "frameType": {
  
    "type": "Text",
  
    "value": "Balanced"
  
  },
  
  "leakageFullyClosed": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-25T15:23:52Z",
  
      "value": 0.44075236436472953
  
    }
  
  },
  
  "nominalAirFlowRate": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-25T15:21:46Z",
  
      "value": 0.47305378645729657
  
    }
  
  },
  
  "numberOfBlades": {
  
    "type": "Float",
  
    "value": 0.8083872561368712
  
  },
  
  "openPressureDrop": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-25T23:49:20Z",
  
      "value": 0.9106213284285767
  
    }
  
  },
  
  "operation": {
  
    "type": "Text",
  
    "value": "Handcrafted Concrete Computer"
  
  },
  
  "operationMode": {
  
    "type": "DamperOperationMode",
  
    "value": "supply"
  
  },
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T08:02:54Z",
  
      "value": 0.87576324331876
  
    }
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T03:24:42Z",
  
      "value": 0.3952529455728351
  
    }
  
  },
  
  "orientation": {
  
    "type": "Text",
  
    "value": "Mozambique"
  
  },
  
  "temperatureRating": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T09:10:28Z",
  
      "value": 0.43326401348250587
  
    }
  
  },
  
  "workingPressureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-26T13:20:51Z",
  
      "value": 0.2695729035947665
  
    }
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:f19ff450-12f4-472a-985e-40b163530ccd"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:ee6c23f3-7261-4807-b3e3-703588646f02"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:a8f8f637-52c0-491d-890e-2806ffbdc6cd"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:7f5f939e-9a41-4ca6-95ff-4ece8ffec42c"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:ff7924ea-c532-40c9-a1ac-449c76216073"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "Damper Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "Damper 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T15:13:23.9679787+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T16:00:58.1902016+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "Damper"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "Damper type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "Damper of limited Damper types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### Damper NGSI-LD key-values Example    

Here is an example of a Damper in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Damper:c12e3b70-82be-4093-83be-0e7172197b35",
  
  "type": "Damper",
  
  "airFlowRateMax": {
  
    "type": "Measurement",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-26T05:26:36Z",
  
    "value": 0.15697569827699642
  
  },
  
  "bladeAction": "Auto Loan Account",
  
  "bladeEdge": "deposit",
  
  "bladeShape": "Belarussian Ruble",
  
  "bladeThickness": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T11:29:14Z",
  
    "value": 0.6634029038351369
  
  },
  
  "closeOffRating": {
  
    "type": "Measurement",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T13:18:03Z",
  
    "value": 0.46526237011749016
  
  },
  
  "faceArea": {
  
    "type": "Measurement",
  
    "unitCode": "m2",
  
    "observedAt": "2023-01-26T02:56:53Z",
  
    "value": 0.3300587365904212
  
  },
  
  "frameDepth": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T13:08:56Z",
  
    "value": 0.28523761527388813
  
  },
  
  "frameThickness": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T09:32:10Z",
  
    "value": 0.6159738353935348
  
  },
  
  "frameType": "withdrawal",
  
  "leakageFullyClosed": {
  
    "type": "Measurement",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-25T21:14:48Z",
  
    "value": 0.32179384741237893
  
  },
  
  "nominalAirFlowRate": {
  
    "type": "Measurement",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-26T00:15:03Z",
  
    "value": 0.879644600722498
  
  },
  
  "numberOfBlades": 0.3464554821961412,
  
  "openPressureDrop": {
  
    "type": "Measurement",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T02:25:22Z",
  
    "value": 0.18032554584030702
  
  },
  
  "operation": "partnerships",
  
  "operationMode": "supply",
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T16:18:38Z",
  
    "value": 0.1356223929297501
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T13:42:27Z",
  
    "value": 0.1559992419485755
  
  },
  
  "orientation": "Avon",
  
  "temperatureRating": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T19:29:30Z",
  
    "value": 0.4468160116175208
  
  },
  
  "workingPressureMax": {
  
    "type": "Measurement",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T05:45:33Z",
  
    "value": 0.8069711939499264
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:997a54be-8069-4236-b4f6-b0c94e9ca4e7",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:7d237099-1c15-4bee-8ce9-9e82046ba9b3",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:a7fde411-a1fc-40f9-82ea-9266af106bce",
  
    "urn:ngsi-ld:System:ae2a2290-fb72-4a6e-9751-d92f876336b8",
  
    "urn:ngsi-ld:System:a2154c1e-c52a-47a7-b57a-cc7a2ec536a6"
  
  ],
  
  "hasManufacturer": "Damper Company Inc.",
  
  "hasModel": "Damper 0.1.2",
  
  "dateCreated": "2023-01-26T01:33:00Z",
  
  "dateModified": "2023-01-25T14:32:05Z",
  
  "source": "Import",
  
  "name": "Damper",
  
  "alternateName": "Damper type 2",
  
  "description": "Damper of limited Damper types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### Damper NGSI-LD normalized Example    

Here is an example of a Damper in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Damper:99cb9b35-5f17-4e4d-89bb-e9d7bb88c2ba",
  
  "type": "Damper",
  
  "airFlowRateMax": {
  
    "type": "Property",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-26T10:15:08Z",
  
    "value": 0.46010915943742847
  
  },
  
  "bladeAction": {
  
    "type": "Property",
  
    "value": "microchip"
  
  },
  
  "bladeEdge": {
  
    "type": "Property",
  
    "value": "Village"
  
  },
  
  "bladeShape": {
  
    "type": "Property",
  
    "value": "Netherlands Antillian Guilder"
  
  },
  
  "bladeThickness": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T21:36:37Z",
  
    "value": 0.5214778377905084
  
  },
  
  "closeOffRating": {
  
    "type": "Property",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-25T18:21:40Z",
  
    "value": 0.8241451329002358
  
  },
  
  "faceArea": {
  
    "type": "Property",
  
    "unitCode": "m2",
  
    "observedAt": "2023-01-25T20:36:04Z",
  
    "value": 0.6197704906516315
  
  },
  
  "frameDepth": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T14:05:58Z",
  
    "value": 0.19371235604272175
  
  },
  
  "frameThickness": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T21:48:43Z",
  
    "value": 0.630746648821536
  
  },
  
  "frameType": {
  
    "type": "Property",
  
    "value": "SAS"
  
  },
  
  "leakageFullyClosed": {
  
    "type": "Property",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-25T21:59:27Z",
  
    "value": 0.8430168839934075
  
  },
  
  "nominalAirFlowRate": {
  
    "type": "Property",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-26T06:30:50Z",
  
    "value": 0.8419372074040988
  
  },
  
  "numberOfBlades": {
  
    "type": "Property",
  
    "value": 0.2730424937241438
  
  },
  
  "openPressureDrop": {
  
    "type": "Property",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T04:03:50Z",
  
    "value": 0.25493844227297535
  
  },
  
  "operation": {
  
    "type": "Property",
  
    "value": "partnerships"
  
  },
  
  "operationMode": {
  
    "type": "Property",
  
    "value": "exhaust"
  
  },
  
  "operationTemperatureMax": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T22:15:50Z",
  
    "value": 0.4402985682699154
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T11:49:40Z",
  
    "value": 0.0015019955460002787
  
  },
  
  "orientation": {
  
    "type": "Property",
  
    "value": "Metrics"
  
  },
  
  "temperatureRating": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T16:28:22Z",
  
    "value": 0.6012606116766228
  
  },
  
  "workingPressureMax": {
  
    "type": "Property",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T09:39:16Z",
  
    "value": 0.320862748056973
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:573f5e7a-806c-4deb-878c-365ef09fe4d2"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:0cbecfb0-1008-4c54-99f6-510fba847457"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:972e3b8b-9613-4b3a-a798-f3e56587d999"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:0d09725f-1468-4352-92e9-39d0b647a683"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:0c5bf106-93a0-4eb9-a15d-a0d834088c94"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "Damper Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "Damper 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-26T10:37:53Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-26T10:42:54Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "Damper"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "Damper type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "Damper of limited Damper types"
  
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
