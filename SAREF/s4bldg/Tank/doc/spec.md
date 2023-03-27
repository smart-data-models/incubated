[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: Tank  
============https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](https://smart-data-models.github.com/dataModel.SAREF4BLDG/flat/s4bldg/Tank/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **A tank is a vessel or container in which a fluid or gas is stored for later use.**  

version: 0.0.2  


## List of properties  


- `accessType`: Defines the types of access (or cover) to a tank that may be specified. Note that covers are generally specified for rectangular tanks. For cylindrical tanks, access will normally be via a manhole.  
- `address`: The mailing address  
- `alternateName`: An alternative name for this item  
- `areaServed`: The geographic area where a service or offered item is provided  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `effectiveCapacity`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `endShapeType`: Defines the types of end shapes that can be used for preformed tanks. The convention for reading these enumerated values is that for a vertical cylinder, the first value is the base and the second is the top for a horizontal cylinder, the order of reading should be left to right. For a speherical tank, the value UNSET should be used.B5  
- `firstCurvatureRadius`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `hasManufacturer`: A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hasModel`: A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `id`: Unique identifier of the entity  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `nominalDepth`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalLengthOrDiameter`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalVolumetricCapacity`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalWidthOrDiameter`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `numberOfSections`: Number of sections used.  
- `operatingWeight`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `patternType`: Defines the types of pattern (or shape of a tank that may be specified.  
- `secondCurvatureRadius`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `storageType`: Defines the general material category intended to be stored.  
- `type`: It must be equal to `Tank`.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
Tank:
    
  description: A tank is a vessel or container in which a fluid or gas is stored for later use.
    
  properties:
    
    accessType:
    
      description: 'Defines the types of access (or cover) to a tank that may be specified. Note that covers are generally specified for rectangular tanks. For cylindrical tanks, access will normally be via a manhole.'
    
      type: string
    
      x-ngsi:
    
        type: Property
    
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
    
    effectiveCapacity:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
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
    
    endShapeType:
    
      description: 'Defines the types of end shapes that can be used for preformed tanks. The convention for reading these enumerated values is that for a vertical cylinder, the first value is the base and the second is the top for a horizontal cylinder, the order of reading should be left to right. For a speherical tank, the value UNSET should be used.B5'
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    firstCurvatureRadius:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
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
    https://github.com/smart-data-models/incubated/tree/master/SAREF/
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
    
    nominalDepth:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalLengthOrDiameter:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalVolumetricCapacity:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalWidthOrDiameter:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    numberOfSections:
    
      description: Number of sections used.
    
      type: number
    
      x-ngsi:
    
        type: Property
    
    operatingWeight:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
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
    
    patternType:
    
      description: Defines the types of pattern (or shape of a tank that may be specified.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    secondCurvatureRadius:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
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
    
    storageType:
    
      description: Defines the general material category intended to be stored.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    type:
    
      description: It must be equal to `Tank`.
    
      enum:
    
        - Tank
    
      type: string
    
      x-ngsi:
    
        type: Property
    
  required:
    
    - id
    
    - type
    
  type: object
    
  x-derived-from: ""
    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'
    
  x-license-url: https://smart-data-models.github.com/dataModel.SAREF4BLDG/flat/s4bldg/Tank/LICENSE.md
    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Tanks/Tank
    
  x-model-tags: SAREF Tank SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### Tank NGSI-v2 key-values Example    

Here is an example of a Tank in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Tank:7a5293bf-87b8-4768-8c25-56bcbfa91649",
  
  "type": "Tank",
  
  "accessType": "Auto Loan Account",
  
  "effectiveCapacity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3.B",
  
      "observedAt": "2023-01-26T11:31:41Z",
  
      "value": 0.6627329008534851
  
    }
  
  },
  
  "endShapeType": "Union",
  
  "firstCurvatureRadius": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T11:17:45Z",
  
      "value": 0.6799132713266423
  
    }
  
  },
  
  "nominalDepth": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T12:42:05Z",
  
      "value": 0.07530609187652448
  
    }
  
  },
  
  "nominalLengthOrDiameter": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T13:56:49Z",
  
      "value": 0.1950493997985394
  
    }
  
  },
  
  "nominalVolumetricCapacity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3",
  
      "observedAt": "2023-01-25T22:15:17Z",
  
      "value": 0.6494794060427406
  
    }
  
  },
  
  "nominalWidthOrDiameter": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T10:10:44Z",
  
      "value": 0.2734692629974923
  
    }
  
  },
  
  "numberOfSections": 0.3094855572354859,
  
  "operatingWeight": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "g",
  
      "observedAt": "2023-01-25T19:49:52Z",
  
      "value": 0.3055837938759739
  
    }
  
  },
  
  "patternType": "Investment Account",
  
  "secondCurvatureRadius": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T17:02:26Z",
  
      "value": 0.0019846058153857316
  
    }
  
  },
  
  "storageType": "Investor",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:ffcd7e11-7c74-45f3-8f5a-3310ababddc8",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:c2540316-a0c2-4363-93b7-e49ab5ed3b2f",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:aae7e0b6-0256-4c58-a3ee-4989bdc205da",
  
    "urn:ngsi-ld:System:857551fc-8a05-4052-9269-8193f148ff2c",
  
    "urn:ngsi-ld:System:e4e88c0a-d78a-4bfd-a76b-af72e518a66e"
  
  ],
  
  "hasManufacturer": "Tank Company Inc.",
  
  "hasModel": "Tank 0.1.2",
  
  "dateCreated": "2023-01-26T12:03:34Z",
  
  "dateModified": "2023-01-25T16:27:50Z",
  
  "source": "Import",
  
  "name": "Tank",
  
  "alternateName": "Tank type 2",
  
  "description": "Tank of limited Tank types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### Tank NGSI-v2 normalized Example    

Here is an example of a Tank in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Tank:dc341150-16f1-4fa1-a674-36714ed2565c",
  
  "type": "Tank",
  
  "accessType": {
  
    "type": "Text",
  
    "value": "Benin"
  
  },
  
  "effectiveCapacity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3.B",
  
      "observedAt": "2023-01-25T19:55:24Z",
  
      "value": 0.34988329549654584
  
    }
  
  },
  
  "endShapeType": {
  
    "type": "Text",
  
    "value": "Lari"
  
  },
  
  "firstCurvatureRadius": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T16:06:21Z",
  
      "value": 0.9159778495815387
  
    }
  
  },
  
  "nominalDepth": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T02:00:11Z",
  
      "value": 0.8630341610754986
  
    }
  
  },
  
  "nominalLengthOrDiameter": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T13:06:07Z",
  
      "value": 0.8867523503955448
  
    }
  
  },
  
  "nominalVolumetricCapacity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3",
  
      "observedAt": "2023-01-26T07:29:43Z",
  
      "value": 0.27704062609207425
  
    }
  
  },
  
  "nominalWidthOrDiameter": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T12:21:39Z",
  
      "value": 0.6770082270929979
  
    }
  
  },
  
  "numberOfSections": {
  
    "type": "Float",
  
    "value": 0.7169194499582789
  
  },
  
  "operatingWeight": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "g",
  
      "observedAt": "2023-01-25T20:25:40Z",
  
      "value": 0.23947734710245394
  
    }
  
  },
  
  "patternType": {
  
    "type": "Text",
  
    "value": "Ergonomic Cotton Ball"
  
  },
  
  "secondCurvatureRadius": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T23:32:20Z",
  
      "value": 0.11478790270153483
  
    }
  
  },
  
  "storageType": {
  
    "type": "Text",
  
    "value": "gold"
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:431e892c-1029-409d-b7b8-b9cad9a0a9e5"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:fd304ea2-572f-4b66-b8ad-d9d84c870fa1"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:b3336716-b468-40f1-be04-9f7ffedcc418"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:05bac9cd-2c56-4046-a70a-b2415e810f43"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:2344579c-27b3-4c5d-9db3-0fd9b46fb7e7"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "Tank Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "Tank 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T00:00:57.3062284+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T06:50:59.7051893+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "Tank"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "Tank type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "Tank of limited Tank types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### Tank NGSI-LD key-values Example    

Here is an example of a Tank in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Tank:57d79bd8-ab0d-42d1-99ae-d32099e28bde",
  
  "type": "Tank",
  
  "accessType": "Reunion",
  
  "effectiveCapacity": {
  
    "type": "Measurement",
  
    "unitCode": "m3.B",
  
    "observedAt": "2023-01-25T15:34:13Z",
  
    "value": 0.6462531189879905
  
  },
  
  "endShapeType": "reboot",
  
  "firstCurvatureRadius": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T07:42:53Z",
  
    "value": 0.12295812053381916
  
  },
  
  "nominalDepth": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T22:33:42Z",
  
    "value": 0.47800172106077865
  
  },
  
  "nominalLengthOrDiameter": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T11:50:45Z",
  
    "value": 0.6301064048931162
  
  },
  
  "nominalVolumetricCapacity": {
  
    "type": "Measurement",
  
    "unitCode": "m3",
  
    "observedAt": "2023-01-26T03:26:19Z",
  
    "value": 0.8460737465082062
  
  },
  
  "nominalWidthOrDiameter": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T15:04:58Z",
  
    "value": 0.8578461751032915
  
  },
  
  "numberOfSections": 0.4242331352066616,
  
  "operatingWeight": {
  
    "type": "Measurement",
  
    "unitCode": "g",
  
    "observedAt": "2023-01-25T15:59:33Z",
  
    "value": 0.20525111952777264
  
  },
  
  "patternType": "Buckinghamshire",
  
  "secondCurvatureRadius": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T21:19:20Z",
  
    "value": 0.38813678263187656
  
  },
  
  "storageType": "Awesome",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:691859b7-7377-412b-8a1c-100a5685852d",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:7efbc6da-aee0-45a5-9284-527f58090e18",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:ac9ad0ee-fff3-4d8b-aeb7-520137348966",
  
    "urn:ngsi-ld:System:c0e88c82-a943-40bc-9ab6-3154b3d5e696",
  
    "urn:ngsi-ld:System:72fcbe92-5021-4b81-b1b5-b0aa7720dbde"
  
  ],
  
  "hasManufacturer": "Tank Company Inc.",
  
  "hasModel": "Tank 0.1.2",
  
  "dateCreated": "2023-01-26T13:03:06Z",
  
  "dateModified": "2023-01-26T03:22:22Z",
  
  "source": "Import",
  
  "name": "Tank",
  
  "alternateName": "Tank type 2",
  
  "description": "Tank of limited Tank types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### Tank NGSI-LD normalized Example    

Here is an example of a Tank in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Tank:3d8b578c-7201-4bf4-bd7f-4aa1d9f5d298",
  
  "type": "Tank",
  
  "accessType": {
  
    "type": "Property",
  
    "value": "solid state"
  
  },
  
  "effectiveCapacity": {
  
    "type": "Property",
  
    "unitCode": "m3.B",
  
    "observedAt": "2023-01-26T08:12:59Z",
  
    "value": 0.30258616298480145
  
  },
  
  "endShapeType": {
  
    "type": "Property",
  
    "value": "Well"
  
  },
  
  "firstCurvatureRadius": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T08:09:31Z",
  
    "value": 0.1755132773764223
  
  },
  
  "nominalDepth": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T09:14:29Z",
  
    "value": 0.005463727391297302
  
  },
  
  "nominalLengthOrDiameter": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T17:31:47Z",
  
    "value": 0.1263533877303663
  
  },
  
  "nominalVolumetricCapacity": {
  
    "type": "Property",
  
    "unitCode": "m3",
  
    "observedAt": "2023-01-26T01:49:01Z",
  
    "value": 0.26912875201450304
  
  },
  
  "nominalWidthOrDiameter": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T23:31:21Z",
  
    "value": 0.7148569363985878
  
  },
  
  "numberOfSections": {
  
    "type": "Property",
  
    "value": 0.4947989850793809
  
  },
  
  "operatingWeight": {
  
    "type": "Property",
  
    "unitCode": "g",
  
    "observedAt": "2023-01-26T07:09:35Z",
  
    "value": 0.3475732824316351
  
  },
  
  "patternType": {
  
    "type": "Property",
  
    "value": "Checking Account"
  
  },
  
  "secondCurvatureRadius": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T05:30:46Z",
  
    "value": 0.16951688752044902
  
  },
  
  "storageType": {
  
    "type": "Property",
  
    "value": "generate"
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:862ca318-44c7-49b8-b0ca-74e1a829af60"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:4b8fd30b-21ae-4587-beaa-21783322f1a8"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:b8611055-a97b-4d01-8cd6-dd7f7931aa2a"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:1f9ab32d-3414-46a9-9bc9-b3f1d1b2c750"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:30979e9d-79b3-4285-ab23-addd0bdb63ef"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "Tank Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "Tank 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-25T19:22:34Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-25T19:58:46Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "Tank"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "Tank type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "Tank of limited Tank types"
  
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
